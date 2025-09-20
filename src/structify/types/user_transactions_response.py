# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["UserTransactionsResponse", "UserTransactionsResponseItem"]


class UserTransactionsResponseItem(BaseModel):
    id: str

    amount: int

    timestamp: datetime

    token_id: str

    credit_grant_id: Optional[str] = None

    job_id: Optional[str] = None


UserTransactionsResponse: TypeAlias = List[UserTransactionsResponseItem]
