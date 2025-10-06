# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FunctionalTestListResponse", "FunctionalTestListResponseItem"]


class FunctionalTestListResponseItem(BaseModel):
    id: str

    created_at: datetime

    created_by: str

    created_by_email: str

    api_model_override: Optional[str] = FieldInfo(alias="model_override", default=None)

    prompt_override: Optional[str] = None


FunctionalTestListResponse: TypeAlias = List[FunctionalTestListResponseItem]
