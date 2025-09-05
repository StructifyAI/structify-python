# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Message", "Content", "ContentText", "ContentImage"]


class ContentText(BaseModel):
    text: str = FieldInfo(alias="Text")


class ContentImage(BaseModel):
    image: object = FieldInfo(alias="Image")


Content: TypeAlias = Union[ContentText, ContentImage]


class Message(BaseModel):
    content: List[Content]
    """
    We want this to be a vec of contents so we can accurately capture an
    interleaving of images and text.

    This is meant to be a completely raw, unprocessed representation of the text.
    Don't take stuff out.
    """

    role: Literal["user", "system", "assistant"]
