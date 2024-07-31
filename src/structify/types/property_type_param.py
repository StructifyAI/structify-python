# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PropertyTypeParam", "Enum"]


class Enum(TypedDict, total=False):
    enum: Required[Annotated[str, PropertyInfo(alias="Enum")]]


PropertyTypeParam = Union[Literal["String"], Enum, Literal["Integer"]]
