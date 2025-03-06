# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .knowledge_graph_param import KnowledgeGraphParam
from .extraction_criteria_param import ExtractionCriteriaParam

__all__ = ["StructureRunAsyncParams", "Source", "SourcePdfIngestor", "SourceWebSearch"]


class StructureRunAsyncParams(TypedDict, total=False):
    dataset: Required[str]

    source: Required[Source]
    """These are all the types that can be converted into a BasicInputType"""

    extraction_criteria: Iterable[ExtractionCriteriaParam]

    seeded_entity: KnowledgeGraphParam
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs. Also the first representation of an LLM output in the
    pipeline from raw tool output to being merged into a Neo4j DB
    """

    special_job_type: Optional[Literal["HumanLLM"]]


class SourcePdfIngestor(TypedDict, total=False):
    path: Required[str]


class SourceWebSearch(TypedDict, total=False):
    starting_searches: List[str]

    starting_urls: List[str]


Source: TypeAlias = Union[SourcePdfIngestor, SourceWebSearch]
