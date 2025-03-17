# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["UserTransactionsResponse", "UserTransactionsResponseItem"]


class UserTransactionsResponseItem(BaseModel):
    id: int

    amount: object

    timestamp: datetime

    token_id: object

    job_id: Optional[int] = None


UserTransactionsResponse: TypeAlias = List[UserTransactionsResponseItem]
