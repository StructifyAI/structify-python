# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["NextActionGetTrainingDataParams"]


class NextActionGetTrainingDataParams(TypedDict, total=False):
    from_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    job_id: Optional[str]

    limit: int

    offset: int

    status: Optional[Literal["HumanLLMLabel", "LLMOutput", "Pending", "Reviewed", "Verified", "Others"]]

    to_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
