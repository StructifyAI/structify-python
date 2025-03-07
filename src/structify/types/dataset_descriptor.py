# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .table import Table
from .._models import BaseModel
from .strategy import Strategy
from .property_type import PropertyType
from .relationship_merge_strategy import RelationshipMergeStrategy

__all__ = ["DatasetDescriptor", "Relationship", "RelationshipProperty"]


class RelationshipProperty(BaseModel):
    description: str

    name: str

    merge_strategy: Optional[Strategy] = None

    prop_type: Optional[PropertyType] = None


class Relationship(BaseModel):
    description: str

    name: str

    source_table: str

    target_table: str

    merge_strategy: Optional[RelationshipMergeStrategy] = None

    properties: Optional[List[RelationshipProperty]] = None


class DatasetDescriptor(BaseModel):
    description: str

    name: str

    relationships: List[Relationship]

    tables: List[Table]

    llm_override_field: Optional[str] = None
