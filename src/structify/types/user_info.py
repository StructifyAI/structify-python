# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["UserInfo"]


class UserInfo(BaseModel):
    credits_remaining: int

    credits_used: int

    is_admin: bool

    permissions: List[Literal["labeler", "debug", "human_llm", "none"]]

    username: str
