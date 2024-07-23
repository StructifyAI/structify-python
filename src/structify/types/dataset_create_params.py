# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "DatasetCreateParams",
    "Relationship",
    "Table",
    "TableProperty",
    "TablePropertyMergeStrategy",
    "TablePropertyMergeStrategyPropertyAttr",
    "TablePropertyMergeStrategyFuzzyStringMatch",
    "TablePropertyPropType",
    "TablePropertyPropTypeEnum",
    "TablePropertyPropTypeEnumEnum",
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


class TablePropertyMergeStrategyPropertyAttr(TypedDict, total=False):
    property_attr: Required[Annotated[str, PropertyInfo(alias="PropertyAttr")]]


class TablePropertyMergeStrategyFuzzyStringMatch(TypedDict, total=False):
    fuzzy_string_match: Required[Annotated[str, PropertyInfo(alias="FuzzyStringMatch")]]
    """
    merge on some list of property names iff the values are the same in the
    extracted KgEntity
    """


TablePropertyMergeStrategy = Union[
    TablePropertyMergeStrategyPropertyAttr, TablePropertyMergeStrategyFuzzyStringMatch, Literal["None"]
]


class TablePropertyPropTypeEnumEnum(TypedDict, total=False):
    types: Required[List[str]]


class TablePropertyPropTypeEnum(TypedDict, total=False):
    enum: Required[Annotated[TablePropertyPropTypeEnumEnum, PropertyInfo(alias="Enum")]]


TablePropertyPropType = Union[Literal["String"], TablePropertyPropTypeEnum, Literal["Integer"]]


class TableProperty(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    merge_strategy: TablePropertyMergeStrategy
    """
    merge on two entities if they have two property keys listed in this type that
    return true to some fuzzy string matching function
    """

    prop_type: TablePropertyPropType


class Table(TypedDict, total=False):
    description: Required[str]

    name: Required[str]
    """Organized in a name, description format."""

    properties: Required[Iterable[TableProperty]]
    """Organized in a name, description format."""
