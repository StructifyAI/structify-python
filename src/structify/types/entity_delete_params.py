# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["EntityDeleteParams"]


class EntityDeleteParams(TypedDict, total=False):
    dataset_name: Required[str]

    entity_id: Required[str]
