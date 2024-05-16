# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "LabelSubmitParams",
    "Body",
    "BodySave",
    "BodySaveSave",
    "BodySaveSaveEntity",
    "BodySaveSaveRelationship",
    "BodyScroll",
    "BodyScrollScroll",
    "BodyExit",
    "BodyExitExit",
    "BodyClick",
    "BodyClickClick",
    "BodyHover",
    "BodyHoverHover",
    "BodyWait",
    "BodyWaitWait",
    "BodyError",
    "BodyErrorError",
    "BodyGoogle",
    "BodyGoogleGoogle",
    "BodyType",
    "BodyTypeType",
]


class LabelSubmitParams(TypedDict, total=False):
    body: Required[Iterable[Body]]


class BodySaveSaveEntity(TypedDict, total=False):
    id: Required[int]

    properties: Required[Dict[str, str]]

    type: Required[str]


class BodySaveSaveRelationship(TypedDict, total=False):
    source: Required[int]

    target: Required[int]

    type: Required[str]


class BodySaveSave(TypedDict, total=False):
    entities: Iterable[BodySaveSaveEntity]

    relationships: Iterable[BodySaveSaveRelationship]


class BodySave(TypedDict, total=False):
    save: Required[Annotated[BodySaveSave, PropertyInfo(alias="Save")]]
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs.
    """


class BodyScrollScroll(TypedDict, total=False):
    reason: Required[str]
    """OpenAI Requires an argument, so we put a dummy one here."""


class BodyScroll(TypedDict, total=False):
    scroll: Required[Annotated[BodyScrollScroll, PropertyInfo(alias="Scroll")]]
    """For tools with no inputs."""


class BodyExitExit(TypedDict, total=False):
    reason: Required[str]
    """OpenAI Requires an argument, so we put a dummy one here."""


class BodyExit(TypedDict, total=False):
    exit: Required[Annotated[BodyExitExit, PropertyInfo(alias="Exit")]]
    """For tools with no inputs."""


class BodyClickClick(TypedDict, total=False):
    flag: Required[int]


class BodyClick(TypedDict, total=False):
    click: Required[Annotated[BodyClickClick, PropertyInfo(alias="Click")]]


class BodyHoverHover(TypedDict, total=False):
    flag: Required[int]


class BodyHover(TypedDict, total=False):
    hover: Required[Annotated[BodyHoverHover, PropertyInfo(alias="Hover")]]


class BodyWaitWait(TypedDict, total=False):
    seconds: Required[int]
    """Time in seconds to wait"""


class BodyWait(TypedDict, total=False):
    wait: Required[Annotated[BodyWaitWait, PropertyInfo(alias="Wait")]]


class BodyErrorError(TypedDict, total=False):
    error: Required[str]


class BodyError(TypedDict, total=False):
    error: Required[Annotated[BodyErrorError, PropertyInfo(alias="Error")]]


class BodyGoogleGoogle(TypedDict, total=False):
    query: Required[str]


class BodyGoogle(TypedDict, total=False):
    google: Required[Annotated[BodyGoogleGoogle, PropertyInfo(alias="Google")]]


class BodyTypeType(TypedDict, total=False):
    flag: Required[int]

    input: Required[str]


class BodyType(TypedDict, total=False):
    type: Required[Annotated[BodyTypeType, PropertyInfo(alias="Type")]]


Body = Union[BodySave, BodyScroll, BodyExit, BodyClick, BodyHover, BodyWait, BodyError, BodyGoogle, BodyType]
