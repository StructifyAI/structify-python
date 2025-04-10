# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .image import Image
from .._models import BaseModel

__all__ = [
    "EntitySearchResponse",
    "EntitySearchResponseItem",
    "EntitySearchResponseItemProperties",
    "EntitySearchResponseItemPropertiesPartialDateObject",
    "EntitySearchResponseItemPropertiesURLObject",
    "EntitySearchResponseItemPropertiesMoneyObject",
    "EntitySearchResponseItemPropertiesPersonName",
    "EntitySearchResponseItemPropertiesAddressObject",
]


class EntitySearchResponseItemPropertiesPartialDateObject(BaseModel):
    original_string: str

    year: int

    day: Optional[int] = None

    month: Optional[int] = None


class EntitySearchResponseItemPropertiesURLObject(BaseModel):
    original_string: str

    url: str


class EntitySearchResponseItemPropertiesMoneyObject(BaseModel):
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


class EntitySearchResponseItemPropertiesPersonName(BaseModel):
    name: str


class EntitySearchResponseItemPropertiesAddressObject(BaseModel):
    components: Dict[str, str]

    original_address: str


EntitySearchResponseItemProperties: TypeAlias = Union[
    str,
    bool,
    float,
    EntitySearchResponseItemPropertiesPartialDateObject,
    str,
    str,
    EntitySearchResponseItemPropertiesURLObject,
    str,
    EntitySearchResponseItemPropertiesMoneyObject,
    Image,
    EntitySearchResponseItemPropertiesPersonName,
    EntitySearchResponseItemPropertiesAddressObject,
    str,
]


class EntitySearchResponseItem(BaseModel):
    id: str

    created_at: datetime

    dataset_id: str

    label: str

    properties: Dict[str, EntitySearchResponseItemProperties]

    updated_at: datetime


EntitySearchResponse: TypeAlias = List[EntitySearchResponseItem]
