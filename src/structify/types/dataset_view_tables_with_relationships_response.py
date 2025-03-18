# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union
from datetime import datetime
from typing_extensions import TypeAlias

from .image import Image
from .._models import BaseModel

__all__ = [
    "DatasetViewTablesWithRelationshipsResponse",
    "ConnectedEntity",
    "ConnectedEntityProperties",
    "Entity",
    "EntityProperties",
    "Relationship",
    "RelationshipProperties",
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


class DatasetViewTablesWithRelationshipsResponse(BaseModel):
    connected_entities: List[ConnectedEntity]

    entities: List[Entity]

    relationships: List[Relationship]
