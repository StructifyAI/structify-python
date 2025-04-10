# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .image import Image
from .._models import BaseModel

__all__ = [
    "DatasetViewRelationshipsResponse",
    "Properties",
    "PropertiesPartialDateObject",
    "PropertiesURLObject",
    "PropertiesMoneyObject",
    "PropertiesPersonName",
    "PropertiesAddressObject",
]


class PropertiesPartialDateObject(BaseModel):
    original_string: str

    year: int

    day: Optional[int] = None

    month: Optional[int] = None


class PropertiesURLObject(BaseModel):
    original_string: str

    url: str


class PropertiesMoneyObject(BaseModel):
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


class PropertiesPersonName(BaseModel):
    name: str


class PropertiesAddressObject(BaseModel):
    components: Dict[str, str]

    original_address: str


Properties: TypeAlias = Union[
    str,
    bool,
    float,
    PropertiesPartialDateObject,
    str,
    str,
    PropertiesURLObject,
    str,
    PropertiesMoneyObject,
    Image,
    PropertiesPersonName,
    PropertiesAddressObject,
    str,
]


class DatasetViewRelationshipsResponse(BaseModel):
    id: str

    created_at: datetime

    dataset_id: str

    from_id: str

    label: str

    properties: Dict[str, Properties]

    to_id: str

    updated_at: datetime
