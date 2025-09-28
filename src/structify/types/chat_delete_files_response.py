# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["ChatDeleteFilesResponse"]


class ChatDeleteFilesResponse(BaseModel):
    files_deleted: int
