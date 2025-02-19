# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TokenResponse"]


class TokenResponse(BaseModel):
    token: str

    permissions: List[Literal["labeler", "qa_labeler", "debug", "human_llm", "none"]]
