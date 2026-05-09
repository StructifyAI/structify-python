# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["WebhookTriggerResponse"]


class WebhookTriggerResponse(BaseModel):
    message: str

    success: bool

    sandbox_id: Optional[str] = None

    tunnel_url: Optional[str] = None
