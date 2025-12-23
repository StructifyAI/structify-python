# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["PendingNangoIntegration"]


class PendingNangoIntegration(BaseModel):
    provider: str

    unique_key: str

    display_name: Optional[str] = None

    logo_url: Optional[str] = None
