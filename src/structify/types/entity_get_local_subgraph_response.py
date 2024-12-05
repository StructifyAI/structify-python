# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = [
    "EntityGetLocalSubgraphResponse",
    "Neighbor",
    "NeighborProperties",
    "NeighborPropertiesImage",
    "Relationship",
    "RelationshipProperties",
    "RelationshipPropertiesImage",
]


class NeighborPropertiesImage(BaseModel):
    number: int

    hash: Optional[str] = None


NeighborProperties: TypeAlias = Union[str, bool, float, NeighborPropertiesImage]


class Neighbor(BaseModel):
    id: str

    creation_time: datetime

    label: str

    properties: Dict[str, NeighborProperties]


class RelationshipPropertiesImage(BaseModel):
    number: int

    hash: Optional[str] = None


RelationshipProperties: TypeAlias = Union[str, bool, float, RelationshipPropertiesImage]


class Relationship(BaseModel):
    from_id: str

    label: str

    properties: Dict[str, RelationshipProperties]

    to_id: str


class EntityGetLocalSubgraphResponse(BaseModel):
    neighbors: List[Neighbor]

    relationships: List[Relationship]
