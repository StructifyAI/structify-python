# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .knowledge_graph import KnowledgeGraph

__all__ = [
    "LabelLlmAssistResponse",
    "LabelLlmAssistResponseItem",
    "LabelLlmAssistResponseItemSave",
    "LabelLlmAssistResponseItemScroll",
    "LabelLlmAssistResponseItemScrollScroll",
    "LabelLlmAssistResponseItemExit",
    "LabelLlmAssistResponseItemExitExit",
    "LabelLlmAssistResponseItemClick",
    "LabelLlmAssistResponseItemClickClick",
    "LabelLlmAssistResponseItemHover",
    "LabelLlmAssistResponseItemHoverHover",
    "LabelLlmAssistResponseItemWait",
    "LabelLlmAssistResponseItemWaitWait",
    "LabelLlmAssistResponseItemError",
    "LabelLlmAssistResponseItemErrorError",
    "LabelLlmAssistResponseItemGoogle",
    "LabelLlmAssistResponseItemGoogleGoogle",
    "LabelLlmAssistResponseItemType",
    "LabelLlmAssistResponseItemTypeType",
]


class LabelLlmAssistResponseItemSave(BaseModel):
    save: KnowledgeGraph = FieldInfo(alias="Save")
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs. Also the first representation of an LLM output in the
    pipeline from raw tool output to being merged into a Neo4j DB
    """


class LabelLlmAssistResponseItemScrollScroll(BaseModel):
    reason: str
    """OpenAI Requires an argument, so we put a dummy one here."""


class LabelLlmAssistResponseItemScroll(BaseModel):
    scroll: LabelLlmAssistResponseItemScrollScroll = FieldInfo(alias="Scroll")
    """For tools with no inputs."""


class LabelLlmAssistResponseItemExitExit(BaseModel):
    reason: str
    """OpenAI Requires an argument, so we put a dummy one here."""


class LabelLlmAssistResponseItemExit(BaseModel):
    exit: LabelLlmAssistResponseItemExitExit = FieldInfo(alias="Exit")
    """For tools with no inputs."""


class LabelLlmAssistResponseItemClickClick(BaseModel):
    flag: int


class LabelLlmAssistResponseItemClick(BaseModel):
    click: LabelLlmAssistResponseItemClickClick = FieldInfo(alias="Click")


class LabelLlmAssistResponseItemHoverHover(BaseModel):
    flag: int


class LabelLlmAssistResponseItemHover(BaseModel):
    hover: LabelLlmAssistResponseItemHoverHover = FieldInfo(alias="Hover")


class LabelLlmAssistResponseItemWaitWait(BaseModel):
    seconds: int
    """Time in seconds to wait"""


class LabelLlmAssistResponseItemWait(BaseModel):
    wait: LabelLlmAssistResponseItemWaitWait = FieldInfo(alias="Wait")


class LabelLlmAssistResponseItemErrorError(BaseModel):
    error: str


class LabelLlmAssistResponseItemError(BaseModel):
    error: LabelLlmAssistResponseItemErrorError = FieldInfo(alias="Error")


class LabelLlmAssistResponseItemGoogleGoogle(BaseModel):
    query: str


class LabelLlmAssistResponseItemGoogle(BaseModel):
    google: LabelLlmAssistResponseItemGoogleGoogle = FieldInfo(alias="Google")


class LabelLlmAssistResponseItemTypeType(BaseModel):
    flag: int

    input: str


class LabelLlmAssistResponseItemType(BaseModel):
    type: LabelLlmAssistResponseItemTypeType = FieldInfo(alias="Type")


LabelLlmAssistResponseItem = Union[
    LabelLlmAssistResponseItemSave,
    LabelLlmAssistResponseItemScroll,
    LabelLlmAssistResponseItemExit,
    LabelLlmAssistResponseItemClick,
    LabelLlmAssistResponseItemHover,
    LabelLlmAssistResponseItemWait,
    LabelLlmAssistResponseItemError,
    LabelLlmAssistResponseItemGoogle,
    LabelLlmAssistResponseItemType,
]

LabelLlmAssistResponse = List[LabelLlmAssistResponseItem]
