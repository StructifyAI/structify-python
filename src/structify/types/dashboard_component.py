# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["DashboardComponent"]


class DashboardComponent(BaseModel):
    node_name: str

    title: str

    description: Optional[str] = None

    span: Optional[int] = None
