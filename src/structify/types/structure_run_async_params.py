# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .knowledge_graph_param import KnowledgeGraphParam
from .save_requirement_param import SaveRequirementParam

__all__ = ["StructureRunAsyncParams", "Source", "SourcePdf", "SourcePdfPdf", "SourceWeb", "SourceWebWeb", "StopConfig"]


class StructureRunAsyncParams(TypedDict, total=False):
    dataset: Required[str]

    source: Required[Source]
    """These are all the types that can be converted into a BasicInputType"""

    node_id: Optional[str]

    save_requirement: Iterable[SaveRequirementParam]

    seeded_entity: KnowledgeGraphParam
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs. Also the first representation of an LLM output in the
    pipeline from raw tool output to being merged into a DB
    """

    special_job_type: Optional[Literal["HumanLLM"]]

    stop_config: Optional[StopConfig]
    """Configuration parameters for the StopChecker"""


class SourcePdfPdf(TypedDict, total=False):
    path: Required[str]


class SourcePdf(TypedDict, total=False):
    pdf: Required[Annotated[SourcePdfPdf, PropertyInfo(alias="PDF")]]
    """Ingest all pages of a PDF and process them independently."""


class SourceWebWeb(TypedDict, total=False):
    banned_domains: SequenceNotStr[str]

    starting_searches: SequenceNotStr[str]

    starting_urls: SequenceNotStr[str]


class SourceWeb(TypedDict, total=False):
    web: Required[Annotated[SourceWebWeb, PropertyInfo(alias="Web")]]


Source: TypeAlias = Union[SourcePdf, SourceWeb]


class StopConfig(TypedDict, total=False):
    max_steps_without_save: Required[int]

    max_errors: Optional[int]

    max_execution_time_secs: Optional[int]

    max_total_steps: Optional[int]
