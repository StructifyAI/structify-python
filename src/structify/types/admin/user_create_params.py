# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["UserCreateParams"]


class UserCreateParams(TypedDict, total=False):
    credit_count: Optional[int]

    email: Optional[str]

    feature_flags: List[Literal["test", "pdf_parsing", "boredm_construction_hack", "boredm_construction_model", "none"]]

    is_admin: bool

    permissions: List[Literal["labeler", "debug", "human_llm", "none"]]

    test: bool
