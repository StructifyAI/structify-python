# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["EntityDeriveParams"]


class EntityDeriveParams(TypedDict, total=False):
    dataset: Required[str]

    derived_property: Required[str]

    entity_id: Required[str]

    instructions: Required[str]

    node_id: Optional[str]
