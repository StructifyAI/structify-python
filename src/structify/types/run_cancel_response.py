# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .structify_id import StructifyID

__all__ = ["RunCancelResponse"]


class RunCancelResponse(BaseModel):
    id: StructifyID

    status: Literal["Queued", "Running", "Completed", "Failed"]
