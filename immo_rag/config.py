from pathlib import Path

class Settings:
    DATA_PATH = Path("./data/annonces_aveccaracteristiques_preprocesse.csv")
    PERSIST_DIR = "./immo_chroma_db"
    EMBEDDING_MODEL = "all-mpnet-base-v2"
    LLM_MODEL = "qwen2.5:7b"
    LLM_TEMPERATURE = 0.1
    MAX_TOKENS = 512

settings = Settings()