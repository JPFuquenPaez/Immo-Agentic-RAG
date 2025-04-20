# agent.py
from typing import TypedDict, List
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_ollama import ChatOllama
from immo_rag.config import settings
from immo_rag.tools import ImmobilierTools
import hashlib

class AgentState(TypedDict):
    messages: List
    context: dict

class AgentManager:
    SYSTEM_PROMPT = SystemMessage(content=(
        "FORMATAGE STRICT - BASEZ-VOUS UNIQUEMENT SUR LES DONNÉES FOURNIES.\n"
        "Pour chaque nouvelle question utilisateur :\n"
        "1) Exécutez l'outil `immo_search(query)` pour récupérer les annonces.\n"
        "2) Parsez les résultats et mettez à jour le contexte avec : `last_results`, `retrieved_count`, `query_hash`.\n"
        "3) Générez la réponse finale en vous basant **uniquement** sur ces données et l'historique.\n\n"
        "Format attendu pour chaque annonce :\n"
        "[🔗 Annonce {ID}]({lien})\n"
        "**Titre**: {Titre}\n"
        "**Prix**: {Prix}€ | **Surface**: {Surface}m²\n"
        "**Localisation**: {Localisation} ({Code postal})\n"
        "**Détails**: {Pièces}pi | {Chambres}ch | DPE {DPE}\n"
        "**Caractéristiques**: {Caracteristiques}\n"
        "**Description**: {Description}\n"
        "**Score de pertinence**: {score:.2f}/1.00\n\n"
        "Si une information est manquante, afficher 'Non spécifié'."
    ))

    def __init__(self):
        self.llm = ChatOllama(
            model=settings.LLM_MODEL,
            temperature=settings.LLM_TEMPERATURE,
            max_new_tokens=settings.MAX_TOKENS
        )
        self.tools = ImmobilierTools()
        # In-memory session state: {thread_id: {'messages': [...], 'context': {...}}}
        self.sessions = {}

    def _hash_query(self, query: str) -> str:
        return hashlib.sha256(query.encode()).hexdigest()

    def run_query(self, query: str, thread_id: str):
        # Load or initialize session state
        state = self.sessions.get(thread_id, {'messages': [], 'context': {}})

        # Append user message
        human = HumanMessage(content=query)
        state['messages'].append(human)

        # Retrieve documents via tool
        raw_results = self.tools.info_retriever(query)
        parsed = []
        for doc, score in raw_results:
            # parse key:value from page_content
            content_data = {k: v for k, v in (
                line.split(': ', 1) for line in doc.page_content.splitlines() if ': ' in line
            )}
            # unify link field from metadata
            metadata = doc.metadata or {}
            lien_url = metadata.get('lien') or metadata.get('Lien page source') or metadata.get('link') or 'Non spécifié'
            content_data['lien'] = lien_url.strip()
            # merge other metadata, without overwriting lien
            for mkey, mval in metadata.items():
                if mkey not in ['lien', 'Lien page source', 'link']:
                    content_data[mkey] = mval
            content_data['score'] = float(score)
            # ensure all expected fields
            for field in ['ID','Titre','Prix','Surface','Localisation','Code postal',
                          'Pièces','Chambres','DPE','Caracteristiques','Description','lien']:
                content_data.setdefault(field, 'Non spécifié')
            parsed.append(content_data)

        # Update context
        context = state['context']
        context.update({
            'last_results': parsed,
            'retrieved_count': len(parsed),
            'query_hash': self._hash_query(query)
        })

        # Build LLM messages
        messages = [self.SYSTEM_PROMPT]
        if 'summary' in context:
            messages.append(SystemMessage(content=f"Résumé: {context['summary']}"))
        messages.extend(state['messages'])
        messages.append(SystemMessage(content=f"Données récupérées: {parsed}"))

        # Invoke LLM
        response: AIMessage = self.llm.invoke(messages)
        state['messages'].append(response)

        # Update summary and save session
        summary = (context.get('summary','') + ' ' + response.content).strip()[:1000]
        context['summary'] = summary
        state['context'] = context
        self.sessions[thread_id] = state

        return {'messages': [response], 'context': context}
