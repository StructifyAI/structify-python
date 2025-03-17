# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..image import Image
from ..._compat import PYDANTIC_V2
from ..._models import BaseModel

__all__ = [
    "EvaluateGetResponse",
    "Stats",
    "StatsTables",
    "StatsTablesUnmatched1",
    "StatsTablesUnmatched1Properties",
    "StatsTablesUnmatched2",
    "StatsTablesUnmatched2Properties",
]

StatsTablesUnmatched1Properties: TypeAlias = Union[str, bool, float, Image]


class StatsTablesUnmatched1(BaseModel):
    id: str

    properties: Dict[str, StatsTablesUnmatched1Properties]

    type: str


StatsTablesUnmatched2Properties: TypeAlias = Union[str, bool, float, Image]


class StatsTablesUnmatched2(BaseModel):
    id: str

    properties: Dict[str, StatsTablesUnmatched2Properties]

    type: str


class StatsTables(BaseModel):
    matched_entities: List["MatchedEntity"]

    unmatched_1: List[StatsTablesUnmatched1]
    """
    We don't want to make the assumption that the dataset is static after eval, so
    it's useful to save the full entities.
    """

    unmatched_2: List[StatsTablesUnmatched2]


class Stats(BaseModel):
    tables: Dict[str, StatsTables]


class EvaluateGetResponse(BaseModel):
    id: str

    dataset_1: str

    dataset_2: str

    dataset_2_is_ground_truth: bool

    email_1: str

    email_2: str

    iou: float

    matched: int

    started_at: datetime

    stats: Stats

    status: Literal["Running", "Completed", "Failed"]

    unmatched: int

    run_message: Optional[str] = None


from ..matched_entity import MatchedEntity

if PYDANTIC_V2:
    EvaluateGetResponse.model_rebuild()
    Stats.model_rebuild()
    StatsTables.model_rebuild()
    StatsTablesUnmatched1.model_rebuild()
    StatsTablesUnmatched2.model_rebuild()
else:
    EvaluateGetResponse.update_forward_refs()  # type: ignore
    Stats.update_forward_refs()  # type: ignore
    StatsTables.update_forward_refs()  # type: ignore
    StatsTablesUnmatched1.update_forward_refs()  # type: ignore
    StatsTablesUnmatched2.update_forward_refs()  # type: ignore
