# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .chat_prompt import ChatPrompt
from .knowledge_graph import KnowledgeGraph

__all__ = [
    "ExecutionStep",
    "Response",
    "ToolCall",
    "Inputs",
    "Save",
    "Scroll",
    "Exit",
    "Click",
    "Hover",
    "Wait",
    "Error",
    "Google",
    "Type",
    "Result",
    "ToolQueued",
    "ToolFail",
    "ParseFail",
    "Success",
]


class Save(BaseModel):
    save: KnowledgeGraph = FieldInfo(alias="Save")
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs. Also the first representation of an LLM output in the
    pipeline from raw tool output to being merged into a Neo4j DB
    """


class Scroll(BaseModel):
    reason: str
    """Dummy argument."""

    scroll: dict = FieldInfo(alias="Scroll")
    """For tools with no inputs."""


class Exit(BaseModel):
    reason: str
    """Dummy argument."""

    exit: dict = FieldInfo(alias="Exit")
    """For tools with no inputs."""


class Click(BaseModel):
    flag: int

    click: dict = FieldInfo(alias="Click")


class Hover(BaseModel):
    flag: int

    hover: dict = FieldInfo(alias="Hover")


class Wait(BaseModel):
    seconds: int
    """Time in seconds to wait"""

    wait: dict = FieldInfo(alias="Wait")


class Error(BaseModel):
    error_message: str

    error: dict = FieldInfo(alias="Error")


class Google(BaseModel):
    query: str

    google: dict = FieldInfo(alias="Google")


class Type(BaseModel):
    flag: int

    input: str

    type: dict = FieldInfo(alias="Type")


Inputs = Union[
    Save,
    Scroll,
    Exit,
    Click,
    Hover,
    Wait,
    Error,
    Google,
    Type,
]


class ToolQueued(BaseModel):
    tool_queued: str = FieldInfo(alias="ToolQueued")


class ToolFail(BaseModel):
    tool_fail: str = FieldInfo(alias="ToolFail")


class ParseFail(BaseModel):
    input_parse_fail: str = FieldInfo(alias="InputParseFail")


class Success(BaseModel):
    success: str = FieldInfo(alias="Success")


Result = Union[
    ToolQueued,
    ToolFail,
    ParseFail,
    Success,
    None,
]


class ToolCall(BaseModel):
    input: Inputs

    name: Literal["Save", "Scroll", "Exit", "Click", "Hover", "Wait", "Error", "Google", "Type"]

    result: Optional[Result] = None


class Response(BaseModel):
    completion_tokens: int

    cost: float
    """Cost in dollars"""

    llm: str

    prompt_tokens: int
    """New tokens"""

    text: str

    tool_calls: List[ToolCall]


class ExecutionStep(BaseModel):
    id: str

    prompt: ChatPrompt

    response: Response
