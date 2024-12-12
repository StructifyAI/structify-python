# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["EntityGetParams"]


class EntityGetParams(TypedDict, total=False):
    id: Required[str]

    resolve_id: bool
