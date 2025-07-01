# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel
from .chat_prompt import ChatPrompt

__all__ = ["JobGetScrapersResponse", "JobGetScrapersResponseItem"]


class JobGetScrapersResponseItem(BaseModel):
    base_url: str

    is_newly_created: bool

    scraper_created_at: datetime

    scraper_id: str

    scraper_updated_at: datetime

    chat: Optional[ChatPrompt] = None

    code: Optional[str] = None

    next_page_code: Optional[str] = None


JobGetScrapersResponse: TypeAlias = List[JobGetScrapersResponseItem]
