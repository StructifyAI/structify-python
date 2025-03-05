# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["TrainingDatasetSizeResponse", "TrainingDatasetSizeResponseItem"]


class TrainingDatasetSizeResponseItem(BaseModel):
    complete_labels: int

    name: str

    nav_labels: int

    nav_verified: int

    potential_sus_nav_datums: int

    potential_sus_save_datums: int

    save_labels: int

    save_verified: int

    sus_nav_datums: int

    sus_save_datums: int

    total_datums: int

    unlabeled_datums: int


TrainingDatasetSizeResponse: TypeAlias = List[TrainingDatasetSizeResponseItem]
