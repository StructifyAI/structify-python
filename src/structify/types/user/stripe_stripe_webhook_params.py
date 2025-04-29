# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["StripeStripeWebhookParams", "Data", "DataObject"]


class StripeStripeWebhookParams(TypedDict, total=False):
    data: Required[Data]

    type: Required[str]


class DataObject(TypedDict, total=False):
    amount_subtotal: Optional[int]

    metadata: Optional[Dict[str, str]]


class Data(TypedDict, total=False):
    object: Required[DataObject]
