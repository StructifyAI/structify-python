# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["ConnectorAddSchemaObjectResponse", "UnionMember0", "UnionMember1", "UnionMember2", "UnionMember3"]


class UnionMember0(BaseModel):
    id: str

    type: Literal["database"]


class UnionMember1(BaseModel):
    id: str

    type: Literal["schema"]


class UnionMember2(BaseModel):
    id: str

    type: Literal["table"]


class UnionMember3(BaseModel):
    id: str

    type: Literal["column"]


ConnectorAddSchemaObjectResponse: TypeAlias = Union[UnionMember0, UnionMember1, UnionMember2, UnionMember3]
