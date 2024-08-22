# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

from typing import List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = ["PropertyType", "Enum"]

class Enum(BaseModel):
    enum: List[str] = FieldInfo(alias = "Enum")

PropertyType: TypeAlias = Union[Literal["String"], Enum, Literal["Integer"]]