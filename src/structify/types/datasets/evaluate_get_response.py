# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..image import Image
from ..._compat import PYDANTIC_V2
from ..._models import BaseModel
from ..entity_match import EntityMatch

__all__ = [
    "EvaluateGetResponse",
    "Stats",
    "StatsRelationshipsA",
    "StatsRelationshipsAProperties",
    "StatsRelationshipsB",
    "StatsRelationshipsBProperties",
    "StatsTableMatches",
    "StatsTableMatchesUnmatchedA",
    "StatsTableMatchesUnmatchedAProperties",
    "StatsTableMatchesUnmatchedB",
    "StatsTableMatchesUnmatchedBProperties",
]

StatsRelationshipsAProperties: TypeAlias = Union[str, bool, float, Image]


class StatsRelationshipsA(BaseModel):
    from_id: str

    label: str

    properties: Dict[str, StatsRelationshipsAProperties]

    to_id: str


StatsRelationshipsBProperties: TypeAlias = Union[str, bool, float, Image]


class StatsRelationshipsB(BaseModel):
    from_id: str

    label: str

    properties: Dict[str, StatsRelationshipsBProperties]

    to_id: str


StatsTableMatchesUnmatchedAProperties: TypeAlias = Union[str, bool, float, Image]


class StatsTableMatchesUnmatchedA(EntityMatch):
    id: str

    created_at: datetime

    dataset_id: str

    label: str

    properties: Dict[str, StatsTableMatchesUnmatchedAProperties]

    updated_at: datetime


StatsTableMatchesUnmatchedBProperties: TypeAlias = Union[str, bool, float, Image]


class StatsTableMatchesUnmatchedB(EntityMatch):
    id: str

    created_at: datetime

    dataset_id: str

    label: str

    properties: Dict[str, StatsTableMatchesUnmatchedBProperties]

    updated_at: datetime


class StatsTableMatches(BaseModel):
    entity_matches: List["EntityMatch"]

    unmatched_a: List[List[StatsTableMatchesUnmatchedA]]

    unmatched_b: List[List[StatsTableMatchesUnmatchedB]]


class Stats(BaseModel):
    relationships_a: List[StatsRelationshipsA]

    relationships_b: List[StatsRelationshipsB]

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
    StatsRelationshipsA.model_rebuild()
    StatsRelationshipsB.model_rebuild()
    StatsTableMatches.model_rebuild()
else:
    EvaluateGetResponse.update_forward_refs()  # type: ignore
    Stats.update_forward_refs()  # type: ignore
    StatsRelationshipsA.update_forward_refs()  # type: ignore
    StatsRelationshipsB.update_forward_refs()  # type: ignore
    StatsTableMatches.update_forward_refs()  # type: ignore
