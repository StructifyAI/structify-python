# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "DatasetDescriptor",
    "Relationship",
    "Table",
    "TableProperty",
    "TablePropertyMergeStrategy",
    "TablePropertyMergeStrategyPropertyAttr",
    "TablePropertyMergeStrategyFuzzyStringMatch",
    "TablePropertyPropType",
    "TablePropertyPropTypeEnum",
    "TablePropertyPropTypeEnumEnum",
]


class Relationship(BaseModel):
    description: str

    name: str

    source_table: str

    target_table: str


class TablePropertyMergeStrategyPropertyAttr(BaseModel):
    property_attr: str = FieldInfo(alias="PropertyAttr")


class TablePropertyMergeStrategyFuzzyStringMatch(BaseModel):
    fuzzy_string_match: str = FieldInfo(alias="FuzzyStringMatch")
    """
    merge on some list of property names iff the values are the same in the
    extracted KgEntity
    """


TablePropertyMergeStrategy = Union[
    TablePropertyMergeStrategyPropertyAttr, TablePropertyMergeStrategyFuzzyStringMatch, Literal["None"]
]


class TablePropertyPropTypeEnumEnum(BaseModel):
    types: List[str]


class TablePropertyPropTypeEnum(BaseModel):
    enum: TablePropertyPropTypeEnumEnum = FieldInfo(alias="Enum")


TablePropertyPropType = Union[Literal["String"], TablePropertyPropTypeEnum, Literal["Integer"]]


class TableProperty(BaseModel):
    description: str

    name: str

    merge_strategy: Optional[TablePropertyMergeStrategy] = None
    """
    merge on two entities if they have two property keys listed in this type that
    return true to some fuzzy string matching function
    """

    prop_type: Optional[TablePropertyPropType] = None


class Table(BaseModel):
    description: str

    name: str
    """Organized in a name, description format."""

    properties: List[TableProperty]
    """Organized in a name, description format."""


class DatasetDescriptor(BaseModel):
    description: str

    name: str

    relationships: List[Relationship]

    tables: List[Table]
