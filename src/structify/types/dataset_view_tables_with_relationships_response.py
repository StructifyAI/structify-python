# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union
from datetime import datetime

from .._models import BaseModel

__all__ = ["DatasetViewTablesWithRelationshipsResponse", "ConnectedEntity", "Entity", "Relationship"]


class ConnectedEntity(BaseModel):
    id: str

    creation_time: datetime

    label: str

    properties: Dict[str, Union[str, bool, float]]


class Entity(BaseModel):
    id: str

    creation_time: datetime

    label: str

    properties: Dict[str, Union[str, bool, float]]


class Relationship(BaseModel):
    from_id: str

    label: str

    properties: Dict[str, Union[str, bool, float]]

    to_id: str


class DatasetViewTablesWithRelationshipsResponse(BaseModel):
    connected_entities: List[ConnectedEntity]

    entities: List[Entity]

    relationships: List[Relationship]
