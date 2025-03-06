# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["WaitInput"]


class WaitInput(BaseModel):
    seconds: Optional[int] = None
    """Time in seconds to wait"""
