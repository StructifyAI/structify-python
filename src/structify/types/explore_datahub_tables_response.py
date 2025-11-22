# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["ExploreDatahubTablesResponse"]


class ExploreDatahubTablesResponse(BaseModel):
    jobs_queued: int

    tables_found: int
