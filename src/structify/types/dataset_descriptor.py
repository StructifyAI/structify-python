# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["DatasetDescriptor", "Table", "TableProperty", "TableRelationship"]


class TableProperty(BaseModel):
    description: str

    name: str


class TableRelationship(BaseModel):
    description: str

    name: str


class Table(BaseModel):
    description: str

    name: str
    """Organized in a name, description format."""

    properties: List[TableProperty]
    """Organized in a name, description format."""

    relationships: List[TableRelationship]


class DatasetDescriptor(BaseModel):
    description: str

    name: str

    tables: List[Table]
