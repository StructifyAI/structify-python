# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["GoogleMapsResult"]


class GoogleMapsResult(BaseModel):
    title: str
    """Place name/title"""

    address: Optional[str] = None
    """Address"""

    coordinates: Optional[object] = None
    """Coordinates"""

    phone: Optional[str] = None
    """Phone number"""

    place_id: Optional[str] = None
    """Place ID"""

    rating: Optional[float] = None
    """Rating (1-5 stars)"""

    reviews: Optional[int] = None
    """Number of reviews"""

    type: Optional[str] = FieldInfo(alias="type_", default=None)
    """Place type (restaurant, hotel, etc.)"""

    website: Optional[str] = None
    """Website URL"""
