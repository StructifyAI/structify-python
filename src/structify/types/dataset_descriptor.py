# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .table import Table
from .._models import BaseModel

__all__ = ["DatasetDescriptor", "Relationship"]


class Relationship(BaseModel):
    description: str

    name: str

    source_table: str

    target_table: str


class DatasetDescriptor(BaseModel):
    description: str

    name: str

    relationships: List[Relationship]

    tables: List[Table]
