# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types.admin import (
    FunctionalTest,
    FunctionalTestListResponse,
    FunctionalTestResultsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFunctionalTests:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Structify) -> None:
        functional_test = client.admin.functional_tests.create(
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FunctionalTest, functional_test, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Structify) -> None:
        functional_test = client.admin.functional_tests.create(
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            model_override="model_override",
            prompt_override="prompt_override",
        )
        assert_matches_type(FunctionalTest, functional_test, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Structify) -> None:
        response = client.admin.functional_tests.with_raw_response.create(
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        functional_test = response.parse()
        assert_matches_type(FunctionalTest, functional_test, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Structify) -> None:
        with client.admin.functional_tests.with_streaming_response.create(
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            functional_test = response.parse()
            assert_matches_type(FunctionalTest, functional_test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Structify) -> None:
        functional_test = client.admin.functional_tests.list()
        assert_matches_type(FunctionalTestListResponse, functional_test, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Structify) -> None:
        response = client.admin.functional_tests.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        functional_test = response.parse()
        assert_matches_type(FunctionalTestListResponse, functional_test, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Structify) -> None:
        with client.admin.functional_tests.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            functional_test = response.parse()
            assert_matches_type(FunctionalTestListResponse, functional_test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_results(self, client: Structify) -> None:
        functional_test = client.admin.functional_tests.get_results()
        assert_matches_type(FunctionalTestResultsResponse, functional_test, path=["response"])

    @parametrize
    def test_method_get_results_with_all_params(self, client: Structify) -> None:
        functional_test = client.admin.functional_tests.get_results(
            functional_test_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            sample_name="sample_name",
        )
        assert_matches_type(FunctionalTestResultsResponse, functional_test, path=["response"])

    @parametrize
    def test_raw_response_get_results(self, client: Structify) -> None:
        response = client.admin.functional_tests.with_raw_response.get_results()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        functional_test = response.parse()
        assert_matches_type(FunctionalTestResultsResponse, functional_test, path=["response"])

    @parametrize
    def test_streaming_response_get_results(self, client: Structify) -> None:
        with client.admin.functional_tests.with_streaming_response.get_results() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            functional_test = response.parse()
            assert_matches_type(FunctionalTestResultsResponse, functional_test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_link_chat(self, client: Structify) -> None:
        functional_test = client.admin.functional_tests.link_chat(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            functional_test_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            results={"foo": "bar"},
            sample_name="sample_name",
        )
        assert functional_test is None

    @parametrize
    def test_raw_response_link_chat(self, client: Structify) -> None:
        response = client.admin.functional_tests.with_raw_response.link_chat(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            functional_test_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            results={"foo": "bar"},
            sample_name="sample_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        functional_test = response.parse()
        assert functional_test is None

    @parametrize
    def test_streaming_response_link_chat(self, client: Structify) -> None:
        with client.admin.functional_tests.with_streaming_response.link_chat(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            functional_test_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            results={"foo": "bar"},
            sample_name="sample_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            functional_test = response.parse()
            assert functional_test is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_system_prompt(self, client: Structify) -> None:
        functional_test = client.admin.functional_tests.system_prompt()
        assert_matches_type(str, functional_test, path=["response"])

    @parametrize
    def test_raw_response_system_prompt(self, client: Structify) -> None:
        response = client.admin.functional_tests.with_raw_response.system_prompt()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        functional_test = response.parse()
        assert_matches_type(str, functional_test, path=["response"])

    @parametrize
    def test_streaming_response_system_prompt(self, client: Structify) -> None:
        with client.admin.functional_tests.with_streaming_response.system_prompt() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            functional_test = response.parse()
            assert_matches_type(str, functional_test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_results(self, client: Structify) -> None:
        functional_test = client.admin.functional_tests.update_results(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            functional_test_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            results={"foo": "bar"},
            sample_name="sample_name",
        )
        assert functional_test is None

    @parametrize
    def test_raw_response_update_results(self, client: Structify) -> None:
        response = client.admin.functional_tests.with_raw_response.update_results(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            functional_test_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            results={"foo": "bar"},
            sample_name="sample_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        functional_test = response.parse()
        assert functional_test is None

    @parametrize
    def test_streaming_response_update_results(self, client: Structify) -> None:
        with client.admin.functional_tests.with_streaming_response.update_results(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            functional_test_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            results={"foo": "bar"},
            sample_name="sample_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            functional_test = response.parse()
            assert functional_test is None

        assert cast(Any, response.is_closed) is True


class TestAsyncFunctionalTests:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncStructify) -> None:
        functional_test = await async_client.admin.functional_tests.create(
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FunctionalTest, functional_test, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncStructify) -> None:
        functional_test = await async_client.admin.functional_tests.create(
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            model_override="model_override",
            prompt_override="prompt_override",
        )
        assert_matches_type(FunctionalTest, functional_test, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.functional_tests.with_raw_response.create(
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        functional_test = await response.parse()
        assert_matches_type(FunctionalTest, functional_test, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.functional_tests.with_streaming_response.create(
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            functional_test = await response.parse()
            assert_matches_type(FunctionalTest, functional_test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncStructify) -> None:
        functional_test = await async_client.admin.functional_tests.list()
        assert_matches_type(FunctionalTestListResponse, functional_test, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.functional_tests.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        functional_test = await response.parse()
        assert_matches_type(FunctionalTestListResponse, functional_test, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.functional_tests.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            functional_test = await response.parse()
            assert_matches_type(FunctionalTestListResponse, functional_test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_results(self, async_client: AsyncStructify) -> None:
        functional_test = await async_client.admin.functional_tests.get_results()
        assert_matches_type(FunctionalTestResultsResponse, functional_test, path=["response"])

    @parametrize
    async def test_method_get_results_with_all_params(self, async_client: AsyncStructify) -> None:
        functional_test = await async_client.admin.functional_tests.get_results(
            functional_test_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            sample_name="sample_name",
        )
        assert_matches_type(FunctionalTestResultsResponse, functional_test, path=["response"])

    @parametrize
    async def test_raw_response_get_results(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.functional_tests.with_raw_response.get_results()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        functional_test = await response.parse()
        assert_matches_type(FunctionalTestResultsResponse, functional_test, path=["response"])

    @parametrize
    async def test_streaming_response_get_results(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.functional_tests.with_streaming_response.get_results() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            functional_test = await response.parse()
            assert_matches_type(FunctionalTestResultsResponse, functional_test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_link_chat(self, async_client: AsyncStructify) -> None:
        functional_test = await async_client.admin.functional_tests.link_chat(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            functional_test_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            results={"foo": "bar"},
            sample_name="sample_name",
        )
        assert functional_test is None

    @parametrize
    async def test_raw_response_link_chat(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.functional_tests.with_raw_response.link_chat(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            functional_test_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            results={"foo": "bar"},
            sample_name="sample_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        functional_test = await response.parse()
        assert functional_test is None

    @parametrize
    async def test_streaming_response_link_chat(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.functional_tests.with_streaming_response.link_chat(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            functional_test_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            results={"foo": "bar"},
            sample_name="sample_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            functional_test = await response.parse()
            assert functional_test is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_system_prompt(self, async_client: AsyncStructify) -> None:
        functional_test = await async_client.admin.functional_tests.system_prompt()
        assert_matches_type(str, functional_test, path=["response"])

    @parametrize
    async def test_raw_response_system_prompt(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.functional_tests.with_raw_response.system_prompt()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        functional_test = await response.parse()
        assert_matches_type(str, functional_test, path=["response"])

    @parametrize
    async def test_streaming_response_system_prompt(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.functional_tests.with_streaming_response.system_prompt() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            functional_test = await response.parse()
            assert_matches_type(str, functional_test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_results(self, async_client: AsyncStructify) -> None:
        functional_test = await async_client.admin.functional_tests.update_results(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            functional_test_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            results={"foo": "bar"},
            sample_name="sample_name",
        )
        assert functional_test is None

    @parametrize
    async def test_raw_response_update_results(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.functional_tests.with_raw_response.update_results(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            functional_test_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            results={"foo": "bar"},
            sample_name="sample_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        functional_test = await response.parse()
        assert functional_test is None

    @parametrize
    async def test_streaming_response_update_results(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.functional_tests.with_streaming_response.update_results(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            functional_test_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            results={"foo": "bar"},
            sample_name="sample_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            functional_test = await response.parse()
            assert functional_test is None

        assert cast(Any, response.is_closed) is True
