# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "PropertyParam",
    "MergeStrategy",
    "MergeStrategyPropertyAttr",
    "MergeStrategyFuzzyStringMatch",
    "PropType",
    "PropTypeEnum",
    "PropTypeEnumEnum",
]


class MergeStrategyPropertyAttr(TypedDict, total=False):
    property_attr: Required[Annotated[str, PropertyInfo(alias="PropertyAttr")]]


class MergeStrategyFuzzyStringMatch(TypedDict, total=False):
    fuzzy_string_match: Required[Annotated[str, PropertyInfo(alias="FuzzyStringMatch")]]
    """
    merge on some list of property names iff the values are the same in the
    extracted KgEntity
    """


MergeStrategy = Union[MergeStrategyPropertyAttr, MergeStrategyFuzzyStringMatch, Literal["None"]]


class PropTypeEnumEnum(TypedDict, total=False):
    types: Required[List[str]]


class PropTypeEnum(TypedDict, total=False):
    enum: Required[Annotated[PropTypeEnumEnum, PropertyInfo(alias="Enum")]]


PropType = Union[Literal["String"], PropTypeEnum, Literal["Integer"]]


class PropertyParam(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    merge_strategy: MergeStrategy
    """
    merge on two entities if they have two property keys listed in this type that
    return true to some fuzzy string matching function
    """

    prop_type: PropType
