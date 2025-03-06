# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .type_input_param import TypeInputParam
from .wait_input_param import WaitInputParam
from .entity_graph_param import EntityGraphParam
from .no_arg_input_param import NoArgInputParam
from .search_input_param import SearchInputParam
from .error_message_param import ErrorMessageParam
from .flag_selector_param import FlagSelectorParam

__all__ = [
    "ToolCallParam",
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


class InputSave(TypedDict, total=False):
    save: Required[Annotated[EntityGraphParam, PropertyInfo(alias="Save")]]
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs. Also the first representation of an LLM output in the
    pipeline from raw tool output to being merged into a Neo4j DB
    """


class InputScroll(TypedDict, total=False):
    scroll: Required[Annotated[NoArgInputParam, PropertyInfo(alias="Scroll")]]
    """For tools with no inputs."""


class InputScrollToBottom(TypedDict, total=False):
    scroll_to_bottom: Required[Annotated[NoArgInputParam, PropertyInfo(alias="ScrollToBottom")]]
    """For tools with no inputs."""


class InputExit(TypedDict, total=False):
    exit: Required[Annotated[NoArgInputParam, PropertyInfo(alias="Exit")]]
    """For tools with no inputs."""


class InputClick(TypedDict, total=False):
    click: Required[Annotated[FlagSelectorParam, PropertyInfo(alias="Click")]]


class InputHover(TypedDict, total=False):
    hover: Required[Annotated[FlagSelectorParam, PropertyInfo(alias="Hover")]]


class InputWait(TypedDict, total=False):
    wait: Required[Annotated[WaitInputParam, PropertyInfo(alias="Wait")]]


class InputError(TypedDict, total=False):
    error: Required[Annotated[ErrorMessageParam, PropertyInfo(alias="Error")]]


class InputGoogle(TypedDict, total=False):
    google: Required[Annotated[SearchInputParam, PropertyInfo(alias="Google")]]


class InputType(TypedDict, total=False):
    type: Required[Annotated[TypeInputParam, PropertyInfo(alias="Type")]]


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


class ResultToolQueued(TypedDict, total=False):
    tool_queued: Required[Annotated[str, PropertyInfo(alias="ToolQueued")]]


class ResultToolFail(TypedDict, total=False):
    tool_fail: Required[Annotated[str, PropertyInfo(alias="ToolFail")]]


class ResultInputParseFail(TypedDict, total=False):
    input_parse_fail: Required[Annotated[str, PropertyInfo(alias="InputParseFail")]]


class ResultSuccess(TypedDict, total=False):
    success: Required[Annotated[str, PropertyInfo(alias="Success")]]


Result: TypeAlias = Union[ResultToolQueued, ResultToolFail, ResultInputParseFail, ResultSuccess]


class ToolCallParam(TypedDict, total=False):
    input: Required[Input]

    name: Required[
        Literal["Exit", "Save", "Wait", "Type", "Scroll", "ScrollToBottom", "Click", "Hover", "Error", "Google"]
    ]

    result: Optional[Result]
