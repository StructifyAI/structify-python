# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SessionCreateEdgeParams"]


class SessionCreateEdgeParams(TypedDict, total=False):
    source_node_id: Required[str]

    target_node_id: Required[str]
