# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .image import Image
from .._models import BaseModel

__all__ = [
    "EntityViewResponse",
    "ConnectedEntity",
    "Entity",
    "Relationship",
    "RelationshipProperties",
    "SimilarEntity",
    "Source",
]


class ConnectedEntity(BaseModel):
    id: str

    created_at: datetime

    dataset_id: object

    label: str

    properties: object

    updated_at: datetime


class Entity(BaseModel):
    id: str

    created_at: datetime

    dataset_id: object

    label: str

    properties: object

    updated_at: datetime


RelationshipProperties: TypeAlias = Union[str, bool, float, Image]


class Relationship(BaseModel):
    from_id: str

    label: str

    properties: Dict[str, RelationshipProperties]

    to_id: str


class SimilarEntity(BaseModel):
    id: str

    created_at: datetime

    dataset_id: object

    label: str

    properties: object

    updated_at: datetime


class Source(BaseModel):
    id: str

    created_at: datetime

    is_summary: bool

    user_specified: bool

    link: Optional[object] = None

    location: Optional[object] = None

    step_id: Optional[str] = None


class EntityViewResponse(BaseModel):
    connected_entities: List[ConnectedEntity]

    entity: Entity

    last_updated: str

    relationships: List[Relationship]

    similar_entities: List[SimilarEntity]

    sources: List[Source]
