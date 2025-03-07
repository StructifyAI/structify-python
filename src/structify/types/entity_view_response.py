# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

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
    "SourceLocationByteOffset",
    "SourceLocationUnionMember1",
    "SourceLocationPageNumber",
]

ConnectedEntityProperties: TypeAlias = Union[str, bool, float, Image]


class ConnectedEntity(BaseModel):
    id: str

    creation_time: datetime

    label: str

    properties: Dict[str, ConnectedEntityProperties]


EntityProperties: TypeAlias = Union[str, bool, float, Image]


class Entity(BaseModel):
    id: str

    creation_time: datetime

    label: str

    properties: Dict[str, EntityProperties]


RelationshipProperties: TypeAlias = Union[str, bool, float, Image]


class Relationship(BaseModel):
    from_id: str

    label: str

    properties: Dict[str, RelationshipProperties]

    to_id: str


SimilarEntityProperties: TypeAlias = Union[str, bool, float, Image]


class SimilarEntity(BaseModel):
    id: str

    creation_time: datetime

    label: str

    properties: Dict[str, SimilarEntityProperties]


class SourceLocationByteOffset(BaseModel):
    byte_offset: int


class SourceLocationUnionMember1(BaseModel):
    x: int

    y: int


class SourceLocationPageNumber(BaseModel):
    page_number: int


SourceLocation: TypeAlias = Union[
    SourceLocationByteOffset, SourceLocationUnionMember1, SourceLocationPageNumber, Optional[object]
]


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
