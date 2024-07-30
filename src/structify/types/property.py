# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "Property",
    "MergeStrategy",
    "MergeStrategyPropertyAttr",
    "MergeStrategyFuzzyStringMatch",
    "PropType",
    "PropTypeEnum",
    "PropTypeEnumEnum",
]


class MergeStrategyPropertyAttr(BaseModel):
    property_attr: str = FieldInfo(alias="PropertyAttr")


class MergeStrategyFuzzyStringMatch(BaseModel):
    fuzzy_string_match: str = FieldInfo(alias="FuzzyStringMatch")
    """
    merge on some list of property names iff the values are the same in the
    extracted KgEntity
    """


MergeStrategy = Union[MergeStrategyPropertyAttr, MergeStrategyFuzzyStringMatch, Literal["None"]]


class PropTypeEnumEnum(BaseModel):
    types: List[str]


class PropTypeEnum(BaseModel):
    enum: PropTypeEnumEnum = FieldInfo(alias="Enum")


PropType = Union[Literal["String"], PropTypeEnum, Literal["Integer"]]


class Property(BaseModel):
    description: str

    name: str

    merge_strategy: Optional[MergeStrategy] = None
    """
    merge on two entities if they have two property keys listed in this type that
    return true to some fuzzy string matching function
    """

    prop_type: Optional[PropType] = None
