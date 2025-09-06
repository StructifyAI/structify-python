# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["MessageParam", "Content", "ContentText", "ContentImage"]


class ContentText(TypedDict, total=False):
    text: Required[Annotated[str, PropertyInfo(alias="Text")]]


class ContentImage(TypedDict, total=False):
    image: Required[Annotated[FileTypes, PropertyInfo(alias="Image")]]


Content: TypeAlias = Union[ContentText, ContentImage]


class MessageParam(TypedDict, total=False):
    content: Required[Iterable[Content]]
    """
    We want this to be a vec of contents so we can accurately capture an
    interleaving of images and text.

    This is meant to be a completely raw, unprocessed representation of the text.
    Don't take stuff out.
    """

    role: Required[Literal["user", "system", "assistant"]]
