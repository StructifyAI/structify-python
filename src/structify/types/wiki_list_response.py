# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["WikiListResponse", "WikiListResponseItem"]


class WikiListResponseItem(BaseModel):
    id: str

    created_at: str

    markdown: str

    slug: str

    team_id: str

    title: str

    updated_at: str

    version: int


WikiListResponse: TypeAlias = List[WikiListResponseItem]
