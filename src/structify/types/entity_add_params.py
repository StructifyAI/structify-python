# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

from .entity_graph_param import EntityGraphParam
from .user_web_source_param import UserWebSourceParam
from .user_document_source_param import UserDocumentSourceParam

__all__ = ["EntityAddParams", "Source"]


class EntityAddParams(TypedDict, total=False):
    dataset: Required[str]

    entity_graph: Required[EntityGraphParam]
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs. Also the first representation of an LLM output in the
    pipeline from raw tool output to being merged into a Neo4j DB
    """

    attempt_merge: bool
    """If true, attempt to merge with existing entities in the dataset"""

    source: Source


Source: TypeAlias = Union[UserWebSourceParam, UserDocumentSourceParam]
