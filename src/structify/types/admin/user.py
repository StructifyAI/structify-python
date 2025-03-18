# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["User"]


class User(BaseModel):
    id: str

    created_at: datetime

    email: str

    feature_flags: List[Optional[Literal["functional_test", "pdf_parsing", "boredm_construction_model", "none"]]]

    permissions: List[Optional[Literal["labeler", "qa_labeler", "debug", "human_llm", "none"]]]

    updated_at: datetime

    user_type: Literal["admin", "public", "end_user"]
