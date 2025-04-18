import streamlit as st
from langchain_core.messages import HumanMessage
import sys
from pathlib import Path
import torch

# Ajouter le répertoire racine du projet au chemin Python
sys.path.append(str(Path(__file__).parent.parent))

# Importer les paramètres et AgentManager depuis immo_rag
from immo_rag.config import settings
from immo_rag.agent import AgentManager

# Solution de contournement pour un éventuel problème d'importation de torch._classes
sys.modules['torch._classes'] = None

def main():
    st.set_page_config(
        page_title="Assistant Immobilier",
        page_icon="🏠",
        layout="centered"
    )
    
    # Initialiser l'agent
    if "agent" not in st.session_state:
        st.session_state.agent = AgentManager()

    # Historique de la conversation
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Initialiser la mémoire
    if "memory" not in st.session_state:
        st.session_state.memory = []

    st.title("🏠 Assistant Immobilier")
    
    # Afficher les messages de la conversation
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Entrée utilisateur
    if prompt := st.chat_input("Posez vos questions sur les biens immobiliers..."):
        # Ajouter le message de l'utilisateur à l'historique de la conversation
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Afficher le message de l'utilisateur
        with st.chat_message("user"):
            st.markdown(prompt)

            # Obtenir la réponse de l'agent
        with st.spinner("Analyse en cours..."):
            try:
                response = st.session_state.agent.run_query(prompt)
                ai_content = response["messages"][-1].content
                
                # Nettoyage HTML
                ai_content = ai_content.replace("🔗", "🔗 ").replace("http", " http")
                
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": ai_content
                })
                
                with st.chat_message("assistant"):
                    st.markdown(ai_content, unsafe_allow_html=True)
                    
            except Exception as e:
                st.error(f"ERREUR CRITIQUE : {str(e)}")
                st.stop()

if __name__ == "__main__":
    main()
