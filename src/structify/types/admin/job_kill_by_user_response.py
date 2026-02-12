# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["JobKillByUserResponse"]


class JobKillByUserResponse(BaseModel):
    killed_jobs: int
