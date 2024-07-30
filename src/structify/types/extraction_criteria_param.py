# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Required, Annotated, TypedDict

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
    entity_id: Required[int]


class EntityExtraction(TypedDict, total=False):
    entity_extraction: Required[Annotated[EntityExtractionEntityExtraction, PropertyInfo(alias="EntityExtraction")]]


class GenericPropertyGenericProperty(TypedDict, total=False):
    property_names: Required[List[str]]

    table_name: Required[str]
    """Vec<ExtractionCriteria> = it has to meet every one."""


class GenericProperty(TypedDict, total=False):
    generic_property: Required[Annotated[GenericPropertyGenericProperty, PropertyInfo(alias="GenericProperty")]]


ExtractionCriteriaParam = Union[RelationshipExtraction, EntityExtraction, GenericProperty]
