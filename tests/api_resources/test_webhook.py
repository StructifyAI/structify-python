# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types import WebhookTriggerResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhook:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_trigger(self, client: Structify) -> None:
        webhook = client.webhook.trigger(
            workflow_schedule_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WebhookTriggerResponse, webhook, path=["response"])

    @parametrize
    def test_method_trigger_with_all_params(self, client: Structify) -> None:
        webhook = client.webhook.trigger(
            workflow_schedule_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            workflow_parameters={"foo": {"foo": "bar"}},
        )
        assert_matches_type(WebhookTriggerResponse, webhook, path=["response"])

    @parametrize
    def test_raw_response_trigger(self, client: Structify) -> None:
        response = client.webhook.with_raw_response.trigger(
            workflow_schedule_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookTriggerResponse, webhook, path=["response"])

    @parametrize
    def test_streaming_response_trigger(self, client: Structify) -> None:
        with client.webhook.with_streaming_response.trigger(
            workflow_schedule_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookTriggerResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWebhook:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_trigger(self, async_client: AsyncStructify) -> None:
        webhook = await async_client.webhook.trigger(
            workflow_schedule_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WebhookTriggerResponse, webhook, path=["response"])

    @parametrize
    async def test_method_trigger_with_all_params(self, async_client: AsyncStructify) -> None:
        webhook = await async_client.webhook.trigger(
            workflow_schedule_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            workflow_parameters={"foo": {"foo": "bar"}},
        )
        assert_matches_type(WebhookTriggerResponse, webhook, path=["response"])

    @parametrize
    async def test_raw_response_trigger(self, async_client: AsyncStructify) -> None:
        response = await async_client.webhook.with_raw_response.trigger(
            workflow_schedule_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookTriggerResponse, webhook, path=["response"])

    @parametrize
    async def test_streaming_response_trigger(self, async_client: AsyncStructify) -> None:
        async with async_client.webhook.with_streaming_response.trigger(
            workflow_schedule_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookTriggerResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True
