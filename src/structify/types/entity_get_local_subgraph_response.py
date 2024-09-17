# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union
from datetime import datetime

from .._models import BaseModel

__all__ = ["EntityGetLocalSubgraphResponse", "Neighbor", "Relationship"]


class Neighbor(BaseModel):
    id: str

    creation_time: datetime

    label: str

    properties: Dict[str, Union[str, bool, float]]


class Relationship(BaseModel):
    from_id: str

    label: str

    properties: Dict[str, Union[str, bool, float]]

    to_id: str


class EntityGetLocalSubgraphResponse(BaseModel):
    neighbors: List[Neighbor]

    relationships: List[Relationship]
