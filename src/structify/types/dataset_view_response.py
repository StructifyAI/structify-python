# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional

from pydantic import Field

from .._models import BaseModel

__all__ = ["DatasetViewResponse", "Entity", "EntityEntity", "Relationship", "RelationshipRelationship"]


class Entity(BaseModel):
    id: str
    label: str
    properties: Dict[str, Union[Optional[str], Optional[bool], Optional[int]]]
    entity: dict = Field(alias="Entity")


class Relationship(BaseModel):
    label: str
    from_id: str
    to_id: str
    relationship: dict = Field(alias="Relationship")


DatasetViewResponse = Union[Entity, Relationship]
