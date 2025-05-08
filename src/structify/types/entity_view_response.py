# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from . import source
from .image import Image
from .._models import BaseModel

__all__ = [
    "EntityViewResponse",
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
    "SimilarEntity",
    "SimilarEntityProperties",
    "SimilarEntityPropertiesPartialDateObject",
    "SimilarEntityPropertiesURLObject",
    "SimilarEntityPropertiesMoneyObject",
    "SimilarEntityPropertiesPersonName",
    "SimilarEntityPropertiesAddressObject",
    "Source",
    "SourceLocation",
    "SourceLocationText",
    "SourceLocationTextText",
    "SourceLocationVisual",
    "SourceLocationVisualVisual",
    "SourceLocationPage",
    "SourceLocationPagePage",
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


class SimilarEntityPropertiesPartialDateObject(BaseModel):
    original_string: str

    year: int

    day: Optional[int] = None

    month: Optional[int] = None


class SimilarEntityPropertiesURLObject(BaseModel):
    original_string: str

    url: str


class SimilarEntityPropertiesMoneyObject(BaseModel):
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


class SimilarEntityPropertiesPersonName(BaseModel):
    name: str


class SimilarEntityPropertiesAddressObject(BaseModel):
    components: Dict[str, str]

    original_address: str


SimilarEntityProperties: TypeAlias = Union[
    str,
    bool,
    float,
    SimilarEntityPropertiesPartialDateObject,
    str,
    str,
    SimilarEntityPropertiesURLObject,
    str,
    SimilarEntityPropertiesMoneyObject,
    Image,
    SimilarEntityPropertiesPersonName,
    SimilarEntityPropertiesAddressObject,
    str,
]


class SimilarEntity(BaseModel):
    id: str

    created_at: datetime

    dataset_id: str

    label: str

    properties: Dict[str, SimilarEntityProperties]

    updated_at: datetime


class SourceLocationTextText(BaseModel):
    byte_offset: int


class SourceLocationText(BaseModel):
    text: SourceLocationTextText = FieldInfo(alias="Text")


class SourceLocationVisualVisual(BaseModel):
    x: int

    y: int


class SourceLocationVisual(BaseModel):
    visual: SourceLocationVisualVisual = FieldInfo(alias="Visual")


class SourceLocationPagePage(BaseModel):
    page_number: int


class SourceLocationPage(BaseModel):
    page: SourceLocationPagePage = FieldInfo(alias="Page")


SourceLocation: TypeAlias = Union[SourceLocationText, SourceLocationVisual, SourceLocationPage, None]


class Source(BaseModel):
    id: str

    created_at: datetime

    is_summary: bool

    user_specified: bool

    link: Optional[source.Source] = None

    location: Optional[SourceLocation] = None

    scraper_id: Optional[str] = None

    step_id: Optional[str] = None


class EntityViewResponse(BaseModel):
    connected_entities: List[ConnectedEntity]

    entity: Entity

    last_updated: str

    relationships: List[Relationship]

    similar_entities: List[SimilarEntity]

    sources: List[Source]
