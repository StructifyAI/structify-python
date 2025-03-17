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
    id: int

    creation_time: datetime

    dataset_id: object

    label: str

    properties: object


class Entity(BaseModel):
    id: int

    creation_time: datetime

    dataset_id: object

    label: str

    properties: object


RelationshipProperties: TypeAlias = Union[str, bool, float, Image]


class Relationship(BaseModel):
    from_id: int

    label: str

    properties: Dict[str, RelationshipProperties]

    to_id: int


class SimilarEntity(BaseModel):
    id: int

    creation_time: datetime

    dataset_id: object

    label: str

    properties: object


class Source(BaseModel):
    id: int

    created_at: datetime

    is_summary: bool

    link: object

    location: object

    user_specified: bool

    step_id: Optional[int] = None


class EntityViewResponse(BaseModel):
    connected_entities: List[ConnectedEntity]

    entity: Entity

    last_updated: str

    relationships: List[Relationship]

    similar_entities: List[SimilarEntity]

    sources: List[Source]
