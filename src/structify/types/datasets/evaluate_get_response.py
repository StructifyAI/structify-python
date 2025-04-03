# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..image import Image
from ..._models import BaseModel
from ..entity_match import EntityMatch

__all__ = [
    "EvaluateGetResponse",
    "Matches",
    "MatchesRelationshipsA",
    "MatchesRelationshipsAProperties",
    "MatchesRelationshipsB",
    "MatchesRelationshipsBProperties",
    "MatchesTableMatches",
    "MatchesTableMatchesUnmatchedA",
    "MatchesTableMatchesUnmatchedAEntity",
    "MatchesTableMatchesUnmatchedAEntityProperties",
    "MatchesTableMatchesUnmatchedB",
    "MatchesTableMatchesUnmatchedBEntity",
    "MatchesTableMatchesUnmatchedBEntityProperties",
    "Stats",
    "StatsPerTable",
    "StatsPerTableEntityGranularity",
    "StatsPerTablePerProperty",
    "StatsPerTablePropGranularity",
]

MatchesRelationshipsAProperties: TypeAlias = Union[str, bool, float, Image]


class MatchesRelationshipsA(BaseModel):
    from_id: str

    label: str

    properties: Dict[str, MatchesRelationshipsAProperties]

    to_id: str


MatchesRelationshipsBProperties: TypeAlias = Union[str, bool, float, Image]


class MatchesRelationshipsB(BaseModel):
    from_id: str

    label: str

    properties: Dict[str, MatchesRelationshipsBProperties]

    to_id: str


MatchesTableMatchesUnmatchedAEntityProperties: TypeAlias = Union[str, bool, float, Image]


class MatchesTableMatchesUnmatchedAEntity(BaseModel):
    id: str

    created_at: datetime

    dataset_id: str

    label: str

    properties: Dict[str, MatchesTableMatchesUnmatchedAEntityProperties]

    updated_at: datetime


class MatchesTableMatchesUnmatchedA(BaseModel):
    entity: MatchesTableMatchesUnmatchedAEntity

    best_match: Optional[EntityMatch] = None


MatchesTableMatchesUnmatchedBEntityProperties: TypeAlias = Union[str, bool, float, Image]


class MatchesTableMatchesUnmatchedBEntity(BaseModel):
    id: str

    created_at: datetime

    dataset_id: str

    label: str

    properties: Dict[str, MatchesTableMatchesUnmatchedBEntityProperties]

    updated_at: datetime


class MatchesTableMatchesUnmatchedB(BaseModel):
    entity: MatchesTableMatchesUnmatchedBEntity

    best_match: Optional[EntityMatch] = None


class MatchesTableMatches(BaseModel):
    entity_matches: List[EntityMatch]

    unmatched_a: List[MatchesTableMatchesUnmatchedA]

    unmatched_b: List[MatchesTableMatchesUnmatchedB]


class Matches(BaseModel):
    relationships_a: List[MatchesRelationshipsA]

    relationships_b: List[MatchesRelationshipsB]

    table_matches: Dict[str, MatchesTableMatches]


class StatsPerTableEntityGranularity(BaseModel):
    false_negatives: int

    false_positives: int

    true_positives: int


class StatsPerTablePerProperty(BaseModel):
    false_negatives: int

    false_positives: int

    true_positives: int


class StatsPerTablePropGranularity(BaseModel):
    false_negatives: int

    false_positives: int

    true_positives: int


class StatsPerTable(BaseModel):
    entity_granularity: StatsPerTableEntityGranularity

    per_property: Dict[str, StatsPerTablePerProperty]

    prop_granularity: StatsPerTablePropGranularity


class Stats(BaseModel):
    per_table: Dict[str, StatsPerTable]


class EvaluateGetResponse(BaseModel):
    id: str

    dataset_1: str

    dataset_1_name: str

    dataset_2: str

    dataset_2_is_ground_truth: bool

    dataset_2_name: str

    iou: float

    matched: int

    matches: Matches

    started_at: datetime

    stats: Stats

    status: Literal["Running", "Completed", "Failed"]

    unmatched: int

    run_message: Optional[str] = None
