# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._types import FileTypes
from .._utils import PropertyInfo
from .extraction_criteria_param import ExtractionCriteriaParam

__all__ = [
    "LabelRunParams",
    "StructureInput",
    "StructureInputSecIngestor",
    "StructureInputSecIngestorSecIngestor",
    "StructureInputPdfIngestor",
    "StructureInputPdfIngestorPdfIngestor",
    "StructureInputBasic",
    "StructureInputBasicBasic",
    "StructureInputBasicBasicTextDocument",
    "StructureInputBasicBasicTextDocumentTextDocument",
    "StructureInputBasicBasicWebSearch",
    "StructureInputBasicBasicWebSearchWebSearch",
    "StructureInputBasicBasicImageDocument",
    "StructureInputBasicBasicImageDocumentImageDocument",
]


class LabelRunParams(TypedDict, total=False):
    dataset_name: Required[str]

    structure_input: Required[StructureInput]
    """These are all the types that can be converted into a BasicInputType"""


class StructureInputSecIngestorSecIngestor(TypedDict, total=False):
    extraction_criteria: Required[Iterable[ExtractionCriteriaParam]]

    accession_number: Optional[str]

    quarter: Optional[int]

    year: Optional[int]


class StructureInputSecIngestor(TypedDict, total=False):
    sec_ingestor: Required[Annotated[StructureInputSecIngestorSecIngestor, PropertyInfo(alias="SECIngestor")]]


class StructureInputPdfIngestorPdfIngestor(TypedDict, total=False):
    extraction_criteria: Required[Iterable[ExtractionCriteriaParam]]

    path: Required[str]


class StructureInputPdfIngestor(TypedDict, total=False):
    pdf_ingestor: Required[Annotated[StructureInputPdfIngestorPdfIngestor, PropertyInfo(alias="PDFIngestor")]]
    """This is currently a very simple ingestor.

    It converts everything to an image and processes them independently.
    """


class StructureInputBasicBasicTextDocumentTextDocument(TypedDict, total=False):
    extraction_criteria: Required[Iterable[ExtractionCriteriaParam]]

    content: Optional[str]

    filepath: Optional[str]

    save: bool


class StructureInputBasicBasicTextDocument(TypedDict, total=False):
    text_document: Required[
        Annotated[StructureInputBasicBasicTextDocumentTextDocument, PropertyInfo(alias="TextDocument")]
    ]


class StructureInputBasicBasicWebSearchWebSearch(TypedDict, total=False):
    extraction_criteria: Required[Iterable[ExtractionCriteriaParam]]

    use_local_browser: Required[bool]

    starting_website: Optional[str]


class StructureInputBasicBasicWebSearch(TypedDict, total=False):
    web_search: Required[Annotated[StructureInputBasicBasicWebSearchWebSearch, PropertyInfo(alias="WebSearch")]]


class StructureInputBasicBasicImageDocumentImageDocument(TypedDict, total=False):
    content: Required[FileTypes]

    document_name: Required[str]

    extraction_criteria: Required[Iterable[ExtractionCriteriaParam]]


class StructureInputBasicBasicImageDocument(TypedDict, total=False):
    image_document: Required[
        Annotated[StructureInputBasicBasicImageDocumentImageDocument, PropertyInfo(alias="ImageDocument")]
    ]


StructureInputBasicBasic = Union[
    StructureInputBasicBasicTextDocument, StructureInputBasicBasicWebSearch, StructureInputBasicBasicImageDocument
]


class StructureInputBasic(TypedDict, total=False):
    basic: Required[Annotated[StructureInputBasicBasic, PropertyInfo(alias="Basic")]]
    """
    These are all the types for which we have an agent that is directly capable of
    navigating. There should be a one to one mapping between them.
    """


StructureInput = Union[StructureInputSecIngestor, StructureInputPdfIngestor, StructureInputBasic]
