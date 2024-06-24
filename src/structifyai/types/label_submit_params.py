# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "LabelSubmitParams",
    "Label",
    "LabelSave",
    "LabelSaveSave",
    "LabelSaveSaveEntity",
    "LabelSaveSaveRelationship",
    "LabelScroll",
    "LabelScrollScroll",
    "LabelExit",
    "LabelExitExit",
    "LabelClick",
    "LabelClickClick",
    "LabelHover",
    "LabelHoverHover",
    "LabelWait",
    "LabelWaitWait",
    "LabelError",
    "LabelErrorError",
    "LabelGoogle",
    "LabelGoogleGoogle",
    "LabelType",
    "LabelTypeType",
]


class LabelSubmitParams(TypedDict, total=False):
    label: Required[Optional[Iterable[Label]]]


class LabelSaveSaveEntity(TypedDict, total=False):
    id: Required[int]

    properties: Required[Dict[str, str]]

    type: Required[str]


class LabelSaveSaveRelationship(TypedDict, total=False):
    source: Required[int]

    target: Required[int]

    type: Required[str]


class LabelSaveSave(TypedDict, total=False):
    entities: Iterable[LabelSaveSaveEntity]

    relationships: Iterable[LabelSaveSaveRelationship]


class LabelSave(TypedDict, total=False):
    save: Required[Annotated[LabelSaveSave, PropertyInfo(alias="Save")]]
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs.
    """


class LabelScrollScroll(TypedDict, total=False):
    reason: Required[str]
    """OpenAI Requires an argument, so we put a dummy one here."""


class LabelScroll(TypedDict, total=False):
    scroll: Required[Annotated[LabelScrollScroll, PropertyInfo(alias="Scroll")]]
    """For tools with no inputs."""


class LabelExitExit(TypedDict, total=False):
    reason: Required[str]
    """OpenAI Requires an argument, so we put a dummy one here."""


class LabelExit(TypedDict, total=False):
    exit: Required[Annotated[LabelExitExit, PropertyInfo(alias="Exit")]]
    """For tools with no inputs."""


class LabelClickClick(TypedDict, total=False):
    flag: Required[int]


class LabelClick(TypedDict, total=False):
    click: Required[Annotated[LabelClickClick, PropertyInfo(alias="Click")]]


class LabelHoverHover(TypedDict, total=False):
    flag: Required[int]


class LabelHover(TypedDict, total=False):
    hover: Required[Annotated[LabelHoverHover, PropertyInfo(alias="Hover")]]


class LabelWaitWait(TypedDict, total=False):
    seconds: Required[int]
    """Time in seconds to wait"""


class LabelWait(TypedDict, total=False):
    wait: Required[Annotated[LabelWaitWait, PropertyInfo(alias="Wait")]]


class LabelErrorError(TypedDict, total=False):
    error: Required[str]


class LabelError(TypedDict, total=False):
    error: Required[Annotated[LabelErrorError, PropertyInfo(alias="Error")]]


class LabelGoogleGoogle(TypedDict, total=False):
    query: Required[str]


class LabelGoogle(TypedDict, total=False):
    google: Required[Annotated[LabelGoogleGoogle, PropertyInfo(alias="Google")]]


class LabelTypeType(TypedDict, total=False):
    flag: Required[int]

    input: Required[str]


class LabelType(TypedDict, total=False):
    type: Required[Annotated[LabelTypeType, PropertyInfo(alias="Type")]]


Label = Union[LabelSave, LabelScroll, LabelExit, LabelClick, LabelHover, LabelWait, LabelError, LabelGoogle, LabelType]
