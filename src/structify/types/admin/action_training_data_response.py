# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .action_training_data_entry import ActionTrainingDataEntry

__all__ = ["ActionTrainingDataResponse"]


class ActionTrainingDataResponse(BaseModel):
    data: List[ActionTrainingDataEntry]
