# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .property_type_param import PropertyTypeParam
from .merge_strategy_param import MergeStrategyParam

__all__ = ["TableParam", "Property"]


class Property(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    merge_strategy: MergeStrategyParam
    """
    merge on two entities if they have two property keys listed in this type that
    return true to some fuzzy string matching function
    """

    prop_type: PropertyTypeParam


class TableParam(TypedDict, total=False):
    description: Required[str]

    name: Required[str]
    """Organized in a name, description format."""

    properties: Required[Iterable[Property]]
    """Organized in a name, description format."""
