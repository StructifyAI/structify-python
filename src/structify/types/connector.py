# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Connector"]


class Connector(BaseModel):
    id: str

    created_at: datetime

    llm_information_store: str

    name: str

    project_id: str

    updated_at: datetime

    description: Optional[str] = None
