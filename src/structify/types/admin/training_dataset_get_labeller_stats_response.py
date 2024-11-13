# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["TrainingDatasetGetLabellerStatsResponse", "TrainingDatasetGetLabellerStatsResponseItem"]


class TrainingDatasetGetLabellerStatsResponseItem(BaseModel):
    count: int

    labeller: str


TrainingDatasetGetLabellerStatsResponse: TypeAlias = List[TrainingDatasetGetLabellerStatsResponseItem]
