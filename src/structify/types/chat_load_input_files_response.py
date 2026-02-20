# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["ChatLoadInputFilesResponse"]


class ChatLoadInputFilesResponse(BaseModel):
    files: Dict[str, str]

    latest_timestamp: Optional[datetime] = None
