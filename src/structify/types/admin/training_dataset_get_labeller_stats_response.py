# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .labeling_stats import LabelingStats

__all__ = ["TrainingDatasetGetLabellerStatsResponse"]

TrainingDatasetGetLabellerStatsResponse: TypeAlias = List[LabelingStats]
