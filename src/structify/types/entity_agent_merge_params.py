# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["EntityAgentMergeParams"]


class EntityAgentMergeParams(TypedDict, total=False):
    dataset: Required[str]

    entity_id: Required[str]

    force_consider_entities: List[str]

    top_k: int
