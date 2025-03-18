# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from . import source
from .image import Image
from .._models import BaseModel

__all__ = [
    "EntityViewResponse",
    "ConnectedEntity",
    "ConnectedEntityProperties",
    "Entity",
    "EntityProperties",
    "Relationship",
    "RelationshipProperties",
    "SimilarEntity",
    "SimilarEntityProperties",
    "Source",
    "SourceLocation",
    "SourceLocationText",
    "SourceLocationTextText",
    "SourceLocationVisual",
    "SourceLocationVisualVisual",
    "SourceLocationPage",
    "SourceLocationPagePage",
]

ConnectedEntityProperties: TypeAlias = Union[str, bool, float, Image]


class ConnectedEntity(BaseModel):
    id: str

    created_at: datetime

    dataset_id: str

    label: str

    properties: Dict[str, ConnectedEntityProperties]

    updated_at: datetime


EntityProperties: TypeAlias = Union[str, bool, float, Image]


class Entity(BaseModel):
    id: str

    created_at: datetime

    dataset_id: str

    label: str

    properties: Dict[str, EntityProperties]

    updated_at: datetime


RelationshipProperties: TypeAlias = Union[str, bool, float, Image]


class Relationship(BaseModel):
    from_id: str

    label: str

    properties: Dict[str, RelationshipProperties]

    to_id: str


SimilarEntityProperties: TypeAlias = Union[str, bool, float, Image]


class SimilarEntity(BaseModel):
    id: str

    created_at: datetime

    dataset_id: str

    label: str

    properties: Dict[str, SimilarEntityProperties]

    updated_at: datetime


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


SourceLocation: TypeAlias = Union[SourceLocationText, SourceLocationVisual, SourceLocationPage, None]


class Source(BaseModel):
    id: str

    created_at: datetime

    is_summary: bool

    user_specified: bool

    link: Optional[source.Source] = None

    location: Optional[SourceLocation] = None

    step_id: Optional[str] = None


class EntityViewResponse(BaseModel):
    connected_entities: List[ConnectedEntity]

    entity: Entity

    last_updated: str

    relationships: List[Relationship]

    similar_entities: List[SimilarEntity]

    sources: List[Source]
