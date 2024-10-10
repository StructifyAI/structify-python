# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .property_type import PropertyType

__all__ = ["Table", "Property"]


class Property(BaseModel):
    description: str

    name: str

    merge_strategy: Optional[Literal["Unique", "FuzzyMatch", "None"]] = None

    prop_type: Optional[PropertyType] = None


class Table(BaseModel):
    description: str

    name: str
    """Organized in a name, description format."""

    properties: List[Property]
    """Organized in a name, description format."""
