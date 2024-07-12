# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .structify_id import StructifyID

__all__ = ["RunListResponse"]


class RunListResponse(BaseModel):
    id: StructifyID

    creation_time: datetime

    status: Literal["Queued", "Running", "Completed", "Failed"]
