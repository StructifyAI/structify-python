# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ConnectorTableInfo"]


class ConnectorTableInfo(BaseModel):
    id: str

    name: str

    description: Optional[str] = None
