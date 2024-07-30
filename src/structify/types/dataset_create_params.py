# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "DatasetCreateParams",
    "Relationship",
    "Table",
    "Property",
    "PropertyMergeStrategy",
    "PropertyMergeStrategyPropertyAttr",
    "PropertyMergeStrategyFuzzyStringMatch",
    "PropType",
    "PropTypeEnum",
    "PropTypeEnumEnum",
]


class DatasetCreateParams(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    relationships: Required[Iterable[Relationship]]

    tables: Required[Iterable[Table]]


class Relationship(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    source_table: Required[str]

    target_table: Required[str]


class PropertyMergeStrategyPropertyAttr(TypedDict, total=False):
    property_attr: Required[Annotated[str, PropertyInfo(alias="PropertyAttr")]]


class PropertyMergeStrategyFuzzyStringMatch(TypedDict, total=False):
    fuzzy_string_match: Required[Annotated[str, PropertyInfo(alias="FuzzyStringMatch")]]
    """
    merge on some list of property names iff the values are the same in the
    extracted KgEntity
    """


PropertyMergeStrategy = Union[
    PropertyMergeStrategyPropertyAttr, PropertyMergeStrategyFuzzyStringMatch, Literal["None"]
]


class PropTypeEnumEnum(TypedDict, total=False):
    types: Required[List[str]]


class PropTypeEnum(TypedDict, total=False):
    enum: Required[Annotated[PropTypeEnumEnum, PropertyInfo(alias="Enum")]]


PropType = Union[Literal["String"], PropTypeEnum, Literal["Integer"]]


class Property(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    merge_strategy: PropertyMergeStrategy
    """
    merge on two entities if they have two property keys listed in this type that
    return true to some fuzzy string matching function
    """

    prop_type: PropType


class Table(TypedDict, total=False):
    description: Required[str]

    name: Required[str]
    """Organized in a name, description format."""

    properties: Required[Iterable[Property]]
    """Organized in a name, description format."""
