# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["GetSecretResponse"]


class GetSecretResponse(BaseModel):
    created_at: datetime

    secret_name: str

    secret_value: str

    updated_at: datetime
