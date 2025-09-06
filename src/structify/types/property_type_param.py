# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["PropertyTypeParam", "Enum"]


class Enum(TypedDict, total=False):
    enum: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="Enum")]]


PropertyTypeParam: TypeAlias = Union[
    Literal["String", "Boolean", "Integer", "Float", "Date", "URL", "Money", "Image", "PersonName", "Address"], Enum
]
