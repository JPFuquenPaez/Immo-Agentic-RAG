#ingest.py
from langchain.vectorstores import Chroma
from langchain_community.vectorstores import Chroma #updated
from immo_rag.data_loader import load_documents
from immo_rag.retriever import VectorStore
from immo_rag.config import settings
from langchain.embeddings import SentenceTransformerEmbeddings
import sys
from pathlib import Path

# Add project root to Python path
sys.path.append(str(Path(__file__).parent.parent))

def create_vector_store():
    # Clear existing collection first
    Chroma(persist_directory=settings.PERSIST_DIR, 
          embedding_function=SentenceTransformerEmbeddings(
              model_name=settings.EMBEDDING_MODEL
          )).delete_collection()
    
    # Create fresh collection
    Chroma.from_documents(
        documents=load_documents(),
        embedding=SentenceTransformerEmbeddings(
            model_name=settings.EMBEDDING_MODEL
        ),
        persist_directory=settings.PERSIST_DIR,
        collection_name="immo_collection",
        collection_metadata={"hnsw:space": "l2"}
    )
    print("Vector store created with explicit schema!")

if __name__ == "__main__":
    create_vector_store()