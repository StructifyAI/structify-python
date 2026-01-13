# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ConnectorSummary"]


class ConnectorSummary(BaseModel):
    id: str

    name: str

    logo_url: Optional[str] = None
    """Base64 data URI for the logo (e.g., "data:image/svg+xml;base64,...")"""
