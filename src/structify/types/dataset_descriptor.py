# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["DatasetDescriptor", "Relationship", "Table", "TableProperty"]


class Relationship(BaseModel):
    description: str

    name: str

    source_table: str

    target_table: str


class TableProperty(BaseModel):
    description: str

    name: str


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
