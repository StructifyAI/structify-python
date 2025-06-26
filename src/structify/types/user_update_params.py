# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["UserUpdateParams"]


class UserUpdateParams(TypedDict, total=False):
    current_email: Optional[str]

    is_developer: Optional[bool]

    new_email: Optional[str]

    new_feature_flags: Optional[
        List[
            Literal[
                "functional_test",
                "pdf_parsing",
                "boredm_construction_model",
                "generic_suspicious_queue",
                "new_use_case_preview",
                "none",
            ]
        ]
    ]

    new_permissions: Optional[List[Literal["labeler", "qa_labeler", "debug", "human_llm", "none"]]]
