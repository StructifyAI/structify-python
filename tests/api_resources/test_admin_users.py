# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types import AdminUserListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAdminUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Structify) -> None:
        admin_user = client.admin_users.list()
        assert_matches_type(AdminUserListResponse, admin_user, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Structify) -> None:
        response = client.admin_users.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin_user = response.parse()
        assert_matches_type(AdminUserListResponse, admin_user, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Structify) -> None:
        with client.admin_users.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin_user = response.parse()
            assert_matches_type(AdminUserListResponse, admin_user, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAdminUsers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncStructify) -> None:
        admin_user = await async_client.admin_users.list()
        assert_matches_type(AdminUserListResponse, admin_user, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin_users.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin_user = await response.parse()
        assert_matches_type(AdminUserListResponse, admin_user, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStructify) -> None:
        async with async_client.admin_users.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin_user = await response.parse()
            assert_matches_type(AdminUserListResponse, admin_user, path=["response"])

        assert cast(Any, response.is_closed) is True
