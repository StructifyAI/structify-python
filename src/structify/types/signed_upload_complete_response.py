# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .workflow_session_node import WorkflowSessionNode

__all__ = ["SignedUploadCompleteResponse", "File"]


class File(BaseModel):
    chat_session_id: str

    content_type: str

    created_at: datetime

    file_size: int

    filename: str


class SignedUploadCompleteResponse(BaseModel):
    file: Optional[File] = None

    node: Optional[WorkflowSessionNode] = None
