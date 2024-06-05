# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = [
    "LabelRunParams",
    "Variant0",
    "Variant0SecIngestor",
    "Variant1",
    "Variant2",
    "Variant2Basic",
    "Variant2BasicTextDocument",
    "Variant2BasicTextDocumentTextDocument",
    "Variant2BasicWebSearch",
    "Variant2BasicWebSearchWebSearch",
    "Variant2BasicImageDocument",
    "Variant2BasicImageDocumentImageDocument",
]


class Variant0(TypedDict, total=False):
    dataset_name: Required[str]

    sec_ingestor: Required[Annotated[Variant0SecIngestor, PropertyInfo(alias="SECIngestor")]]

    custom_instruction: Optional[str]


class Variant0SecIngestor(TypedDict, total=False):
    accession_number: Optional[str]

    quarter: Optional[int]

    year: Optional[int]


class Variant1(TypedDict, total=False):
    dataset_name: Required[str]

    pdf_ingestor: Required[Annotated[str, PropertyInfo(alias="PDFIngestor")]]
    """This is currently a very simple ingestor.

    It converts everything to an image and processes them independently.
    """

    custom_instruction: Optional[str]


class Variant2(TypedDict, total=False):
    dataset_name: Required[str]

    basic: Required[Annotated[Variant2Basic, PropertyInfo(alias="Basic")]]
    """
    These are all the types for which we have an agent that is directly capable of
    navigating. There should be a one to one mapping between them.
    """

    custom_instruction: Optional[str]


class Variant2BasicTextDocumentTextDocument(TypedDict, total=False):
    content: Optional[str]

    document_name: Optional[str]

    save: bool


class Variant2BasicTextDocument(TypedDict, total=False):
    text_document: Required[Annotated[Variant2BasicTextDocumentTextDocument, PropertyInfo(alias="TextDocument")]]


class Variant2BasicWebSearchWebSearch(TypedDict, total=False):
    conditioning_phrase: Required[str]

    use_local_browser: Required[bool]

    starting_website: Optional[str]


class Variant2BasicWebSearch(TypedDict, total=False):
    web_search: Required[Annotated[Variant2BasicWebSearchWebSearch, PropertyInfo(alias="WebSearch")]]


class Variant2BasicImageDocumentImageDocument(TypedDict, total=False):
    content: Required[FileTypes]

    document_name: Required[str]


class Variant2BasicImageDocument(TypedDict, total=False):
    image_document: Required[Annotated[Variant2BasicImageDocumentImageDocument, PropertyInfo(alias="ImageDocument")]]


Variant2Basic = Union[Variant2BasicTextDocument, Variant2BasicWebSearch, Variant2BasicImageDocument]

LabelRunParams = Union[Variant0, Variant1, Variant2]
