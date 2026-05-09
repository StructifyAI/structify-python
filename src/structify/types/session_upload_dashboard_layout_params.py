# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

from .dashboard_param import DashboardParam
from .dashboard_spec_param import DashboardSpecParam

__all__ = ["SessionUploadDashboardLayoutParams", "Variant0", "Variant1", "Variant1DashboardSpec"]


class Variant0(TypedDict, total=False):
    layout: Required[DashboardParam]
    """
    A page is the top-level container with title/description Can contain multiple
    dashboards with different datasets
    """


class Variant1(TypedDict, total=False):
    dashboard_specs: Required[Iterable[Variant1DashboardSpec]]


class Variant1DashboardSpec(TypedDict, total=False):
    file_name: Required[str]

    spec: Required[DashboardSpecParam]


SessionUploadDashboardLayoutParams: TypeAlias = Union[Variant0, Variant1]
