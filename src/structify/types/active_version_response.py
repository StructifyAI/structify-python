# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .active_version_data import ActiveVersionData

__all__ = ["ActiveVersionResponse"]


class ActiveVersionResponse(BaseModel):
    active_version: Optional[ActiveVersionData] = None
    """Active version data"""
