from .._models import BaseModel
from typing import List

__all__ = ["Log"]

class Log(BaseModel):
    messages: List[str]