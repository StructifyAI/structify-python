# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types import (
    Sandbox,
    SandboxListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSandbox:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Structify) -> None:
        sandbox = client.sandbox.create(
            chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            modal_id="modal_id",
            modal_url="modal_url",
            status="alive",
        )
        assert_matches_type(Sandbox, sandbox, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Structify) -> None:
        sandbox = client.sandbox.create(
            chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            modal_id="modal_id",
            modal_url="modal_url",
            status="alive",
            latest_node="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Sandbox, sandbox, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Structify) -> None:
        response = client.sandbox.with_raw_response.create(
            chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            modal_id="modal_id",
            modal_url="modal_url",
            status="alive",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = response.parse()
        assert_matches_type(Sandbox, sandbox, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Structify) -> None:
        with client.sandbox.with_streaming_response.create(
            chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            modal_id="modal_id",
            modal_url="modal_url",
            status="alive",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = response.parse()
            assert_matches_type(Sandbox, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.sandbox.with_raw_response.create(
                chat_id="",
                chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                modal_id="modal_id",
                modal_url="modal_url",
                status="alive",
            )

    @parametrize
    def test_method_list(self, client: Structify) -> None:
        sandbox = client.sandbox.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SandboxListResponse, sandbox, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Structify) -> None:
        response = client.sandbox.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = response.parse()
        assert_matches_type(SandboxListResponse, sandbox, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Structify) -> None:
        with client.sandbox.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = response.parse()
            assert_matches_type(SandboxListResponse, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.sandbox.with_raw_response.list(
                "",
            )

    @parametrize
    def test_method_get(self, client: Structify) -> None:
        sandbox = client.sandbox.get(
            chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Sandbox, sandbox, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Structify) -> None:
        sandbox = client.sandbox.get(
            chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            sandbox_url_override="sandbox_url_override",
        )
        assert_matches_type(Sandbox, sandbox, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Structify) -> None:
        response = client.sandbox.with_raw_response.get(
            chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = response.parse()
        assert_matches_type(Sandbox, sandbox, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Structify) -> None:
        with client.sandbox.with_streaming_response.get(
            chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = response.parse()
            assert_matches_type(Sandbox, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.sandbox.with_raw_response.get(
                chat_id="",
            )

    @parametrize
    def test_method_update_status(self, client: Structify) -> None:
        sandbox = client.sandbox.update_status(
            sandbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="status",
        )
        assert_matches_type(Sandbox, sandbox, path=["response"])

    @parametrize
    def test_raw_response_update_status(self, client: Structify) -> None:
        response = client.sandbox.with_raw_response.update_status(
            sandbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="status",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = response.parse()
        assert_matches_type(Sandbox, sandbox, path=["response"])

    @parametrize
    def test_streaming_response_update_status(self, client: Structify) -> None:
        with client.sandbox.with_streaming_response.update_status(
            sandbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="status",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = response.parse()
            assert_matches_type(Sandbox, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_status(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sandbox_id` but received ''"):
            client.sandbox.with_raw_response.update_status(
                sandbox_id="",
                status="status",
            )


class TestAsyncSandbox:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncStructify) -> None:
        sandbox = await async_client.sandbox.create(
            chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            modal_id="modal_id",
            modal_url="modal_url",
            status="alive",
        )
        assert_matches_type(Sandbox, sandbox, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncStructify) -> None:
        sandbox = await async_client.sandbox.create(
            chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            modal_id="modal_id",
            modal_url="modal_url",
            status="alive",
            latest_node="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Sandbox, sandbox, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStructify) -> None:
        response = await async_client.sandbox.with_raw_response.create(
            chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            modal_id="modal_id",
            modal_url="modal_url",
            status="alive",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = await response.parse()
        assert_matches_type(Sandbox, sandbox, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStructify) -> None:
        async with async_client.sandbox.with_streaming_response.create(
            chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            modal_id="modal_id",
            modal_url="modal_url",
            status="alive",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = await response.parse()
            assert_matches_type(Sandbox, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.sandbox.with_raw_response.create(
                chat_id="",
                chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                modal_id="modal_id",
                modal_url="modal_url",
                status="alive",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncStructify) -> None:
        sandbox = await async_client.sandbox.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SandboxListResponse, sandbox, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStructify) -> None:
        response = await async_client.sandbox.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = await response.parse()
        assert_matches_type(SandboxListResponse, sandbox, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStructify) -> None:
        async with async_client.sandbox.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = await response.parse()
            assert_matches_type(SandboxListResponse, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.sandbox.with_raw_response.list(
                "",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncStructify) -> None:
        sandbox = await async_client.sandbox.get(
            chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Sandbox, sandbox, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncStructify) -> None:
        sandbox = await async_client.sandbox.get(
            chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            sandbox_url_override="sandbox_url_override",
        )
        assert_matches_type(Sandbox, sandbox, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncStructify) -> None:
        response = await async_client.sandbox.with_raw_response.get(
            chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = await response.parse()
        assert_matches_type(Sandbox, sandbox, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncStructify) -> None:
        async with async_client.sandbox.with_streaming_response.get(
            chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = await response.parse()
            assert_matches_type(Sandbox, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.sandbox.with_raw_response.get(
                chat_id="",
            )

    @parametrize
    async def test_method_update_status(self, async_client: AsyncStructify) -> None:
        sandbox = await async_client.sandbox.update_status(
            sandbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="status",
        )
        assert_matches_type(Sandbox, sandbox, path=["response"])

    @parametrize
    async def test_raw_response_update_status(self, async_client: AsyncStructify) -> None:
        response = await async_client.sandbox.with_raw_response.update_status(
            sandbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="status",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = await response.parse()
        assert_matches_type(Sandbox, sandbox, path=["response"])

    @parametrize
    async def test_streaming_response_update_status(self, async_client: AsyncStructify) -> None:
        async with async_client.sandbox.with_streaming_response.update_status(
            sandbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="status",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = await response.parse()
            assert_matches_type(Sandbox, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_status(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sandbox_id` but received ''"):
            await async_client.sandbox.with_raw_response.update_status(
                sandbox_id="",
                status="status",
            )
