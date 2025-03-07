# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .image import Image
from .source import Source
from .._models import BaseModel

__all__ = [
    "EntityGetSourceEntitiesResponse",
    "SourceEntity",
    "SourceEntityLocation",
    "SourceEntityLocationByteOffset",
    "SourceEntityLocationUnionMember1",
    "SourceEntityLocationPageNumber",
    "SourceEntityProperties",
]


class SourceEntityLocationByteOffset(BaseModel):
    byte_offset: int


class SourceEntityLocationUnionMember1(BaseModel):
    x: int

    y: int


class SourceEntityLocationPageNumber(BaseModel):
    page_number: int


SourceEntityLocation: TypeAlias = Union[
    SourceEntityLocationByteOffset, SourceEntityLocationUnionMember1, SourceEntityLocationPageNumber, Optional[object]
]

SourceEntityProperties: TypeAlias = Union[str, bool, float, Image]


class SourceEntity(BaseModel):
    id: str

    creation_time: datetime

    is_summary: bool

    label: str

    link: Source

    llm_id: int

    location: SourceEntityLocation

    properties: Dict[str, SourceEntityProperties]

    user_specified: bool


class EntityGetSourceEntitiesResponse(BaseModel):
    source_entities: List[List[SourceEntity]]
