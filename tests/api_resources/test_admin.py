# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAdmin:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_report_critical(self, client: Structify) -> None:
        admin = client.admin.report_critical(
            message="message",
        )
        assert admin is None

    @parametrize
    def test_raw_response_report_critical(self, client: Structify) -> None:
        response = client.admin.with_raw_response.report_critical(
            message="message",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = response.parse()
        assert admin is None

    @parametrize
    def test_streaming_response_report_critical(self, client: Structify) -> None:
        with client.admin.with_streaming_response.report_critical(
            message="message",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = response.parse()
            assert admin is None

        assert cast(Any, response.is_closed) is True


class TestAsyncAdmin:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_report_critical(self, async_client: AsyncStructify) -> None:
        admin = await async_client.admin.report_critical(
            message="message",
        )
        assert admin is None

    @parametrize
    async def test_raw_response_report_critical(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.with_raw_response.report_critical(
            message="message",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = await response.parse()
        assert admin is None

    @parametrize
    async def test_streaming_response_report_critical(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.with_streaming_response.report_critical(
            message="message",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = await response.parse()
            assert admin is None

        assert cast(Any, response.is_closed) is True
