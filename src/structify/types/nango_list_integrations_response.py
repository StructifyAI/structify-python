# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["NangoListIntegrationsResponse", "NangoListIntegrationsResponseItem"]


class NangoListIntegrationsResponseItem(BaseModel):
    """A Nango integration (OAuth provider configuration)"""

    created_at: datetime

    provider: str

    unique_key: str

    updated_at: datetime

    display_name: Optional[str] = None

    logo: Optional[str] = None


NangoListIntegrationsResponse: TypeAlias = List[NangoListIntegrationsResponseItem]
