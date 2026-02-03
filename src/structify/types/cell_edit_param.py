# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CellEditParam"]


class CellEditParam(TypedDict, total=False):
    column_name: Required[str]

    row_index: Required[int]

    value: Required[str]
