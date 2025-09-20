# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["UserInfo"]


class UserInfo(BaseModel):
    credits_remaining: int

    credits_used: int

    feature_flags: List[
        Literal[
            "functional_test",
            "pdf_parsing",
            "boredm_construction_model",
            "generic_suspicious_queue",
            "new_use_case_preview",
            "bedrock_codegen",
            "cerebras_codegen",
            "none",
        ]
    ]

    full_name: str

    is_developer: bool

    permissions: List[Literal["labeler", "qa_labeler", "debug", "human_llm", "none"]]

    user_id: str

    user_type: Literal["admin", "public", "end_user"]

    username: str

    survey_completed_at: Optional[datetime] = None
