# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["TemplateQuestion"]


class TemplateQuestion(BaseModel):
    prompt: str

    options: Optional[List[str]] = None
