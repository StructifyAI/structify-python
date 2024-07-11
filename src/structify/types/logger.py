from typing import List

from .._models import BaseModel

__all__ = ["Log"]


class Log(BaseModel):
    messages: List[str]
