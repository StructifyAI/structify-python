# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["WikiPage"]


class WikiPage(BaseModel):
    id: str

    created_at: str

    markdown: str

    slug: str

    team_id: str

    title: str

    updated_at: str

    version: int
