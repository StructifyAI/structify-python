# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types import (
    ListEventsResponse,
    ListTrackersResponse,
    CreateTrackerResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAnalytics:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_tracker(self, client: Structify) -> None:
        analytics = client.analytics.create_tracker(
            name="name",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CreateTrackerResponse, analytics, path=["response"])

    @parametrize
    def test_method_create_tracker_with_all_params(self, client: Structify) -> None:
        analytics = client.analytics.create_tracker(
            name="name",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            allowed_origins=["string"],
        )
        assert_matches_type(CreateTrackerResponse, analytics, path=["response"])

    @parametrize
    def test_raw_response_create_tracker(self, client: Structify) -> None:
        response = client.analytics.with_raw_response.create_tracker(
            name="name",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = response.parse()
        assert_matches_type(CreateTrackerResponse, analytics, path=["response"])

    @parametrize
    def test_streaming_response_create_tracker(self, client: Structify) -> None:
        with client.analytics.with_streaming_response.create_tracker(
            name="name",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = response.parse()
            assert_matches_type(CreateTrackerResponse, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_events(self, client: Structify) -> None:
        analytics = client.analytics.list_events(
            tracker_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ListEventsResponse, analytics, path=["response"])

    @parametrize
    def test_method_list_events_with_all_params(self, client: Structify) -> None:
        analytics = client.analytics.list_events(
            tracker_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cursor="cursor",
            limit=0,
        )
        assert_matches_type(ListEventsResponse, analytics, path=["response"])

    @parametrize
    def test_raw_response_list_events(self, client: Structify) -> None:
        response = client.analytics.with_raw_response.list_events(
            tracker_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = response.parse()
        assert_matches_type(ListEventsResponse, analytics, path=["response"])

    @parametrize
    def test_streaming_response_list_events(self, client: Structify) -> None:
        with client.analytics.with_streaming_response.list_events(
            tracker_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = response.parse()
            assert_matches_type(ListEventsResponse, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_events(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tracker_id` but received ''"):
            client.analytics.with_raw_response.list_events(
                tracker_id="",
            )

    @parametrize
    def test_method_list_trackers(self, client: Structify) -> None:
        analytics = client.analytics.list_trackers(
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ListTrackersResponse, analytics, path=["response"])

    @parametrize
    def test_raw_response_list_trackers(self, client: Structify) -> None:
        response = client.analytics.with_raw_response.list_trackers(
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = response.parse()
        assert_matches_type(ListTrackersResponse, analytics, path=["response"])

    @parametrize
    def test_streaming_response_list_trackers(self, client: Structify) -> None:
        with client.analytics.with_streaming_response.list_trackers(
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = response.parse()
            assert_matches_type(ListTrackersResponse, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_revoke_tracker(self, client: Structify) -> None:
        analytics = client.analytics.revoke_tracker(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert analytics is None

    @parametrize
    def test_raw_response_revoke_tracker(self, client: Structify) -> None:
        response = client.analytics.with_raw_response.revoke_tracker(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = response.parse()
        assert analytics is None

    @parametrize
    def test_streaming_response_revoke_tracker(self, client: Structify) -> None:
        with client.analytics.with_streaming_response.revoke_tracker(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = response.parse()
            assert analytics is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_revoke_tracker(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tracker_id` but received ''"):
            client.analytics.with_raw_response.revoke_tracker(
                "",
            )


class TestAsyncAnalytics:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create_tracker(self, async_client: AsyncStructify) -> None:
        analytics = await async_client.analytics.create_tracker(
            name="name",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CreateTrackerResponse, analytics, path=["response"])

    @parametrize
    async def test_method_create_tracker_with_all_params(self, async_client: AsyncStructify) -> None:
        analytics = await async_client.analytics.create_tracker(
            name="name",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            allowed_origins=["string"],
        )
        assert_matches_type(CreateTrackerResponse, analytics, path=["response"])

    @parametrize
    async def test_raw_response_create_tracker(self, async_client: AsyncStructify) -> None:
        response = await async_client.analytics.with_raw_response.create_tracker(
            name="name",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = await response.parse()
        assert_matches_type(CreateTrackerResponse, analytics, path=["response"])

    @parametrize
    async def test_streaming_response_create_tracker(self, async_client: AsyncStructify) -> None:
        async with async_client.analytics.with_streaming_response.create_tracker(
            name="name",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = await response.parse()
            assert_matches_type(CreateTrackerResponse, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_events(self, async_client: AsyncStructify) -> None:
        analytics = await async_client.analytics.list_events(
            tracker_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ListEventsResponse, analytics, path=["response"])

    @parametrize
    async def test_method_list_events_with_all_params(self, async_client: AsyncStructify) -> None:
        analytics = await async_client.analytics.list_events(
            tracker_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cursor="cursor",
            limit=0,
        )
        assert_matches_type(ListEventsResponse, analytics, path=["response"])

    @parametrize
    async def test_raw_response_list_events(self, async_client: AsyncStructify) -> None:
        response = await async_client.analytics.with_raw_response.list_events(
            tracker_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = await response.parse()
        assert_matches_type(ListEventsResponse, analytics, path=["response"])

    @parametrize
    async def test_streaming_response_list_events(self, async_client: AsyncStructify) -> None:
        async with async_client.analytics.with_streaming_response.list_events(
            tracker_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = await response.parse()
            assert_matches_type(ListEventsResponse, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_events(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tracker_id` but received ''"):
            await async_client.analytics.with_raw_response.list_events(
                tracker_id="",
            )

    @parametrize
    async def test_method_list_trackers(self, async_client: AsyncStructify) -> None:
        analytics = await async_client.analytics.list_trackers(
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ListTrackersResponse, analytics, path=["response"])

    @parametrize
    async def test_raw_response_list_trackers(self, async_client: AsyncStructify) -> None:
        response = await async_client.analytics.with_raw_response.list_trackers(
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = await response.parse()
        assert_matches_type(ListTrackersResponse, analytics, path=["response"])

    @parametrize
    async def test_streaming_response_list_trackers(self, async_client: AsyncStructify) -> None:
        async with async_client.analytics.with_streaming_response.list_trackers(
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = await response.parse()
            assert_matches_type(ListTrackersResponse, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_revoke_tracker(self, async_client: AsyncStructify) -> None:
        analytics = await async_client.analytics.revoke_tracker(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert analytics is None

    @parametrize
    async def test_raw_response_revoke_tracker(self, async_client: AsyncStructify) -> None:
        response = await async_client.analytics.with_raw_response.revoke_tracker(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = await response.parse()
        assert analytics is None

    @parametrize
    async def test_streaming_response_revoke_tracker(self, async_client: AsyncStructify) -> None:
        async with async_client.analytics.with_streaming_response.revoke_tracker(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = await response.parse()
            assert analytics is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_revoke_tracker(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tracker_id` but received ''"):
            await async_client.analytics.with_raw_response.revoke_tracker(
                "",
            )
