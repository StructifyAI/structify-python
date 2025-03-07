# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

from .knowledge_graph_param import KnowledgeGraphParam

__all__ = ["EntityAddParams", "Source", "SourceUserWebSource", "SourceUserDocumentSource"]


class EntityAddParams(TypedDict, total=False):
    dataset: Required[str]

    entity_graph: Required[KnowledgeGraphParam]
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs. Also the first representation of an LLM output in the
    pipeline from raw tool output to being merged into a Neo4j DB
    """

    attempt_merge: bool
    """If true, attempt to merge with existing entities in the dataset"""

    source: Source


class SourceUserWebSource(TypedDict, total=False):
    url: Required[str]


class SourceUserDocumentSource(TypedDict, total=False):
    name: Required[str]

    page: Required[int]


Source: TypeAlias = Union[SourceUserWebSource, SourceUserDocumentSource]
