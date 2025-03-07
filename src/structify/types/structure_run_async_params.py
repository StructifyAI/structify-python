# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .knowledge_graph_param import KnowledgeGraphParam
from .extraction_criteria_param import ExtractionCriteriaParam

__all__ = [
    "StructureRunAsyncParams",
    "StructureInput",
    "StructureInputPdfIngestor",
    "StructureInputPdfIngestorPdfIngestor",
    "StructureInputWebSearch",
    "StructureInputWebSearchWebSearch",
]


class StructureRunAsyncParams(TypedDict, total=False):
    name: Required[str]

    structure_input: Required[StructureInput]
    """These are all the types that can be converted into a BasicInputType"""

    extraction_criteria: Iterable[ExtractionCriteriaParam]

    seeded_entity: KnowledgeGraphParam
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs. Also the first representation of an LLM output in the
    pipeline from raw tool output to being merged into a Neo4j DB
    """

    special_job_type: Optional[Literal["HumanLLM"]]


class StructureInputPdfIngestorPdfIngestor(TypedDict, total=False):
    path: Required[str]


class StructureInputPdfIngestor(TypedDict, total=False):
    pdf_ingestor: Required[Annotated[StructureInputPdfIngestorPdfIngestor, PropertyInfo(alias="PDFIngestor")]]
    """Ingest all pages of a PDF and process them independently."""


class StructureInputWebSearchWebSearch(TypedDict, total=False):
    starting_searches: List[str]

    starting_urls: List[str]


class StructureInputWebSearch(TypedDict, total=False):
    web_search: Required[Annotated[StructureInputWebSearchWebSearch, PropertyInfo(alias="WebSearch")]]


StructureInput: TypeAlias = Union[StructureInputPdfIngestor, StructureInputWebSearch]
