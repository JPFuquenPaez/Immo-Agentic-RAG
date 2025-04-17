from typing import TypedDict, Annotated, List
from langgraph.graph import StateGraph
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.messages import AnyMessage, HumanMessage, AIMessage
from langchain_ollama import ChatOllama
from immo_rag.config import settings
from immo_rag.tools import ImmobilierTools
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, END

class AgentManager:
    def __init__(self):
        self.llm = ChatOllama(
            model=settings.LLM_MODEL,
            temperature=settings.LLM_TEMPERATURE,
            max_new_tokens=settings.MAX_TOKENS
        )
        self.tools = ImmobilierTools().tools
        self.graph = self._setup_graph()

    class AgentState(TypedDict):
        messages: Annotated[List[AnyMessage], add_messages]
        memory: List[AnyMessage]

    def _setup_graph(self):
        builder = StateGraph(self.AgentState)
        
        # Add nodes
        builder.add_node("assistant", self._assistant_node)
        builder.add_node("tools", ToolNode([self.tools]))
        
        # Define edges using string identifiers
        builder.set_entry_point("assistant")
        builder.add_conditional_edges(
            "assistant",
            tools_condition,
            {"tools": "tools", "end": END}
        )
        builder.add_edge("tools", "assistant")
        
        return builder.compile()

    def _assistant_node(self, state: AgentState):
        response = self.llm.bind_tools([self.tools]).invoke(
            state["memory"] + state["messages"]
        )
        return {
            "messages": [response],
            "memory": state["memory"] + state["messages"] + [response]
        }

    def run_query(self, query: str):
        return self.graph.invoke({
            "messages": [HumanMessage(content=query)],
            "memory": []
        })