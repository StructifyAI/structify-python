# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .user import User

__all__ = ["UserListResponse", "UserListResponseItem"]


class UserListResponseItem(User):
    tokens: List[str]


UserListResponse: TypeAlias = List[UserListResponseItem]
