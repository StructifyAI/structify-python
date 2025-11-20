# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["ConnectorGetClarificationRequestsResponse", "Request"]


class Request(BaseModel):
    id: str

    created_at: datetime

    question: str

    resolved: bool

    table_id: str

    updated_at: datetime

    column_id: Optional[str] = None


class ConnectorGetClarificationRequestsResponse(BaseModel):
    requests: List[Request]
