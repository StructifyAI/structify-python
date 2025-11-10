# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["UserUpdateParams", "Updates"]


class UserUpdateParams(TypedDict, total=False):
    updates: Required[Updates]

    current_email: Optional[str]


class Updates(TypedDict, total=False):
    apollo_data: object

    company_description: Optional[str]

    company_name: Optional[str]

    cufinder_data: object

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
                "gemini25pro",
                "claude_sonnet4",
                "none",
            ]
        ]
    ]

    feature_overrides: object

    full_name: Optional[str]

    is_developer: Optional[bool]

    job_title: Optional[str]

    last_selected_team_id: Optional[str]

    linkedin_url: Optional[str]

    permissions: Optional[List[Literal["labeler", "qa_labeler", "debug", "human_llm", "none"]]]

    user_type: Optional[Literal["admin", "public", "end_user"]]
