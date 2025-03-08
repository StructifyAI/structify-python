# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .knowledge_graph_param import KnowledgeGraphParam

__all__ = [
    "StructureRunAsyncParams",
    "Source",
    "SourcePdf",
    "SourcePdfPdf",
    "SourceWeb",
    "SourceWebWeb",
    "SaveRequirement",
    "SaveRequirementRequiredRelationship",
    "SaveRequirementRequiredEntity",
    "SaveRequirementRequiredProperty",
]


class StructureRunAsyncParams(TypedDict, total=False):
    dataset: Required[str]

    source: Required[Source]
    """These are all the types that can be converted into a BasicInputType"""

    save_requirement: Iterable[SaveRequirement]

    seeded_entity: KnowledgeGraphParam
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs. Also the first representation of an LLM output in the
    pipeline from raw tool output to being merged into a Neo4j DB
    """

    special_job_type: Optional[Literal["HumanLLM"]]


class SourcePdfPdf(TypedDict, total=False):
    path: Required[str]


class SourcePdf(TypedDict, total=False):
    pdf: Required[Annotated[SourcePdfPdf, PropertyInfo(alias="PDF")]]
    """Ingest all pages of a PDF and process them independently."""


class SourceWebWeb(TypedDict, total=False):
    starting_searches: List[str]

    starting_urls: List[str]


class SourceWeb(TypedDict, total=False):
    web: Required[Annotated[SourceWebWeb, PropertyInfo(alias="Web")]]


Source: TypeAlias = Union[SourcePdf, SourceWeb]


class SaveRequirementRequiredRelationship(TypedDict, total=False):
    relationship_name: Required[str]


class SaveRequirementRequiredEntity(TypedDict, total=False):
    seeded_entity_id: Required[int]
    """
    The integer id corresponding to an entity in the seeded entity graph (different
    from the global dataset entity id)
    """

    entity_id: Optional[str]


class SaveRequirementRequiredProperty(TypedDict, total=False):
    property_names: Required[List[str]]
    """If there are multiple properties, it can match just one of them"""

    table_name: Required[str]
    """The table name of the entity to update"""


SaveRequirement: TypeAlias = Union[
    SaveRequirementRequiredRelationship, SaveRequirementRequiredEntity, SaveRequirementRequiredProperty
]
