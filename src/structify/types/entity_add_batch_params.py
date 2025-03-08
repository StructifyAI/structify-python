# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Required, TypedDict

from .knowledge_graph_param import KnowledgeGraphParam

__all__ = ["EntityAddBatchParams"]


class EntityAddBatchParams(TypedDict, total=False):
    dataset: Required[str]

    entity_graphs: Required[Iterable[KnowledgeGraphParam]]

    attempt_merge: bool
    """If true, attempt to merge with existing entities in the dataset"""

    source: Union[str, Iterable[object], Iterable[object], Optional[object]]
