# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

from .entity_graph_param import EntityGraphParam
from .user_web_source_param import UserWebSourceParam
from .user_document_source_param import UserDocumentSourceParam

__all__ = ["EntityAddBatchParams", "Source"]


class EntityAddBatchParams(TypedDict, total=False):
    dataset: Required[str]

    entity_graphs: Required[Iterable[EntityGraphParam]]

    attempt_merge: bool
    """If true, attempt to merge with existing entities in the dataset"""

    source: Source


Source: TypeAlias = Union[UserWebSourceParam, UserDocumentSourceParam]
