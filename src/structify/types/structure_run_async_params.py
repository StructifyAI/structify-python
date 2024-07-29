# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._types import FileTypes
from .._utils import PropertyInfo
from .knowledge_graph_param import KnowledgeGraphParam
from .extraction_criteria_param import ExtractionCriteriaParam

__all__ = [
    "RunAsyncParams",
    "SECFiling",
    "PDF",
    "Text",
    "Web",
    "DocumentImage",
]


class RunAsyncParams(TypedDict, total=False):
    dataset_name: Required[str]

    source: Required[Union[SECFiling, PDF, Text, Web, DocumentImage]]
    """These are all the types that a structuring run can be created from."""

    extraction_criteria: Required[Iterable[ExtractionCriteriaParam]]

    starting_entity: KnowledgeGraphParam
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs. Also the first representation of an LLM output in the
    pipeline from raw tool output to being merged into a Neo4j DB
    """


class SECFiling(TypedDict, total=False):
    accession_number: Optional[str]

    quarter: Optional[int]

    year: Optional[int]

    sec_filing: Required[Annotated[dict, PropertyInfo(alias="SECFiling")]]


class PDF(TypedDict, total=False):
    path: Required[str]

    pdf: Required[Annotated[dict, PropertyInfo(alias="PDF")]]
    """This is currently a very simple ingestor.

    It converts everything to an image and processes them independently.
    """


class Text(TypedDict, total=False):
    content: Optional[str]

    path: Optional[str]

    save: bool

    text: Required[Annotated[dict, PropertyInfo(alias="Text")]]


class Web(TypedDict, total=False):
    use_local_browser: Required[bool]

    starting_website: Optional[str]

    web: Required[Annotated[dict, PropertyInfo(alias="Web")]]


class DocumentImage(TypedDict, total=False):
    content: Required[FileTypes]

    document_name: Required[str]

    document: Required[Annotated[dict, PropertyInfo(alias="DocumentImage")]]
