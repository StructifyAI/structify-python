# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .source import Source
from .._models import BaseModel

__all__ = [
    "SourceListResponse",
    "SourceListResponseItem",
    "SourceListResponseItemLocation",
    "SourceListResponseItemLocationByteOffset",
    "SourceListResponseItemLocationUnionMember1",
    "SourceListResponseItemLocationPageNumber",
]


class SourceListResponseItemLocationByteOffset(BaseModel):
    byte_offset: int


class SourceListResponseItemLocationUnionMember1(BaseModel):
    x: int

    y: int


class SourceListResponseItemLocationPageNumber(BaseModel):
    page_number: int


SourceListResponseItemLocation: TypeAlias = Union[
    SourceListResponseItemLocationByteOffset,
    SourceListResponseItemLocationUnionMember1,
    SourceListResponseItemLocationPageNumber,
    Optional[object],
]


class SourceListResponseItem(BaseModel):
    id: str

    creation_time: datetime

    is_summary: bool

    link: Source

    location: SourceListResponseItemLocation

    user_specified: bool


SourceListResponse: TypeAlias = List[SourceListResponseItem]
