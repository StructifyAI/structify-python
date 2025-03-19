# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .datum_status import DatumStatus

__all__ = ["TrainingDatasetListDatumsResponse", "TrainingDatasetListDatumsResponseItem"]


class TrainingDatasetListDatumsResponseItem(BaseModel):
    id: str

    nav_labelers: List[str]

    nav_verifiers: List[str]

    save_labelers: List[str]

    save_verifiers: List[str]

    status: DatumStatus

    updated_at: datetime

    origin: Optional[
        Literal["human_l_l_m", "user_reported", "manual_upload", "manual_transfer", "tool_parse_failure"]
    ] = None


TrainingDatasetListDatumsResponse: TypeAlias = List[TrainingDatasetListDatumsResponseItem]
