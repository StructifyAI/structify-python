# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "ToolInput",
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


class SaveSaveEntity(BaseModel):
    id: int

    properties: Dict[str, str]

    type: str


class SaveSaveRelationship(BaseModel):
    source: int

    target: int

    type: str


class SaveSave(BaseModel):
    entities: Optional[List[SaveSaveEntity]] = None

    relationships: Optional[List[SaveSaveRelationship]] = None


class Save(BaseModel):
    save: SaveSave = FieldInfo(alias="Save")
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs.
    """


class ScrollScroll(BaseModel):
    reason: str
    """OpenAI Requires an argument, so we put a dummy one here."""


class Scroll(BaseModel):
    scroll: ScrollScroll = FieldInfo(alias="Scroll")
    """For tools with no inputs."""


class ExitExit(BaseModel):
    reason: str
    """OpenAI Requires an argument, so we put a dummy one here."""


class Exit(BaseModel):
    exit: ExitExit = FieldInfo(alias="Exit")
    """For tools with no inputs."""


class ClickClick(BaseModel):
    flag: int


class Click(BaseModel):
    click: ClickClick = FieldInfo(alias="Click")


class HoverHover(BaseModel):
    flag: int


class Hover(BaseModel):
    hover: HoverHover = FieldInfo(alias="Hover")


class WaitWait(BaseModel):
    seconds: int
    """Time in seconds to wait"""


class Wait(BaseModel):
    wait: WaitWait = FieldInfo(alias="Wait")


class ErrorError(BaseModel):
    error: str


class Error(BaseModel):
    error: ErrorError = FieldInfo(alias="Error")


class GoogleGoogle(BaseModel):
    query: str


class Google(BaseModel):
    google: GoogleGoogle = FieldInfo(alias="Google")


class TypeType(BaseModel):
    flag: int

    input: str


class Type(BaseModel):
    type: TypeType = FieldInfo(alias="Type")


ToolInput = Union[Save, Scroll, Exit, Click, Hover, Wait, Error, Google, Type]
