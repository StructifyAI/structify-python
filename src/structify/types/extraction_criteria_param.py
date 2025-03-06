# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "ExtractionCriteriaParam",
    "Relationship",
    "RelationshipRelationship",
    "Entity",
    "EntityEntity",
    "Property",
    "PropertyProperty",
]


class RelationshipRelationship(TypedDict, total=False):
    relationship_name: Required[str]


class Relationship(TypedDict, total=False):
    relationship: Required[Annotated[RelationshipRelationship, PropertyInfo(alias="Relationship")]]


class EntityEntity(TypedDict, total=False):
    seeded_kg_id: Required[int]
    """The integer id corresponding to an entity in the seeded kg"""

    dataset_entity_id: Optional[str]


class Entity(TypedDict, total=False):
    entity: Required[Annotated[EntityEntity, PropertyInfo(alias="Entity")]]


class PropertyProperty(TypedDict, total=False):
    property_names: Required[List[str]]

    table_name: Required[str]
    """Vec<ExtractionCriteria> = it has to meet every one."""


class Property(TypedDict, total=False):
    property: Required[Annotated[PropertyProperty, PropertyInfo(alias="Property")]]


ExtractionCriteriaParam: TypeAlias = Union[Relationship, Entity, Property]
