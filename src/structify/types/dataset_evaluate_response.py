# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union
from typing_extensions import TypeAlias

from .image import Image
from .._models import BaseModel

__all__ = [
    "DatasetEvaluateResponse",
    "Stats",
    "StatsTables",
    "StatsTablesMatchedEntity",
    "StatsTablesMatchedEntityPropertyMatches",
    "StatsTablesMatchedEntityPropertyMatchesMatchedProperties",
    "StatsTablesMatchedEntityPropertyMatchesMatchedPropertiesValue1",
    "StatsTablesMatchedEntityPropertyMatchesMatchedPropertiesValue2",
    "StatsTablesMatchedEntityPropertyMatchesUnmatchedProperties1",
    "StatsTablesMatchedEntityPropertyMatchesUnmatchedProperties2",
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


class StatsTables(BaseModel):
    matched_entities: List[StatsTablesMatchedEntity]

    unmatched_1: List[str]

    unmatched_2: List[str]


class Stats(BaseModel):
    tables: Dict[str, StatsTables]


class DatasetEvaluateResponse(BaseModel):
    id: str

    iou: float

    matched: int

    stats: Stats

    unmatched: int
