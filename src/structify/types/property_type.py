# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PropertyType", "Enum"]


class Enum(BaseModel):
    enum: List[str] = FieldInfo(alias="Enum")


PropertyType: TypeAlias = Union[Literal["String"], Literal["Boolean"], Enum, Literal["Integer"], Literal["Float"]]
