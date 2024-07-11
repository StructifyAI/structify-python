# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["DatasetViewResponse", "Entity", "EntityEntity", "Relationship", "RelationshipRelationship"]


class EntityEntity(BaseModel):
    id: int

    label: str
    """
    Since all Entities have exactly two labels (ENTITY_LABEL and their table name),
    we only store the non-ENTITY_LABEL label here.
    """

    properties: Dict[str, Union[Optional[str], Optional[bool], Optional[int]]]


class Entity(BaseModel):
    entity: EntityEntity = FieldInfo(alias="Entity")


class RelationshipRelationship(BaseModel):
    from_id: int

    label: str

    to_id: int


class Relationship(BaseModel):
    relationship: RelationshipRelationship = FieldInfo(alias="Relationship")
    """Don't actually create these. These are solely used as return types in the API

    TODO: Remove them from models.
    """


DatasetViewResponse = Union[Entity, Relationship]
