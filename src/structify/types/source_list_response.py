# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .source import Source
from .._models import BaseModel

__all__ = [
    "SourceListResponse",
    "Location",
    "Text",
    "Visual",
]


class Text(BaseModel):
    byte_offset: int

    text: dict = FieldInfo(alias="Text")


class Visual(BaseModel):
    x: int

    y: int

    visual: dict = FieldInfo(alias="Visual")


Location = Union[Text, Visual, Literal["None"]]


class SourceListResponse(BaseModel):
    id: str

    link: Source

    location: Location
