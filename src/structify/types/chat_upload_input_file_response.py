# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["ChatUploadInputFileResponse", "File"]


class File(BaseModel):
    chat_session_id: str

    content_type: str

    created_at: datetime

    file_size: int

    filename: str


class ChatUploadInputFileResponse(BaseModel):
    file: File
