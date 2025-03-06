# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .type_input import TypeInput
from .wait_input import WaitInput
from .entity_graph import EntityGraph
from .no_arg_input import NoArgInput
from .search_input import SearchInput
from .error_message import ErrorMessage
from .flag_selector import FlagSelector

__all__ = [
    "ToolCall",
    "Input",
    "InputSave",
    "InputScroll",
    "InputScrollToBottom",
    "InputExit",
    "InputClick",
    "InputHover",
    "InputWait",
    "InputError",
    "InputGoogle",
    "InputType",
    "Result",
    "ResultToolQueued",
    "ResultToolFail",
    "ResultInputParseFail",
    "ResultSuccess",
]


class InputSave(BaseModel):
    save: EntityGraph = FieldInfo(alias="Save")
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs. Also the first representation of an LLM output in the
    pipeline from raw tool output to being merged into a Neo4j DB
    """


class InputScroll(BaseModel):
    scroll: NoArgInput = FieldInfo(alias="Scroll")
    """For tools with no inputs."""


class InputScrollToBottom(BaseModel):
    scroll_to_bottom: NoArgInput = FieldInfo(alias="ScrollToBottom")
    """For tools with no inputs."""


class InputExit(BaseModel):
    exit: NoArgInput = FieldInfo(alias="Exit")
    """For tools with no inputs."""


class InputClick(BaseModel):
    click: FlagSelector = FieldInfo(alias="Click")


class InputHover(BaseModel):
    hover: FlagSelector = FieldInfo(alias="Hover")


class InputWait(BaseModel):
    wait: WaitInput = FieldInfo(alias="Wait")


class InputError(BaseModel):
    error: ErrorMessage = FieldInfo(alias="Error")


class InputGoogle(BaseModel):
    google: SearchInput = FieldInfo(alias="Google")


class InputType(BaseModel):
    type: TypeInput = FieldInfo(alias="Type")


Input: TypeAlias = Union[
    InputSave,
    InputScroll,
    InputScrollToBottom,
    InputExit,
    InputClick,
    InputHover,
    InputWait,
    InputError,
    InputGoogle,
    InputType,
]


class ResultToolQueued(BaseModel):
    tool_queued: str = FieldInfo(alias="ToolQueued")


class ResultToolFail(BaseModel):
    tool_fail: str = FieldInfo(alias="ToolFail")


class ResultInputParseFail(BaseModel):
    input_parse_fail: str = FieldInfo(alias="InputParseFail")


class ResultSuccess(BaseModel):
    success: str = FieldInfo(alias="Success")


Result: TypeAlias = Union[ResultToolQueued, ResultToolFail, ResultInputParseFail, ResultSuccess, None]


class ToolCall(BaseModel):
    input: Input

    name: Literal["Exit", "Save", "Wait", "Type", "Scroll", "ScrollToBottom", "Click", "Hover", "Error", "Google"]

    result: Optional[Result] = None
