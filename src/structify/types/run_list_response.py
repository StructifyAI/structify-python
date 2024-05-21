# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RunListResponse", "RunListResponseItem"]


class RunListResponseItem(BaseModel):
    id: str

    status: Literal["Running", "Completed", "Failed"]


RunListResponse = List[RunListResponseItem]
