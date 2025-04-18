# agent.py
from typing import TypedDict, Annotated, List
from langgraph.graph import StateGraph
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.messages import AnyMessage, HumanMessage, AIMessage
from langchain_ollama import ChatOllama
from immo_rag.config import settings
from immo_rag.tools import ImmobilierTools
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, END
from langchain_core.messages import SystemMessage

class AgentState(TypedDict):
    messages: Annotated[List[AnyMessage], add_messages]
    memory: Annotated[List[AnyMessage], add_messages]
    
class AgentManager:
    def __init__(self):
        self.llm = ChatOllama(
            model=settings.LLM_MODEL,
            temperature=settings.LLM_TEMPERATURE,
            max_new_tokens=settings.MAX_TOKENS
        )
        self.tools = ImmobilierTools().tools
        self.graph = self._setup_graph()


        
    SYSTEM_PROMPT = (
    "Vous êtes un assistant immobilier expert. Formatez les réponses avec :\n"
    "- Détails clairs (prix, surface, localisation, description)\n"
    "- Liens sous forme [🔗 Annonce X](URL)\n"
    "- Liste des liens en bas de réponse si nécessaire\n"
    "- Si score de similarité < 0.5 dire que l'annonce correspond fortement à ce qui est cherché f\n"
    "- Style professionnel et informatif"
    )

    def _setup_graph(self):
        builder = StateGraph(AgentState)
        
        builder.add_node("assistant", self._assistant_node)
        builder.add_node("tools", ToolNode([self.tools]))
        
        builder.set_entry_point("assistant")
        builder.add_conditional_edges(
            "assistant",
            lambda state: "tools" if any(
                msg.tool_calls for msg in state["messages"] 
                if isinstance(msg, AIMessage)
            ) else END,
            {"tools": "tools", END: END}
        )
        builder.add_edge("tools", "assistant")
        
        return builder.compile()


    def _assistant_node(self, state: AgentState):
        # Ajout du message système
        system_message = SystemMessage(content=self.SYSTEM_PROMPT)
        messages = [system_message] + state["memory"] + state["messages"]
        
        response = self.llm.bind_tools([self.tools]).invoke(messages)
        return {
            "messages": [response],
            "memory": state["memory"] + state["messages"] + [response]
        }

    def run_query(self, query: str):
        return self.graph.invoke({
            "messages": [HumanMessage(content=query)],
            "memory": []
        })