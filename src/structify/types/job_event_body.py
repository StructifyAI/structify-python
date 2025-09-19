# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = ["JobEventBody", "AgentNavigated", "AgentSearched", "AgentSaved", "Completed", "Scraped", "Custom"]


class AgentNavigated(BaseModel):
    event_type: Literal["agent_navigated"]

    url: str


class AgentSearched(BaseModel):
    event_type: Literal["agent_searched"]

    query: str


class AgentSaved(BaseModel):
    event_type: Literal["agent_saved"]

    n_entities: int

    n_relationships: int

    url: str


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
    Union[AgentNavigated, AgentSearched, AgentSaved, Completed, Scraped, Custom],
    PropertyInfo(discriminator="event_type"),
]
