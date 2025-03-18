# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .action_training_datum_metadata import ActionTrainingDatumMetadata

__all__ = ["ActionTrainingDataMetadataResponse"]


class ActionTrainingDataMetadataResponse(BaseModel):
    data: List[ActionTrainingDatumMetadata]
