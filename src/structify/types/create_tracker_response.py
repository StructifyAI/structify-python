# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .tracker import Tracker
from .._models import BaseModel

__all__ = ["CreateTrackerResponse"]


class CreateTrackerResponse(BaseModel):
    post_path: str

    tracker: Tracker
