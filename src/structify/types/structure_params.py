# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .table_param import Property
from .dataset_descriptor_param import DatasetDescriptorParam

__all__ = [
    "StructureParams",
    "BrowserConfig",
    "SandboxConfig",
    "BrowserParam",
    "SandboxParam",
]


class BrowserConfig(TypedDict, total=False):
    starting_urls: SequenceNotStr[str]

    starting_searches: SequenceNotStr[str]

    banned_domains: SequenceNotStr[str]

    proxy: bool


class SandboxConfig(TypedDict, total=False):
    pass


BrowserParam: TypeAlias = Union[bool, BrowserConfig]
SandboxParam: TypeAlias = Union[bool, SandboxConfig]


class StructureParams(TypedDict, total=False):
    dataset_descriptor: Required[DatasetDescriptorParam]

    table_name: Required[str]

    new_columns: Required[Iterable[Property]]

    allow_expand_rows: bool

    instruction: Optional[str]

    browser: Optional[BrowserParam]

    sandbox: Optional[SandboxParam]

    nsteps: Optional[int]

    model: Optional[str]

    node_id: Optional[str]
