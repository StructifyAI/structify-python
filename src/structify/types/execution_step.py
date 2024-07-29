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
    "ScrollScroll",
    "Exit",
    "ExitExit",
    "Click",
    "ClickClick",
    "Hover",
    "HoverHover",
    "Wait",
    "WaitWait",
    "Error",
    "ErrorError",
    "Google",
    "GoogleGoogle",
    "Type",
    "TypeType",
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


class ScrollParams(BaseModel):
    reason: str
    """OpenAI Requires an argument, so we put a dummy one here."""


class Scroll(BaseModel):
    scroll: ScrollParams = FieldInfo(alias="Scroll")
    """For tools with no inputs."""


class ExitParams(BaseModel):
    reason: str
    """OpenAI Requires an argument, so we put a dummy one here."""


class Exit(BaseModel):
    exit: ExitParams = FieldInfo(alias="Exit")
    """For tools with no inputs."""


class ClickParams(BaseModel):
    flag: int


class Click(BaseModel):
    click: ClickParams = FieldInfo(alias="Click")


class HoverParams(BaseModel):
    flag: int


class Hover(BaseModel):
    hover: HoverParams = FieldInfo(alias="Hover")


class WaitParams(BaseModel):
    seconds: int
    """Time in seconds to wait"""


class Wait(BaseModel):
    wait: WaitParams = FieldInfo(alias="Wait")


class ErrorParams(BaseModel):
    error: str


class Error(BaseModel):
    error: ErrorParams = FieldInfo(alias="Error")


class GoogleParams(BaseModel):
    query: str


class Google(BaseModel):
    google: Google = FieldInfo(alias="Google")


class TypeParams(BaseModel):
    flag: int

    input: str


class Type(BaseModel):
    type: TypeParams = FieldInfo(alias="Type")


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
