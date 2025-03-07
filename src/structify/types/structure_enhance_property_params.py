# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .enhance_property_param import EnhancePropertyParam

__all__ = ["StructureEnhancePropertyParams", "Body"]


class StructureEnhancePropertyParams(TypedDict, total=False):
    body: Required[Body]


class Body(EnhancePropertyParam):
    special_job_type: Optional[Literal["HumanLLM"]]
