# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .image import Image
from .._models import BaseModel

__all__ = [
    "EntityGetLocalSubgraphResponse",
    "Neighbor",
    "NeighborProperties",
    "NeighborPropertiesPartialDateObject",
    "NeighborPropertiesURLObject",
    "NeighborPropertiesMoneyObject",
    "NeighborPropertiesPersonName",
    "NeighborPropertiesAddressObject",
    "Relationship",
    "RelationshipProperties",
    "RelationshipPropertiesPartialDateObject",
    "RelationshipPropertiesURLObject",
    "RelationshipPropertiesMoneyObject",
    "RelationshipPropertiesPersonName",
    "RelationshipPropertiesAddressObject",
]


class NeighborPropertiesPartialDateObject(BaseModel):
    original_string: str

    year: int

    day: Optional[int] = None

    month: Optional[int] = None


class NeighborPropertiesURLObject(BaseModel):
    original_string: str

    url: str


class NeighborPropertiesMoneyObject(BaseModel):
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


class NeighborPropertiesPersonName(BaseModel):
    name: str


class NeighborPropertiesAddressObject(BaseModel):
    components: Dict[str, str]

    original_address: str


NeighborProperties: TypeAlias = Union[
    str,
    bool,
    float,
    NeighborPropertiesPartialDateObject,
    str,
    str,
    NeighborPropertiesURLObject,
    str,
    NeighborPropertiesMoneyObject,
    Image,
    NeighborPropertiesPersonName,
    NeighborPropertiesAddressObject,
    str,
]


class Neighbor(BaseModel):
    id: str

    created_at: datetime

    dataset_id: str

    label: str

    properties: Dict[str, NeighborProperties]

    updated_at: datetime


class RelationshipPropertiesPartialDateObject(BaseModel):
    original_string: str

    year: int

    day: Optional[int] = None

    month: Optional[int] = None


class RelationshipPropertiesURLObject(BaseModel):
    original_string: str

    url: str


class RelationshipPropertiesMoneyObject(BaseModel):
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


class RelationshipPropertiesPersonName(BaseModel):
    name: str


class RelationshipPropertiesAddressObject(BaseModel):
    components: Dict[str, str]

    original_address: str


RelationshipProperties: TypeAlias = Union[
    str,
    bool,
    float,
    RelationshipPropertiesPartialDateObject,
    str,
    str,
    RelationshipPropertiesURLObject,
    str,
    RelationshipPropertiesMoneyObject,
    Image,
    RelationshipPropertiesPersonName,
    RelationshipPropertiesAddressObject,
    str,
]


class Relationship(BaseModel):
    id: str

    created_at: datetime

    dataset_id: str

    from_id: str

    label: str

    properties: Dict[str, RelationshipProperties]

    to_id: str

    updated_at: datetime


class EntityGetLocalSubgraphResponse(BaseModel):
    neighbors: List[Neighbor]

    relationships: List[Relationship]
