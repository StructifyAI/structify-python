# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union
from typing_extensions import TypeAlias

from .image import Image
from .._models import BaseModel
from .structify_entity import StructifyEntity

__all__ = ["EntityGetLocalSubgraphResponse", "Relationship", "RelationshipProperties"]

RelationshipProperties: TypeAlias = Union[str, bool, float, Image]


class Relationship(BaseModel):
    from_id: str

    label: str

    properties: Dict[str, RelationshipProperties]

    to_id: str


class EntityGetLocalSubgraphResponse(BaseModel):
    neighbors: List[StructifyEntity]

    relationships: List[Relationship]
