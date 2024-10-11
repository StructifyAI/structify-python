# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .source import Source
from .._models import BaseModel

__all__ = [
    "EntityGetSourceEntitiesResponse",
    "SourceEntity",
    "SourceEntityLocation",
    "SourceEntityLocationText",
    "SourceEntityLocationTextText",
    "SourceEntityLocationVisual",
    "SourceEntityLocationVisualVisual",
    "SourceEntityLocationPage",
    "SourceEntityLocationPagePage",
]


class SourceEntityLocationTextText(BaseModel):
    byte_offset: int


class SourceEntityLocationText(BaseModel):
    text: SourceEntityLocationTextText = FieldInfo(alias="Text")


class SourceEntityLocationVisualVisual(BaseModel):
    x: int

    y: int


class SourceEntityLocationVisual(BaseModel):
    visual: SourceEntityLocationVisualVisual = FieldInfo(alias="Visual")


class SourceEntityLocationPagePage(BaseModel):
    page_number: int


class SourceEntityLocationPage(BaseModel):
    page: SourceEntityLocationPagePage = FieldInfo(alias="Page")


SourceEntityLocation: TypeAlias = Union[
    SourceEntityLocationText, SourceEntityLocationVisual, SourceEntityLocationPage, Literal["None"]
]


class SourceEntity(BaseModel):
    id: str

    creation_time: datetime

    is_summary: bool

    label: str

    link: Source

    llm_id: int

    location: SourceEntityLocation

    properties: Dict[str, Union[str, bool, float]]

    user_specified: bool


class EntityGetSourceEntitiesResponse(BaseModel):
    source_entities: List[List[SourceEntity]]
