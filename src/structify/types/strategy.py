# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .merge_config import MergeConfig

__all__ = ["Strategy", "Probabilistic"]


class Probabilistic(BaseModel):
    probabilistic: MergeConfig = FieldInfo(alias="Probabilistic")
    """The configuration for a probabilistic merge strategy"""


Strategy: TypeAlias = Union[Literal["Unique", "NoSignal"], Probabilistic]
