# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .entity_graph_param import EntityGraphParam

__all__ = ["EntityVerifyParams"]


class EntityVerifyParams(TypedDict, total=False):
    dataset: Required[str]

    kg: Required[EntityGraphParam]
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs. Also the first representation of an LLM output in the
    pipeline from raw tool output to being merged into a Neo4j DB
    """

    fix: bool
    """Whether to apply fixes to the dataset"""
