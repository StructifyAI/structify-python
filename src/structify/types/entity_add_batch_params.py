# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

from .knowledge_graph_param import KnowledgeGraphParam

__all__ = ["EntityAddBatchParams", "Source", "SourceUserWebSource", "SourceUserDocumentSource"]


class EntityAddBatchParams(TypedDict, total=False):
    dataset: Required[str]

    entity_graphs: Required[Iterable[KnowledgeGraphParam]]

    attempt_merge: bool
    """If true, attempt to merge with existing entities in the dataset"""

    source: Source


class SourceUserWebSource(TypedDict, total=False):
    url: Required[str]


class SourceUserDocumentSource(TypedDict, total=False):
    name: Required[str]

    page: Required[int]


Source: TypeAlias = Union[SourceUserWebSource, SourceUserDocumentSource]
