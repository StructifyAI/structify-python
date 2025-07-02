# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["ChatAddGitCommitResponse", "Commit"]


class Commit(BaseModel):
    id: str

    chat_session_id: str

    commit_hash: str

    created_at: datetime


class ChatAddGitCommitResponse(BaseModel):
    commit: Commit
