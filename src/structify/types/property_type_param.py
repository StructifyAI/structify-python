# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PropertyTypeParam", "Enum", "EnumEnum"]


class EnumEnum(TypedDict, total=False):
    types: Required[List[str]]


class Enum(TypedDict, total=False):
    enum: Required[Annotated[EnumEnum, PropertyInfo(alias="Enum")]]


PropertyTypeParam = Union[Literal["String"], Enum, Literal["Integer"]]
