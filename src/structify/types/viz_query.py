# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["VizQuery"]


class VizQuery(BaseModel):
    id: str

    sql: str
