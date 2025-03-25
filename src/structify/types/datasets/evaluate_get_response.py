# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..image import Image
from ..._models import BaseModel

__all__ = [
    "EvaluateGetResponse",
    "Stats",
    "StatsTableMatches",
    "StatsTableMatchesEntityMatch",
    "StatsTableMatchesEntityMatchEntityA",
    "StatsTableMatchesEntityMatchEntityAProperties",
    "StatsTableMatchesEntityMatchEntityB",
    "StatsTableMatchesEntityMatchEntityBProperties",
    "StatsTableMatchesEntityMatchMatchedProperty",
    "StatsTableMatchesUnmatchedA",
    "StatsTableMatchesUnmatchedAProperties",
    "StatsTableMatchesUnmatchedB",
    "StatsTableMatchesUnmatchedBProperties",
]

StatsTableMatchesEntityMatchEntityAProperties: TypeAlias = Union[str, bool, float, Image]


class StatsTableMatchesEntityMatchEntityA(BaseModel):
    id: str

    created_at: datetime

    dataset_id: str

    label: str

    properties: Dict[str, StatsTableMatchesEntityMatchEntityAProperties]

    updated_at: datetime


StatsTableMatchesEntityMatchEntityBProperties: TypeAlias = Union[str, bool, float, Image]


class StatsTableMatchesEntityMatchEntityB(BaseModel):
    id: str

    created_at: datetime

    dataset_id: str

    label: str

    properties: Dict[str, StatsTableMatchesEntityMatchEntityBProperties]

    updated_at: datetime


class StatsTableMatchesEntityMatchMatchedProperty(BaseModel):
    match_prob: float

    match_transfer_prob: float

    name: str

    property_cardinality: int

    unique: bool


class StatsTableMatchesEntityMatch(BaseModel):
    alternate_matches: List[object]
    """Alternate matches for entity a - just used for dataset eval"""

    baseline_cardinality: int

    entity_a: StatsTableMatchesEntityMatchEntityA

    entity_b: StatsTableMatchesEntityMatchEntityB

    matched_properties: List[StatsTableMatchesEntityMatchMatchedProperty]

    p_match: float

    p_match_threshold: float


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
    entity_matches: List[StatsTableMatchesEntityMatch]

    unmatched_a: List[StatsTableMatchesUnmatchedA]

    unmatched_b: List[StatsTableMatchesUnmatchedB]


class Stats(BaseModel):
    table_matches: Dict[str, StatsTableMatches]


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
