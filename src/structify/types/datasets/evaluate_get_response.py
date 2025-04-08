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
    "MatchesRelationshipMatches",
    "MatchesRelationshipMatchesRelationshipMatch",
    "MatchesRelationshipMatchesRelationshipMatchMatchedProperty",
    "MatchesRelationshipMatchesRelationshipMatchRelationshipA",
    "MatchesRelationshipMatchesRelationshipMatchRelationshipAProperties",
    "MatchesRelationshipMatchesRelationshipMatchRelationshipB",
    "MatchesRelationshipMatchesRelationshipMatchRelationshipBProperties",
    "MatchesRelationshipMatchesUnmatchedA",
    "MatchesRelationshipMatchesUnmatchedAProperties",
    "MatchesRelationshipMatchesUnmatchedB",
    "MatchesRelationshipMatchesUnmatchedBProperties",
    "MatchesTableMatches",
    "MatchesTableMatchesUnmatchedA",
    "MatchesTableMatchesUnmatchedAEntity",
    "MatchesTableMatchesUnmatchedAEntityProperties",
    "MatchesTableMatchesUnmatchedB",
    "MatchesTableMatchesUnmatchedBEntity",
    "MatchesTableMatchesUnmatchedBEntityProperties",
    "Stats",
    "StatsPerRelationship",
    "StatsPerRelationshipPerProperty",
    "StatsPerRelationshipPropGranularity",
    "StatsPerRelationshipRelationshipGranularity",
    "StatsPerTable",
    "StatsPerTableEntityGranularity",
    "StatsPerTablePerProperty",
    "StatsPerTablePropGranularity",
]


class MatchesRelationshipMatchesRelationshipMatchMatchedProperty(BaseModel):
    match_prob: float

    match_transfer_prob: float

    name: str

    property_cardinality: int

    unique: bool


MatchesRelationshipMatchesRelationshipMatchRelationshipAProperties: TypeAlias = Union[str, bool, float, Image]


class MatchesRelationshipMatchesRelationshipMatchRelationshipA(BaseModel):
    from_id: str

    label: str

    properties: Dict[str, MatchesRelationshipMatchesRelationshipMatchRelationshipAProperties]

    to_id: str


MatchesRelationshipMatchesRelationshipMatchRelationshipBProperties: TypeAlias = Union[str, bool, float, Image]


class MatchesRelationshipMatchesRelationshipMatchRelationshipB(BaseModel):
    from_id: str

    label: str

    properties: Dict[str, MatchesRelationshipMatchesRelationshipMatchRelationshipBProperties]

    to_id: str


class MatchesRelationshipMatchesRelationshipMatch(BaseModel):
    matched_properties: List[MatchesRelationshipMatchesRelationshipMatchMatchedProperty]

    relationship_a: MatchesRelationshipMatchesRelationshipMatchRelationshipA

    relationship_b: MatchesRelationshipMatchesRelationshipMatchRelationshipB


MatchesRelationshipMatchesUnmatchedAProperties: TypeAlias = Union[str, bool, float, Image]


class MatchesRelationshipMatchesUnmatchedA(BaseModel):
    from_id: str

    label: str

    properties: Dict[str, MatchesRelationshipMatchesUnmatchedAProperties]

    to_id: str


MatchesRelationshipMatchesUnmatchedBProperties: TypeAlias = Union[str, bool, float, Image]


class MatchesRelationshipMatchesUnmatchedB(BaseModel):
    from_id: str

    label: str

    properties: Dict[str, MatchesRelationshipMatchesUnmatchedBProperties]

    to_id: str


class MatchesRelationshipMatches(BaseModel):
    relationship_matches: List[MatchesRelationshipMatchesRelationshipMatch]

    unmatched_a: List[MatchesRelationshipMatchesUnmatchedA]

    unmatched_b: List[MatchesRelationshipMatchesUnmatchedB]


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
    relationship_matches: Dict[str, MatchesRelationshipMatches]

    table_matches: Dict[str, MatchesTableMatches]


class StatsPerRelationshipPerProperty(BaseModel):
    false_negatives: int

    false_positives: int

    true_positives: int


class StatsPerRelationshipPropGranularity(BaseModel):
    false_negatives: int

    false_positives: int

    true_positives: int


class StatsPerRelationshipRelationshipGranularity(BaseModel):
    false_negatives: int

    false_positives: int

    true_positives: int


class StatsPerRelationship(BaseModel):
    per_property: Dict[str, StatsPerRelationshipPerProperty]

    prop_granularity: StatsPerRelationshipPropGranularity

    relationship_granularity: StatsPerRelationshipRelationshipGranularity


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
    per_relationship: Dict[str, StatsPerRelationship]

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
