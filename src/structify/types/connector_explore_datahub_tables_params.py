# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .explore_datahub_tables_request_param import ExploreDatahubTablesRequestParam

__all__ = ["ConnectorExploreDatahubTablesParams"]


class ConnectorExploreDatahubTablesParams(TypedDict, total=False):
    explore_datahub_tables_request: Required[ExploreDatahubTablesRequestParam]
