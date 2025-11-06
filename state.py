from typing import TypedDict, List
from typing_extensions import Annotated
from langgraph.graph.message import add_messages
from langchain_core.messages import AnyMessage, HumanMessage, SystemMessage

class AgentState(TypedDict):
    messages: Annotated[List[AnyMessage], add_messages]