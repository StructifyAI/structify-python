# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ReportWrongParams"]


class ReportWrongParams(TypedDict, total=False):
    id: Required[str]

    property: Optional[str]
    """A property that is being reported"""

    source_url: Optional[str]
    """Correct source URL for the reported entity"""
