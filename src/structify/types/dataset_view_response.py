# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["DatasetViewResponse", "Entity", "EntityEntity", "Relationship", "RelationshipRelationship"]


class EntityEntity(BaseModel):
    id: str

    creation_time: datetime

    label: str

    properties: Dict[str, Union[Optional[str], Optional[bool], Optional[int]]]


class Entity(BaseModel):
    entity: EntityEntity = FieldInfo(alias="Entity")


class RelationshipRelationship(BaseModel):
    from_id: str

    label: str

    to_id: str


class Relationship(BaseModel):
    relationship: RelationshipRelationship = FieldInfo(alias="Relationship")


DatasetViewResponse: TypeAlias = Union[Entity, Relationship]
