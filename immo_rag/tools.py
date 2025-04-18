# tools.py
from langchain.tools import Tool
from .retriever import VectorStore

class ImmobilierTools:
    def __init__(self):
        self.retriever = VectorStore()
        
    def info_retriever(self, query: str) -> str:
        """Retrieve real estate information with similarity scores"""
        results = self.retriever.semantic_search(query)
        
        if not results:
            return "Aucun résultat trouvé"
        
        return "\n\n".join(
            f"{doc.page_content}\n"
            f"🔗 Lien: {doc.metadata.get('Lien annonce', 'N/A')}\n"
            f"Score: {score:.2f}\n" 
            for doc, score in results
        ) 

    @property
    def tools(self):
        return Tool(
            name="immo_info_retriever",
            func=self.info_retriever,
            description="Recherche d'annonces immobilières avec liens directs. "
                    "Utiliser pour les questions sur les logements, prix, "
                    "localisations, et caractéristiques. Inclut toujours les URLs des annonces."
        )