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
    "SourceNode",
    "SourceNodeLocation",
    "SourceNodeLocationText",
    "SourceNodeLocationTextText",
    "SourceNodeLocationVisual",
    "SourceNodeLocationVisualVisual",
    "SourceNodeLocationPage",
    "SourceNodeLocationPagePage",
]


class SourceEntity(BaseModel):
    id: str

    creation_time: datetime

    label: str

    llm_id: int

    properties: Dict[str, Union[str, bool, float]]


class SourceNodeLocationTextText(BaseModel):
    byte_offset: int


class SourceNodeLocationText(BaseModel):
    text: SourceNodeLocationTextText = FieldInfo(alias="Text")


class SourceNodeLocationVisualVisual(BaseModel):
    x: int

    y: int


class SourceNodeLocationVisual(BaseModel):
    visual: SourceNodeLocationVisualVisual = FieldInfo(alias="Visual")


class SourceNodeLocationPagePage(BaseModel):
    page_number: int


class SourceNodeLocationPage(BaseModel):
    page: SourceNodeLocationPagePage = FieldInfo(alias="Page")


SourceNodeLocation: TypeAlias = Union[
    SourceNodeLocationText, SourceNodeLocationVisual, SourceNodeLocationPage, Literal["None"]
]


class SourceNode(BaseModel):
    id: str

    creation_time: datetime

    link: Source

    location: SourceNodeLocation

    user_specified: bool


class EntityGetSourceEntitiesResponse(BaseModel):
    source_entities: List[SourceEntity]

    source_nodes: List[SourceNode]
