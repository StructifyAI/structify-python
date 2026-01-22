# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .clone_connector_item_param import CloneConnectorItemParam

__all__ = ["ConnectorCloneParams"]


class ConnectorCloneParams(TypedDict, total=False):
    connectors: Required[Iterable[CloneConnectorItemParam]]

    target_team_id: Required[str]
