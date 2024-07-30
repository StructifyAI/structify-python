# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MergeStrategyParam", "PropertyAttr", "FuzzyStringMatch"]


class PropertyAttr(TypedDict, total=False):
    property_attr: Required[Annotated[str, PropertyInfo(alias="PropertyAttr")]]


class FuzzyStringMatch(TypedDict, total=False):
    fuzzy_string_match: Required[Annotated[str, PropertyInfo(alias="FuzzyStringMatch")]]
    """
    merge on some list of property names iff the values are the same in the
    extracted KgEntity
    """


MergeStrategyParam = Union[PropertyAttr, FuzzyStringMatch, Literal["None"]]
