# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["DatasetDescriptorParam", "Table", "TableProperty", "TableRelationship"]


class TableProperty(TypedDict, total=False):
    description: Required[str]

    name: Required[str]


class TableRelationship(TypedDict, total=False):
    description: Required[str]

    name: Required[str]


class Table(TypedDict, total=False):
    description: Required[str]

    name: Required[str]
    """Organized in a name, description format."""

    properties: Required[Iterable[TableProperty]]
    """Organized in a name, description format."""

    relationships: Required[Iterable[TableRelationship]]


class DatasetDescriptorParam(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    tables: Required[Iterable[Table]]
