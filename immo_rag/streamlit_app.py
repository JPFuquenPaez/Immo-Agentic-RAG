# streamlit_app.py
import streamlit as st
from langchain_core.messages import HumanMessage
import sys
from pathlib import Path
# streamlit_app.py - Add this at the top before other imports
import sys
import torch
sys.modules['torch._classes'] = None

# Add project root to Python path
sys.path.append(str(Path(__file__).parent.parent))
from immo_rag.agent import AgentManager

def main():
    st.set_page_config(
        page_title="Real Estate Assistant",
        page_icon="🏠",
        layout="centered"
    )
    
    # Initialize agent
    if "agent" not in st.session_state:
        st.session_state.agent = AgentManager()
    
    # Chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    st.title("🏠 Real Estate Assistant")
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # User input
    if prompt := st.chat_input("Ask about properties..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Get agent response
        with st.spinner("Analyzing properties..."):
            try:
                response = st.session_state.agent.run_query(prompt)
                ai_content = response["messages"][-1].content
                
                # Add assistant response
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": ai_content
                })
                
                # Display assistant response
                with st.chat_message("assistant"):
                    st.markdown(ai_content)
            
            except Exception as e:
                st.error(f"Error processing request: {str(e)}")

if __name__ == "__main__":
    main()