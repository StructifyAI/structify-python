# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from . import source
from .._models import BaseModel

__all__ = [
    "EntityViewResponse",
    "ConnectedEntity",
    "ConnectedEntityProperties",
    "ConnectedEntityPropertiesImage",
    "Entity",
    "EntityProperties",
    "EntityPropertiesImage",
    "Relationship",
    "RelationshipProperties",
    "RelationshipPropertiesImage",
    "SimilarEntity",
    "SimilarEntityProperties",
    "SimilarEntityPropertiesImage",
    "Source",
    "SourceLocation",
    "SourceLocationText",
    "SourceLocationTextText",
    "SourceLocationVisual",
    "SourceLocationVisualVisual",
    "SourceLocationPage",
    "SourceLocationPagePage",
]


class ConnectedEntityPropertiesImage(BaseModel):
    number: int

    hash: Optional[str] = None


ConnectedEntityProperties: TypeAlias = Union[str, bool, float, ConnectedEntityPropertiesImage]


class ConnectedEntity(BaseModel):
    id: str

    creation_time: datetime

    label: str

    properties: Dict[str, ConnectedEntityProperties]


class EntityPropertiesImage(BaseModel):
    number: int

    hash: Optional[str] = None


EntityProperties: TypeAlias = Union[str, bool, float, EntityPropertiesImage]


class Entity(BaseModel):
    id: str

    creation_time: datetime

    label: str

    properties: Dict[str, EntityProperties]


class RelationshipPropertiesImage(BaseModel):
    number: int

    hash: Optional[str] = None


RelationshipProperties: TypeAlias = Union[str, bool, float, RelationshipPropertiesImage]


class Relationship(BaseModel):
    from_id: str

    label: str

    properties: Dict[str, RelationshipProperties]

    to_id: str


class SimilarEntityPropertiesImage(BaseModel):
    number: int

    hash: Optional[str] = None


SimilarEntityProperties: TypeAlias = Union[str, bool, float, SimilarEntityPropertiesImage]


class SimilarEntity(BaseModel):
    id: str

    creation_time: datetime

    label: str

    properties: Dict[str, SimilarEntityProperties]


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
