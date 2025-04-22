# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .strategy import Strategy
from .property_type import PropertyType

__all__ = ["Table", "Property"]


class Property(BaseModel):
    description: str

    name: str

    merge_strategy: Optional[Strategy] = None

    prop_type: Optional[PropertyType] = None


class Table(BaseModel):
    description: str

    name: str
    """Organized in a name, description format."""

    properties: List[Property]
    """Organized in a name, description format."""

    expected_cardinality: Optional[int] = None
    """Expected number of unique values in the complete dataset.

    This is used for our probabilistic merge strategy.
    """

    primary_column: Optional[str] = None
