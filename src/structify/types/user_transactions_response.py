# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["UserTransactionsResponse", "UserTransactionsResponseItem"]


class UserTransactionsResponseItem(BaseModel):
    amount: int

    timestamp: datetime

    transaction_id: str


UserTransactionsResponse: TypeAlias = List[UserTransactionsResponseItem]
