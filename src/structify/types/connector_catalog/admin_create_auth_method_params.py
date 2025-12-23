# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AdminCreateAuthMethodParams"]


class AdminCreateAuthMethodParams(TypedDict, total=False):
    auth_type: Required[Literal["credentials", "oauth_nango"]]

    connector_catalog_id: Required[str]

    is_active: Required[bool]

    priority: Required[int]

    label: Optional[str]

    nango_integration_key: Optional[str]
