# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["ConnectorDeleteSchemaObjectParams", "Variant0", "Variant1", "Variant2", "Variant3"]


class Variant0(TypedDict, total=False):
    id: Required[str]

    type: Required[Literal["column"]]


class Variant1(TypedDict, total=False):
    id: Required[str]

    type: Required[Literal["table"]]


class Variant2(TypedDict, total=False):
    id: Required[str]

    type: Required[Literal["schema"]]


class Variant3(TypedDict, total=False):
    id: Required[str]

    type: Required[Literal["database"]]


ConnectorDeleteSchemaObjectParams: TypeAlias = Union[Variant0, Variant1, Variant2, Variant3]
