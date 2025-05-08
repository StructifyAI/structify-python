# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .source import Source
from .._models import BaseModel

__all__ = [
    "SourceListResponse",
    "SourceListResponseItem",
    "SourceListResponseItemLocation",
    "SourceListResponseItemLocationText",
    "SourceListResponseItemLocationTextText",
    "SourceListResponseItemLocationVisual",
    "SourceListResponseItemLocationVisualVisual",
    "SourceListResponseItemLocationPage",
    "SourceListResponseItemLocationPagePage",
]


class SourceListResponseItemLocationTextText(BaseModel):
    byte_offset: int


class SourceListResponseItemLocationText(BaseModel):
    text: SourceListResponseItemLocationTextText = FieldInfo(alias="Text")


class SourceListResponseItemLocationVisualVisual(BaseModel):
    x: int

    y: int


class SourceListResponseItemLocationVisual(BaseModel):
    visual: SourceListResponseItemLocationVisualVisual = FieldInfo(alias="Visual")


class SourceListResponseItemLocationPagePage(BaseModel):
    page_number: int


class SourceListResponseItemLocationPage(BaseModel):
    page: SourceListResponseItemLocationPagePage = FieldInfo(alias="Page")


SourceListResponseItemLocation: TypeAlias = Union[
    SourceListResponseItemLocationText, SourceListResponseItemLocationVisual, SourceListResponseItemLocationPage, None
]


class SourceListResponseItem(BaseModel):
    id: str

    created_at: datetime

    is_summary: bool

    user_specified: bool

    link: Optional[Source] = None

    location: Optional[SourceListResponseItemLocation] = None

    scraper_id: Optional[str] = None

    step_id: Optional[str] = None


SourceListResponse: TypeAlias = List[SourceListResponseItem]
