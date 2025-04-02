# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..image import Image
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
    "StatsTableMatchesUnmatchedAEntity",
    "StatsTableMatchesUnmatchedAEntityProperties",
    "StatsTableMatchesUnmatchedB",
    "StatsTableMatchesUnmatchedBEntity",
    "StatsTableMatchesUnmatchedBEntityProperties",
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


StatsTableMatchesUnmatchedAEntityProperties: TypeAlias = Union[str, bool, float, Image]


class StatsTableMatchesUnmatchedAEntity(BaseModel):
    id: str

    created_at: datetime

    dataset_id: str

    label: str

    properties: Dict[str, StatsTableMatchesUnmatchedAEntityProperties]

    updated_at: datetime


class StatsTableMatchesUnmatchedA(BaseModel):
    entity: StatsTableMatchesUnmatchedAEntity

    best_match: Optional[EntityMatch] = None


StatsTableMatchesUnmatchedBEntityProperties: TypeAlias = Union[str, bool, float, Image]


class StatsTableMatchesUnmatchedBEntity(BaseModel):
    id: str

    created_at: datetime

    dataset_id: str

    label: str

    properties: Dict[str, StatsTableMatchesUnmatchedBEntityProperties]

    updated_at: datetime


class StatsTableMatchesUnmatchedB(BaseModel):
    entity: StatsTableMatchesUnmatchedBEntity

    best_match: Optional[EntityMatch] = None


class StatsTableMatches(BaseModel):
    entity_matches: List[EntityMatch]

    unmatched_a: List[StatsTableMatchesUnmatchedA]

    unmatched_b: List[StatsTableMatchesUnmatchedB]


class Stats(BaseModel):
    relationships_a: List[StatsRelationshipsA]

    relationships_b: List[StatsRelationshipsB]

    table_matches: Dict[str, StatsTableMatches]


class EvaluateGetResponse(BaseModel):
    id: str

    dataset_1: str

    dataset_1_name: str

    dataset_2: str

    dataset_2_is_ground_truth: bool

    dataset_2_name: str

    iou: float

    matched: int

    started_at: datetime

    stats: Stats

    status: Literal["Running", "Completed", "Failed"]

    unmatched: int

    run_message: Optional[str] = None
