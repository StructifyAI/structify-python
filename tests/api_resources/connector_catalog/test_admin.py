# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types import ConnectorAuthMethod, ConnectorCredentialField
from structify.types.connector_catalog import (
    ConnectorCatalog,
    AdminListNangoPendingResponse,
    AdminBatchCreateCredentialFieldsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAdmin:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_batch_create_credential_fields(self, client: Structify) -> None:
        admin = client.connector_catalog.admin.batch_create_credential_fields(
            fields=[
                {
                    "auth_method_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "display_order": 0,
                    "field_type": "field_type",
                    "is_optional": True,
                    "name": "name",
                }
            ],
        )
        assert_matches_type(AdminBatchCreateCredentialFieldsResponse, admin, path=["response"])

    @parametrize
    def test_raw_response_batch_create_credential_fields(self, client: Structify) -> None:
        response = client.connector_catalog.admin.with_raw_response.batch_create_credential_fields(
            fields=[
                {
                    "auth_method_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "display_order": 0,
                    "field_type": "field_type",
                    "is_optional": True,
                    "name": "name",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = response.parse()
        assert_matches_type(AdminBatchCreateCredentialFieldsResponse, admin, path=["response"])

    @parametrize
    def test_streaming_response_batch_create_credential_fields(self, client: Structify) -> None:
        with client.connector_catalog.admin.with_streaming_response.batch_create_credential_fields(
            fields=[
                {
                    "auth_method_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "display_order": 0,
                    "field_type": "field_type",
                    "is_optional": True,
                    "name": "name",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = response.parse()
            assert_matches_type(AdminBatchCreateCredentialFieldsResponse, admin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_auth_method(self, client: Structify) -> None:
        admin = client.connector_catalog.admin.create_auth_method(
            auth_type="credentials",
            connector_catalog_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            is_active=True,
            priority=0,
        )
        assert_matches_type(ConnectorAuthMethod, admin, path=["response"])

    @parametrize
    def test_method_create_auth_method_with_all_params(self, client: Structify) -> None:
        admin = client.connector_catalog.admin.create_auth_method(
            auth_type="credentials",
            connector_catalog_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            is_active=True,
            priority=0,
            label="label",
            nango_integration_key="nango_integration_key",
        )
        assert_matches_type(ConnectorAuthMethod, admin, path=["response"])

    @parametrize
    def test_raw_response_create_auth_method(self, client: Structify) -> None:
        response = client.connector_catalog.admin.with_raw_response.create_auth_method(
            auth_type="credentials",
            connector_catalog_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            is_active=True,
            priority=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = response.parse()
        assert_matches_type(ConnectorAuthMethod, admin, path=["response"])

    @parametrize
    def test_streaming_response_create_auth_method(self, client: Structify) -> None:
        with client.connector_catalog.admin.with_streaming_response.create_auth_method(
            auth_type="credentials",
            connector_catalog_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            is_active=True,
            priority=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = response.parse()
            assert_matches_type(ConnectorAuthMethod, admin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_catalog(self, client: Structify) -> None:
        admin = client.connector_catalog.admin.create_catalog(
            name="name",
            slug="slug",
        )
        assert_matches_type(ConnectorCatalog, admin, path=["response"])

    @parametrize
    def test_method_create_catalog_with_all_params(self, client: Structify) -> None:
        admin = client.connector_catalog.admin.create_catalog(
            name="name",
            slug="slug",
            categories=["string"],
            description="description",
            logo_path="logo_path",
            priority=0,
        )
        assert_matches_type(ConnectorCatalog, admin, path=["response"])

    @parametrize
    def test_raw_response_create_catalog(self, client: Structify) -> None:
        response = client.connector_catalog.admin.with_raw_response.create_catalog(
            name="name",
            slug="slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = response.parse()
        assert_matches_type(ConnectorCatalog, admin, path=["response"])

    @parametrize
    def test_streaming_response_create_catalog(self, client: Structify) -> None:
        with client.connector_catalog.admin.with_streaming_response.create_catalog(
            name="name",
            slug="slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = response.parse()
            assert_matches_type(ConnectorCatalog, admin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_credential_field(self, client: Structify) -> None:
        admin = client.connector_catalog.admin.create_credential_field(
            auth_method_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            display_order=0,
            field_type="field_type",
            is_optional=True,
            name="name",
        )
        assert_matches_type(ConnectorCredentialField, admin, path=["response"])

    @parametrize
    def test_method_create_credential_field_with_all_params(self, client: Structify) -> None:
        admin = client.connector_catalog.admin.create_credential_field(
            auth_method_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            display_order=0,
            field_type="field_type",
            is_optional=True,
            name="name",
            default_value="default_value",
            description="description",
            label="label",
            options={},
        )
        assert_matches_type(ConnectorCredentialField, admin, path=["response"])

    @parametrize
    def test_raw_response_create_credential_field(self, client: Structify) -> None:
        response = client.connector_catalog.admin.with_raw_response.create_credential_field(
            auth_method_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            display_order=0,
            field_type="field_type",
            is_optional=True,
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = response.parse()
        assert_matches_type(ConnectorCredentialField, admin, path=["response"])

    @parametrize
    def test_streaming_response_create_credential_field(self, client: Structify) -> None:
        with client.connector_catalog.admin.with_streaming_response.create_credential_field(
            auth_method_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            display_order=0,
            field_type="field_type",
            is_optional=True,
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = response.parse()
            assert_matches_type(ConnectorCredentialField, admin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete_credential_field(self, client: Structify) -> None:
        admin = client.connector_catalog.admin.delete_credential_field(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert admin is None

    @parametrize
    def test_raw_response_delete_credential_field(self, client: Structify) -> None:
        response = client.connector_catalog.admin.with_raw_response.delete_credential_field(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = response.parse()
        assert admin is None

    @parametrize
    def test_streaming_response_delete_credential_field(self, client: Structify) -> None:
        with client.connector_catalog.admin.with_streaming_response.delete_credential_field(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = response.parse()
            assert admin is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete_credential_field(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.connector_catalog.admin.with_raw_response.delete_credential_field(
                "",
            )

    @parametrize
    def test_method_list_nango_pending(self, client: Structify) -> None:
        admin = client.connector_catalog.admin.list_nango_pending()
        assert_matches_type(AdminListNangoPendingResponse, admin, path=["response"])

    @parametrize
    def test_raw_response_list_nango_pending(self, client: Structify) -> None:
        response = client.connector_catalog.admin.with_raw_response.list_nango_pending()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = response.parse()
        assert_matches_type(AdminListNangoPendingResponse, admin, path=["response"])

    @parametrize
    def test_streaming_response_list_nango_pending(self, client: Structify) -> None:
        with client.connector_catalog.admin.with_streaming_response.list_nango_pending() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = response.parse()
            assert_matches_type(AdminListNangoPendingResponse, admin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_auth_method(self, client: Structify) -> None:
        admin = client.connector_catalog.admin.update_auth_method(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ConnectorAuthMethod, admin, path=["response"])

    @parametrize
    def test_method_update_auth_method_with_all_params(self, client: Structify) -> None:
        admin = client.connector_catalog.admin.update_auth_method(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            is_active=True,
            label="label",
            priority=0,
        )
        assert_matches_type(ConnectorAuthMethod, admin, path=["response"])

    @parametrize
    def test_raw_response_update_auth_method(self, client: Structify) -> None:
        response = client.connector_catalog.admin.with_raw_response.update_auth_method(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = response.parse()
        assert_matches_type(ConnectorAuthMethod, admin, path=["response"])

    @parametrize
    def test_streaming_response_update_auth_method(self, client: Structify) -> None:
        with client.connector_catalog.admin.with_streaming_response.update_auth_method(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = response.parse()
            assert_matches_type(ConnectorAuthMethod, admin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_auth_method(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.connector_catalog.admin.with_raw_response.update_auth_method(
                id="",
            )

    @parametrize
    def test_method_update_catalog(self, client: Structify) -> None:
        admin = client.connector_catalog.admin.update_catalog(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ConnectorCatalog, admin, path=["response"])

    @parametrize
    def test_method_update_catalog_with_all_params(self, client: Structify) -> None:
        admin = client.connector_catalog.admin.update_catalog(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            categories=["string"],
            description="description",
            logo_path="logo_path",
            name="name",
            priority=0,
        )
        assert_matches_type(ConnectorCatalog, admin, path=["response"])

    @parametrize
    def test_raw_response_update_catalog(self, client: Structify) -> None:
        response = client.connector_catalog.admin.with_raw_response.update_catalog(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = response.parse()
        assert_matches_type(ConnectorCatalog, admin, path=["response"])

    @parametrize
    def test_streaming_response_update_catalog(self, client: Structify) -> None:
        with client.connector_catalog.admin.with_streaming_response.update_catalog(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = response.parse()
            assert_matches_type(ConnectorCatalog, admin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_catalog(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.connector_catalog.admin.with_raw_response.update_catalog(
                id="",
            )

    @parametrize
    def test_method_update_credential_field(self, client: Structify) -> None:
        admin = client.connector_catalog.admin.update_credential_field(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ConnectorCredentialField, admin, path=["response"])

    @parametrize
    def test_method_update_credential_field_with_all_params(self, client: Structify) -> None:
        admin = client.connector_catalog.admin.update_credential_field(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            default_value="default_value",
            description="description",
            display_order=0,
            field_type="field_type",
            is_optional=True,
            label="label",
            name="name",
            options={},
        )
        assert_matches_type(ConnectorCredentialField, admin, path=["response"])

    @parametrize
    def test_raw_response_update_credential_field(self, client: Structify) -> None:
        response = client.connector_catalog.admin.with_raw_response.update_credential_field(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = response.parse()
        assert_matches_type(ConnectorCredentialField, admin, path=["response"])

    @parametrize
    def test_streaming_response_update_credential_field(self, client: Structify) -> None:
        with client.connector_catalog.admin.with_streaming_response.update_credential_field(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = response.parse()
            assert_matches_type(ConnectorCredentialField, admin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_credential_field(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.connector_catalog.admin.with_raw_response.update_credential_field(
                id="",
            )


class TestAsyncAdmin:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_batch_create_credential_fields(self, async_client: AsyncStructify) -> None:
        admin = await async_client.connector_catalog.admin.batch_create_credential_fields(
            fields=[
                {
                    "auth_method_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "display_order": 0,
                    "field_type": "field_type",
                    "is_optional": True,
                    "name": "name",
                }
            ],
        )
        assert_matches_type(AdminBatchCreateCredentialFieldsResponse, admin, path=["response"])

    @parametrize
    async def test_raw_response_batch_create_credential_fields(self, async_client: AsyncStructify) -> None:
        response = await async_client.connector_catalog.admin.with_raw_response.batch_create_credential_fields(
            fields=[
                {
                    "auth_method_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "display_order": 0,
                    "field_type": "field_type",
                    "is_optional": True,
                    "name": "name",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = await response.parse()
        assert_matches_type(AdminBatchCreateCredentialFieldsResponse, admin, path=["response"])

    @parametrize
    async def test_streaming_response_batch_create_credential_fields(self, async_client: AsyncStructify) -> None:
        async with async_client.connector_catalog.admin.with_streaming_response.batch_create_credential_fields(
            fields=[
                {
                    "auth_method_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "display_order": 0,
                    "field_type": "field_type",
                    "is_optional": True,
                    "name": "name",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = await response.parse()
            assert_matches_type(AdminBatchCreateCredentialFieldsResponse, admin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_auth_method(self, async_client: AsyncStructify) -> None:
        admin = await async_client.connector_catalog.admin.create_auth_method(
            auth_type="credentials",
            connector_catalog_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            is_active=True,
            priority=0,
        )
        assert_matches_type(ConnectorAuthMethod, admin, path=["response"])

    @parametrize
    async def test_method_create_auth_method_with_all_params(self, async_client: AsyncStructify) -> None:
        admin = await async_client.connector_catalog.admin.create_auth_method(
            auth_type="credentials",
            connector_catalog_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            is_active=True,
            priority=0,
            label="label",
            nango_integration_key="nango_integration_key",
        )
        assert_matches_type(ConnectorAuthMethod, admin, path=["response"])

    @parametrize
    async def test_raw_response_create_auth_method(self, async_client: AsyncStructify) -> None:
        response = await async_client.connector_catalog.admin.with_raw_response.create_auth_method(
            auth_type="credentials",
            connector_catalog_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            is_active=True,
            priority=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = await response.parse()
        assert_matches_type(ConnectorAuthMethod, admin, path=["response"])

    @parametrize
    async def test_streaming_response_create_auth_method(self, async_client: AsyncStructify) -> None:
        async with async_client.connector_catalog.admin.with_streaming_response.create_auth_method(
            auth_type="credentials",
            connector_catalog_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            is_active=True,
            priority=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = await response.parse()
            assert_matches_type(ConnectorAuthMethod, admin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_catalog(self, async_client: AsyncStructify) -> None:
        admin = await async_client.connector_catalog.admin.create_catalog(
            name="name",
            slug="slug",
        )
        assert_matches_type(ConnectorCatalog, admin, path=["response"])

    @parametrize
    async def test_method_create_catalog_with_all_params(self, async_client: AsyncStructify) -> None:
        admin = await async_client.connector_catalog.admin.create_catalog(
            name="name",
            slug="slug",
            categories=["string"],
            description="description",
            logo_path="logo_path",
            priority=0,
        )
        assert_matches_type(ConnectorCatalog, admin, path=["response"])

    @parametrize
    async def test_raw_response_create_catalog(self, async_client: AsyncStructify) -> None:
        response = await async_client.connector_catalog.admin.with_raw_response.create_catalog(
            name="name",
            slug="slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = await response.parse()
        assert_matches_type(ConnectorCatalog, admin, path=["response"])

    @parametrize
    async def test_streaming_response_create_catalog(self, async_client: AsyncStructify) -> None:
        async with async_client.connector_catalog.admin.with_streaming_response.create_catalog(
            name="name",
            slug="slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = await response.parse()
            assert_matches_type(ConnectorCatalog, admin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_credential_field(self, async_client: AsyncStructify) -> None:
        admin = await async_client.connector_catalog.admin.create_credential_field(
            auth_method_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            display_order=0,
            field_type="field_type",
            is_optional=True,
            name="name",
        )
        assert_matches_type(ConnectorCredentialField, admin, path=["response"])

    @parametrize
    async def test_method_create_credential_field_with_all_params(self, async_client: AsyncStructify) -> None:
        admin = await async_client.connector_catalog.admin.create_credential_field(
            auth_method_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            display_order=0,
            field_type="field_type",
            is_optional=True,
            name="name",
            default_value="default_value",
            description="description",
            label="label",
            options={},
        )
        assert_matches_type(ConnectorCredentialField, admin, path=["response"])

    @parametrize
    async def test_raw_response_create_credential_field(self, async_client: AsyncStructify) -> None:
        response = await async_client.connector_catalog.admin.with_raw_response.create_credential_field(
            auth_method_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            display_order=0,
            field_type="field_type",
            is_optional=True,
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = await response.parse()
        assert_matches_type(ConnectorCredentialField, admin, path=["response"])

    @parametrize
    async def test_streaming_response_create_credential_field(self, async_client: AsyncStructify) -> None:
        async with async_client.connector_catalog.admin.with_streaming_response.create_credential_field(
            auth_method_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            display_order=0,
            field_type="field_type",
            is_optional=True,
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = await response.parse()
            assert_matches_type(ConnectorCredentialField, admin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete_credential_field(self, async_client: AsyncStructify) -> None:
        admin = await async_client.connector_catalog.admin.delete_credential_field(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert admin is None

    @parametrize
    async def test_raw_response_delete_credential_field(self, async_client: AsyncStructify) -> None:
        response = await async_client.connector_catalog.admin.with_raw_response.delete_credential_field(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = await response.parse()
        assert admin is None

    @parametrize
    async def test_streaming_response_delete_credential_field(self, async_client: AsyncStructify) -> None:
        async with async_client.connector_catalog.admin.with_streaming_response.delete_credential_field(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = await response.parse()
            assert admin is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete_credential_field(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.connector_catalog.admin.with_raw_response.delete_credential_field(
                "",
            )

    @parametrize
    async def test_method_list_nango_pending(self, async_client: AsyncStructify) -> None:
        admin = await async_client.connector_catalog.admin.list_nango_pending()
        assert_matches_type(AdminListNangoPendingResponse, admin, path=["response"])

    @parametrize
    async def test_raw_response_list_nango_pending(self, async_client: AsyncStructify) -> None:
        response = await async_client.connector_catalog.admin.with_raw_response.list_nango_pending()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = await response.parse()
        assert_matches_type(AdminListNangoPendingResponse, admin, path=["response"])

    @parametrize
    async def test_streaming_response_list_nango_pending(self, async_client: AsyncStructify) -> None:
        async with async_client.connector_catalog.admin.with_streaming_response.list_nango_pending() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = await response.parse()
            assert_matches_type(AdminListNangoPendingResponse, admin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_auth_method(self, async_client: AsyncStructify) -> None:
        admin = await async_client.connector_catalog.admin.update_auth_method(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ConnectorAuthMethod, admin, path=["response"])

    @parametrize
    async def test_method_update_auth_method_with_all_params(self, async_client: AsyncStructify) -> None:
        admin = await async_client.connector_catalog.admin.update_auth_method(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            is_active=True,
            label="label",
            priority=0,
        )
        assert_matches_type(ConnectorAuthMethod, admin, path=["response"])

    @parametrize
    async def test_raw_response_update_auth_method(self, async_client: AsyncStructify) -> None:
        response = await async_client.connector_catalog.admin.with_raw_response.update_auth_method(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = await response.parse()
        assert_matches_type(ConnectorAuthMethod, admin, path=["response"])

    @parametrize
    async def test_streaming_response_update_auth_method(self, async_client: AsyncStructify) -> None:
        async with async_client.connector_catalog.admin.with_streaming_response.update_auth_method(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = await response.parse()
            assert_matches_type(ConnectorAuthMethod, admin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_auth_method(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.connector_catalog.admin.with_raw_response.update_auth_method(
                id="",
            )

    @parametrize
    async def test_method_update_catalog(self, async_client: AsyncStructify) -> None:
        admin = await async_client.connector_catalog.admin.update_catalog(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ConnectorCatalog, admin, path=["response"])

    @parametrize
    async def test_method_update_catalog_with_all_params(self, async_client: AsyncStructify) -> None:
        admin = await async_client.connector_catalog.admin.update_catalog(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            categories=["string"],
            description="description",
            logo_path="logo_path",
            name="name",
            priority=0,
        )
        assert_matches_type(ConnectorCatalog, admin, path=["response"])

    @parametrize
    async def test_raw_response_update_catalog(self, async_client: AsyncStructify) -> None:
        response = await async_client.connector_catalog.admin.with_raw_response.update_catalog(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = await response.parse()
        assert_matches_type(ConnectorCatalog, admin, path=["response"])

    @parametrize
    async def test_streaming_response_update_catalog(self, async_client: AsyncStructify) -> None:
        async with async_client.connector_catalog.admin.with_streaming_response.update_catalog(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = await response.parse()
            assert_matches_type(ConnectorCatalog, admin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_catalog(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.connector_catalog.admin.with_raw_response.update_catalog(
                id="",
            )

    @parametrize
    async def test_method_update_credential_field(self, async_client: AsyncStructify) -> None:
        admin = await async_client.connector_catalog.admin.update_credential_field(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ConnectorCredentialField, admin, path=["response"])

    @parametrize
    async def test_method_update_credential_field_with_all_params(self, async_client: AsyncStructify) -> None:
        admin = await async_client.connector_catalog.admin.update_credential_field(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            default_value="default_value",
            description="description",
            display_order=0,
            field_type="field_type",
            is_optional=True,
            label="label",
            name="name",
            options={},
        )
        assert_matches_type(ConnectorCredentialField, admin, path=["response"])

    @parametrize
    async def test_raw_response_update_credential_field(self, async_client: AsyncStructify) -> None:
        response = await async_client.connector_catalog.admin.with_raw_response.update_credential_field(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = await response.parse()
        assert_matches_type(ConnectorCredentialField, admin, path=["response"])

    @parametrize
    async def test_streaming_response_update_credential_field(self, async_client: AsyncStructify) -> None:
        async with async_client.connector_catalog.admin.with_streaming_response.update_credential_field(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = await response.parse()
            assert_matches_type(ConnectorCredentialField, admin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_credential_field(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.connector_catalog.admin.with_raw_response.update_credential_field(
                id="",
            )
