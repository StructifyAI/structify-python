# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["StructureJobStatusResponse"]


class StructureJobStatusResponse(BaseModel):
    job_status: List[Literal["Queued", "Running", "Completed", "Failed"]]

    log_nodes: List[str]
