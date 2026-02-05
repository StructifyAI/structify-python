# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["DashboardComponentParam"]


class DashboardComponentParam(TypedDict, total=False):
    """A component references a viz node and optional display metadata."""

    node_name: Required[str]
    """Function name of the viz node that outputs the chart spec."""

    title: Required[str]
    """Display title shown in the dashboard layout."""

    description: Optional[str]
    """Optional description shown under the component title."""

    span: Optional[int]
    """Grid span: 1 (quarter), 2 (half), 3 (three-quarters), 4 (full width)."""
