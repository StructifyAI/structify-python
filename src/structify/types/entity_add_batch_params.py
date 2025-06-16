# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .knowledge_graph_param import KnowledgeGraphParam

__all__ = ["EntityAddBatchParams", "Source", "SourceWeb", "SourceDocumentPage", "SourceSecFiling", "StopConfig"]


class EntityAddBatchParams(TypedDict, total=False):
    dataset: Required[str]

    entity_graphs: Required[Iterable[KnowledgeGraphParam]]

    attempt_merge: bool
    """If true, attempt to merge with existing entities in the dataset"""

    skip_malformed_entities: bool

    source: Source

    stop_config: Optional[StopConfig]
    """Configuration parameters for the StopChecker"""

    triggering_workflow: Optional[str]


class SourceWeb(TypedDict, total=False):
    web: Required[Annotated[str, PropertyInfo(alias="Web")]]


class SourceDocumentPage(TypedDict, total=False):
    document_page: Required[Annotated[Iterable[object], PropertyInfo(alias="DocumentPage")]]


class SourceSecFiling(TypedDict, total=False):
    sec_filing: Required[Annotated[Iterable[object], PropertyInfo(alias="SecFiling")]]


Source: TypeAlias = Union[Literal["None"], SourceWeb, SourceDocumentPage, SourceSecFiling]


class StopConfig(TypedDict, total=False):
    max_steps_without_save: Required[int]

    max_errors: Optional[int]

    max_execution_time_secs: Optional[int]

    max_total_steps: Optional[int]
