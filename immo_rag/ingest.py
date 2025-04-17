from langchain.vectorstores import Chroma
from immo_rag.data_loader import load_documents
from immo_rag.retriever import VectorStore
from immo_rag.config import settings

def create_vector_store():
    vector_store = VectorStore()
    
    # Recreate collection with proper schema
    Chroma.from_documents(
        documents=load_documents(),
        embedding=vector_store.embeddings,
        persist_directory=settings.PERSIST_DIR,
        collection_name="immo_collection",
        collection_metadata={
            "hnsw:space": "l2",
            "_type": "CollectionConfig"
        }
    )
    print("Vector store created with explicit schema!")
    
if __name__ == "__main__":
    create_vector_store()
    
"""
# ingest.py - Modified cleanup section only
from pathlib import Path
import shutil
from immo_rag.retriever import VectorStore
from immo_rag.data_loader import load_documents
from config import settings

def create_vector_store():
# Replace the client reset with filesystem cleanup
persist_path = Path(settings.PERSIST_DIR)
if persist_path.exists():
shutil.rmtree(persist_path)
print("🧹 Removed existing vector store data")

# Keep existing Chroma initialization
vector_store = VectorStore()
Chroma.from_documents(
documents=load_documents(),
embedding=vector_store.embeddings,
persist_directory=settings.PERSIST_DIR,
collection_name="immo_collection"
)
print("✅ New vector store created successfully!")

if __name__ == "__main__":
create_vector_store()

"""