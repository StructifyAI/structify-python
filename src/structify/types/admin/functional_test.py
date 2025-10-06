# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FunctionalTest"]


class FunctionalTest(BaseModel):
    id: str

    created_at: datetime

    created_by: str

    api_model_override: Optional[str] = FieldInfo(alias="model_override", default=None)

    prompt_override: Optional[str] = None
