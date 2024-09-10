# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["EntityMergeParams"]


class EntityMergeParams(TypedDict, total=False):
    entity_1_id: Required[str]

    entity_2_id: Required[str]
