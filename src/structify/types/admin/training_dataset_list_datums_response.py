# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = ["TrainingDatasetListDatumsResponse", "TrainingDatasetListDatumsResponseItem"]


class TrainingDatasetListDatumsResponseItem(BaseModel):
    id: str

    labelers: List[str]

    last_updated: datetime

    status: Literal["Unlabeled", "Labeled", "Verified", "Pending", "Skipped"]


TrainingDatasetListDatumsResponse: TypeAlias = List[TrainingDatasetListDatumsResponseItem]
