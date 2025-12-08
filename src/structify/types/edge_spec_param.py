# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["EdgeSpecParam"]


class EdgeSpecParam(TypedDict, total=False):
    source_node_index: Required[int]

    target_node_index: Required[int]
