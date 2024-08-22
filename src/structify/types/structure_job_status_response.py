# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import List

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = ["StructureJobStatusResponse"]

class StructureJobStatusResponse(BaseModel):
    job_status: List[Literal["Queued", "Running", "Completed", "Failed"]]

    log_nodes: List[str]