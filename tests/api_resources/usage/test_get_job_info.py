# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGetJobInfo:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Structify) -> None:
        get_job_info = client.usage.get_job_info.create(
            job_id="string",
        )
        assert_matches_type(object, get_job_info, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Structify) -> None:
        response = client.usage.get_job_info.with_raw_response.create(
            job_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        get_job_info = response.parse()
        assert_matches_type(object, get_job_info, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Structify) -> None:
        with client.usage.get_job_info.with_streaming_response.create(
            job_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            get_job_info = response.parse()
            assert_matches_type(object, get_job_info, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGetJobInfo:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncStructify) -> None:
        get_job_info = await async_client.usage.get_job_info.create(
            job_id="string",
        )
        assert_matches_type(object, get_job_info, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStructify) -> None:
        response = await async_client.usage.get_job_info.with_raw_response.create(
            job_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        get_job_info = await response.parse()
        assert_matches_type(object, get_job_info, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStructify) -> None:
        async with async_client.usage.get_job_info.with_streaming_response.create(
            job_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            get_job_info = await response.parse()
            assert_matches_type(object, get_job_info, path=["response"])

        assert cast(Any, response.is_closed) is True
