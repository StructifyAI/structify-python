# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Image"]


class Image(BaseModel):
    flag_number: Optional[int] = None

    image: Optional[object] = None
