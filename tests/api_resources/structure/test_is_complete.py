# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types.structure import IsComplete

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIsComplete:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Structify) -> None:
        is_complete = client.structure.is_complete.create(
            body=["string", "string", "string"],
        )
        assert_matches_type(IsComplete, is_complete, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Structify) -> None:
        response = client.structure.is_complete.with_raw_response.create(
            body=["string", "string", "string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        is_complete = response.parse()
        assert_matches_type(IsComplete, is_complete, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Structify) -> None:
        with client.structure.is_complete.with_streaming_response.create(
            body=["string", "string", "string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            is_complete = response.parse()
            assert_matches_type(IsComplete, is_complete, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncIsComplete:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncStructify) -> None:
        is_complete = await async_client.structure.is_complete.create(
            body=["string", "string", "string"],
        )
        assert_matches_type(IsComplete, is_complete, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStructify) -> None:
        response = await async_client.structure.is_complete.with_raw_response.create(
            body=["string", "string", "string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        is_complete = await response.parse()
        assert_matches_type(IsComplete, is_complete, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStructify) -> None:
        async with async_client.structure.is_complete.with_streaming_response.create(
            body=["string", "string", "string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            is_complete = await response.parse()
            assert_matches_type(IsComplete, is_complete, path=["response"])

        assert cast(Any, response.is_closed) is True
