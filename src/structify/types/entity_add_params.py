# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .knowledge_graph_param import KnowledgeGraphParam

__all__ = ["EntityAddParams"]


class EntityAddParams(TypedDict, total=False):
    dataset_name: Required[str]
    """Dataset name"""

    entity: Required[KnowledgeGraphParam]
    """Entities and relationships to add"""
