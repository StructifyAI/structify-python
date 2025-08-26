# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .entity_param import EntityParam
from .dataset_descriptor_param import DatasetDescriptorParam

__all__ = [
    "ScrapeListParams",
    "Input",
    "InputDirect",
    "InputDirectDirect",
    "InputRelated",
    "InputRelatedRelated",
    "StopConfig",
]


class ScrapeListParams(TypedDict, total=False):
    dataset_descriptor: Required[DatasetDescriptorParam]
    """A dataset is where you put multiple referential schemas.

    A dataset is a complete namespace where all references between schemas are held
    within the dataset.
    """

    input: Required[Input]

    table_name: Required[str]

    dataset_name: Optional[str]

    node_id: Optional[str]

    stop_config: Optional[StopConfig]
    """Configuration parameters for the StopChecker"""

    use_proxy: Optional[bool]


class InputDirectDirect(TypedDict, total=False):
    url: Required[str]


class InputDirect(TypedDict, total=False):
    direct: Required[Annotated[InputDirectDirect, PropertyInfo(alias="Direct")]]


class InputRelatedRelated(TypedDict, total=False):
    relationship_name: Required[str]

    source_entity: Required[EntityParam]

    source_url_column: Required[str]


class InputRelated(TypedDict, total=False):
    related: Required[Annotated[InputRelatedRelated, PropertyInfo(alias="Related")]]


Input: TypeAlias = Union[InputDirect, InputRelated]


class StopConfig(TypedDict, total=False):
    max_steps_without_save: Required[int]

    max_errors: Optional[int]

    max_execution_time_secs: Optional[int]

    max_total_steps: Optional[int]
