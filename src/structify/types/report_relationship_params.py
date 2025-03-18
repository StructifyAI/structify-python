# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ReportRelationshipParams"]


class ReportRelationshipParams(TypedDict, total=False):
    relationship_type: Required[str]

    source_id: Optional[str]

    source_url: Optional[str]

    target_id: Optional[str]
