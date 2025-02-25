# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = ["TrainingDatasetGetLabellerStatsResponse", "TrainingDatasetGetLabellerStatsResponseItem"]


class TrainingDatasetGetLabellerStatsResponseItem(BaseModel):
    author: str

    count: int

    dataset: str

    period: datetime

    status: Literal[
        "Unlabeled",
        "NavLabeled",
        "SaveLabeled",
        "NavVerified",
        "SaveVerified",
        "Pending",
        "Skipped",
        "SuspiciousNav",
        "SuspiciousSave",
        "PotentialSuspiciousNav",
        "PotentialSuspiciousSave",
    ]


TrainingDatasetGetLabellerStatsResponse: TypeAlias = List[TrainingDatasetGetLabellerStatsResponseItem]
