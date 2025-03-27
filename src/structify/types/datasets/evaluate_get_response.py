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
    "StatsTableMatches",
    "StatsTableMatchesUnmatchedA",
    "StatsTableMatchesUnmatchedAProperties",
    "StatsTableMatchesUnmatchedB",
    "StatsTableMatchesUnmatchedBProperties",
]

StatsTableMatchesUnmatchedAProperties: TypeAlias = Union[str, bool, float, Image]


class StatsTableMatchesUnmatchedA(BaseModel):
    id: str

    created_at: datetime

    dataset_id: str

    label: str

    properties: Dict[str, StatsTableMatchesUnmatchedAProperties]

    updated_at: datetime


StatsTableMatchesUnmatchedBProperties: TypeAlias = Union[str, bool, float, Image]


class StatsTableMatchesUnmatchedB(BaseModel):
    id: str

    created_at: datetime

    dataset_id: str

    label: str

    properties: Dict[str, StatsTableMatchesUnmatchedBProperties]

    updated_at: datetime


class StatsTableMatches(BaseModel):
    entity_matches: List["EntityMatch"]

    unmatched_a: List[StatsTableMatchesUnmatchedA]

    unmatched_b: List[StatsTableMatchesUnmatchedB]


class Stats(BaseModel):
    table_matches: Dict[str, StatsTableMatches]


class EvaluateGetResponse(BaseModel):
    id: str

    dataset_1: str

    dataset_2: str

    dataset_2_is_ground_truth: bool

    iou: float

    matched: int

    started_at: datetime

    stats: Stats

    status: Literal["Running", "Completed", "Failed"]

    unmatched: int

    run_message: Optional[str] = None


from ..entity_match import EntityMatch

if PYDANTIC_V2:
    EvaluateGetResponse.model_rebuild()
    Stats.model_rebuild()
    StatsTableMatches.model_rebuild()
    StatsTableMatchesUnmatchedA.model_rebuild()
    StatsTableMatchesUnmatchedB.model_rebuild()
else:
    EvaluateGetResponse.update_forward_refs()  # type: ignore
    Stats.update_forward_refs()  # type: ignore
    StatsTableMatches.update_forward_refs()  # type: ignore
    StatsTableMatchesUnmatchedA.update_forward_refs()  # type: ignore
    StatsTableMatchesUnmatchedB.update_forward_refs()  # type: ignore
