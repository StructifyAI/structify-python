# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .source import Source
from .._models import BaseModel

__all__ = [
    "SourceListResponse",
    "Location",
    "LocationText",
    "LocationTextText",
    "LocationVisual",
    "LocationVisualVisual",
]


class LocationTextText(BaseModel):
    byte_offset: int


class LocationText(BaseModel):
    text: LocationTextText = FieldInfo(alias="Text")


class LocationVisualVisual(BaseModel):
    x: int

    y: int


class LocationVisual(BaseModel):
    visual: LocationVisualVisual = FieldInfo(alias="Visual")


Location = Union[LocationText, LocationVisual, Literal["None"]]


class SourceListResponse(BaseModel):
    extra_properties: Dict[str, Union[Optional[str], Optional[bool], Optional[int]]]

    link: Source

    location: Location
