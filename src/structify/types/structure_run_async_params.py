# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["StructureRunAsyncParams", "Variant0", "Variant1", "Variant2"]


class Variant0(TypedDict, total=False):
    dataset_name: Required[str]

    basic: Required[Annotated[object, PropertyInfo(alias="Basic")]]

    custom_instruction: Optional[str]


class Variant1(TypedDict, total=False):
    dataset_name: Required[str]

    sec_ingestor: Required[Annotated[object, PropertyInfo(alias="SECIngestor")]]

    custom_instruction: Optional[str]


class Variant2(TypedDict, total=False):
    dataset_name: Required[str]

    pdf_ingestor: Required[Annotated[object, PropertyInfo(alias="PDFIngestor")]]

    custom_instruction: Optional[str]


StructureRunAsyncParams = Union[Variant0, Variant1, Variant2]
