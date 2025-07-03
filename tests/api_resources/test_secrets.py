# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types import (
    GetSecretResponse,
    SecretListResponse,
    UpdateSecretResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSecrets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Structify) -> None:
        secret = client.secrets.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            secret_name="secret_name",
            secret_value="secret_value",
        )
        assert secret is None

    @parametrize
    def test_raw_response_create(self, client: Structify) -> None:
        response = client.secrets.with_raw_response.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            secret_name="secret_name",
            secret_value="secret_value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert secret is None

    @parametrize
    def test_streaming_response_create(self, client: Structify) -> None:
        with client.secrets.with_streaming_response.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            secret_name="secret_name",
            secret_value="secret_value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert secret is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.secrets.with_raw_response.create(
                project_id="",
                secret_name="secret_name",
                secret_value="secret_value",
            )

    @parametrize
    def test_method_update(self, client: Structify) -> None:
        secret = client.secrets.update(
            secret_name="secret_name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            secret_value="secret_value",
        )
        assert_matches_type(UpdateSecretResponse, secret, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Structify) -> None:
        response = client.secrets.with_raw_response.update(
            secret_name="secret_name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            secret_value="secret_value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(UpdateSecretResponse, secret, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Structify) -> None:
        with client.secrets.with_streaming_response.update(
            secret_name="secret_name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            secret_value="secret_value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(UpdateSecretResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.secrets.with_raw_response.update(
                secret_name="secret_name",
                project_id="",
                secret_value="secret_value",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `secret_name` but received ''"):
            client.secrets.with_raw_response.update(
                secret_name="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                secret_value="secret_value",
            )

    @parametrize
    def test_method_list(self, client: Structify) -> None:
        secret = client.secrets.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SecretListResponse, secret, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Structify) -> None:
        response = client.secrets.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(SecretListResponse, secret, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Structify) -> None:
        with client.secrets.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(SecretListResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.secrets.with_raw_response.list(
                "",
            )

    @parametrize
    def test_method_delete(self, client: Structify) -> None:
        secret = client.secrets.delete(
            secret_name="secret_name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert secret is None

    @parametrize
    def test_raw_response_delete(self, client: Structify) -> None:
        response = client.secrets.with_raw_response.delete(
            secret_name="secret_name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert secret is None

    @parametrize
    def test_streaming_response_delete(self, client: Structify) -> None:
        with client.secrets.with_streaming_response.delete(
            secret_name="secret_name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert secret is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.secrets.with_raw_response.delete(
                secret_name="secret_name",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `secret_name` but received ''"):
            client.secrets.with_raw_response.delete(
                secret_name="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_get(self, client: Structify) -> None:
        secret = client.secrets.get(
            secret_name="secret_name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GetSecretResponse, secret, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Structify) -> None:
        response = client.secrets.with_raw_response.get(
            secret_name="secret_name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(GetSecretResponse, secret, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Structify) -> None:
        with client.secrets.with_streaming_response.get(
            secret_name="secret_name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(GetSecretResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.secrets.with_raw_response.get(
                secret_name="secret_name",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `secret_name` but received ''"):
            client.secrets.with_raw_response.get(
                secret_name="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncSecrets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncStructify) -> None:
        secret = await async_client.secrets.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            secret_name="secret_name",
            secret_value="secret_value",
        )
        assert secret is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStructify) -> None:
        response = await async_client.secrets.with_raw_response.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            secret_name="secret_name",
            secret_value="secret_value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert secret is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStructify) -> None:
        async with async_client.secrets.with_streaming_response.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            secret_name="secret_name",
            secret_value="secret_value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert secret is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.secrets.with_raw_response.create(
                project_id="",
                secret_name="secret_name",
                secret_value="secret_value",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncStructify) -> None:
        secret = await async_client.secrets.update(
            secret_name="secret_name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            secret_value="secret_value",
        )
        assert_matches_type(UpdateSecretResponse, secret, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncStructify) -> None:
        response = await async_client.secrets.with_raw_response.update(
            secret_name="secret_name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            secret_value="secret_value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(UpdateSecretResponse, secret, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncStructify) -> None:
        async with async_client.secrets.with_streaming_response.update(
            secret_name="secret_name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            secret_value="secret_value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(UpdateSecretResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.secrets.with_raw_response.update(
                secret_name="secret_name",
                project_id="",
                secret_value="secret_value",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `secret_name` but received ''"):
            await async_client.secrets.with_raw_response.update(
                secret_name="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                secret_value="secret_value",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncStructify) -> None:
        secret = await async_client.secrets.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SecretListResponse, secret, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStructify) -> None:
        response = await async_client.secrets.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(SecretListResponse, secret, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStructify) -> None:
        async with async_client.secrets.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(SecretListResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.secrets.with_raw_response.list(
                "",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncStructify) -> None:
        secret = await async_client.secrets.delete(
            secret_name="secret_name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert secret is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncStructify) -> None:
        response = await async_client.secrets.with_raw_response.delete(
            secret_name="secret_name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert secret is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncStructify) -> None:
        async with async_client.secrets.with_streaming_response.delete(
            secret_name="secret_name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert secret is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.secrets.with_raw_response.delete(
                secret_name="secret_name",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `secret_name` but received ''"):
            await async_client.secrets.with_raw_response.delete(
                secret_name="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncStructify) -> None:
        secret = await async_client.secrets.get(
            secret_name="secret_name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GetSecretResponse, secret, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncStructify) -> None:
        response = await async_client.secrets.with_raw_response.get(
            secret_name="secret_name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(GetSecretResponse, secret, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncStructify) -> None:
        async with async_client.secrets.with_streaming_response.get(
            secret_name="secret_name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(GetSecretResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.secrets.with_raw_response.get(
                secret_name="secret_name",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `secret_name` but received ''"):
            await async_client.secrets.with_raw_response.get(
                secret_name="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
