# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..connector import Connector

__all__ = ["AdminListConnectorsResponse"]


class AdminListConnectorsResponse(BaseModel):
    connectors: List[Connector]
