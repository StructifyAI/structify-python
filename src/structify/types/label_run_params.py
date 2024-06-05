# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = [
    "LabelRunParams",
    "Variant0",
    "Variant0Basic",
    "Variant0BasicTextDataInput",
    "Variant0BasicWebsiteData",
    "Variant0BasicImageInputData",
    "Variant1",
    "Variant1SecIngestor",
    "Variant2",
]


class Variant0(TypedDict, total=False):
    dataset_name: Required[str]

    basic: Required[Annotated[Variant0Basic, PropertyInfo(alias="Basic")]]
    """
    These are all the types for which we have an agent that is directly capable of
    navigating. There should be a one to one mapping between them.
    """

    custom_instruction: Optional[str]


class Variant0BasicTextDataInput(TypedDict, total=False):
    content: Optional[str]

    document_name: Optional[str]

    save: bool


class Variant0BasicWebsiteData(TypedDict, total=False):
    conditioning_phrase: Required[str]

    use_local_browser: Required[bool]

    starting_website: Optional[str]


class Variant0BasicImageInputData(TypedDict, total=False):
    content: Required[FileTypes]

    document_name: Required[str]


Variant0Basic = Union[Variant0BasicTextDataInput, Variant0BasicWebsiteData, Variant0BasicImageInputData]


class Variant1(TypedDict, total=False):
    dataset_name: Required[str]

    sec_ingestor: Required[Annotated[Variant1SecIngestor, PropertyInfo(alias="SECIngestor")]]

    custom_instruction: Optional[str]


class Variant1SecIngestor(TypedDict, total=False):
    accession_number: Optional[str]

    quarter: Optional[int]

    year: Optional[int]


class Variant2(TypedDict, total=False):
    dataset_name: Required[str]

    pdf_ingestor: Required[Annotated[str, PropertyInfo(alias="PDFIngestor")]]
    """This is currently a very simple ingestor.

    It converts everything to an image and processes them independently.
    """

    custom_instruction: Optional[str]


LabelRunParams = Union[Variant0, Variant1, Variant2]
