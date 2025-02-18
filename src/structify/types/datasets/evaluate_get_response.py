# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..image import Image
from ..._models import BaseModel

__all__ = [
    "EvaluateGetResponse",
    "Stats",
    "StatsTables",
    "StatsTablesMatchedEntity",
    "StatsTablesMatchedEntityPropertyMatches",
    "StatsTablesMatchedEntityPropertyMatchesMatchedProperties",
    "StatsTablesMatchedEntityPropertyMatchesMatchedPropertiesValue1",
    "StatsTablesMatchedEntityPropertyMatchesMatchedPropertiesValue2",
    "StatsTablesMatchedEntityPropertyMatchesUnmatchedProperties1",
    "StatsTablesMatchedEntityPropertyMatchesUnmatchedProperties2",
    "StatsTablesUnmatched1",
    "StatsTablesUnmatched1Properties",
    "StatsTablesUnmatched2",
    "StatsTablesUnmatched2Properties",
]

StatsTablesMatchedEntityPropertyMatchesMatchedPropertiesValue1: TypeAlias = Union[str, bool, float, Image]

StatsTablesMatchedEntityPropertyMatchesMatchedPropertiesValue2: TypeAlias = Union[str, bool, float, Image]


class StatsTablesMatchedEntityPropertyMatchesMatchedProperties(BaseModel):
    match_score: float

    value1: StatsTablesMatchedEntityPropertyMatchesMatchedPropertiesValue1

    value2: StatsTablesMatchedEntityPropertyMatchesMatchedPropertiesValue2


StatsTablesMatchedEntityPropertyMatchesUnmatchedProperties1: TypeAlias = Union[str, bool, float, Image]

StatsTablesMatchedEntityPropertyMatchesUnmatchedProperties2: TypeAlias = Union[str, bool, float, Image]


class StatsTablesMatchedEntityPropertyMatches(BaseModel):
    matched_properties: Dict[str, StatsTablesMatchedEntityPropertyMatchesMatchedProperties]

    unmatched_properties_1: Dict[str, StatsTablesMatchedEntityPropertyMatchesUnmatchedProperties1]

    unmatched_properties_2: Dict[str, StatsTablesMatchedEntityPropertyMatchesUnmatchedProperties2]


class StatsTablesMatchedEntity(BaseModel):
    e1_id: str

    e2_id: str

    match_score: float

    property_matches: StatsTablesMatchedEntityPropertyMatches


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
    matched_entities: List[StatsTablesMatchedEntity]

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
