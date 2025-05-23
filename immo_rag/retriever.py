# retriever.py
from langchain.vectorstores import Chroma
from langchain.embeddings import SentenceTransformerEmbeddings
from immo_rag.config import settings

class VectorStore:
    def __init__(self):
        self.embeddings = SentenceTransformerEmbeddings(
            model_name=settings.EMBEDDING_MODEL
        )
        self.vectorstore = Chroma(
            persist_directory=settings.PERSIST_DIR,
            embedding_function=self.embeddings,
            collection_name="immo_collection")

    def semantic_search(self, query: str, k: int) -> list:
        return self.vectorstore.similarity_search_with_score(query, k=k)