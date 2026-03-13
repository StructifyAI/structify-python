# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types.admin import CloneConnectorsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConnector:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_clone(self, client: Structify) -> None:
        connector = client.admin.connector.clone(
            connectors=[
                {
                    "known_connector_type": "known_connector_type",
                    "name": "name",
                    "source_connector_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            source_membership_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            source_team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CloneConnectorsResponse, connector, path=["response"])

    @parametrize
    def test_raw_response_clone(self, client: Structify) -> None:
        response = client.admin.connector.with_raw_response.clone(
            connectors=[
                {
                    "known_connector_type": "known_connector_type",
                    "name": "name",
                    "source_connector_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            source_membership_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            source_team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector = response.parse()
        assert_matches_type(CloneConnectorsResponse, connector, path=["response"])

    @parametrize
    def test_streaming_response_clone(self, client: Structify) -> None:
        with client.admin.connector.with_streaming_response.clone(
            connectors=[
                {
                    "known_connector_type": "known_connector_type",
                    "name": "name",
                    "source_connector_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            source_membership_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            source_team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector = response.parse()
            assert_matches_type(CloneConnectorsResponse, connector, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConnector:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_clone(self, async_client: AsyncStructify) -> None:
        connector = await async_client.admin.connector.clone(
            connectors=[
                {
                    "known_connector_type": "known_connector_type",
                    "name": "name",
                    "source_connector_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            source_membership_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            source_team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CloneConnectorsResponse, connector, path=["response"])

    @parametrize
    async def test_raw_response_clone(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.connector.with_raw_response.clone(
            connectors=[
                {
                    "known_connector_type": "known_connector_type",
                    "name": "name",
                    "source_connector_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            source_membership_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            source_team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector = await response.parse()
        assert_matches_type(CloneConnectorsResponse, connector, path=["response"])

    @parametrize
    async def test_streaming_response_clone(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.connector.with_streaming_response.clone(
            connectors=[
                {
                    "known_connector_type": "known_connector_type",
                    "name": "name",
                    "source_connector_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            source_membership_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            source_team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector = await response.parse()
            assert_matches_type(CloneConnectorsResponse, connector, path=["response"])

        assert cast(Any, response.is_closed) is True
