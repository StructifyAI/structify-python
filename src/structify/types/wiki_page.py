# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["WikiPage"]


class WikiPage(BaseModel):
    id: str

    created_at: str

    created_by: str

    markdown: str

    slug: str

    team_id: str

    title: str

    updated_at: str

    version: int

    approved_at: Optional[str] = None

    approved_by: Optional[str] = None

    chat_session_id: Optional[str] = None
