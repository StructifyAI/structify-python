# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["DashboardComponentParam"]


class DashboardComponentParam(TypedDict, total=False):
    node_name: Required[str]

    title: Required[str]

    description: Optional[str]

    span: Optional[int]
