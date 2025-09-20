# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["UserUpdateParams", "Updates"]


class UserUpdateParams(TypedDict, total=False):
    updates: Required[Updates]

    current_email: Optional[str]


class Updates(TypedDict, total=False):
    email: Optional[str]

    feature_flags: Optional[
        List[
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
    ]

    full_name: Optional[str]

    is_developer: Optional[bool]

    permissions: Optional[List[Literal["labeler", "qa_labeler", "debug", "human_llm", "none"]]]

    user_type: Optional[Literal["admin", "public", "end_user"]]
