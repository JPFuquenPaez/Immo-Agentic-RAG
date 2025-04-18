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
            return "No matching information found..."
            
        return "\n\n".join(
            f"{doc.page_content}\nSimilarity Score (L2 Distance): {score:.2f}"
            for doc, score in results
        ) if results else "No results found"

    @property
    def tools(self):
        return Tool(
            name="immo_info_retriever",
            func=self.info_retriever,
            description="Retrieves property details with similarity scores. Use for questions about features, prices, or locations."
        )
        
        