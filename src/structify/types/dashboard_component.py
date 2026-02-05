# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["DashboardComponent"]


class DashboardComponent(BaseModel):
    """A component references a viz node and optional display metadata."""

    node_name: str
    """Function name of the viz node that outputs the chart spec."""

    title: str
    """Display title shown in the dashboard layout."""

    description: Optional[str] = None
    """Optional description shown under the component title."""

    span: Optional[int] = None
    """Grid span: 1 (quarter), 2 (half), 3 (three-quarters), 4 (full width)."""
