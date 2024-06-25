# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = [
    "StructureRunAsyncParams",
    "StructureInput",
    "StructureInputSecIngestor",
    "StructureInputSecIngestorSecIngestor",
    "StructureInputSecIngestorSecIngestorExtractionCriterion",
    "StructureInputPdfIngestor",
    "StructureInputPdfIngestorPdfIngestor",
    "StructureInputPdfIngestorPdfIngestorExtractionCriterion",
    "StructureInputBasic",
    "StructureInputBasicBasic",
    "StructureInputBasicBasicTextDocument",
    "StructureInputBasicBasicWebSearch",
    "StructureInputBasicBasicWebSearchWebSearch",
    "StructureInputBasicBasicWebSearchWebSearchExtractionCriterion",
    "StructureInputBasicBasicImageDocument",
    "StructureInputBasicBasicImageDocumentImageDocument",
    "StructureInputBasicBasicImageDocumentImageDocumentExtractionCriterion",
]


class StructureRunAsyncParams(TypedDict, total=False):
    dataset_name: Required[str]

    structure_input: Required[StructureInput]
    """These are all the types that can be converted into a BasicInputType"""


class StructureInputSecIngestorSecIngestorExtractionCriterion(TypedDict, total=False):
    property_names: Required[List[str]]

    table_name: Required[str]
    """Vec<ExtractionCriteria> = it has to meet every one."""


class StructureInputSecIngestorSecIngestor(TypedDict, total=False):
    extraction_criteria: Required[Iterable[StructureInputSecIngestorSecIngestorExtractionCriterion]]

    accession_number: Optional[str]

    quarter: Optional[int]

    year: Optional[int]


class StructureInputSecIngestor(TypedDict, total=False):
    sec_ingestor: Required[Annotated[StructureInputSecIngestorSecIngestor, PropertyInfo(alias="SECIngestor")]]


class StructureInputPdfIngestorPdfIngestorExtractionCriterion(TypedDict, total=False):
    property_names: Required[List[str]]

    table_name: Required[str]
    """Vec<ExtractionCriteria> = it has to meet every one."""


class StructureInputPdfIngestorPdfIngestor(TypedDict, total=False):
    extraction_criteria: Required[Iterable[StructureInputPdfIngestorPdfIngestorExtractionCriterion]]

    path: Required[str]


class StructureInputPdfIngestor(TypedDict, total=False):
    pdf_ingestor: Required[Annotated[StructureInputPdfIngestorPdfIngestor, PropertyInfo(alias="PDFIngestor")]]
    """This is currently a very simple ingestor.

    It converts everything to an image and processes them independently.
    """


class StructureInputBasicBasicTextDocument(TypedDict, total=False):
    text_document: Required[Annotated[object, PropertyInfo(alias="TextDocument")]]


class StructureInputBasicBasicWebSearchWebSearchExtractionCriterion(TypedDict, total=False):
    property_names: Required[List[str]]

    table_name: Required[str]
    """Vec<ExtractionCriteria> = it has to meet every one."""


class StructureInputBasicBasicWebSearchWebSearch(TypedDict, total=False):
    extraction_criteria: Required[Iterable[StructureInputBasicBasicWebSearchWebSearchExtractionCriterion]]

    use_local_browser: Required[bool]

    starting_website: Optional[str]


class StructureInputBasicBasicWebSearch(TypedDict, total=False):
    web_search: Required[Annotated[StructureInputBasicBasicWebSearchWebSearch, PropertyInfo(alias="WebSearch")]]


class StructureInputBasicBasicImageDocumentImageDocumentExtractionCriterion(TypedDict, total=False):
    property_names: Required[List[str]]

    table_name: Required[str]
    """Vec<ExtractionCriteria> = it has to meet every one."""


class StructureInputBasicBasicImageDocumentImageDocument(TypedDict, total=False):
    content: Required[FileTypes]

    document_name: Required[str]

    extraction_criteria: Required[Iterable[StructureInputBasicBasicImageDocumentImageDocumentExtractionCriterion]]


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
