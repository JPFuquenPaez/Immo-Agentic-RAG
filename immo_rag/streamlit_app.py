import streamlit as st
import uuid
import sys

# Append the parent directory of 'immo_rag' to sys.path
sys.path.append('/Users/juanpablofuquenpaez/immoRAG')

# Now import the module
from immo_rag.agent import AgentManager

def main():
    st.set_page_config(
        page_title="Assistant Immobilier",
        page_icon="🏠",
        layout="centered"
    )

    # Gestion des sessions utilisateur
    if "session_id" not in st.session_state:
        st.session_state.session_id = str(uuid.uuid4())

    if "agent" not in st.session_state:
        st.session_state.agent = AgentManager()

    st.title("🏠 Assistant Immobilier Expert")

    # Affichage de l'historique
    for msg in st.session_state.get("messages", []):
        st.chat_message(msg["role"]).markdown(msg["content"])

    if prompt := st.chat_input("Posez votre question immobilière..."):
        # Ajout du message utilisateur
        st.session_state.messages = st.session_state.get("messages", [])
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("user"):
            st.markdown(prompt)

        try:
            with st.spinner("Recherche en cours..."):
                response = st.session_state.agent.run_query(
                    prompt,
                    st.session_state.session_id
                )

                ai_content = response["messages"][-1].content
                ai_content = ai_content.replace("🔗", "🔗 ").replace("http", " http")

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": ai_content
                })

                with st.chat_message("assistant"):
                    st.markdown(ai_content)

            # Debug
            with st.expander("Détails techniques"):
                st.json({
                    "session_id": st.session_state.session_id,
                    "retrieved_count": response["context"].get("retrieved_count"),
                    "last_query_hash": response["context"].get("query_hash")
                })

        except Exception as e:
            st.error(f"Erreur : {str(e)}")
            st.session_state.messages.append({
                "role": "assistant",
                "content": f"Erreur système : {str(e)}"
            })

if __name__ == "__main__":
    main()
