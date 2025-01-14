# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["User"]


class User(BaseModel):
    email: str

    feature_flags: Optional[List[str]] = None

    user_type: Optional[Literal["Admin", "Public", "EndUser"]] = None
