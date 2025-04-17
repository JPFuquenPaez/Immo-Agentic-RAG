from immo_rag.data_loader import load_documents
from immo_rag.retriever import VectorStore
from immo_rag.config import settings
from langchain_chroma import Chroma 

def create_vector_store():
    docs = load_documents()
    
    # Explicit collection creation
    Chroma.from_documents(
        documents=docs,
        embedding=VectorStore().embeddings,
        persist_directory=settings.PERSIST_DIR,
        collection_name="immo_collection",
        collection_metadata={
            "hnsw:space": "l2",
            "_type": "CollectionConfig"
        }
    )
    print("Vector store created successfully!")

if __name__ == "__main__":
    create_vector_store()