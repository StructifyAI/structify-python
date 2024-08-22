# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = ["UserInfo"]

class UserInfo(BaseModel):
    credits_remaining: int

    credits_used: int

    is_admin: bool

    username: str