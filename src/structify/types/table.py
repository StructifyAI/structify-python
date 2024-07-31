# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .property_type import PropertyType
from .merge_strategy import MergeStrategy

__all__ = ["Table", "Property"]


class Property(BaseModel):
    description: str

    name: str

    merge_strategy: Optional[MergeStrategy] = None
    """
    merge on two entities if they have two property keys listed in this type that
    return true to some fuzzy string matching function
    """

    prop_type: Optional[PropertyType] = None


class Table(BaseModel):
    description: str

    name: str
    """Organized in a name, description format."""

    properties: List[Property]
    """Organized in a name, description format."""
