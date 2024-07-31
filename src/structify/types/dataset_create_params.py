# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "DatasetCreateParams",
    "Relationship",
    "Table",
    "TableProperty",
    "TablePropertyPropType",
    "TablePropertyPropTypeEnum",
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


class TablePropertyPropTypeEnum(TypedDict, total=False):
    enum: Required[Annotated[str, PropertyInfo(alias="Enum")]]


TablePropertyPropType = Union[Literal["String"], TablePropertyPropTypeEnum, Literal["Integer"]]


class TableProperty(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    merge_strategy: Literal["Unique", "FuzzyMatch", "None"]

    prop_type: TablePropertyPropType


class Table(TypedDict, total=False):
    description: Required[str]

    name: Required[str]
    """Organized in a name, description format."""

    properties: Required[Iterable[TableProperty]]
    """Organized in a name, description format."""
