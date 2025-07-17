# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["ScrapeListResponse"]


class ScrapeListResponse(BaseModel):
    dataset_name: str

    job_id: str
