# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["DatasetMatchResponse", "DatasetMatchResponseItem"]


class DatasetMatchResponseItem(BaseModel):
    entity: str

    score: float


DatasetMatchResponse: TypeAlias = Dict[str, DatasetMatchResponseItem]
