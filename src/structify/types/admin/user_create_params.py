# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["UserCreateParams"]


class UserCreateParams(TypedDict, total=False):
    credit_count: Optional[int]

    email: Optional[str]

    feature_flags: Optional[List[Literal["PDFParsing", "Labeler", "None"]]]

    is_admin: bool

    test: bool
