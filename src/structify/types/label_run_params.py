# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "LabelRunParams",
    "Variant0",
    "Variant0Text",
    "Variant1",
    "Variant1Document",
    "Variant2",
    "Variant2Web",
    "Variant3",
    "Variant3SecFiling",
]


class Variant0(TypedDict, total=False):
    dataset_name: Required[str]

    text: Required[Annotated[Variant0Text, PropertyInfo(alias="Text")]]

    custom_instruction: Optional[str]


class Variant0Text(TypedDict, total=False):
    text_content: Required[str]


class Variant1(TypedDict, total=False):
    dataset_name: Required[str]

    document: Required[Annotated[Variant1Document, PropertyInfo(alias="Document")]]

    custom_instruction: Optional[str]


class Variant1Document(TypedDict, total=False):
    path: Required[str]


class Variant2(TypedDict, total=False):
    dataset_name: Required[str]

    web: Required[Annotated[Variant2Web, PropertyInfo(alias="Web")]]

    custom_instruction: Optional[str]


class Variant2Web(TypedDict, total=False):
    phrase: Required[str]

    starting_website: Optional[str]


class Variant3(TypedDict, total=False):
    dataset_name: Required[str]

    sec_filing: Required[Annotated[Variant3SecFiling, PropertyInfo(alias="SECFiling")]]

    custom_instruction: Optional[str]


class Variant3SecFiling(TypedDict, total=False):
    accession_number: Optional[str]

    quarter: Optional[int]

    year: Optional[int]


LabelRunParams = Union[Variant0, Variant1, Variant2, Variant3]
