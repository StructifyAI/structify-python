# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["EntityReportParams"]


class EntityReportParams(TypedDict, total=False):
    id: Required[str]

    property: Optional[str]
    """Property name that is incorrect"""
