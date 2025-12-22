# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ConnectorAuthMethod"]


class ConnectorAuthMethod(BaseModel):
    id: str

    auth_type: Literal["credentials", "oauth_nango"]

    connector_catalog_id: str

    created_at: datetime

    is_active: bool

    priority: int

    updated_at: datetime

    label: Optional[str] = None

    nango_integration_key: Optional[str] = None
