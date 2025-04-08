# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["UserInfo"]


class UserInfo(BaseModel):
    credits_remaining: int

    credits_used: int

    feature_flags: List[
        Literal["functional_test", "pdf_parsing", "boredm_construction_model", "generic_suspicious_queue", "none"]
    ]

    is_admin: bool

    permissions: List[Literal["labeler", "qa_labeler", "debug", "human_llm", "none"]]

    username: str
