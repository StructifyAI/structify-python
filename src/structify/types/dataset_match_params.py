# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .knowledge_graph_param import KnowledgeGraphParam

__all__ = ["DatasetMatchParams"]


class DatasetMatchParams(TypedDict, total=False):
    dataset: Required[str]
    """The dataset to match against"""

    query_kg: Required[KnowledgeGraphParam]
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs. Also the first representation of an LLM output in the
    pipeline from raw tool output to being merged into a Neo4j DB
    """
