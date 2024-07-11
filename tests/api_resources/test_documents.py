# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types import DocumentListResponse
from structify._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

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
            "path",
        )
        assert document is None

    @parametrize
    def test_raw_response_delete(self, client: Structify) -> None:
        response = client.documents.with_raw_response.delete(
            "path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert document is None

    @parametrize
    def test_streaming_response_delete(self, client: Structify) -> None:
        with client.documents.with_streaming_response.delete(
            "path",
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
    @pytest.mark.respx(base_url=base_url)
    def test_method_download(self, client: Structify, respx_mock: MockRouter) -> None:
        respx_mock.get("/documents/download/path").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        document = client.documents.download(
            "path",
        )
        assert document.is_closed
        assert document.json() == {"foo": "bar"}
        assert cast(Any, document.is_closed) is True
        assert isinstance(document, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_download(self, client: Structify, respx_mock: MockRouter) -> None:
        respx_mock.get("/documents/download/path").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        document = client.documents.with_raw_response.download(
            "path",
        )

        assert document.is_closed is True
        assert document.http_request.headers.get("X-Stainless-Lang") == "python"
        assert document.json() == {"foo": "bar"}
        assert isinstance(document, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_download(self, client: Structify, respx_mock: MockRouter) -> None:
        respx_mock.get("/documents/download/path").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.documents.with_streaming_response.download(
            "path",
        ) as document:
            assert not document.is_closed
            assert document.http_request.headers.get("X-Stainless-Lang") == "python"

            assert document.json() == {"foo": "bar"}
            assert cast(Any, document.is_closed) is True
            assert isinstance(document, StreamedBinaryAPIResponse)

        assert cast(Any, document.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_download(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path` but received ''"):
            client.documents.with_raw_response.download(
                "",
            )

    @parametrize
    def test_method_upload(self, client: Structify) -> None:
        document = client.documents.upload(
            content=b"raw file contents",
            file_type="Text",
            path=b"raw file contents",
        )
        assert document is None

    @parametrize
    def test_raw_response_upload(self, client: Structify) -> None:
        response = client.documents.with_raw_response.upload(
            content=b"raw file contents",
            file_type="Text",
            path=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert document is None

    @parametrize
    def test_streaming_response_upload(self, client: Structify) -> None:
        with client.documents.with_streaming_response.upload(
            content=b"raw file contents",
            file_type="Text",
            path=b"raw file contents",
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
            "path",
        )
        assert document is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncStructify) -> None:
        response = await async_client.documents.with_raw_response.delete(
            "path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert document is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncStructify) -> None:
        async with async_client.documents.with_streaming_response.delete(
            "path",
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
    @pytest.mark.respx(base_url=base_url)
    async def test_method_download(self, async_client: AsyncStructify, respx_mock: MockRouter) -> None:
        respx_mock.get("/documents/download/path").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        document = await async_client.documents.download(
            "path",
        )
        assert document.is_closed
        assert await document.json() == {"foo": "bar"}
        assert cast(Any, document.is_closed) is True
        assert isinstance(document, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_download(self, async_client: AsyncStructify, respx_mock: MockRouter) -> None:
        respx_mock.get("/documents/download/path").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        document = await async_client.documents.with_raw_response.download(
            "path",
        )

        assert document.is_closed is True
        assert document.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await document.json() == {"foo": "bar"}
        assert isinstance(document, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_download(self, async_client: AsyncStructify, respx_mock: MockRouter) -> None:
        respx_mock.get("/documents/download/path").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.documents.with_streaming_response.download(
            "path",
        ) as document:
            assert not document.is_closed
            assert document.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await document.json() == {"foo": "bar"}
            assert cast(Any, document.is_closed) is True
            assert isinstance(document, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, document.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_download(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path` but received ''"):
            await async_client.documents.with_raw_response.download(
                "",
            )

    @parametrize
    async def test_method_upload(self, async_client: AsyncStructify) -> None:
        document = await async_client.documents.upload(
            content=b"raw file contents",
            file_type="Text",
            path=b"raw file contents",
        )
        assert document is None

    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncStructify) -> None:
        response = await async_client.documents.with_raw_response.upload(
            content=b"raw file contents",
            file_type="Text",
            path=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert document is None

    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncStructify) -> None:
        async with async_client.documents.with_streaming_response.upload(
            content=b"raw file contents",
            file_type="Text",
            path=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert document is None

        assert cast(Any, response.is_closed) is True
