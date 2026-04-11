# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DatahubProgress"]


class DatahubProgress(BaseModel):
    databases_created: int

    job_id: str

    job_status: Literal["Queued", "Running", "Completed", "Failed"]

    pages_fetched: int

    records_written: int

    schemas_created: int

    tables_processed: int

    total_datasets: int
