# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .strategy_param import StrategyParam
from .property_type_param import PropertyTypeParam

__all__ = ["DatasetAddPropertyParams", "Property"]


class DatasetAddPropertyParams(TypedDict, total=False):
    dataset_name: Required[str]

    property: Required[Property]

    table_name: Required[str]


class Property(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    merge_strategy: StrategyParam

    prop_type: PropertyTypeParam
