# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .image_param import ImageParam

__all__ = [
    "EntityUpdatePropertyParams",
    "Properties",
    "PropertiesPartialDateObject",
    "PropertiesURLObject",
    "PropertiesMoneyObject",
    "PropertiesPersonName",
    "PropertiesAddressObject",
    "Source",
    "SourceWeb",
    "SourceDocumentPage",
    "SourceSecFiling",
]


class EntityUpdatePropertyParams(TypedDict, total=False):
    dataset: Required[str]

    entity_id: Required[str]

    properties: Required[Dict[str, Properties]]

    source: Source


class PropertiesPartialDateObject(TypedDict, total=False):
    original_string: Required[str]

    year: Required[int]

    day: Optional[int]

    month: Optional[int]


class PropertiesURLObject(TypedDict, total=False):
    original_string: Required[str]

    url: Required[str]


class PropertiesMoneyObject(TypedDict, total=False):
    amount: Required[float]

    currency_code: Required[
        Literal[
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
    ]

    original_string: Required[str]


class PropertiesPersonName(TypedDict, total=False):
    name: Required[str]


class PropertiesAddressObject(TypedDict, total=False):
    components: Required[Dict[str, str]]

    original_address: Required[str]


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
    ImageParam,
    PropertiesPersonName,
    PropertiesAddressObject,
    str,
]


class SourceWeb(TypedDict, total=False):
    web: Required[Annotated[str, PropertyInfo(alias="Web")]]


class SourceDocumentPage(TypedDict, total=False):
    document_page: Required[Annotated[Iterable[object], PropertyInfo(alias="DocumentPage")]]


class SourceSecFiling(TypedDict, total=False):
    sec_filing: Required[Annotated[Iterable[object], PropertyInfo(alias="SecFiling")]]


Source: TypeAlias = Union[Literal["None"], SourceWeb, SourceDocumentPage, SourceSecFiling]
