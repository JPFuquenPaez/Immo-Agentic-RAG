# data_loader.py
import pandas as pd
from langchain.docstore.document import Document
from immo_rag.config import settings

def load_documents():
    """Load and convert CSV data to Document objects"""
    df = pd.read_csv(settings.DATA_PATH)
    return [_row_to_document(row) for _, row in df.iterrows()]

# alternatively: f"ID: {row['ID']}",  # Explicitly include ID first *[f"{col}: {val}" for col, val in row.items() if col != "ID"]   
# data_loader.py (version corrigée)
def _row_to_document(row):
    """Conversion complète de toutes les colonnes CSV"""
    return Document(
        page_content=(
            f"ID: {row['ID']}\n"
            f"Titre: {row['Titre']}\n"
            f"Prix: {row['Prix']}€\n"
            f"Localisation: {row['Localisation']}\n"
            f"Surface: {row['Surface']}m²\n"
            f"Pièces: {row['Pièces']}\n"
            f"Chambres: {row['Chambres']}\n"
            f"DPE: {row['DPE']}\n"
            f"Description: {row['Description'][:200]}...\n"  # Truncate long text
            f"Date publication: {row['Date de publication']}\n"
            f"Agence: {row['Agence']}\n"
            f"Caractéristiques: {row['Caracteristiques']}\n"
            f"Lien: {row['lien']}\n"
            f"Source: {row['Lien page source']}"
        ),
        metadata= dict(row.items())
    )
    