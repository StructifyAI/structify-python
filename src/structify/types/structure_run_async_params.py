# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .knowledge_graph_param import KnowledgeGraphParam
from .save_requirement_param import SaveRequirementParam

__all__ = [
    "StructureRunAsyncParams",
    "Source",
    "SourceScrape",
    "SourceScrapeScrape",
]


class StructureRunAsyncParams(TypedDict, total=False):
    dataset: Required[str]

    source: Source
    """Optional source to use for the run. Omit for no-resources mode."""

    instructions: Optional[str]

    model: Optional[str]

    use_proxy: Optional[bool]

    node_id: Optional[str]

    save_requirement: Iterable[SaveRequirementParam]

    seeded_entity: KnowledgeGraphParam
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs. Also the first representation of an LLM output in the
    pipeline from raw tool output to being merged into a DB
    """


class SourceScrapeScrape(TypedDict, total=False):
    url_column: Required[str]


class SourceScrape(TypedDict, total=False):
    scrape: Required[Annotated[SourceScrapeScrape, PropertyInfo(alias="Scrape")]]


Source: TypeAlias = Union[Literal["Web"], SourceScrape]
