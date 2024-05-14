# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types import DocumentListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDocuments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Structify) -> None:
        document = client.documents.list()
        assert_matches_type(DocumentListResponse, document, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Structify) -> None:
        response = client.documents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentListResponse, document, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Structify) -> None:
        with client.documents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentListResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Structify) -> None:
        document = client.documents.delete(
            "string",
        )
        assert document is None

    @parametrize
    def test_raw_response_delete(self, client: Structify) -> None:
        response = client.documents.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert document is None

    @parametrize
    def test_streaming_response_delete(self, client: Structify) -> None:
        with client.documents.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert document is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path` but received ''"):
            client.documents.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_download(self, client: Structify) -> None:
        document = client.documents.download(
            "string",
        )
        assert_matches_type(str, document, path=["response"])

    @parametrize
    def test_raw_response_download(self, client: Structify) -> None:
        response = client.documents.with_raw_response.download(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(str, document, path=["response"])

    @parametrize
    def test_streaming_response_download(self, client: Structify) -> None:
        with client.documents.with_streaming_response.download(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(str, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_download(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.documents.with_raw_response.download(
                "",
            )

    @parametrize
    def test_method_upload(self, client: Structify) -> None:
        document = client.documents.upload(
            doctype="Text",
            path="string",
            body={},
        )
        assert document is None

    @parametrize
    def test_raw_response_upload(self, client: Structify) -> None:
        response = client.documents.with_raw_response.upload(
            doctype="Text",
            path="string",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert document is None

    @parametrize
    def test_streaming_response_upload(self, client: Structify) -> None:
        with client.documents.with_streaming_response.upload(
            doctype="Text",
            path="string",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert document is None

        assert cast(Any, response.is_closed) is True


class TestAsyncDocuments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncStructify) -> None:
        document = await async_client.documents.list()
        assert_matches_type(DocumentListResponse, document, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStructify) -> None:
        response = await async_client.documents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentListResponse, document, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStructify) -> None:
        async with async_client.documents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentListResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncStructify) -> None:
        document = await async_client.documents.delete(
            "string",
        )
        assert document is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncStructify) -> None:
        response = await async_client.documents.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert document is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncStructify) -> None:
        async with async_client.documents.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert document is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path` but received ''"):
            await async_client.documents.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_download(self, async_client: AsyncStructify) -> None:
        document = await async_client.documents.download(
            "string",
        )
        assert_matches_type(str, document, path=["response"])

    @parametrize
    async def test_raw_response_download(self, async_client: AsyncStructify) -> None:
        response = await async_client.documents.with_raw_response.download(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(str, document, path=["response"])

    @parametrize
    async def test_streaming_response_download(self, async_client: AsyncStructify) -> None:
        async with async_client.documents.with_streaming_response.download(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(str, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_download(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.documents.with_raw_response.download(
                "",
            )

    @pytest.mark.skip(reason="stainless doesn't support this yet.")
    @parametrize
    async def test_method_upload(self, async_client: AsyncStructify) -> None:
        document = await async_client.documents.upload(
            doctype="Text",
            path="string",
            body={},
        )
        assert document is None

    @pytest.mark.skip(reason="stainless doesn't support yet.")
    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncStructify) -> None:
        response = await async_client.documents.with_raw_response.upload(
            doctype="Text",
            path="string",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert document is None

    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncStructify) -> None:
        async with async_client.documents.with_streaming_response.upload(
            doctype="Text",
            path="string",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert document is None

        assert cast(Any, response.is_closed) is True
