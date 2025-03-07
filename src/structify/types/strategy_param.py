# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .merge_config_param import MergeConfigParam

__all__ = ["StrategyParam", "Probabilistic"]


class Probabilistic(TypedDict, total=False):
    probabilistic: Required[Annotated[MergeConfigParam, PropertyInfo(alias="Probabilistic")]]
    """The configuration for a probabilistic merge strategy"""


StrategyParam: TypeAlias = Union[Literal["Unique", "NoSignal"], Probabilistic]
