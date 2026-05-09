# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict
from datetime import datetime

from .._models import BaseModel

__all__ = ["SignedUploadInitResponse"]


class SignedUploadInitResponse(BaseModel):
    blob_name: str

    expires_at: datetime

    required_headers: Dict[str, str]

    upload_url: str
