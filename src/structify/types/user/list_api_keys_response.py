# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .api_key_info import APIKeyInfo

__all__ = ["ListAPIKeysResponse"]


class ListAPIKeysResponse(BaseModel):
    api_keys: List[APIKeyInfo]
