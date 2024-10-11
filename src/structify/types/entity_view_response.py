# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from . import source
from .._models import BaseModel

__all__ = [
    "EntityViewResponse",
    "ConnectedEntity",
    "Entity",
    "Relationship",
    "SimilarEntity",
    "Source",
    "SourceLocation",
    "SourceLocationText",
    "SourceLocationTextText",
    "SourceLocationVisual",
    "SourceLocationVisualVisual",
    "SourceLocationPage",
    "SourceLocationPagePage",
]


class ConnectedEntity(BaseModel):
    id: str

    creation_time: datetime

    label: str

    properties: Dict[str, Union[str, bool, float]]


class Entity(BaseModel):
    id: str

    creation_time: datetime

    label: str

    properties: Dict[str, Union[str, bool, float]]


class Relationship(BaseModel):
    from_id: str

    label: str

    properties: Dict[str, Union[str, bool, float]]

    to_id: str


class SimilarEntity(BaseModel):
    id: str

    creation_time: datetime

    label: str

    properties: Dict[str, Union[str, bool, float]]


class SourceLocationTextText(BaseModel):
    byte_offset: int


class SourceLocationText(BaseModel):
    text: SourceLocationTextText = FieldInfo(alias="Text")


class SourceLocationVisualVisual(BaseModel):
    x: int

    y: int


class SourceLocationVisual(BaseModel):
    visual: SourceLocationVisualVisual = FieldInfo(alias="Visual")


class SourceLocationPagePage(BaseModel):
    page_number: int


class SourceLocationPage(BaseModel):
    page: SourceLocationPagePage = FieldInfo(alias="Page")


SourceLocation: TypeAlias = Union[SourceLocationText, SourceLocationVisual, SourceLocationPage, Literal["None"]]


class Source(BaseModel):
    id: str

    creation_time: datetime

    is_summary: bool

    link: source.Source

    location: SourceLocation

    user_specified: bool


class EntityViewResponse(BaseModel):
    connected_entities: List[ConnectedEntity]

    entity: Entity

    last_updated: str

    relationships: List[Relationship]

    similar_entities: List[SimilarEntity]

    sources: List[Source]
