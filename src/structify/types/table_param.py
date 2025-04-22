# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .strategy_param import StrategyParam
from .property_type_param import PropertyTypeParam

__all__ = ["TableParam", "Property"]


class Property(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    merge_strategy: StrategyParam

    prop_type: PropertyTypeParam


class TableParam(TypedDict, total=False):
    description: Required[str]

    name: Required[str]
    """Organized in a name, description format."""

    properties: Required[Iterable[Property]]
    """Organized in a name, description format."""

    expected_cardinality: Optional[int]
    """Expected number of unique values in the complete dataset.

    This is used for our probabilistic merge strategy.
    """

    primary_column: Optional[str]
