# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "ToolInputParam",
    "Save",
    "SaveSave",
    "SaveSaveEntity",
    "SaveSaveRelationship",
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
]


class SaveSaveEntity(TypedDict, total=False):
    id: Required[int]

    properties: Required[Dict[str, str]]

    type: Required[str]


class SaveSaveRelationship(TypedDict, total=False):
    source: Required[int]

    target: Required[int]

    type: Required[str]


class SaveSave(TypedDict, total=False):
    entities: Iterable[SaveSaveEntity]

    relationships: Iterable[SaveSaveRelationship]


class Save(TypedDict, total=False):
    save: Required[Annotated[SaveSave, PropertyInfo(alias="Save")]]
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs.
    """


class ScrollScroll(TypedDict, total=False):
    reason: Required[str]
    """OpenAI Requires an argument, so we put a dummy one here."""


class Scroll(TypedDict, total=False):
    scroll: Required[Annotated[ScrollScroll, PropertyInfo(alias="Scroll")]]
    """For tools with no inputs."""


class ExitExit(TypedDict, total=False):
    reason: Required[str]
    """OpenAI Requires an argument, so we put a dummy one here."""


class Exit(TypedDict, total=False):
    exit: Required[Annotated[ExitExit, PropertyInfo(alias="Exit")]]
    """For tools with no inputs."""


class ClickClick(TypedDict, total=False):
    flag: Required[int]


class Click(TypedDict, total=False):
    click: Required[Annotated[ClickClick, PropertyInfo(alias="Click")]]


class HoverHover(TypedDict, total=False):
    flag: Required[int]


class Hover(TypedDict, total=False):
    hover: Required[Annotated[HoverHover, PropertyInfo(alias="Hover")]]


class WaitWait(TypedDict, total=False):
    seconds: Required[int]
    """Time in seconds to wait"""


class Wait(TypedDict, total=False):
    wait: Required[Annotated[WaitWait, PropertyInfo(alias="Wait")]]


class ErrorError(TypedDict, total=False):
    error: Required[str]


class Error(TypedDict, total=False):
    error: Required[Annotated[ErrorError, PropertyInfo(alias="Error")]]


class GoogleGoogle(TypedDict, total=False):
    query: Required[str]


class Google(TypedDict, total=False):
    google: Required[Annotated[GoogleGoogle, PropertyInfo(alias="Google")]]


class TypeType(TypedDict, total=False):
    flag: Required[int]

    input: Required[str]


class Type(TypedDict, total=False):
    type: Required[Annotated[TypeType, PropertyInfo(alias="Type")]]


ToolInputParam = Union[Save, Scroll, Exit, Click, Hover, Wait, Error, Google, Type]
