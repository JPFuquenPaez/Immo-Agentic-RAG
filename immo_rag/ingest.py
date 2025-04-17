from immo_rag.data_loader import load_documents
from immo_rag.retriever import VectorStore
from immo_rag.config import settings

def create_vector_store():
    docs = load_documents()
    
    # Explicit collection creation
    vector_store = VectorStore()
    vector_store.vectorstore.from_documents(
        documents=docs,
        embedding=vector_store.embeddings,
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