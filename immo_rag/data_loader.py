# data_loader.py
import pandas as pd
from langchain.docstore.document import Document
from immo_rag.config import settings

def load_documents():
    """Load and convert CSV data to Document objects"""
    df = pd.read_csv(settings.DATA_PATH)
    return [_row_to_document(row) for _, row in df.iterrows()]

# alternatively: f"ID: {row['ID']}",  # Explicitly include ID first *[f"{col}: {val}" for col, val in row.items() if col != "ID"]   
def _row_to_document(row):
    """Convertir une ligne du DataFrame en Document avec mise en forme explicite"""
    return Document(
        page_content="\n".join([
            f"ID: {row['ID']}",
            f"Titre: {row['Titre']}",
            f"Prix: {row['Prix']}",
            f"Localisation: {row['Localisation']}",
            f"Surface: {row['Surface']}", 
            f"Pièces: {row['Pièces']}",
            f"Chambres: {row['Chambres']}",
            f"DPE: {row['DPE']}",
            f"Description: {row['Description']}",
            f"Lien annonce: {row['Lien annonce']}",  # Ligne ajoutée
            f"Caracteristiques: {row['Caracteristiques']}"
        ]),
        metadata={
            "Lien annonce": row["Lien annonce"] #str(row["Lien annonce"])
            }
    )
    
    
"""def _row_to_document(row):
    return Document(
        page_content="\n".join([
            f"ID: {row['ID']}",  # Explicitly include ID first
            *[f"{col}: {val}" for col, val in row.items() if col != "ID"]
        ]),
        metadata={"ID": row["ID"]}
    )"""