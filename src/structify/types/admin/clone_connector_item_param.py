# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CloneConnectorItemParam"]


class CloneConnectorItemParam(TypedDict, total=False):
    known_connector_type: Required[str]

    name: Required[str]

    source_connector_id: Required[str]
