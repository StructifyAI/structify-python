# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["JobStatusResponse"]


class JobStatusResponse(BaseModel):
    completed: int

    failed: int

    queued: int

    running: int

    total: int
