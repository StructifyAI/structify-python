# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .table_param import TableParam
from .strategy_param import StrategyParam
from .property_type_param import PropertyTypeParam
from .relationship_merge_strategy_param import RelationshipMergeStrategyParam

__all__ = ["DatasetCreateParams", "Relationship", "RelationshipProperty"]


class DatasetCreateParams(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    relationships: Required[Iterable[Relationship]]

    tables: Required[Iterable[TableParam]]

    llm_override_field: Optional[str]


class RelationshipProperty(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    merge_strategy: StrategyParam

    prop_type: PropertyTypeParam


class Relationship(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    source_table: Required[str]

    target_table: Required[str]

    merge_strategy: Optional[RelationshipMergeStrategyParam]

    properties: Iterable[RelationshipProperty]
