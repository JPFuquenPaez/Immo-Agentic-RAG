#tools.py
from langchain.tools import Tool
from .retriever import VectorStore

class ImmobilierTools:
    def __init__(self):
        self.retriever = VectorStore()
        self.cache = {}
        # Define tool once
        self._search_tool = Tool.from_function(
            func=self.info_retriever,
            name="immo_search",
            description="Recherche immobilière sémantique via ChromaDB"
        )

    def info_retriever(self, query: str):
        # Simple in-memory cache
        if query in self.cache:
            return self.cache[query]
        results = self.retriever.semantic_search(query, k=10)
        self.cache[query] = results
        return results

    @property
    def tools(self):
        # Return list of tools to integrate with agent
        return [self._search_tool]

