# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = ["SlackEventsParams", "Variant0", "Variant1", "Variant1Event"]


class Variant0(TypedDict, total=False):
    challenge: Required[str]

    type: Required[Literal["url_verification"]]

    token: Optional[str]


class Variant1(TypedDict, total=False):
    event: Required[Variant1Event]

    team_id: Required[str]

    type: Required[Literal["event_callback"]]

    api_app_id: Optional[str]

    authed_users: Optional[SequenceNotStr[str]]

    event_context: Optional[str]

    event_id: Optional[str]

    event_time: Optional[int]


class Variant1Event(TypedDict, total=False):
    channel: Required[str]

    text: Required[str]

    ts: Required[str]

    type: Required[Literal["app_mention"]]

    user: Required[str]

    channel_type: Optional[str]

    client_msg_id: Optional[str]

    event_ts: Optional[str]

    team: Optional[str]

    thread_ts: Optional[str]


SlackEventsParams: TypeAlias = Union[Variant0, Variant1]
