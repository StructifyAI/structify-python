# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types.label import LlmAssistRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLlmAssist:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Structify) -> None:
        llm_assist = client.label.llm_assist.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(LlmAssistRetrieveResponse, llm_assist, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Structify) -> None:
        response = client.label.llm_assist.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm_assist = response.parse()
        assert_matches_type(LlmAssistRetrieveResponse, llm_assist, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Structify) -> None:
        with client.label.llm_assist.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm_assist = response.parse()
            assert_matches_type(LlmAssistRetrieveResponse, llm_assist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.label.llm_assist.with_raw_response.retrieve(
                "",
            )


class TestAsyncLlmAssist:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncStructify) -> None:
        llm_assist = await async_client.label.llm_assist.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(LlmAssistRetrieveResponse, llm_assist, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncStructify) -> None:
        response = await async_client.label.llm_assist.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm_assist = await response.parse()
        assert_matches_type(LlmAssistRetrieveResponse, llm_assist, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncStructify) -> None:
        async with async_client.label.llm_assist.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm_assist = await response.parse()
            assert_matches_type(LlmAssistRetrieveResponse, llm_assist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.label.llm_assist.with_raw_response.retrieve(
                "",
            )
