# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["ChatRevertToCommitResponse"]


class ChatRevertToCommitResponse(BaseModel):
    commit_hash: str
    """The commit hash that was reverted to"""

    reverted_at: datetime
    """Timestamp when the revert occurred"""
