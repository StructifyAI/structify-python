# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

from .dashboard_param import DashboardParam
from .dashboard_spec_param import DashboardSpecParam

__all__ = ["UploadDashboardLayoutRequestParam", "Layout", "DashboardSpecs", "DashboardSpecsDashboardSpec"]


class Layout(TypedDict, total=False):
    layout: Required[DashboardParam]
    """
    A page is the top-level container with title/description Can contain multiple
    dashboards with different datasets
    """


class DashboardSpecsDashboardSpec(TypedDict, total=False):
    file_name: Required[str]

    spec: Required[DashboardSpecParam]


class DashboardSpecs(TypedDict, total=False):
    dashboard_specs: Required[Iterable[DashboardSpecsDashboardSpec]]


UploadDashboardLayoutRequestParam: TypeAlias = Union[Layout, DashboardSpecs]
