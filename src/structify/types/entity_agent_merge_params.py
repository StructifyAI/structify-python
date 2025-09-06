# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["EntityAgentMergeParams"]


class EntityAgentMergeParams(TypedDict, total=False):
    dataset: Required[str]

    entity_id: Required[str]

    force_consider_entities: SequenceNotStr[str]

    top_k: int
