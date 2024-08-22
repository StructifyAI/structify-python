# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional, List

from typing_extensions import Literal

from .property_type import PropertyType

from .table import Table

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = ["DatasetDescriptor", "Relationship", "RelationshipProperty"]

class RelationshipProperty(BaseModel):
    description: str

    name: str

    merge_strategy: Optional[Literal["Unique", "FuzzyMatch", "None"]] = None

    prop_type: Optional[PropertyType] = None

class Relationship(BaseModel):
    description: str

    name: str

    source_table: str

    target_table: str

    properties: Optional[List[RelationshipProperty]] = None

class DatasetDescriptor(BaseModel):
    description: str

    name: str

    relationships: List[Relationship]

    tables: List[Table]