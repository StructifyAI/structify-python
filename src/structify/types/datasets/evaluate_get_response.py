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
    "MatchesRelationshipMatchesRelationshipMatchRelationshipAPropertiesPartialDateObject",
    "MatchesRelationshipMatchesRelationshipMatchRelationshipAPropertiesURLObject",
    "MatchesRelationshipMatchesRelationshipMatchRelationshipAPropertiesMoneyObject",
    "MatchesRelationshipMatchesRelationshipMatchRelationshipAPropertiesPersonName",
    "MatchesRelationshipMatchesRelationshipMatchRelationshipAPropertiesAddressObject",
    "MatchesRelationshipMatchesRelationshipMatchRelationshipB",
    "MatchesRelationshipMatchesRelationshipMatchRelationshipBProperties",
    "MatchesRelationshipMatchesRelationshipMatchRelationshipBPropertiesPartialDateObject",
    "MatchesRelationshipMatchesRelationshipMatchRelationshipBPropertiesURLObject",
    "MatchesRelationshipMatchesRelationshipMatchRelationshipBPropertiesMoneyObject",
    "MatchesRelationshipMatchesRelationshipMatchRelationshipBPropertiesPersonName",
    "MatchesRelationshipMatchesRelationshipMatchRelationshipBPropertiesAddressObject",
    "MatchesRelationshipMatchesUnmatchedA",
    "MatchesRelationshipMatchesUnmatchedAProperties",
    "MatchesRelationshipMatchesUnmatchedAPropertiesPartialDateObject",
    "MatchesRelationshipMatchesUnmatchedAPropertiesURLObject",
    "MatchesRelationshipMatchesUnmatchedAPropertiesMoneyObject",
    "MatchesRelationshipMatchesUnmatchedAPropertiesPersonName",
    "MatchesRelationshipMatchesUnmatchedAPropertiesAddressObject",
    "MatchesRelationshipMatchesUnmatchedB",
    "MatchesRelationshipMatchesUnmatchedBProperties",
    "MatchesRelationshipMatchesUnmatchedBPropertiesPartialDateObject",
    "MatchesRelationshipMatchesUnmatchedBPropertiesURLObject",
    "MatchesRelationshipMatchesUnmatchedBPropertiesMoneyObject",
    "MatchesRelationshipMatchesUnmatchedBPropertiesPersonName",
    "MatchesRelationshipMatchesUnmatchedBPropertiesAddressObject",
    "MatchesTableMatches",
    "MatchesTableMatchesUnmatchedA",
    "MatchesTableMatchesUnmatchedAEntity",
    "MatchesTableMatchesUnmatchedAEntityProperties",
    "MatchesTableMatchesUnmatchedAEntityPropertiesPartialDateObject",
    "MatchesTableMatchesUnmatchedAEntityPropertiesURLObject",
    "MatchesTableMatchesUnmatchedAEntityPropertiesMoneyObject",
    "MatchesTableMatchesUnmatchedAEntityPropertiesPersonName",
    "MatchesTableMatchesUnmatchedAEntityPropertiesAddressObject",
    "MatchesTableMatchesUnmatchedB",
    "MatchesTableMatchesUnmatchedBEntity",
    "MatchesTableMatchesUnmatchedBEntityProperties",
    "MatchesTableMatchesUnmatchedBEntityPropertiesPartialDateObject",
    "MatchesTableMatchesUnmatchedBEntityPropertiesURLObject",
    "MatchesTableMatchesUnmatchedBEntityPropertiesMoneyObject",
    "MatchesTableMatchesUnmatchedBEntityPropertiesPersonName",
    "MatchesTableMatchesUnmatchedBEntityPropertiesAddressObject",
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


class MatchesRelationshipMatchesRelationshipMatchRelationshipAPropertiesPartialDateObject(BaseModel):
    original_string: str

    year: int

    day: Optional[int] = None

    month: Optional[int] = None


class MatchesRelationshipMatchesRelationshipMatchRelationshipAPropertiesURLObject(BaseModel):
    original_string: str

    url: str


class MatchesRelationshipMatchesRelationshipMatchRelationshipAPropertiesMoneyObject(BaseModel):
    amount: float

    currency_code: Literal[
        "USD",
        "EUR",
        "GBP",
        "JPY",
        "CNY",
        "INR",
        "RUB",
        "CAD",
        "AUD",
        "CHF",
        "ILS",
        "NZD",
        "SGD",
        "HKD",
        "NOK",
        "SEK",
        "PLN",
        "TRY",
        "DKK",
        "MXN",
        "ZAR",
        "PHP",
        "VND",
        "THB",
        "BRL",
        "KRW",
    ]

    original_string: str


class MatchesRelationshipMatchesRelationshipMatchRelationshipAPropertiesPersonName(BaseModel):
    name: str


class MatchesRelationshipMatchesRelationshipMatchRelationshipAPropertiesAddressObject(BaseModel):
    components: Dict[str, str]

    original_address: str


MatchesRelationshipMatchesRelationshipMatchRelationshipAProperties: TypeAlias = Union[
    str,
    bool,
    float,
    MatchesRelationshipMatchesRelationshipMatchRelationshipAPropertiesPartialDateObject,
    str,
    str,
    MatchesRelationshipMatchesRelationshipMatchRelationshipAPropertiesURLObject,
    str,
    MatchesRelationshipMatchesRelationshipMatchRelationshipAPropertiesMoneyObject,
    Image,
    MatchesRelationshipMatchesRelationshipMatchRelationshipAPropertiesPersonName,
    MatchesRelationshipMatchesRelationshipMatchRelationshipAPropertiesAddressObject,
    str,
]


class MatchesRelationshipMatchesRelationshipMatchRelationshipA(BaseModel):
    id: str

    created_at: datetime

    dataset_id: str

    from_id: str

    label: str

    properties: Dict[str, MatchesRelationshipMatchesRelationshipMatchRelationshipAProperties]

    to_id: str

    updated_at: datetime


class MatchesRelationshipMatchesRelationshipMatchRelationshipBPropertiesPartialDateObject(BaseModel):
    original_string: str

    year: int

    day: Optional[int] = None

    month: Optional[int] = None


class MatchesRelationshipMatchesRelationshipMatchRelationshipBPropertiesURLObject(BaseModel):
    original_string: str

    url: str


class MatchesRelationshipMatchesRelationshipMatchRelationshipBPropertiesMoneyObject(BaseModel):
    amount: float

    currency_code: Literal[
        "USD",
        "EUR",
        "GBP",
        "JPY",
        "CNY",
        "INR",
        "RUB",
        "CAD",
        "AUD",
        "CHF",
        "ILS",
        "NZD",
        "SGD",
        "HKD",
        "NOK",
        "SEK",
        "PLN",
        "TRY",
        "DKK",
        "MXN",
        "ZAR",
        "PHP",
        "VND",
        "THB",
        "BRL",
        "KRW",
    ]

    original_string: str


class MatchesRelationshipMatchesRelationshipMatchRelationshipBPropertiesPersonName(BaseModel):
    name: str


class MatchesRelationshipMatchesRelationshipMatchRelationshipBPropertiesAddressObject(BaseModel):
    components: Dict[str, str]

    original_address: str


MatchesRelationshipMatchesRelationshipMatchRelationshipBProperties: TypeAlias = Union[
    str,
    bool,
    float,
    MatchesRelationshipMatchesRelationshipMatchRelationshipBPropertiesPartialDateObject,
    str,
    str,
    MatchesRelationshipMatchesRelationshipMatchRelationshipBPropertiesURLObject,
    str,
    MatchesRelationshipMatchesRelationshipMatchRelationshipBPropertiesMoneyObject,
    Image,
    MatchesRelationshipMatchesRelationshipMatchRelationshipBPropertiesPersonName,
    MatchesRelationshipMatchesRelationshipMatchRelationshipBPropertiesAddressObject,
    str,
]


class MatchesRelationshipMatchesRelationshipMatchRelationshipB(BaseModel):
    id: str

    created_at: datetime

    dataset_id: str

    from_id: str

    label: str

    properties: Dict[str, MatchesRelationshipMatchesRelationshipMatchRelationshipBProperties]

    to_id: str

    updated_at: datetime


class MatchesRelationshipMatchesRelationshipMatch(BaseModel):
    matched_properties: List[MatchesRelationshipMatchesRelationshipMatchMatchedProperty]

    relationship_a: MatchesRelationshipMatchesRelationshipMatchRelationshipA

    relationship_b: MatchesRelationshipMatchesRelationshipMatchRelationshipB


class MatchesRelationshipMatchesUnmatchedAPropertiesPartialDateObject(BaseModel):
    original_string: str

    year: int

    day: Optional[int] = None

    month: Optional[int] = None


class MatchesRelationshipMatchesUnmatchedAPropertiesURLObject(BaseModel):
    original_string: str

    url: str


class MatchesRelationshipMatchesUnmatchedAPropertiesMoneyObject(BaseModel):
    amount: float

    currency_code: Literal[
        "USD",
        "EUR",
        "GBP",
        "JPY",
        "CNY",
        "INR",
        "RUB",
        "CAD",
        "AUD",
        "CHF",
        "ILS",
        "NZD",
        "SGD",
        "HKD",
        "NOK",
        "SEK",
        "PLN",
        "TRY",
        "DKK",
        "MXN",
        "ZAR",
        "PHP",
        "VND",
        "THB",
        "BRL",
        "KRW",
    ]

    original_string: str


class MatchesRelationshipMatchesUnmatchedAPropertiesPersonName(BaseModel):
    name: str


class MatchesRelationshipMatchesUnmatchedAPropertiesAddressObject(BaseModel):
    components: Dict[str, str]

    original_address: str


MatchesRelationshipMatchesUnmatchedAProperties: TypeAlias = Union[
    str,
    bool,
    float,
    MatchesRelationshipMatchesUnmatchedAPropertiesPartialDateObject,
    str,
    str,
    MatchesRelationshipMatchesUnmatchedAPropertiesURLObject,
    str,
    MatchesRelationshipMatchesUnmatchedAPropertiesMoneyObject,
    Image,
    MatchesRelationshipMatchesUnmatchedAPropertiesPersonName,
    MatchesRelationshipMatchesUnmatchedAPropertiesAddressObject,
    str,
]


class MatchesRelationshipMatchesUnmatchedA(BaseModel):
    id: str

    created_at: datetime

    dataset_id: str

    from_id: str

    label: str

    properties: Dict[str, MatchesRelationshipMatchesUnmatchedAProperties]

    to_id: str

    updated_at: datetime


class MatchesRelationshipMatchesUnmatchedBPropertiesPartialDateObject(BaseModel):
    original_string: str

    year: int

    day: Optional[int] = None

    month: Optional[int] = None


class MatchesRelationshipMatchesUnmatchedBPropertiesURLObject(BaseModel):
    original_string: str

    url: str


class MatchesRelationshipMatchesUnmatchedBPropertiesMoneyObject(BaseModel):
    amount: float

    currency_code: Literal[
        "USD",
        "EUR",
        "GBP",
        "JPY",
        "CNY",
        "INR",
        "RUB",
        "CAD",
        "AUD",
        "CHF",
        "ILS",
        "NZD",
        "SGD",
        "HKD",
        "NOK",
        "SEK",
        "PLN",
        "TRY",
        "DKK",
        "MXN",
        "ZAR",
        "PHP",
        "VND",
        "THB",
        "BRL",
        "KRW",
    ]

    original_string: str


class MatchesRelationshipMatchesUnmatchedBPropertiesPersonName(BaseModel):
    name: str


class MatchesRelationshipMatchesUnmatchedBPropertiesAddressObject(BaseModel):
    components: Dict[str, str]

    original_address: str


MatchesRelationshipMatchesUnmatchedBProperties: TypeAlias = Union[
    str,
    bool,
    float,
    MatchesRelationshipMatchesUnmatchedBPropertiesPartialDateObject,
    str,
    str,
    MatchesRelationshipMatchesUnmatchedBPropertiesURLObject,
    str,
    MatchesRelationshipMatchesUnmatchedBPropertiesMoneyObject,
    Image,
    MatchesRelationshipMatchesUnmatchedBPropertiesPersonName,
    MatchesRelationshipMatchesUnmatchedBPropertiesAddressObject,
    str,
]


class MatchesRelationshipMatchesUnmatchedB(BaseModel):
    id: str

    created_at: datetime

    dataset_id: str

    from_id: str

    label: str

    properties: Dict[str, MatchesRelationshipMatchesUnmatchedBProperties]

    to_id: str

    updated_at: datetime


class MatchesRelationshipMatches(BaseModel):
    relationship_matches: List[MatchesRelationshipMatchesRelationshipMatch]

    unmatched_a: List[MatchesRelationshipMatchesUnmatchedA]

    unmatched_b: List[MatchesRelationshipMatchesUnmatchedB]


class MatchesTableMatchesUnmatchedAEntityPropertiesPartialDateObject(BaseModel):
    original_string: str

    year: int

    day: Optional[int] = None

    month: Optional[int] = None


class MatchesTableMatchesUnmatchedAEntityPropertiesURLObject(BaseModel):
    original_string: str

    url: str


class MatchesTableMatchesUnmatchedAEntityPropertiesMoneyObject(BaseModel):
    amount: float

    currency_code: Literal[
        "USD",
        "EUR",
        "GBP",
        "JPY",
        "CNY",
        "INR",
        "RUB",
        "CAD",
        "AUD",
        "CHF",
        "ILS",
        "NZD",
        "SGD",
        "HKD",
        "NOK",
        "SEK",
        "PLN",
        "TRY",
        "DKK",
        "MXN",
        "ZAR",
        "PHP",
        "VND",
        "THB",
        "BRL",
        "KRW",
    ]

    original_string: str


class MatchesTableMatchesUnmatchedAEntityPropertiesPersonName(BaseModel):
    name: str


class MatchesTableMatchesUnmatchedAEntityPropertiesAddressObject(BaseModel):
    components: Dict[str, str]

    original_address: str


MatchesTableMatchesUnmatchedAEntityProperties: TypeAlias = Union[
    str,
    bool,
    float,
    MatchesTableMatchesUnmatchedAEntityPropertiesPartialDateObject,
    str,
    str,
    MatchesTableMatchesUnmatchedAEntityPropertiesURLObject,
    str,
    MatchesTableMatchesUnmatchedAEntityPropertiesMoneyObject,
    Image,
    MatchesTableMatchesUnmatchedAEntityPropertiesPersonName,
    MatchesTableMatchesUnmatchedAEntityPropertiesAddressObject,
    str,
]


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


class MatchesTableMatchesUnmatchedBEntityPropertiesPartialDateObject(BaseModel):
    original_string: str

    year: int

    day: Optional[int] = None

    month: Optional[int] = None


class MatchesTableMatchesUnmatchedBEntityPropertiesURLObject(BaseModel):
    original_string: str

    url: str


class MatchesTableMatchesUnmatchedBEntityPropertiesMoneyObject(BaseModel):
    amount: float

    currency_code: Literal[
        "USD",
        "EUR",
        "GBP",
        "JPY",
        "CNY",
        "INR",
        "RUB",
        "CAD",
        "AUD",
        "CHF",
        "ILS",
        "NZD",
        "SGD",
        "HKD",
        "NOK",
        "SEK",
        "PLN",
        "TRY",
        "DKK",
        "MXN",
        "ZAR",
        "PHP",
        "VND",
        "THB",
        "BRL",
        "KRW",
    ]

    original_string: str


class MatchesTableMatchesUnmatchedBEntityPropertiesPersonName(BaseModel):
    name: str


class MatchesTableMatchesUnmatchedBEntityPropertiesAddressObject(BaseModel):
    components: Dict[str, str]

    original_address: str


MatchesTableMatchesUnmatchedBEntityProperties: TypeAlias = Union[
    str,
    bool,
    float,
    MatchesTableMatchesUnmatchedBEntityPropertiesPartialDateObject,
    str,
    str,
    MatchesTableMatchesUnmatchedBEntityPropertiesURLObject,
    str,
    MatchesTableMatchesUnmatchedBEntityPropertiesMoneyObject,
    Image,
    MatchesTableMatchesUnmatchedBEntityPropertiesPersonName,
    MatchesTableMatchesUnmatchedBEntityPropertiesAddressObject,
    str,
]


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
    false_negatives: float

    false_positives: float

    true_positives: float


class StatsPerRelationshipPropGranularity(BaseModel):
    false_negatives: float

    false_positives: float

    true_positives: float


class StatsPerRelationshipRelationshipGranularity(BaseModel):
    false_negatives: float

    false_positives: float

    true_positives: float


class StatsPerRelationship(BaseModel):
    per_property: Dict[str, StatsPerRelationshipPerProperty]

    prop_granularity: StatsPerRelationshipPropGranularity

    relationship_granularity: StatsPerRelationshipRelationshipGranularity


class StatsPerTableEntityGranularity(BaseModel):
    false_negatives: float

    false_positives: float

    true_positives: float


class StatsPerTablePerProperty(BaseModel):
    false_negatives: float

    false_positives: float

    true_positives: float


class StatsPerTablePropGranularity(BaseModel):
    false_negatives: float

    false_positives: float

    true_positives: float


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
