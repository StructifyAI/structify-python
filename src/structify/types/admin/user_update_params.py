# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["UserUpdateParams"]


class UserUpdateParams(TypedDict, total=False):
    current_email: Required[str]

    new_email: Optional[str]

    new_permissions: Optional[List[Literal["pdf_parsing", "labeler", "debug", "none"]]]
