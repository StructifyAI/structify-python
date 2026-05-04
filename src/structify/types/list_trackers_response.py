# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .tracker import Tracker
from .._models import BaseModel

__all__ = ["ListTrackersResponse"]


class ListTrackersResponse(BaseModel):
    trackers: List[Tracker]
