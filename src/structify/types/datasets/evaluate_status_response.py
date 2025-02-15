# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["EvaluateStatusResponse", "Failed"]


class Failed(BaseModel):
    failed: str = FieldInfo(alias="Failed")


EvaluateStatusResponse: TypeAlias = Union[Literal["Running", "Completed"], Failed]
