# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types import UsageGetJobInfoResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_job_info(self, client: Structify) -> None:
        usage = client.usage.get_job_info()
        assert_matches_type(UsageGetJobInfoResponse, usage, path=["response"])

    @parametrize
    def test_raw_response_get_job_info(self, client: Structify) -> None:
        response = client.usage.with_raw_response.get_job_info()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageGetJobInfoResponse, usage, path=["response"])

    @parametrize
    def test_streaming_response_get_job_info(self, client: Structify) -> None:
        with client.usage.with_streaming_response.get_job_info() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(UsageGetJobInfoResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUsage:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get_job_info(self, async_client: AsyncStructify) -> None:
        usage = await async_client.usage.get_job_info()
        assert_matches_type(UsageGetJobInfoResponse, usage, path=["response"])

    @parametrize
    async def test_raw_response_get_job_info(self, async_client: AsyncStructify) -> None:
        response = await async_client.usage.with_raw_response.get_job_info()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(UsageGetJobInfoResponse, usage, path=["response"])

    @parametrize
    async def test_streaming_response_get_job_info(self, async_client: AsyncStructify) -> None:
        async with async_client.usage.with_streaming_response.get_job_info() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(UsageGetJobInfoResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True
