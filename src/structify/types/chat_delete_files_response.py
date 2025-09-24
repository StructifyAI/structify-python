# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["ChatDeleteFilesResponse"]


class ChatDeleteFilesResponse(BaseModel):
    commit_hash: str

    files_deleted: int
