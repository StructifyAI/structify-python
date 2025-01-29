# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = ["TrainingDatasetSizeResponse", "TrainingDatasetSizeResponseItem"]


class TrainingDatasetSizeResponseItem(BaseModel):
    count: int

    name: str

    status: Literal[
        "Unlabeled", "NavLabeled", "SaveLabeled", "Verified", "Pending", "Skipped", "SuspiciousNav", "SuspiciousSave"
    ]


TrainingDatasetSizeResponse: TypeAlias = List[TrainingDatasetSizeResponseItem]
