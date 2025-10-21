# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["EntityDeriveAllParams"]


class EntityDeriveAllParams(TypedDict, total=False):
    dataset: Required[str]

    derived_property: Required[str]

    instructions: Required[str]

    table_name: Required[str]

    node_id: Optional[str]
