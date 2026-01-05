# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types import ChatTemplate
from structify.types.admin import (
    ChatTemplateListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChatTemplates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Structify) -> None:
        chat_template = client.admin.chat_templates.create(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            display_order=0,
            image_url="image_url",
            is_active=True,
            title="title",
        )
        assert_matches_type(ChatTemplate, chat_template, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Structify) -> None:
        response = client.admin.chat_templates.with_raw_response.create(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            display_order=0,
            image_url="image_url",
            is_active=True,
            title="title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat_template = response.parse()
        assert_matches_type(ChatTemplate, chat_template, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Structify) -> None:
        with client.admin.chat_templates.with_streaming_response.create(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            display_order=0,
            image_url="image_url",
            is_active=True,
            title="title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat_template = response.parse()
            assert_matches_type(ChatTemplate, chat_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Structify) -> None:
        chat_template = client.admin.chat_templates.update(
            template_id="template_id",
        )
        assert_matches_type(ChatTemplate, chat_template, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Structify) -> None:
        chat_template = client.admin.chat_templates.update(
            template_id="template_id",
            description="description",
            display_order=0,
            image_url="image_url",
            is_active=True,
            title="title",
            updated_by="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ChatTemplate, chat_template, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Structify) -> None:
        response = client.admin.chat_templates.with_raw_response.update(
            template_id="template_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat_template = response.parse()
        assert_matches_type(ChatTemplate, chat_template, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Structify) -> None:
        with client.admin.chat_templates.with_streaming_response.update(
            template_id="template_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat_template = response.parse()
            assert_matches_type(ChatTemplate, chat_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            client.admin.chat_templates.with_raw_response.update(
                template_id="",
            )

    @parametrize
    def test_method_list(self, client: Structify) -> None:
        chat_template = client.admin.chat_templates.list()
        assert_matches_type(ChatTemplateListResponse, chat_template, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Structify) -> None:
        chat_template = client.admin.chat_templates.list(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ChatTemplateListResponse, chat_template, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Structify) -> None:
        response = client.admin.chat_templates.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat_template = response.parse()
        assert_matches_type(ChatTemplateListResponse, chat_template, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Structify) -> None:
        with client.admin.chat_templates.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat_template = response.parse()
            assert_matches_type(ChatTemplateListResponse, chat_template, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncChatTemplates:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncStructify) -> None:
        chat_template = await async_client.admin.chat_templates.create(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            display_order=0,
            image_url="image_url",
            is_active=True,
            title="title",
        )
        assert_matches_type(ChatTemplate, chat_template, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.chat_templates.with_raw_response.create(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            display_order=0,
            image_url="image_url",
            is_active=True,
            title="title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat_template = await response.parse()
        assert_matches_type(ChatTemplate, chat_template, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.chat_templates.with_streaming_response.create(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            display_order=0,
            image_url="image_url",
            is_active=True,
            title="title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat_template = await response.parse()
            assert_matches_type(ChatTemplate, chat_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncStructify) -> None:
        chat_template = await async_client.admin.chat_templates.update(
            template_id="template_id",
        )
        assert_matches_type(ChatTemplate, chat_template, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncStructify) -> None:
        chat_template = await async_client.admin.chat_templates.update(
            template_id="template_id",
            description="description",
            display_order=0,
            image_url="image_url",
            is_active=True,
            title="title",
            updated_by="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ChatTemplate, chat_template, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.chat_templates.with_raw_response.update(
            template_id="template_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat_template = await response.parse()
        assert_matches_type(ChatTemplate, chat_template, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.chat_templates.with_streaming_response.update(
            template_id="template_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat_template = await response.parse()
            assert_matches_type(ChatTemplate, chat_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            await async_client.admin.chat_templates.with_raw_response.update(
                template_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncStructify) -> None:
        chat_template = await async_client.admin.chat_templates.list()
        assert_matches_type(ChatTemplateListResponse, chat_template, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncStructify) -> None:
        chat_template = await async_client.admin.chat_templates.list(
            chat_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ChatTemplateListResponse, chat_template, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.chat_templates.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat_template = await response.parse()
        assert_matches_type(ChatTemplateListResponse, chat_template, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.chat_templates.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat_template = await response.parse()
            assert_matches_type(ChatTemplateListResponse, chat_template, path=["response"])

        assert cast(Any, response.is_closed) is True
