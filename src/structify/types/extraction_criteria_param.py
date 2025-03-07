# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "ExtractionCriteriaParam",
    "RelationshipExtraction",
    "RelationshipExtractionRelationshipExtraction",
    "EntityExtraction",
    "EntityExtractionEntityExtraction",
    "GenericProperty",
    "GenericPropertyGenericProperty",
]


class RelationshipExtractionRelationshipExtraction(TypedDict, total=False):
    relationship_name: Required[str]


class RelationshipExtraction(TypedDict, total=False):
    relationship_extraction: Required[
        Annotated[RelationshipExtractionRelationshipExtraction, PropertyInfo(alias="RelationshipExtraction")]
    ]


class EntityExtractionEntityExtraction(TypedDict, total=False):
    seeded_kg_id: Required[int]
    """The integer id corresponding to an entity in the seeded kg"""

    dataset_entity_id: Optional[str]


class EntityExtraction(TypedDict, total=False):
    entity_extraction: Required[Annotated[EntityExtractionEntityExtraction, PropertyInfo(alias="EntityExtraction")]]


class GenericPropertyGenericProperty(TypedDict, total=False):
    property_names: Required[List[str]]

    table_name: Required[str]
    """Vec<ExtractionCriteria> = it has to meet every one."""


class GenericProperty(TypedDict, total=False):
    generic_property: Required[Annotated[GenericPropertyGenericProperty, PropertyInfo(alias="GenericProperty")]]


ExtractionCriteriaParam: TypeAlias = Union[RelationshipExtraction, EntityExtraction, GenericProperty]
