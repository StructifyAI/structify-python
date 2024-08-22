# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .property_type_param import PropertyTypeParam

__all__ = ["TableParam", "Property"]


class Property(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    merge_strategy: Literal["Unique", "FuzzyMatch", "None"]

    prop_type: PropertyTypeParam


class TableParam(TypedDict, total=False):
    description: Required[str]

    name: Required[str]
    """Organized in a name, description format."""

    properties: Required[Iterable[Property]]
    """Organized in a name, description format."""
