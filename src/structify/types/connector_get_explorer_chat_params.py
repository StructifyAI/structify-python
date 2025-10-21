# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ConnectorGetExplorerChatParams"]


class ConnectorGetExplorerChatParams(TypedDict, total=False):
    run_id: Required[str]
    """Exploration run ID (required)"""
