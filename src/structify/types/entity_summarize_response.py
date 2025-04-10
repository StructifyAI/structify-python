# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .image import Image
from .._models import BaseModel

__all__ = [
    "EntitySummarizeResponse",
    "EntitySummarizeResponseItem",
    "EntitySummarizeResponseItemProperties",
    "EntitySummarizeResponseItemPropertiesPartialDateObject",
    "EntitySummarizeResponseItemPropertiesURLObject",
    "EntitySummarizeResponseItemPropertiesMoneyObject",
    "EntitySummarizeResponseItemPropertiesPersonName",
    "EntitySummarizeResponseItemPropertiesAddressObject",
]


class EntitySummarizeResponseItemPropertiesPartialDateObject(BaseModel):
    original_string: str

    year: int

    day: Optional[int] = None

    month: Optional[int] = None


class EntitySummarizeResponseItemPropertiesURLObject(BaseModel):
    original_string: str

    url: str


class EntitySummarizeResponseItemPropertiesMoneyObject(BaseModel):
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


class EntitySummarizeResponseItemPropertiesPersonName(BaseModel):
    name: str


class EntitySummarizeResponseItemPropertiesAddressObject(BaseModel):
    components: Dict[str, str]

    original_address: str


EntitySummarizeResponseItemProperties: TypeAlias = Union[
    str,
    bool,
    float,
    EntitySummarizeResponseItemPropertiesPartialDateObject,
    str,
    str,
    EntitySummarizeResponseItemPropertiesURLObject,
    str,
    EntitySummarizeResponseItemPropertiesMoneyObject,
    Image,
    EntitySummarizeResponseItemPropertiesPersonName,
    EntitySummarizeResponseItemPropertiesAddressObject,
    str,
]


class EntitySummarizeResponseItem(BaseModel):
    id: str

    created_at: datetime

    dataset_id: str

    label: str

    properties: Dict[str, EntitySummarizeResponseItemProperties]

    updated_at: datetime


EntitySummarizeResponse: TypeAlias = List[EntitySummarizeResponseItem]
