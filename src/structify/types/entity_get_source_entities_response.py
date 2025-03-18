# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .image import Image
from .source import Source
from .._models import BaseModel

__all__ = [
    "EntityGetSourceEntitiesResponse",
    "SourceEntity",
    "SourceEntityProperties",
    "SourceEntityLocation",
    "SourceEntityLocationText",
    "SourceEntityLocationTextText",
    "SourceEntityLocationVisual",
    "SourceEntityLocationVisualVisual",
    "SourceEntityLocationPage",
    "SourceEntityLocationPagePage",
]

SourceEntityProperties: TypeAlias = Union[str, bool, float, Image]


class SourceEntityLocationTextText(BaseModel):
    byte_offset: int


class SourceEntityLocationText(BaseModel):
    text: SourceEntityLocationTextText = FieldInfo(alias="Text")


class SourceEntityLocationVisualVisual(BaseModel):
    x: int

    y: int


class SourceEntityLocationVisual(BaseModel):
    visual: SourceEntityLocationVisualVisual = FieldInfo(alias="Visual")


class SourceEntityLocationPagePage(BaseModel):
    page_number: int


class SourceEntityLocationPage(BaseModel):
    page: SourceEntityLocationPagePage = FieldInfo(alias="Page")


SourceEntityLocation: TypeAlias = Union[
    SourceEntityLocationText, SourceEntityLocationVisual, SourceEntityLocationPage, None
]


class SourceEntity(BaseModel):
    id: str

    created_at: datetime

    is_summary: bool

    label: str

    llm_id: int

    properties: Dict[str, SourceEntityProperties]

    source_id: str

    user_specified: bool

    job_id: Optional[str] = None

    kg_entity_id: Optional[str] = None

    link: Optional[Source] = None

    location: Optional[SourceEntityLocation] = None

    step_id: Optional[str] = None


class EntityGetSourceEntitiesResponse(BaseModel):
    source_entities: List[List[SourceEntity]]
