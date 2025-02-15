# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["EvaluateListResponse", "EvaluateListResponseItem"]


class EvaluateListResponseItem(BaseModel):
    id: str

    dataset_1: str

    dataset_2: str

    email_1: str

    email_2: str

    started_at: datetime


EvaluateListResponse: TypeAlias = List[EvaluateListResponseItem]
