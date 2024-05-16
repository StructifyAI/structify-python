# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types import (
    LabelLlmAssistResponse,
    LabelGetMessagesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLabel:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_messages(self, client: Structify) -> None:
        label = client.label.get_messages()
        assert_matches_type(Optional[LabelGetMessagesResponse], label, path=["response"])

    @parametrize
    def test_method_get_messages_with_all_params(self, client: Structify) -> None:
        label = client.label.get_messages(
            uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Optional[LabelGetMessagesResponse], label, path=["response"])

    @parametrize
    def test_raw_response_get_messages(self, client: Structify) -> None:
        response = client.label.with_raw_response.get_messages()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = response.parse()
        assert_matches_type(Optional[LabelGetMessagesResponse], label, path=["response"])

    @parametrize
    def test_streaming_response_get_messages(self, client: Structify) -> None:
        with client.label.with_streaming_response.get_messages() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = response.parse()
            assert_matches_type(Optional[LabelGetMessagesResponse], label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_llm_assist(self, client: Structify) -> None:
        label = client.label.llm_assist(
            decoding_params={"parameters": [{"max_tokens": 0}, {"max_tokens": 0}, {"max_tokens": 0}]},
            messages=[
                {
                    "content": [{"text": "string"}, {"text": "string"}, {"text": "string"}],
                    "role": "user",
                },
                {
                    "content": [{"text": "string"}, {"text": "string"}, {"text": "string"}],
                    "role": "user",
                },
                {
                    "content": [{"text": "string"}, {"text": "string"}, {"text": "string"}],
                    "role": "user",
                },
            ],
        )
        assert_matches_type(Optional[LabelLlmAssistResponse], label, path=["response"])

    @parametrize
    def test_method_llm_assist_with_all_params(self, client: Structify) -> None:
        label = client.label.llm_assist(
            decoding_params={"parameters": [{"max_tokens": 0}, {"max_tokens": 0}, {"max_tokens": 0}]},
            messages=[
                {
                    "content": [{"text": "string"}, {"text": "string"}, {"text": "string"}],
                    "role": "user",
                },
                {
                    "content": [{"text": "string"}, {"text": "string"}, {"text": "string"}],
                    "role": "user",
                },
                {
                    "content": [{"text": "string"}, {"text": "string"}, {"text": "string"}],
                    "role": "user",
                },
            ],
            metadata={
                "conditioning_prompt": "string",
                "dataset_descriptor": {
                    "description": "string",
                    "name": "string",
                    "tables": [
                        {
                            "description": "string",
                            "name": "string",
                            "properties": [
                                {
                                    "description": "string",
                                    "name": "string",
                                },
                                {
                                    "description": "string",
                                    "name": "string",
                                },
                                {
                                    "description": "string",
                                    "name": "string",
                                },
                            ],
                            "relationships": [
                                {
                                    "description": "string",
                                    "name": "string",
                                },
                                {
                                    "description": "string",
                                    "name": "string",
                                },
                                {
                                    "description": "string",
                                    "name": "string",
                                },
                            ],
                        },
                        {
                            "description": "string",
                            "name": "string",
                            "properties": [
                                {
                                    "description": "string",
                                    "name": "string",
                                },
                                {
                                    "description": "string",
                                    "name": "string",
                                },
                                {
                                    "description": "string",
                                    "name": "string",
                                },
                            ],
                            "relationships": [
                                {
                                    "description": "string",
                                    "name": "string",
                                },
                                {
                                    "description": "string",
                                    "name": "string",
                                },
                                {
                                    "description": "string",
                                    "name": "string",
                                },
                            ],
                        },
                        {
                            "description": "string",
                            "name": "string",
                            "properties": [
                                {
                                    "description": "string",
                                    "name": "string",
                                },
                                {
                                    "description": "string",
                                    "name": "string",
                                },
                                {
                                    "description": "string",
                                    "name": "string",
                                },
                            ],
                            "relationships": [
                                {
                                    "description": "string",
                                    "name": "string",
                                },
                                {
                                    "description": "string",
                                    "name": "string",
                                },
                                {
                                    "description": "string",
                                    "name": "string",
                                },
                            ],
                        },
                    ],
                },
                "extracted_entities": [
                    {
                        "entities": [
                            {
                                "id": 0,
                                "properties": {"foo": "string"},
                                "type": "string",
                            },
                            {
                                "id": 0,
                                "properties": {"foo": "string"},
                                "type": "string",
                            },
                            {
                                "id": 0,
                                "properties": {"foo": "string"},
                                "type": "string",
                            },
                        ],
                        "relationships": [
                            {
                                "source": 0,
                                "target": 0,
                                "type": "string",
                            },
                            {
                                "source": 0,
                                "target": 0,
                                "type": "string",
                            },
                            {
                                "source": 0,
                                "target": 0,
                                "type": "string",
                            },
                        ],
                    },
                    {
                        "entities": [
                            {
                                "id": 0,
                                "properties": {"foo": "string"},
                                "type": "string",
                            },
                            {
                                "id": 0,
                                "properties": {"foo": "string"},
                                "type": "string",
                            },
                            {
                                "id": 0,
                                "properties": {"foo": "string"},
                                "type": "string",
                            },
                        ],
                        "relationships": [
                            {
                                "source": 0,
                                "target": 0,
                                "type": "string",
                            },
                            {
                                "source": 0,
                                "target": 0,
                                "type": "string",
                            },
                            {
                                "source": 0,
                                "target": 0,
                                "type": "string",
                            },
                        ],
                    },
                    {
                        "entities": [
                            {
                                "id": 0,
                                "properties": {"foo": "string"},
                                "type": "string",
                            },
                            {
                                "id": 0,
                                "properties": {"foo": "string"},
                                "type": "string",
                            },
                            {
                                "id": 0,
                                "properties": {"foo": "string"},
                                "type": "string",
                            },
                        ],
                        "relationships": [
                            {
                                "source": 0,
                                "target": 0,
                                "type": "string",
                            },
                            {
                                "source": 0,
                                "target": 0,
                                "type": "string",
                            },
                            {
                                "source": 0,
                                "target": 0,
                                "type": "string",
                            },
                        ],
                    },
                ],
                "tool_metadata": [
                    {
                        "description": "string",
                        "name": "Save",
                        "regex_validator": "string",
                        "tool_validator": {},
                    },
                    {
                        "description": "string",
                        "name": "Save",
                        "regex_validator": "string",
                        "tool_validator": {},
                    },
                    {
                        "description": "string",
                        "name": "Save",
                        "regex_validator": "string",
                        "tool_validator": {},
                    },
                ],
                "web_flags": [
                    {
                        "aria_label": "string",
                        "text": "string",
                        "type": "string",
                        "x": 0,
                        "y": 0,
                    },
                    {
                        "aria_label": "string",
                        "text": "string",
                        "type": "string",
                        "x": 0,
                        "y": 0,
                    },
                    {
                        "aria_label": "string",
                        "text": "string",
                        "type": "string",
                        "x": 0,
                        "y": 0,
                    },
                ],
            },
        )
        assert_matches_type(Optional[LabelLlmAssistResponse], label, path=["response"])

    @parametrize
    def test_raw_response_llm_assist(self, client: Structify) -> None:
        response = client.label.with_raw_response.llm_assist(
            decoding_params={"parameters": [{"max_tokens": 0}, {"max_tokens": 0}, {"max_tokens": 0}]},
            messages=[
                {
                    "content": [{"text": "string"}, {"text": "string"}, {"text": "string"}],
                    "role": "user",
                },
                {
                    "content": [{"text": "string"}, {"text": "string"}, {"text": "string"}],
                    "role": "user",
                },
                {
                    "content": [{"text": "string"}, {"text": "string"}, {"text": "string"}],
                    "role": "user",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = response.parse()
        assert_matches_type(Optional[LabelLlmAssistResponse], label, path=["response"])

    @parametrize
    def test_streaming_response_llm_assist(self, client: Structify) -> None:
        with client.label.with_streaming_response.llm_assist(
            decoding_params={"parameters": [{"max_tokens": 0}, {"max_tokens": 0}, {"max_tokens": 0}]},
            messages=[
                {
                    "content": [{"text": "string"}, {"text": "string"}, {"text": "string"}],
                    "role": "user",
                },
                {
                    "content": [{"text": "string"}, {"text": "string"}, {"text": "string"}],
                    "role": "user",
                },
                {
                    "content": [{"text": "string"}, {"text": "string"}, {"text": "string"}],
                    "role": "user",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = response.parse()
            assert_matches_type(Optional[LabelLlmAssistResponse], label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_run_overload_1(self, client: Structify) -> None:
        label = client.label.run(
            dataset_name="string",
            text={"text_content": "string"},
        )
        assert label is None

    @parametrize
    def test_method_run_with_all_params_overload_1(self, client: Structify) -> None:
        label = client.label.run(
            dataset_name="string",
            text={"text_content": "string"},
            custom_instruction="string",
        )
        assert label is None

    @parametrize
    def test_raw_response_run_overload_1(self, client: Structify) -> None:
        response = client.label.with_raw_response.run(
            dataset_name="string",
            text={"text_content": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = response.parse()
        assert label is None

    @parametrize
    def test_streaming_response_run_overload_1(self, client: Structify) -> None:
        with client.label.with_streaming_response.run(
            dataset_name="string",
            text={"text_content": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = response.parse()
            assert label is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_run_overload_2(self, client: Structify) -> None:
        label = client.label.run(
            dataset_name="string",
            document={"path": "string"},
        )
        assert label is None

    @parametrize
    def test_method_run_with_all_params_overload_2(self, client: Structify) -> None:
        label = client.label.run(
            dataset_name="string",
            document={"path": "string"},
            custom_instruction="string",
        )
        assert label is None

    @parametrize
    def test_raw_response_run_overload_2(self, client: Structify) -> None:
        response = client.label.with_raw_response.run(
            dataset_name="string",
            document={"path": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = response.parse()
        assert label is None

    @parametrize
    def test_streaming_response_run_overload_2(self, client: Structify) -> None:
        with client.label.with_streaming_response.run(
            dataset_name="string",
            document={"path": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = response.parse()
            assert label is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_run_overload_3(self, client: Structify) -> None:
        label = client.label.run(
            dataset_name="string",
            web={"phrase": "string"},
        )
        assert label is None

    @parametrize
    def test_method_run_with_all_params_overload_3(self, client: Structify) -> None:
        label = client.label.run(
            dataset_name="string",
            web={
                "phrase": "string",
                "starting_website": "string",
            },
            custom_instruction="string",
        )
        assert label is None

    @parametrize
    def test_raw_response_run_overload_3(self, client: Structify) -> None:
        response = client.label.with_raw_response.run(
            dataset_name="string",
            web={"phrase": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = response.parse()
        assert label is None

    @parametrize
    def test_streaming_response_run_overload_3(self, client: Structify) -> None:
        with client.label.with_streaming_response.run(
            dataset_name="string",
            web={"phrase": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = response.parse()
            assert label is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_run_overload_4(self, client: Structify) -> None:
        label = client.label.run(
            dataset_name="string",
            sec_filing={},
        )
        assert label is None

    @parametrize
    def test_method_run_with_all_params_overload_4(self, client: Structify) -> None:
        label = client.label.run(
            dataset_name="string",
            sec_filing={
                "accession_number": "string",
                "quarter": 0,
                "year": 0,
            },
            custom_instruction="string",
        )
        assert label is None

    @parametrize
    def test_raw_response_run_overload_4(self, client: Structify) -> None:
        response = client.label.with_raw_response.run(
            dataset_name="string",
            sec_filing={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = response.parse()
        assert label is None

    @parametrize
    def test_streaming_response_run_overload_4(self, client: Structify) -> None:
        with client.label.with_streaming_response.run(
            dataset_name="string",
            sec_filing={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = response.parse()
            assert label is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_submit(self, client: Structify) -> None:
        label = client.label.submit(
            "string",
            body=[{"save": {}}, {"save": {}}, {"save": {}}],
        )
        assert_matches_type(str, label, path=["response"])

    @parametrize
    def test_raw_response_submit(self, client: Structify) -> None:
        response = client.label.with_raw_response.submit(
            "string",
            body=[{"save": {}}, {"save": {}}, {"save": {}}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = response.parse()
        assert_matches_type(str, label, path=["response"])

    @parametrize
    def test_streaming_response_submit(self, client: Structify) -> None:
        with client.label.with_streaming_response.submit(
            "string",
            body=[{"save": {}}, {"save": {}}, {"save": {}}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = response.parse()
            assert_matches_type(str, label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_submit(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.label.with_raw_response.submit(
                "",
                body=[{"save": {}}, {"save": {}}, {"save": {}}],
            )


class TestAsyncLabel:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get_messages(self, async_client: AsyncStructify) -> None:
        label = await async_client.label.get_messages()
        assert_matches_type(Optional[LabelGetMessagesResponse], label, path=["response"])

    @parametrize
    async def test_method_get_messages_with_all_params(self, async_client: AsyncStructify) -> None:
        label = await async_client.label.get_messages(
            uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Optional[LabelGetMessagesResponse], label, path=["response"])

    @parametrize
    async def test_raw_response_get_messages(self, async_client: AsyncStructify) -> None:
        response = await async_client.label.with_raw_response.get_messages()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = await response.parse()
        assert_matches_type(Optional[LabelGetMessagesResponse], label, path=["response"])

    @parametrize
    async def test_streaming_response_get_messages(self, async_client: AsyncStructify) -> None:
        async with async_client.label.with_streaming_response.get_messages() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = await response.parse()
            assert_matches_type(Optional[LabelGetMessagesResponse], label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_llm_assist(self, async_client: AsyncStructify) -> None:
        label = await async_client.label.llm_assist(
            decoding_params={"parameters": [{"max_tokens": 0}, {"max_tokens": 0}, {"max_tokens": 0}]},
            messages=[
                {
                    "content": [{"text": "string"}, {"text": "string"}, {"text": "string"}],
                    "role": "user",
                },
                {
                    "content": [{"text": "string"}, {"text": "string"}, {"text": "string"}],
                    "role": "user",
                },
                {
                    "content": [{"text": "string"}, {"text": "string"}, {"text": "string"}],
                    "role": "user",
                },
            ],
        )
        assert_matches_type(Optional[LabelLlmAssistResponse], label, path=["response"])

    @parametrize
    async def test_method_llm_assist_with_all_params(self, async_client: AsyncStructify) -> None:
        label = await async_client.label.llm_assist(
            decoding_params={"parameters": [{"max_tokens": 0}, {"max_tokens": 0}, {"max_tokens": 0}]},
            messages=[
                {
                    "content": [{"text": "string"}, {"text": "string"}, {"text": "string"}],
                    "role": "user",
                },
                {
                    "content": [{"text": "string"}, {"text": "string"}, {"text": "string"}],
                    "role": "user",
                },
                {
                    "content": [{"text": "string"}, {"text": "string"}, {"text": "string"}],
                    "role": "user",
                },
            ],
            metadata={
                "conditioning_prompt": "string",
                "dataset_descriptor": {
                    "description": "string",
                    "name": "string",
                    "tables": [
                        {
                            "description": "string",
                            "name": "string",
                            "properties": [
                                {
                                    "description": "string",
                                    "name": "string",
                                },
                                {
                                    "description": "string",
                                    "name": "string",
                                },
                                {
                                    "description": "string",
                                    "name": "string",
                                },
                            ],
                            "relationships": [
                                {
                                    "description": "string",
                                    "name": "string",
                                },
                                {
                                    "description": "string",
                                    "name": "string",
                                },
                                {
                                    "description": "string",
                                    "name": "string",
                                },
                            ],
                        },
                        {
                            "description": "string",
                            "name": "string",
                            "properties": [
                                {
                                    "description": "string",
                                    "name": "string",
                                },
                                {
                                    "description": "string",
                                    "name": "string",
                                },
                                {
                                    "description": "string",
                                    "name": "string",
                                },
                            ],
                            "relationships": [
                                {
                                    "description": "string",
                                    "name": "string",
                                },
                                {
                                    "description": "string",
                                    "name": "string",
                                },
                                {
                                    "description": "string",
                                    "name": "string",
                                },
                            ],
                        },
                        {
                            "description": "string",
                            "name": "string",
                            "properties": [
                                {
                                    "description": "string",
                                    "name": "string",
                                },
                                {
                                    "description": "string",
                                    "name": "string",
                                },
                                {
                                    "description": "string",
                                    "name": "string",
                                },
                            ],
                            "relationships": [
                                {
                                    "description": "string",
                                    "name": "string",
                                },
                                {
                                    "description": "string",
                                    "name": "string",
                                },
                                {
                                    "description": "string",
                                    "name": "string",
                                },
                            ],
                        },
                    ],
                },
                "extracted_entities": [
                    {
                        "entities": [
                            {
                                "id": 0,
                                "properties": {"foo": "string"},
                                "type": "string",
                            },
                            {
                                "id": 0,
                                "properties": {"foo": "string"},
                                "type": "string",
                            },
                            {
                                "id": 0,
                                "properties": {"foo": "string"},
                                "type": "string",
                            },
                        ],
                        "relationships": [
                            {
                                "source": 0,
                                "target": 0,
                                "type": "string",
                            },
                            {
                                "source": 0,
                                "target": 0,
                                "type": "string",
                            },
                            {
                                "source": 0,
                                "target": 0,
                                "type": "string",
                            },
                        ],
                    },
                    {
                        "entities": [
                            {
                                "id": 0,
                                "properties": {"foo": "string"},
                                "type": "string",
                            },
                            {
                                "id": 0,
                                "properties": {"foo": "string"},
                                "type": "string",
                            },
                            {
                                "id": 0,
                                "properties": {"foo": "string"},
                                "type": "string",
                            },
                        ],
                        "relationships": [
                            {
                                "source": 0,
                                "target": 0,
                                "type": "string",
                            },
                            {
                                "source": 0,
                                "target": 0,
                                "type": "string",
                            },
                            {
                                "source": 0,
                                "target": 0,
                                "type": "string",
                            },
                        ],
                    },
                    {
                        "entities": [
                            {
                                "id": 0,
                                "properties": {"foo": "string"},
                                "type": "string",
                            },
                            {
                                "id": 0,
                                "properties": {"foo": "string"},
                                "type": "string",
                            },
                            {
                                "id": 0,
                                "properties": {"foo": "string"},
                                "type": "string",
                            },
                        ],
                        "relationships": [
                            {
                                "source": 0,
                                "target": 0,
                                "type": "string",
                            },
                            {
                                "source": 0,
                                "target": 0,
                                "type": "string",
                            },
                            {
                                "source": 0,
                                "target": 0,
                                "type": "string",
                            },
                        ],
                    },
                ],
                "tool_metadata": [
                    {
                        "description": "string",
                        "name": "Save",
                        "regex_validator": "string",
                        "tool_validator": {},
                    },
                    {
                        "description": "string",
                        "name": "Save",
                        "regex_validator": "string",
                        "tool_validator": {},
                    },
                    {
                        "description": "string",
                        "name": "Save",
                        "regex_validator": "string",
                        "tool_validator": {},
                    },
                ],
                "web_flags": [
                    {
                        "aria_label": "string",
                        "text": "string",
                        "type": "string",
                        "x": 0,
                        "y": 0,
                    },
                    {
                        "aria_label": "string",
                        "text": "string",
                        "type": "string",
                        "x": 0,
                        "y": 0,
                    },
                    {
                        "aria_label": "string",
                        "text": "string",
                        "type": "string",
                        "x": 0,
                        "y": 0,
                    },
                ],
            },
        )
        assert_matches_type(Optional[LabelLlmAssistResponse], label, path=["response"])

    @parametrize
    async def test_raw_response_llm_assist(self, async_client: AsyncStructify) -> None:
        response = await async_client.label.with_raw_response.llm_assist(
            decoding_params={"parameters": [{"max_tokens": 0}, {"max_tokens": 0}, {"max_tokens": 0}]},
            messages=[
                {
                    "content": [{"text": "string"}, {"text": "string"}, {"text": "string"}],
                    "role": "user",
                },
                {
                    "content": [{"text": "string"}, {"text": "string"}, {"text": "string"}],
                    "role": "user",
                },
                {
                    "content": [{"text": "string"}, {"text": "string"}, {"text": "string"}],
                    "role": "user",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = await response.parse()
        assert_matches_type(Optional[LabelLlmAssistResponse], label, path=["response"])

    @parametrize
    async def test_streaming_response_llm_assist(self, async_client: AsyncStructify) -> None:
        async with async_client.label.with_streaming_response.llm_assist(
            decoding_params={"parameters": [{"max_tokens": 0}, {"max_tokens": 0}, {"max_tokens": 0}]},
            messages=[
                {
                    "content": [{"text": "string"}, {"text": "string"}, {"text": "string"}],
                    "role": "user",
                },
                {
                    "content": [{"text": "string"}, {"text": "string"}, {"text": "string"}],
                    "role": "user",
                },
                {
                    "content": [{"text": "string"}, {"text": "string"}, {"text": "string"}],
                    "role": "user",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = await response.parse()
            assert_matches_type(Optional[LabelLlmAssistResponse], label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_run_overload_1(self, async_client: AsyncStructify) -> None:
        label = await async_client.label.run(
            dataset_name="string",
            text={"text_content": "string"},
        )
        assert label is None

    @parametrize
    async def test_method_run_with_all_params_overload_1(self, async_client: AsyncStructify) -> None:
        label = await async_client.label.run(
            dataset_name="string",
            text={"text_content": "string"},
            custom_instruction="string",
        )
        assert label is None

    @parametrize
    async def test_raw_response_run_overload_1(self, async_client: AsyncStructify) -> None:
        response = await async_client.label.with_raw_response.run(
            dataset_name="string",
            text={"text_content": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = await response.parse()
        assert label is None

    @parametrize
    async def test_streaming_response_run_overload_1(self, async_client: AsyncStructify) -> None:
        async with async_client.label.with_streaming_response.run(
            dataset_name="string",
            text={"text_content": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = await response.parse()
            assert label is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_run_overload_2(self, async_client: AsyncStructify) -> None:
        label = await async_client.label.run(
            dataset_name="string",
            document={"path": "string"},
        )
        assert label is None

    @parametrize
    async def test_method_run_with_all_params_overload_2(self, async_client: AsyncStructify) -> None:
        label = await async_client.label.run(
            dataset_name="string",
            document={"path": "string"},
            custom_instruction="string",
        )
        assert label is None

    @parametrize
    async def test_raw_response_run_overload_2(self, async_client: AsyncStructify) -> None:
        response = await async_client.label.with_raw_response.run(
            dataset_name="string",
            document={"path": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = await response.parse()
        assert label is None

    @parametrize
    async def test_streaming_response_run_overload_2(self, async_client: AsyncStructify) -> None:
        async with async_client.label.with_streaming_response.run(
            dataset_name="string",
            document={"path": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = await response.parse()
            assert label is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_run_overload_3(self, async_client: AsyncStructify) -> None:
        label = await async_client.label.run(
            dataset_name="string",
            web={"phrase": "string"},
        )
        assert label is None

    @parametrize
    async def test_method_run_with_all_params_overload_3(self, async_client: AsyncStructify) -> None:
        label = await async_client.label.run(
            dataset_name="string",
            web={
                "phrase": "string",
                "starting_website": "string",
            },
            custom_instruction="string",
        )
        assert label is None

    @parametrize
    async def test_raw_response_run_overload_3(self, async_client: AsyncStructify) -> None:
        response = await async_client.label.with_raw_response.run(
            dataset_name="string",
            web={"phrase": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = await response.parse()
        assert label is None

    @parametrize
    async def test_streaming_response_run_overload_3(self, async_client: AsyncStructify) -> None:
        async with async_client.label.with_streaming_response.run(
            dataset_name="string",
            web={"phrase": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = await response.parse()
            assert label is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_run_overload_4(self, async_client: AsyncStructify) -> None:
        label = await async_client.label.run(
            dataset_name="string",
            sec_filing={},
        )
        assert label is None

    @parametrize
    async def test_method_run_with_all_params_overload_4(self, async_client: AsyncStructify) -> None:
        label = await async_client.label.run(
            dataset_name="string",
            sec_filing={
                "accession_number": "string",
                "quarter": 0,
                "year": 0,
            },
            custom_instruction="string",
        )
        assert label is None

    @parametrize
    async def test_raw_response_run_overload_4(self, async_client: AsyncStructify) -> None:
        response = await async_client.label.with_raw_response.run(
            dataset_name="string",
            sec_filing={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = await response.parse()
        assert label is None

    @parametrize
    async def test_streaming_response_run_overload_4(self, async_client: AsyncStructify) -> None:
        async with async_client.label.with_streaming_response.run(
            dataset_name="string",
            sec_filing={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = await response.parse()
            assert label is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_submit(self, async_client: AsyncStructify) -> None:
        label = await async_client.label.submit(
            "string",
            body=[{"save": {}}, {"save": {}}, {"save": {}}],
        )
        assert_matches_type(str, label, path=["response"])

    @parametrize
    async def test_raw_response_submit(self, async_client: AsyncStructify) -> None:
        response = await async_client.label.with_raw_response.submit(
            "string",
            body=[{"save": {}}, {"save": {}}, {"save": {}}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = await response.parse()
        assert_matches_type(str, label, path=["response"])

    @parametrize
    async def test_streaming_response_submit(self, async_client: AsyncStructify) -> None:
        async with async_client.label.with_streaming_response.submit(
            "string",
            body=[{"save": {}}, {"save": {}}, {"save": {}}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = await response.parse()
            assert_matches_type(str, label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_submit(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.label.with_raw_response.submit(
                "",
                body=[{"save": {}}, {"save": {}}, {"save": {}}],
            )
