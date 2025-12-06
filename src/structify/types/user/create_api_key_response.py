# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .api_key_info import APIKeyInfo

__all__ = ["CreateAPIKeyResponse"]


class CreateAPIKeyResponse(BaseModel):
    api_key: APIKeyInfo

    raw_key: str
