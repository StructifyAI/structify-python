# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ExtractionCriteria",
    "Relationship",
    "RelationshipRelationship",
    "Entity",
    "EntityEntity",
    "Property",
    "PropertyProperty",
]


class RelationshipRelationship(BaseModel):
    relationship_name: str


class Relationship(BaseModel):
    relationship: RelationshipRelationship = FieldInfo(alias="Relationship")


class EntityEntity(BaseModel):
    seeded_kg_id: int
    """The integer id corresponding to an entity in the seeded kg"""

    dataset_entity_id: Optional[str] = None


class Entity(BaseModel):
    entity: EntityEntity = FieldInfo(alias="Entity")


class PropertyProperty(BaseModel):
    property_names: List[str]

    table_name: str
    """Vec<ExtractionCriteria> = it has to meet every one."""


class Property(BaseModel):
    property: PropertyProperty = FieldInfo(alias="Property")


ExtractionCriteria: TypeAlias = Union[Relationship, Entity, Property]
