# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = ["TrainingDatasetListDatumsResponse", "TrainingDatasetListDatumsResponseItem"]


class TrainingDatasetListDatumsResponseItem(BaseModel):
    id: str

    last_updated: datetime

    nav_labelers: List[str]

    nav_verifiers: List[str]

    save_labelers: List[str]

    save_verifiers: List[str]

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
    ]

    origin: Optional[Literal["HumanLLM", "UserReported", "ManualUpload", "ManualTransfer", "ToolParseFailure"]] = None


TrainingDatasetListDatumsResponse: TypeAlias = List[TrainingDatasetListDatumsResponseItem]
