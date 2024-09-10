# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .source import Source
from .._models import BaseModel

__all__ = [
    "SourceListResponse",
    "SourceListResponseItem",
    "SourceListResponseItemLocation",
    "SourceListResponseItemLocationText",
    "SourceListResponseItemLocationTextText",
    "SourceListResponseItemLocationVisual",
    "SourceListResponseItemLocationVisualVisual",
]


class SourceListResponseItemLocationTextText(BaseModel):
    byte_offset: int


class SourceListResponseItemLocationText(BaseModel):
    text: SourceListResponseItemLocationTextText = FieldInfo(alias="Text")


class SourceListResponseItemLocationVisualVisual(BaseModel):
    x: int

    y: int


class SourceListResponseItemLocationVisual(BaseModel):
    visual: SourceListResponseItemLocationVisualVisual = FieldInfo(alias="Visual")


SourceListResponseItemLocation: TypeAlias = Union[
    SourceListResponseItemLocationText, SourceListResponseItemLocationVisual, Literal["None"]
]


class SourceListResponseItem(BaseModel):
    id: str

    creation_time: datetime

    link: Source

    location: SourceListResponseItemLocation


SourceListResponse: TypeAlias = List[SourceListResponseItem]
