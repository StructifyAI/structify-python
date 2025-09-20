# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .location_result import LocationResult

__all__ = ["LocationResponse"]


class LocationResponse(BaseModel):
    locations: List[LocationResult]
    """Array of location results"""

    search_information: Optional[object] = None
    """Search information"""
