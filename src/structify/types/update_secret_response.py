# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["UpdateSecretResponse"]


class UpdateSecretResponse(BaseModel):
    secret_name: str

    updated_at: datetime
