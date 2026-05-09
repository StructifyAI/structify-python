# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .exploration_phase_id import ExplorationPhaseID

__all__ = ["PhaseActivity"]


class PhaseActivity(BaseModel):
    job_id: str

    phase_id: ExplorationPhaseID
    """Identifies the phase of connector exploration

    This enum is used to track which phase of exploration a chat session belongs to.
    It's stored as JSONB in the database to allow for flexible phase identification.
    """

    status: Literal["Queued", "Running", "Completed", "Failed"]

    chat_id: Optional[str] = None
