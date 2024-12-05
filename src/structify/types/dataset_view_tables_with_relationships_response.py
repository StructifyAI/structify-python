# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = [
    "DatasetViewTablesWithRelationshipsResponse",
    "ConnectedEntity",
    "ConnectedEntityProperties",
    "ConnectedEntityPropertiesImage",
    "Entity",
    "EntityProperties",
    "EntityPropertiesImage",
    "Relationship",
    "RelationshipProperties",
    "RelationshipPropertiesImage",
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


class DatasetViewTablesWithRelationshipsResponse(BaseModel):
    connected_entities: List[ConnectedEntity]

    entities: List[Entity]

    relationships: List[Relationship]
