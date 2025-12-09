# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["UserTransactionsResponse", "UserTransactionsResponseItem"]


class UserTransactionsResponseItem(BaseModel):
    """Represents a transaction in our database."""

    id: str

    amount: int

    membership_id: str

    timestamp: datetime

    credit_grant_id: Optional[str] = None

    external_service: Optional[Literal["People", "Search", "News"]] = None

    job_id: Optional[str] = None


UserTransactionsResponse: TypeAlias = List[UserTransactionsResponseItem]
