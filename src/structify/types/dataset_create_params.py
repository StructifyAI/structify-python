# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .table_param import TableParam
from .property_type_param import PropertyTypeParam

__all__ = ["DatasetCreateParams", "Relationship", "RelationshipProperty"]


class DatasetCreateParams(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    relationships: Required[Iterable[Relationship]]

    tables: Required[Iterable[TableParam]]


class RelationshipProperty(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    merge_strategy: Literal["Unique", "FuzzyMatch", "None"]

    prop_type: PropertyTypeParam


class Relationship(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    source_table: Required[str]

    target_table: Required[str]

    properties: Iterable[RelationshipProperty]
