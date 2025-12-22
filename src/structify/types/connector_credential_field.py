# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["ConnectorCredentialField"]


class ConnectorCredentialField(BaseModel):
    id: str

    auth_method_id: str

    created_at: datetime

    display_order: int

    field_type: str

    is_optional: bool

    name: str

    updated_at: datetime

    default_value: Optional[str] = None

    description: Optional[str] = None

    label: Optional[str] = None

    options: Optional[object] = None
