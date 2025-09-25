# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types import (
    Connector,
    ConnectorGetResponse,
    ConnectorWithSecrets,
)
from structify.pagination import SyncJobsList, AsyncJobsList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConnectors:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Structify) -> None:
        connector = client.connectors.create(
            llm_information_store="llm_information_store",
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Connector, connector, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Structify) -> None:
        connector = client.connectors.create(
            llm_information_store="llm_information_store",
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            secrets={"foo": "string"},
        )
        assert_matches_type(Connector, connector, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Structify) -> None:
        response = client.connectors.with_raw_response.create(
            llm_information_store="llm_information_store",
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector = response.parse()
        assert_matches_type(Connector, connector, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Structify) -> None:
        with client.connectors.with_streaming_response.create(
            llm_information_store="llm_information_store",
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector = response.parse()
            assert_matches_type(Connector, connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Structify) -> None:
        connector = client.connectors.update(
            connector_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert connector is None

    @parametrize
    def test_method_update_with_all_params(self, client: Structify) -> None:
        connector = client.connectors.update(
            connector_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            llm_information_store="llm_information_store",
            name="name",
        )
        assert connector is None

    @parametrize
    def test_raw_response_update(self, client: Structify) -> None:
        response = client.connectors.with_raw_response.update(
            connector_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector = response.parse()
        assert connector is None

    @parametrize
    def test_streaming_response_update(self, client: Structify) -> None:
        with client.connectors.with_streaming_response.update(
            connector_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector = response.parse()
            assert connector is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connector_id` but received ''"):
            client.connectors.with_raw_response.update(
                connector_id="",
            )

    @parametrize
    def test_method_list(self, client: Structify) -> None:
        connector = client.connectors.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncJobsList[ConnectorWithSecrets], connector, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Structify) -> None:
        connector = client.connectors.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            offset=0,
        )
        assert_matches_type(SyncJobsList[ConnectorWithSecrets], connector, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Structify) -> None:
        response = client.connectors.with_raw_response.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector = response.parse()
        assert_matches_type(SyncJobsList[ConnectorWithSecrets], connector, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Structify) -> None:
        with client.connectors.with_streaming_response.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector = response.parse()
            assert_matches_type(SyncJobsList[ConnectorWithSecrets], connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Structify) -> None:
        connector = client.connectors.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert connector is None

    @parametrize
    def test_raw_response_delete(self, client: Structify) -> None:
        response = client.connectors.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector = response.parse()
        assert connector is None

    @parametrize
    def test_streaming_response_delete(self, client: Structify) -> None:
        with client.connectors.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector = response.parse()
            assert connector is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connector_id` but received ''"):
            client.connectors.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_create_secret(self, client: Structify) -> None:
        connector = client.connectors.create_secret(
            connector_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            secret_name="secret_name",
            secret_value="secret_value",
        )
        assert connector is None

    @parametrize
    def test_raw_response_create_secret(self, client: Structify) -> None:
        response = client.connectors.with_raw_response.create_secret(
            connector_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            secret_name="secret_name",
            secret_value="secret_value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector = response.parse()
        assert connector is None

    @parametrize
    def test_streaming_response_create_secret(self, client: Structify) -> None:
        with client.connectors.with_streaming_response.create_secret(
            connector_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            secret_name="secret_name",
            secret_value="secret_value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector = response.parse()
            assert connector is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_secret(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connector_id` but received ''"):
            client.connectors.with_raw_response.create_secret(
                connector_id="",
                secret_name="secret_name",
                secret_value="secret_value",
            )

    @parametrize
    def test_method_delete_secret(self, client: Structify) -> None:
        connector = client.connectors.delete_secret(
            secret_name="secret_name",
            connector_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert connector is None

    @parametrize
    def test_raw_response_delete_secret(self, client: Structify) -> None:
        response = client.connectors.with_raw_response.delete_secret(
            secret_name="secret_name",
            connector_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector = response.parse()
        assert connector is None

    @parametrize
    def test_streaming_response_delete_secret(self, client: Structify) -> None:
        with client.connectors.with_streaming_response.delete_secret(
            secret_name="secret_name",
            connector_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector = response.parse()
            assert connector is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete_secret(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connector_id` but received ''"):
            client.connectors.with_raw_response.delete_secret(
                secret_name="secret_name",
                connector_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `secret_name` but received ''"):
            client.connectors.with_raw_response.delete_secret(
                secret_name="",
                connector_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_get(self, client: Structify) -> None:
        connector = client.connectors.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ConnectorGetResponse, connector, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Structify) -> None:
        response = client.connectors.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector = response.parse()
        assert_matches_type(ConnectorGetResponse, connector, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Structify) -> None:
        with client.connectors.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector = response.parse()
            assert_matches_type(ConnectorGetResponse, connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connector_id` but received ''"):
            client.connectors.with_raw_response.get(
                "",
            )


class TestAsyncConnectors:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncStructify) -> None:
        connector = await async_client.connectors.create(
            llm_information_store="llm_information_store",
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Connector, connector, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncStructify) -> None:
        connector = await async_client.connectors.create(
            llm_information_store="llm_information_store",
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            secrets={"foo": "string"},
        )
        assert_matches_type(Connector, connector, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStructify) -> None:
        response = await async_client.connectors.with_raw_response.create(
            llm_information_store="llm_information_store",
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector = await response.parse()
        assert_matches_type(Connector, connector, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStructify) -> None:
        async with async_client.connectors.with_streaming_response.create(
            llm_information_store="llm_information_store",
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector = await response.parse()
            assert_matches_type(Connector, connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncStructify) -> None:
        connector = await async_client.connectors.update(
            connector_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert connector is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncStructify) -> None:
        connector = await async_client.connectors.update(
            connector_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            llm_information_store="llm_information_store",
            name="name",
        )
        assert connector is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncStructify) -> None:
        response = await async_client.connectors.with_raw_response.update(
            connector_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector = await response.parse()
        assert connector is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncStructify) -> None:
        async with async_client.connectors.with_streaming_response.update(
            connector_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector = await response.parse()
            assert connector is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connector_id` but received ''"):
            await async_client.connectors.with_raw_response.update(
                connector_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncStructify) -> None:
        connector = await async_client.connectors.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncJobsList[ConnectorWithSecrets], connector, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncStructify) -> None:
        connector = await async_client.connectors.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            offset=0,
        )
        assert_matches_type(AsyncJobsList[ConnectorWithSecrets], connector, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStructify) -> None:
        response = await async_client.connectors.with_raw_response.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector = await response.parse()
        assert_matches_type(AsyncJobsList[ConnectorWithSecrets], connector, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStructify) -> None:
        async with async_client.connectors.with_streaming_response.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector = await response.parse()
            assert_matches_type(AsyncJobsList[ConnectorWithSecrets], connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncStructify) -> None:
        connector = await async_client.connectors.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert connector is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncStructify) -> None:
        response = await async_client.connectors.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector = await response.parse()
        assert connector is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncStructify) -> None:
        async with async_client.connectors.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector = await response.parse()
            assert connector is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connector_id` but received ''"):
            await async_client.connectors.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_create_secret(self, async_client: AsyncStructify) -> None:
        connector = await async_client.connectors.create_secret(
            connector_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            secret_name="secret_name",
            secret_value="secret_value",
        )
        assert connector is None

    @parametrize
    async def test_raw_response_create_secret(self, async_client: AsyncStructify) -> None:
        response = await async_client.connectors.with_raw_response.create_secret(
            connector_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            secret_name="secret_name",
            secret_value="secret_value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector = await response.parse()
        assert connector is None

    @parametrize
    async def test_streaming_response_create_secret(self, async_client: AsyncStructify) -> None:
        async with async_client.connectors.with_streaming_response.create_secret(
            connector_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            secret_name="secret_name",
            secret_value="secret_value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector = await response.parse()
            assert connector is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_secret(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connector_id` but received ''"):
            await async_client.connectors.with_raw_response.create_secret(
                connector_id="",
                secret_name="secret_name",
                secret_value="secret_value",
            )

    @parametrize
    async def test_method_delete_secret(self, async_client: AsyncStructify) -> None:
        connector = await async_client.connectors.delete_secret(
            secret_name="secret_name",
            connector_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert connector is None

    @parametrize
    async def test_raw_response_delete_secret(self, async_client: AsyncStructify) -> None:
        response = await async_client.connectors.with_raw_response.delete_secret(
            secret_name="secret_name",
            connector_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector = await response.parse()
        assert connector is None

    @parametrize
    async def test_streaming_response_delete_secret(self, async_client: AsyncStructify) -> None:
        async with async_client.connectors.with_streaming_response.delete_secret(
            secret_name="secret_name",
            connector_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector = await response.parse()
            assert connector is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete_secret(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connector_id` but received ''"):
            await async_client.connectors.with_raw_response.delete_secret(
                secret_name="secret_name",
                connector_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `secret_name` but received ''"):
            await async_client.connectors.with_raw_response.delete_secret(
                secret_name="",
                connector_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncStructify) -> None:
        connector = await async_client.connectors.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ConnectorGetResponse, connector, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncStructify) -> None:
        response = await async_client.connectors.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector = await response.parse()
        assert_matches_type(ConnectorGetResponse, connector, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncStructify) -> None:
        async with async_client.connectors.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector = await response.parse()
            assert_matches_type(ConnectorGetResponse, connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connector_id` but received ''"):
            await async_client.connectors.with_raw_response.get(
                "",
            )
