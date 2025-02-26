# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..._models import BaseModel
from .datum_status import DatumStatus

__all__ = ["TrainingDatasetSizeResponse", "TrainingDatasetSizeResponseItem"]


class TrainingDatasetSizeResponseItem(BaseModel):
    count: int

    name: str

    status: DatumStatus


TrainingDatasetSizeResponse: TypeAlias = List[TrainingDatasetSizeResponseItem]
