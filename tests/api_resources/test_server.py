# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from structify import Structify, AsyncStructify

from structify.types import ServerInformation

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestServer:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_version(self, client: Structify) -> None:
        server = client.server.version()
        assert_matches_type(ServerInformation, server, path=['response'])

    @parametrize
    def test_raw_response_version(self, client: Structify) -> None:

        response = client.server.with_raw_response.version()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        server = response.parse()
        assert_matches_type(ServerInformation, server, path=['response'])

    @parametrize
    def test_streaming_response_version(self, client: Structify) -> None:
        with client.server.with_streaming_response.version() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            server = response.parse()
            assert_matches_type(ServerInformation, server, path=['response'])

        assert cast(Any, response.is_closed) is True
class TestAsyncServer:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    async def test_method_version(self, async_client: AsyncStructify) -> None:
        server = await async_client.server.version()
        assert_matches_type(ServerInformation, server, path=['response'])

    @parametrize
    async def test_raw_response_version(self, async_client: AsyncStructify) -> None:

        response = await async_client.server.with_raw_response.version()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        server = await response.parse()
        assert_matches_type(ServerInformation, server, path=['response'])

    @parametrize
    async def test_streaming_response_version(self, async_client: AsyncStructify) -> None:
        async with async_client.server.with_streaming_response.version() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            server = await response.parse()
            assert_matches_type(ServerInformation, server, path=['response'])

        assert cast(Any, response.is_closed) is True