# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Event"]


class Event(BaseModel):
    collector_tstamp: datetime

    event_id: str

    tracker_id: str

    app_id: Optional[str] = None

    contexts: Optional[object] = None

    device: Optional[object] = None

    domain_sessionid: Optional[str] = None

    domain_sessionidx: Optional[int] = None

    domain_userid: Optional[str] = None

    dvce_created_tstamp: Optional[datetime] = None

    event: Optional[str] = None

    event_name: Optional[str] = None

    mkt_campaign: Optional[str] = None

    mkt_clickid: Optional[str] = None

    mkt_content: Optional[str] = None

    mkt_medium: Optional[str] = None

    mkt_network: Optional[str] = None

    mkt_source: Optional[str] = None

    mkt_term: Optional[str] = None

    network_userid: Optional[str] = None

    page_referrer: Optional[str] = None

    page_title: Optional[str] = None

    page_url: Optional[str] = None

    page_urlhost: Optional[str] = None

    page_urlpath: Optional[str] = None

    page_urlquery: Optional[str] = None

    platform: Optional[str] = None

    unstruct_event: Optional[object] = None

    user_id: Optional[str] = None

    user_ipaddress: Optional[str] = None

    useragent: Optional[str] = None

    v_tracker: Optional[str] = None
