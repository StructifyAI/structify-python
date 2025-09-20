# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .location_coordinates import LocationCoordinates

__all__ = ["LocationResult"]


class LocationResult(BaseModel):
    name: str
    """Location name"""

    address: Optional[str] = None
    """Full address"""

    coordinates: Optional[LocationCoordinates] = None

    location_type: Optional[str] = None
    """Location type (city, country, etc.)"""

    place_id: Optional[str] = None
    """Place ID (if available)"""
