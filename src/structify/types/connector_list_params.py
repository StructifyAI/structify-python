# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ConnectorListParams"]


class ConnectorListParams(TypedDict, total=False):
    project_id: Required[str]
    """Project ID to list connectors for"""

    limit: int

    offset: int
