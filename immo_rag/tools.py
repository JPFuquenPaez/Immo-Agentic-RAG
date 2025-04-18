# tools.py
from langchain.tools import Tool
from .retriever import VectorStore

class ImmobilierTools:
    def __init__(self):
        self.retriever = VectorStore()
        
    def info_retriever(self, query: str) -> str:
        """Retrieve real estate info with proper formatting"""
        results = self.retriever.semantic_search(query, k=5)
        
        if not results:
            return "Aucun résultat trouvé"
        
        return "\n\n".join(
            f"### Annonce {i+1}\n"
            f"{doc.page_content}\n"
            f"Lien: [🔗 Voir l'annonce]({doc.metadata['Lien annonce']})" 
            for i, (doc, score) in enumerate(results)
        )

    @property
    def tools(self):
        return Tool.from_function(
            name="immo_search",
            func=self.info_retriever,
            description="Recherche d'annonces immobilières. Renvoie toujours les liens au format [🔗 Voir l'annonce](URL)"
        )