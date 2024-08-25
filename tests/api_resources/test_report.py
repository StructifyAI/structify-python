# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReport:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_entity(self, client: Structify) -> None:
        report = client.report.entity(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(str, report, path=["response"])

    @parametrize
    def test_method_entity_with_all_params(self, client: Structify) -> None:
        report = client.report.entity(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            property="property",
        )
        assert_matches_type(str, report, path=["response"])

    @parametrize
    def test_raw_response_entity(self, client: Structify) -> None:
        response = client.report.with_raw_response.entity(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(str, report, path=["response"])

    @parametrize
    def test_streaming_response_entity(self, client: Structify) -> None:
        with client.report.with_streaming_response.entity(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(str, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_step(self, client: Structify) -> None:
        report = client.report.step(
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(str, report, path=["response"])

    @parametrize
    def test_method_step_with_all_params(self, client: Structify) -> None:
        report = client.report.step(
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            message="message",
        )
        assert_matches_type(str, report, path=["response"])

    @parametrize
    def test_raw_response_step(self, client: Structify) -> None:
        response = client.report.with_raw_response.step(
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(str, report, path=["response"])

    @parametrize
    def test_streaming_response_step(self, client: Structify) -> None:
        with client.report.with_streaming_response.step(
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(str, report, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncReport:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_entity(self, async_client: AsyncStructify) -> None:
        report = await async_client.report.entity(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(str, report, path=["response"])

    @parametrize
    async def test_method_entity_with_all_params(self, async_client: AsyncStructify) -> None:
        report = await async_client.report.entity(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            property="property",
        )
        assert_matches_type(str, report, path=["response"])

    @parametrize
    async def test_raw_response_entity(self, async_client: AsyncStructify) -> None:
        response = await async_client.report.with_raw_response.entity(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(str, report, path=["response"])

    @parametrize
    async def test_streaming_response_entity(self, async_client: AsyncStructify) -> None:
        async with async_client.report.with_streaming_response.entity(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(str, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_step(self, async_client: AsyncStructify) -> None:
        report = await async_client.report.step(
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(str, report, path=["response"])

    @parametrize
    async def test_method_step_with_all_params(self, async_client: AsyncStructify) -> None:
        report = await async_client.report.step(
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            message="message",
        )
        assert_matches_type(str, report, path=["response"])

    @parametrize
    async def test_raw_response_step(self, async_client: AsyncStructify) -> None:
        response = await async_client.report.with_raw_response.step(
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(str, report, path=["response"])

    @parametrize
    async def test_streaming_response_step(self, async_client: AsyncStructify) -> None:
        async with async_client.report.with_streaming_response.step(
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(str, report, path=["response"])

        assert cast(Any, response.is_closed) is True
