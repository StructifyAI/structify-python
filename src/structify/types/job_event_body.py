# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .knowledge_graph import KnowledgeGraph

__all__ = [
    "JobEventBody",
    "AgentNavigated",
    "AgentSearched",
    "AgentSaved",
    "AgentExited",
    "Failed",
    "Completed",
    "Scraped",
    "Custom",
]


class AgentNavigated(BaseModel):
    event_type: Literal["agent_navigated"]

    mode: Literal["visual", "text"]

    url: str


class AgentSearched(BaseModel):
    event_type: Literal["agent_searched"]

    query: str

    results: List[List[str]]


class AgentSaved(BaseModel):
    event_type: Literal["agent_saved"]

    kg: KnowledgeGraph
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs. Also the first representation of an LLM output in the
    pipeline from raw tool output to being merged into a DB
    """

    sources: List[str]

    page: Optional[int] = None

    reason: Optional[str] = None


class AgentExited(BaseModel):
    event_type: Literal["agent_exited"]

    reason: Optional[str] = None


class Failed(BaseModel):
    error: str

    event_type: Literal["failed"]

    summary: Optional[str] = None


class Completed(BaseModel):
    event_type: Literal["completed"]

    message: Optional[str] = None


class Scraped(BaseModel):
    count: int

    event_type: Literal["scraped"]

    page: int

    url: str


class Custom(BaseModel):
    data: Dict[str, object]

    event_name: str

    event_type: Literal["custom"]


JobEventBody: TypeAlias = Annotated[
    Union[AgentNavigated, AgentSearched, AgentSaved, AgentExited, Failed, Completed, Scraped, Custom],
    PropertyInfo(discriminator="event_type"),
]
