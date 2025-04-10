# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .image import Image
from .._models import BaseModel

__all__ = [
    "EntityMatch",
    "EntityA",
    "EntityAProperties",
    "EntityAPropertiesPartialDateObject",
    "EntityAPropertiesURLObject",
    "EntityAPropertiesMoneyObject",
    "EntityAPropertiesPersonName",
    "EntityAPropertiesAddressObject",
    "EntityB",
    "EntityBProperties",
    "EntityBPropertiesPartialDateObject",
    "EntityBPropertiesURLObject",
    "EntityBPropertiesMoneyObject",
    "EntityBPropertiesPersonName",
    "EntityBPropertiesAddressObject",
    "MatchedProperty",
    "CardinalityOverride",
]


class EntityAPropertiesPartialDateObject(BaseModel):
    original_string: str

    year: int

    day: Optional[int] = None

    month: Optional[int] = None


class EntityAPropertiesURLObject(BaseModel):
    original_string: str

    url: str


class EntityAPropertiesMoneyObject(BaseModel):
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


class EntityAPropertiesPersonName(BaseModel):
    name: str


class EntityAPropertiesAddressObject(BaseModel):
    components: Dict[str, str]

    original_address: str


EntityAProperties: TypeAlias = Union[
    str,
    bool,
    float,
    EntityAPropertiesPartialDateObject,
    str,
    str,
    EntityAPropertiesURLObject,
    str,
    EntityAPropertiesMoneyObject,
    Image,
    EntityAPropertiesPersonName,
    EntityAPropertiesAddressObject,
    str,
]


class EntityA(BaseModel):
    id: str

    created_at: datetime

    dataset_id: str

    label: str

    properties: Dict[str, EntityAProperties]

    updated_at: datetime


class EntityBPropertiesPartialDateObject(BaseModel):
    original_string: str

    year: int

    day: Optional[int] = None

    month: Optional[int] = None


class EntityBPropertiesURLObject(BaseModel):
    original_string: str

    url: str


class EntityBPropertiesMoneyObject(BaseModel):
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


class EntityBPropertiesPersonName(BaseModel):
    name: str


class EntityBPropertiesAddressObject(BaseModel):
    components: Dict[str, str]

    original_address: str


EntityBProperties: TypeAlias = Union[
    str,
    bool,
    float,
    EntityBPropertiesPartialDateObject,
    str,
    str,
    EntityBPropertiesURLObject,
    str,
    EntityBPropertiesMoneyObject,
    Image,
    EntityBPropertiesPersonName,
    EntityBPropertiesAddressObject,
    str,
]


class EntityB(BaseModel):
    id: str

    created_at: datetime

    dataset_id: str

    label: str

    properties: Dict[str, EntityBProperties]

    updated_at: datetime


class MatchedProperty(BaseModel):
    match_prob: float

    match_transfer_prob: float

    name: str

    property_cardinality: int

    unique: bool


class CardinalityOverride(BaseModel):
    cardinality: int

    entity_id: str

    relationship_name: str


class EntityMatch(BaseModel):
    baseline_cardinality: int

    entity_a: EntityA

    entity_b: EntityB

    matched_properties: List[MatchedProperty]

    p_match: float

    p_match_threshold: float

    cardinality_override: Optional[CardinalityOverride] = None
