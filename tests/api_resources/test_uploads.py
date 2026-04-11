# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types import (
    SignedUploadInitResponse,
    SignedUploadCompleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUploads:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_complete(self, client: Structify) -> None:
        upload = client.uploads.complete(
            blob_name="blob_name",
            content_type="content_type",
            target="chat_input",
        )
        assert_matches_type(SignedUploadCompleteResponse, upload, path=["response"])

    @parametrize
    def test_method_complete_with_all_params(self, client: Structify) -> None:
        upload = client.uploads.complete(
            blob_name="blob_name",
            content_type="content_type",
            target="chat_input",
            cache_final_rows=0,
            cache_final_size_bytes=0,
            cache_max_bytes=0,
            cache_original_rows=0,
            cache_original_size_bytes=0,
            cache_truncated=True,
            chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_name="file_name",
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            output_schema={},
        )
        assert_matches_type(SignedUploadCompleteResponse, upload, path=["response"])

    @parametrize
    def test_raw_response_complete(self, client: Structify) -> None:
        response = client.uploads.with_raw_response.complete(
            blob_name="blob_name",
            content_type="content_type",
            target="chat_input",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = response.parse()
        assert_matches_type(SignedUploadCompleteResponse, upload, path=["response"])

    @parametrize
    def test_streaming_response_complete(self, client: Structify) -> None:
        with client.uploads.with_streaming_response.complete(
            blob_name="blob_name",
            content_type="content_type",
            target="chat_input",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = response.parse()
            assert_matches_type(SignedUploadCompleteResponse, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_init(self, client: Structify) -> None:
        upload = client.uploads.init(
            content_type="content_type",
            file_size=0,
            target="chat_input",
        )
        assert_matches_type(SignedUploadInitResponse, upload, path=["response"])

    @parametrize
    def test_method_init_with_all_params(self, client: Structify) -> None:
        upload = client.uploads.init(
            content_type="content_type",
            file_size=0,
            target="chat_input",
            chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SignedUploadInitResponse, upload, path=["response"])

    @parametrize
    def test_raw_response_init(self, client: Structify) -> None:
        response = client.uploads.with_raw_response.init(
            content_type="content_type",
            file_size=0,
            target="chat_input",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = response.parse()
        assert_matches_type(SignedUploadInitResponse, upload, path=["response"])

    @parametrize
    def test_streaming_response_init(self, client: Structify) -> None:
        with client.uploads.with_streaming_response.init(
            content_type="content_type",
            file_size=0,
            target="chat_input",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = response.parse()
            assert_matches_type(SignedUploadInitResponse, upload, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUploads:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_complete(self, async_client: AsyncStructify) -> None:
        upload = await async_client.uploads.complete(
            blob_name="blob_name",
            content_type="content_type",
            target="chat_input",
        )
        assert_matches_type(SignedUploadCompleteResponse, upload, path=["response"])

    @parametrize
    async def test_method_complete_with_all_params(self, async_client: AsyncStructify) -> None:
        upload = await async_client.uploads.complete(
            blob_name="blob_name",
            content_type="content_type",
            target="chat_input",
            cache_final_rows=0,
            cache_final_size_bytes=0,
            cache_max_bytes=0,
            cache_original_rows=0,
            cache_original_size_bytes=0,
            cache_truncated=True,
            chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_name="file_name",
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            output_schema={},
        )
        assert_matches_type(SignedUploadCompleteResponse, upload, path=["response"])

    @parametrize
    async def test_raw_response_complete(self, async_client: AsyncStructify) -> None:
        response = await async_client.uploads.with_raw_response.complete(
            blob_name="blob_name",
            content_type="content_type",
            target="chat_input",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = await response.parse()
        assert_matches_type(SignedUploadCompleteResponse, upload, path=["response"])

    @parametrize
    async def test_streaming_response_complete(self, async_client: AsyncStructify) -> None:
        async with async_client.uploads.with_streaming_response.complete(
            blob_name="blob_name",
            content_type="content_type",
            target="chat_input",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = await response.parse()
            assert_matches_type(SignedUploadCompleteResponse, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_init(self, async_client: AsyncStructify) -> None:
        upload = await async_client.uploads.init(
            content_type="content_type",
            file_size=0,
            target="chat_input",
        )
        assert_matches_type(SignedUploadInitResponse, upload, path=["response"])

    @parametrize
    async def test_method_init_with_all_params(self, async_client: AsyncStructify) -> None:
        upload = await async_client.uploads.init(
            content_type="content_type",
            file_size=0,
            target="chat_input",
            chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SignedUploadInitResponse, upload, path=["response"])

    @parametrize
    async def test_raw_response_init(self, async_client: AsyncStructify) -> None:
        response = await async_client.uploads.with_raw_response.init(
            content_type="content_type",
            file_size=0,
            target="chat_input",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = await response.parse()
        assert_matches_type(SignedUploadInitResponse, upload, path=["response"])

    @parametrize
    async def test_streaming_response_init(self, async_client: AsyncStructify) -> None:
        async with async_client.uploads.with_streaming_response.init(
            content_type="content_type",
            file_size=0,
            target="chat_input",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = await response.parse()
            assert_matches_type(SignedUploadInitResponse, upload, path=["response"])

        assert cast(Any, response.is_closed) is True
