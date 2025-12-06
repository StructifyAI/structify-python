# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TokenResponse"]


class TokenResponse(BaseModel):
    permissions: List[Literal["labeler", "qa_labeler", "debug", "human_llm", "none"]]

    refresh_token: str

    session_expires_at: str

    session_token: str
