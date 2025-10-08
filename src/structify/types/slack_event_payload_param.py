# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = ["SlackEventPayloadParam", "URLVerification", "EventCallback", "EventCallbackEvent"]


class URLVerification(TypedDict, total=False):
    challenge: Required[str]

    type: Required[Literal["url_verification"]]

    token: Optional[str]


class EventCallbackEvent(TypedDict, total=False):
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


class EventCallback(TypedDict, total=False):
    event: Required[EventCallbackEvent]

    team_id: Required[str]

    type: Required[Literal["event_callback"]]

    api_app_id: Optional[str]

    authed_users: Optional[SequenceNotStr[str]]

    event_context: Optional[str]

    event_id: Optional[str]

    event_time: Optional[int]


SlackEventPayloadParam: TypeAlias = Union[URLVerification, EventCallback]
