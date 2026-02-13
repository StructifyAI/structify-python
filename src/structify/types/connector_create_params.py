# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["ConnectorCreateParams"]


class ConnectorCreateParams(TypedDict, total=False):
    known_connector_type: Required[str]

    name: Required[str]

    team_id: Required[str]

    description: Optional[str]

    nango_connection_id: Optional[str]
    """Nango connection ID for OAuth token management"""

    nango_integration_id: Optional[str]
    """Nango integration ID (e.g., "linear", "slack")"""

    secrets: Dict[str, str]
    """Optional secrets/environment variables for the connector"""
