# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = ["TrainingDatasetListDatumsResponse", "TrainingDatasetListDatumsResponseItem"]


class TrainingDatasetListDatumsResponseItem(BaseModel):
    id: str

    labelers: List[str]

    last_updated: datetime

    review_messages: List[str]

    status: Literal["Unlabeled", "Labeled", "Verified", "Pending", "Skipped", "Suspicious"]

    last_labeled: Optional[datetime] = None

    last_verified: Optional[datetime] = None

    verifiers: Optional[List[str]] = None


TrainingDatasetListDatumsResponse: TypeAlias = List[TrainingDatasetListDatumsResponseItem]
