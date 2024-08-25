# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ReportEntityParams"]


class ReportEntityParams(TypedDict, total=False):
    id: Required[str]

    property: Optional[str]
    """A short message about why the entity is being reported"""
