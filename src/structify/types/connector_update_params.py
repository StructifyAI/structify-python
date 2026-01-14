# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ConnectorUpdateParams"]


class ConnectorUpdateParams(TypedDict, total=False):
    connector_catalouge_id: Required[str]

    description: Optional[str]

    name: Optional[str]

    refresh_script: Optional[str]

    usage_snippet_override: Optional[str]
