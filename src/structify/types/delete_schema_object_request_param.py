# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["DeleteSchemaObjectRequestParam", "UnionMember0", "UnionMember1", "UnionMember2", "UnionMember3"]


class UnionMember0(TypedDict, total=False):
    id: Required[str]

    type: Required[Literal["column"]]


class UnionMember1(TypedDict, total=False):
    id: Required[str]

    type: Required[Literal["table"]]


class UnionMember2(TypedDict, total=False):
    id: Required[str]

    type: Required[Literal["schema"]]


class UnionMember3(TypedDict, total=False):
    id: Required[str]

    type: Required[Literal["database"]]


DeleteSchemaObjectRequestParam: TypeAlias = Union[UnionMember0, UnionMember1, UnionMember2, UnionMember3]
