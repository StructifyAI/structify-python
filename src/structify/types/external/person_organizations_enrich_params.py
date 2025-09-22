# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["PersonOrganizationsEnrichParams"]


class PersonOrganizationsEnrichParams(TypedDict, total=False):
    domain: Optional[str]
    """Organization domain"""

    organization_name: Optional[str]
    """Organization name"""
