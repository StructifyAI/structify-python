# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .knowledge_graph_param import KnowledgeGraphParam

__all__ = [
    "StructureRunAsyncParams",
    "Source",
    "SourcePdfIngestor",
    "SourcePdfIngestorPdfIngestor",
    "SourceWebSearch",
    "SourceWebSearchWebSearch",
    "ExtractionCriterion",
    "ExtractionCriterionRelationship",
    "ExtractionCriterionRelationshipRelationship",
    "ExtractionCriterionEntity",
    "ExtractionCriterionEntityEntity",
    "ExtractionCriterionProperty",
    "ExtractionCriterionPropertyProperty",
]


class StructureRunAsyncParams(TypedDict, total=False):
    dataset: Required[str]

    source: Required[Source]
    """These are all the types that can be converted into a BasicInputType"""

    extraction_criteria: Iterable[ExtractionCriterion]

    seeded_entity: KnowledgeGraphParam
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs. Also the first representation of an LLM output in the
    pipeline from raw tool output to being merged into a Neo4j DB
    """

    special_job_type: Optional[Literal["HumanLLM"]]


class SourcePdfIngestorPdfIngestor(TypedDict, total=False):
    path: Required[str]


class SourcePdfIngestor(TypedDict, total=False):
    pdf_ingestor: Required[Annotated[SourcePdfIngestorPdfIngestor, PropertyInfo(alias="PDFIngestor")]]
    """Ingest all pages of a PDF and process them independently."""


class SourceWebSearchWebSearch(TypedDict, total=False):
    starting_searches: List[str]

    starting_urls: List[str]


class SourceWebSearch(TypedDict, total=False):
    web_search: Required[Annotated[SourceWebSearchWebSearch, PropertyInfo(alias="WebSearch")]]


Source: TypeAlias = Union[SourcePdfIngestor, SourceWebSearch]


class ExtractionCriterionRelationshipRelationship(TypedDict, total=False):
    relationship_name: Required[str]


class ExtractionCriterionRelationship(TypedDict, total=False):
    relationship: Required[Annotated[ExtractionCriterionRelationshipRelationship, PropertyInfo(alias="Relationship")]]


class ExtractionCriterionEntityEntity(TypedDict, total=False):
    seeded_kg_id: Required[int]
    """The integer id corresponding to an entity in the seeded kg"""

    dataset_entity_id: Optional[str]


class ExtractionCriterionEntity(TypedDict, total=False):
    entity: Required[Annotated[ExtractionCriterionEntityEntity, PropertyInfo(alias="Entity")]]


class ExtractionCriterionPropertyProperty(TypedDict, total=False):
    property_names: Required[List[str]]

    table_name: Required[str]
    """Vec<ExtractionCriteria> = it has to meet every one."""


class ExtractionCriterionProperty(TypedDict, total=False):
    property: Required[Annotated[ExtractionCriterionPropertyProperty, PropertyInfo(alias="Property")]]


ExtractionCriterion: TypeAlias = Union[
    ExtractionCriterionRelationship, ExtractionCriterionEntity, ExtractionCriterionProperty
]
