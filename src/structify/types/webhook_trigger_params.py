# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["WebhookTriggerParams"]


class WebhookTriggerParams(TypedDict, total=False):
    workflow_schedule_id: Required[str]

    workflow_parameters: Dict[str, Dict[str, object]]
