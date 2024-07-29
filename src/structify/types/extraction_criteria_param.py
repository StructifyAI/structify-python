# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "ExtractionCriteriaParam",
    "RequiredRelationship",
    "RequiredEntity",
    "RequiredProperty",
]


class RequiredRelationship(TypedDict, total=False):
    relationship_name: Required[str]
    required_relationship: Required[
        Annotated[dict, PropertyInfo(alias="RequiredRelationship")]
    ]


class RequiredEntity(TypedDict, total=False):
    entity_id: Required[int]
    required_entity: Required[Annotated[dict, PropertyInfo(alias="RequiredEntity")]]


class RequiredProperty(TypedDict, total=False):
    property_names: Required[List[str]]

    table_name: Required[str]
    """Vec<ExtractionCriteria> = it has to meet every one."""

    required_property: Required[Annotated[dict, PropertyInfo(alias="RequiredProperty")]]


ExtractionCriteriaParam = Union[RequiredRelationship, RequiredEntity, RequiredProperty]
