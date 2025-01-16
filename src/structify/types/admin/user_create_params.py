# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["UserCreateParams"]


class UserCreateParams(TypedDict, total=False):
    credit_count: Optional[int]

    email: Optional[str]

    is_admin: bool

    permissions: Optional[List[Literal["pdf_parsing", "labeler", "debug", "none"]]]

    test: bool
