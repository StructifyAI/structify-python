# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SortByParam"]


class SortByParam(TypedDict, total=False):
    col_id: Required[Literal["creation_time"]]

    sort: Required[Literal["asc", "desc"]]
