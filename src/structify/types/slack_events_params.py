# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "SlackEventsParams",
    "Variant0",
    "Variant1",
    "Variant1Event",
    "Variant1EventAppMention",
    "Variant1EventAppMentionFile",
    "Variant1EventMessage",
]


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


class Variant1EventAppMentionFile(TypedDict, total=False):
    id: Required[str]

    name: Required[str]

    filetype: Optional[str]

    mimetype: Optional[str]

    url_private: Optional[str]

    url_private_download: Optional[str]


class Variant1EventAppMention(TypedDict, total=False):
    channel: Required[str]

    text: Required[str]

    ts: Required[str]

    type: Required[Literal["app_mention"]]

    user: Required[str]

    channel_type: Optional[str]

    client_msg_id: Optional[str]

    event_ts: Optional[str]

    files: Optional[Iterable[Variant1EventAppMentionFile]]

    team: Optional[str]

    thread_ts: Optional[str]


class Variant1EventMessage(TypedDict, total=False):
    channel: Required[str]

    ts: Required[str]

    type: Required[Literal["message"]]

    bot_id: Optional[str]

    channel_type: Optional[str]

    client_msg_id: Optional[str]

    event_ts: Optional[str]

    team: Optional[str]

    text: Optional[str]

    thread_ts: Optional[str]

    user: Optional[str]


Variant1Event: TypeAlias = Union[Variant1EventAppMention, Variant1EventMessage]

SlackEventsParams: TypeAlias = Union[Variant0, Variant1]
