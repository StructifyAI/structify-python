# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .image import Image
from .._models import BaseModel

__all__ = [
    "DatasetViewTablesWithRelationshipsResponse",
    "ConnectedEntity",
    "ConnectedEntityProperties",
    "ConnectedEntityPropertiesPartialDateObject",
    "ConnectedEntityPropertiesURLObject",
    "ConnectedEntityPropertiesMoneyObject",
    "ConnectedEntityPropertiesPersonName",
    "ConnectedEntityPropertiesAddressObject",
    "Entity",
    "EntityProperties",
    "EntityPropertiesPartialDateObject",
    "EntityPropertiesURLObject",
    "EntityPropertiesMoneyObject",
    "EntityPropertiesPersonName",
    "EntityPropertiesAddressObject",
    "Relationship",
    "RelationshipProperties",
    "RelationshipPropertiesPartialDateObject",
    "RelationshipPropertiesURLObject",
    "RelationshipPropertiesMoneyObject",
    "RelationshipPropertiesPersonName",
    "RelationshipPropertiesAddressObject",
]


class ConnectedEntityPropertiesPartialDateObject(BaseModel):
    original_string: str

    year: int

    day: Optional[int] = None

    month: Optional[int] = None


class ConnectedEntityPropertiesURLObject(BaseModel):
    original_string: str

    url: str


class ConnectedEntityPropertiesMoneyObject(BaseModel):
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


class ConnectedEntityPropertiesPersonName(BaseModel):
    name: str


class ConnectedEntityPropertiesAddressObject(BaseModel):
    components: Dict[str, str]

    original_address: str


ConnectedEntityProperties: TypeAlias = Union[
    str,
    bool,
    float,
    ConnectedEntityPropertiesPartialDateObject,
    str,
    str,
    ConnectedEntityPropertiesURLObject,
    str,
    ConnectedEntityPropertiesMoneyObject,
    Image,
    ConnectedEntityPropertiesPersonName,
    ConnectedEntityPropertiesAddressObject,
    str,
]


class ConnectedEntity(BaseModel):
    id: str

    created_at: datetime

    dataset_id: str

    label: str

    properties: Dict[str, ConnectedEntityProperties]

    updated_at: datetime


class EntityPropertiesPartialDateObject(BaseModel):
    original_string: str

    year: int

    day: Optional[int] = None

    month: Optional[int] = None


class EntityPropertiesURLObject(BaseModel):
    original_string: str

    url: str


class EntityPropertiesMoneyObject(BaseModel):
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


class EntityPropertiesPersonName(BaseModel):
    name: str


class EntityPropertiesAddressObject(BaseModel):
    components: Dict[str, str]

    original_address: str


EntityProperties: TypeAlias = Union[
    str,
    bool,
    float,
    EntityPropertiesPartialDateObject,
    str,
    str,
    EntityPropertiesURLObject,
    str,
    EntityPropertiesMoneyObject,
    Image,
    EntityPropertiesPersonName,
    EntityPropertiesAddressObject,
    str,
]


class Entity(BaseModel):
    id: str

    created_at: datetime

    dataset_id: str

    label: str

    properties: Dict[str, EntityProperties]

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


class DatasetViewTablesWithRelationshipsResponse(BaseModel):
    connected_entities: List[ConnectedEntity]

    entities: List[Entity]

    relationships: List[Relationship]
