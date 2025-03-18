# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union
from datetime import datetime
from typing_extensions import TypeAlias

from .image import Image
from .._models import BaseModel

__all__ = ["EntityGetLocalSubgraphResponse", "Neighbor", "NeighborProperties", "Relationship", "RelationshipProperties"]

NeighborProperties: TypeAlias = Union[str, bool, float, Image]


class Neighbor(BaseModel):
    id: str

    creation_time: datetime

    label: str

    properties: Dict[str, NeighborProperties]


RelationshipProperties: TypeAlias = Union[str, bool, float, Image]


class Relationship(BaseModel):
    from_id: str

    label: str

    properties: Dict[str, RelationshipProperties]

    to_id: str


class EntityGetLocalSubgraphResponse(BaseModel):
    neighbors: List[Neighbor]

    relationships: List[Relationship]
