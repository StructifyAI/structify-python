# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = ["TrainingDatasetListDatumsResponse", "TrainingDatasetListDatumsResponseItem"]


class TrainingDatasetListDatumsResponseItem(BaseModel):
    id: str

    last_updated: datetime

    nav_labelers: List[str]

    save_labelers: List[str]

    status: Literal[
        "Unlabeled", "NavLabeled", "SaveLabeled", "Verified", "Pending", "Skipped", "SuspiciousNav", "SuspiciousSave"
    ]

    verifiers: List[str]


TrainingDatasetListDatumsResponse: TypeAlias = List[TrainingDatasetListDatumsResponseItem]
