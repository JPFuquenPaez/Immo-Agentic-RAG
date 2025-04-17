import pandas as pd
from langchain.docstore.document import Document
from immo_rag.config import settings

def load_documents():
    """Load and convert CSV data to Document objects"""
    df = pd.read_csv(settings.DATA_PATH)
    return [_row_to_document(row) for _, row in df.iterrows()]

def _row_to_document(row):
    """Convert a DataFrame row to LangChain Document"""
    return Document(
        page_content="\n".join(
            [f"{col}: {val}" for col, val in row.items() if col != "ID"]
        ),
        metadata={"ID": row["ID"]}
    )