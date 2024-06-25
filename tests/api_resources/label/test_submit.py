# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubmit:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Structify) -> None:
        submit = client.label.submit.create(
            "string",
            body=[{"save": {}}, {"save": {}}, {"save": {}}],
        )
        assert_matches_type(str, submit, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Structify) -> None:
        response = client.label.submit.with_raw_response.create(
            "string",
            body=[{"save": {}}, {"save": {}}, {"save": {}}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        submit = response.parse()
        assert_matches_type(str, submit, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Structify) -> None:
        with client.label.submit.with_streaming_response.create(
            "string",
            body=[{"save": {}}, {"save": {}}, {"save": {}}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            submit = response.parse()
            assert_matches_type(str, submit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.label.submit.with_raw_response.create(
                "",
                body=[{"save": {}}, {"save": {}}, {"save": {}}],
            )


class TestAsyncSubmit:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncStructify) -> None:
        submit = await async_client.label.submit.create(
            "string",
            body=[{"save": {}}, {"save": {}}, {"save": {}}],
        )
        assert_matches_type(str, submit, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStructify) -> None:
        response = await async_client.label.submit.with_raw_response.create(
            "string",
            body=[{"save": {}}, {"save": {}}, {"save": {}}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        submit = await response.parse()
        assert_matches_type(str, submit, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStructify) -> None:
        async with async_client.label.submit.with_streaming_response.create(
            "string",
            body=[{"save": {}}, {"save": {}}, {"save": {}}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            submit = await response.parse()
            assert_matches_type(str, submit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.label.submit.with_raw_response.create(
                "",
                body=[{"save": {}}, {"save": {}}, {"save": {}}],
            )
