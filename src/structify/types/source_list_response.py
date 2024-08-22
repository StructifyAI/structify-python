# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

from datetime import datetime

from .source import Source

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = ["SourceListResponse", "Location", "LocationText", "LocationTextText", "LocationVisual", "LocationVisualVisual"]

class LocationTextText(BaseModel):
    byte_offset: int

class LocationText(BaseModel):
    text: LocationTextText = FieldInfo(alias = "Text")

class LocationVisualVisual(BaseModel):
    x: int

    y: int

class LocationVisual(BaseModel):
    visual: LocationVisualVisual = FieldInfo(alias = "Visual")

Location: TypeAlias = Union[LocationText, LocationVisual, Literal["None"]]

class SourceListResponse(BaseModel):
    id: str

    creation_time: datetime

    link: Source

    location: Location