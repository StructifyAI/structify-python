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
    "TablePropertyPropType",
    "TablePropertyPropTypeEnum",
]


class Relationship(BaseModel):
    description: str

    name: str

    source_table: str

    target_table: str


class TablePropertyPropTypeEnum(BaseModel):
    enum: str = FieldInfo(alias="Enum")


TablePropertyPropType = Union[Literal["String"], TablePropertyPropTypeEnum, Literal["Integer"]]


class TableProperty(BaseModel):
    description: str

    name: str

    merge_strategy: Optional[Literal["Unique", "FuzzyMatch", "None"]] = None

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
