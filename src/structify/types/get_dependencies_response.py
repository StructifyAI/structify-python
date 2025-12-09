# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .chat_dependency import ChatDependency

__all__ = ["GetDependenciesResponse"]


class GetDependenciesResponse(BaseModel):
    """Response structure for getting chat dependencies"""

    dependencies: List[ChatDependency]
    """List of dependencies for the chat session"""
