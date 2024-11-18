# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .users import (
    UsersResource,
    AsyncUsersResource,
    UsersResourceWithRawResponse,
    AsyncUsersResourceWithRawResponse,
    UsersResourceWithStreamingResponse,
    AsyncUsersResourceWithStreamingResponse,
)
from .entity import (
    EntityResource,
    AsyncEntityResource,
    EntityResourceWithRawResponse,
    AsyncEntityResourceWithRawResponse,
    EntityResourceWithStreamingResponse,
    AsyncEntityResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .human_llm import (
    HumanLlmResource,
    AsyncHumanLlmResource,
    HumanLlmResourceWithRawResponse,
    AsyncHumanLlmResourceWithRawResponse,
    HumanLlmResourceWithStreamingResponse,
    AsyncHumanLlmResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .training_datasets import (
    TrainingDatasetsResource,
    AsyncTrainingDatasetsResource,
    TrainingDatasetsResourceWithRawResponse,
    AsyncTrainingDatasetsResourceWithRawResponse,
    TrainingDatasetsResourceWithStreamingResponse,
    AsyncTrainingDatasetsResourceWithStreamingResponse,
)

__all__ = ["AdminResource", "AsyncAdminResource"]


class AdminResource(SyncAPIResource):
    @cached_property
    def entity(self) -> EntityResource:
        return EntityResource(self._client)

    @cached_property
    def human_llm(self) -> HumanLlmResource:
        return HumanLlmResource(self._client)

    @cached_property
    def users(self) -> UsersResource:
        return UsersResource(self._client)

    @cached_property
    def training_datasets(self) -> TrainingDatasetsResource:
        return TrainingDatasetsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AdminResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return AdminResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AdminResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return AdminResourceWithStreamingResponse(self)


class AsyncAdminResource(AsyncAPIResource):
    @cached_property
    def entity(self) -> AsyncEntityResource:
        return AsyncEntityResource(self._client)

    @cached_property
    def human_llm(self) -> AsyncHumanLlmResource:
        return AsyncHumanLlmResource(self._client)

    @cached_property
    def users(self) -> AsyncUsersResource:
        return AsyncUsersResource(self._client)

    @cached_property
    def training_datasets(self) -> AsyncTrainingDatasetsResource:
        return AsyncTrainingDatasetsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAdminResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAdminResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAdminResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return AsyncAdminResourceWithStreamingResponse(self)


class AdminResourceWithRawResponse:
    def __init__(self, admin: AdminResource) -> None:
        self._admin = admin

    @cached_property
    def entity(self) -> EntityResourceWithRawResponse:
        return EntityResourceWithRawResponse(self._admin.entity)

    @cached_property
    def human_llm(self) -> HumanLlmResourceWithRawResponse:
        return HumanLlmResourceWithRawResponse(self._admin.human_llm)

    @cached_property
    def users(self) -> UsersResourceWithRawResponse:
        return UsersResourceWithRawResponse(self._admin.users)

    @cached_property
    def training_datasets(self) -> TrainingDatasetsResourceWithRawResponse:
        return TrainingDatasetsResourceWithRawResponse(self._admin.training_datasets)


class AsyncAdminResourceWithRawResponse:
    def __init__(self, admin: AsyncAdminResource) -> None:
        self._admin = admin

    @cached_property
    def entity(self) -> AsyncEntityResourceWithRawResponse:
        return AsyncEntityResourceWithRawResponse(self._admin.entity)

    @cached_property
    def human_llm(self) -> AsyncHumanLlmResourceWithRawResponse:
        return AsyncHumanLlmResourceWithRawResponse(self._admin.human_llm)

    @cached_property
    def users(self) -> AsyncUsersResourceWithRawResponse:
        return AsyncUsersResourceWithRawResponse(self._admin.users)

    @cached_property
    def training_datasets(self) -> AsyncTrainingDatasetsResourceWithRawResponse:
        return AsyncTrainingDatasetsResourceWithRawResponse(self._admin.training_datasets)


class AdminResourceWithStreamingResponse:
    def __init__(self, admin: AdminResource) -> None:
        self._admin = admin

    @cached_property
    def entity(self) -> EntityResourceWithStreamingResponse:
        return EntityResourceWithStreamingResponse(self._admin.entity)

    @cached_property
    def human_llm(self) -> HumanLlmResourceWithStreamingResponse:
        return HumanLlmResourceWithStreamingResponse(self._admin.human_llm)

    @cached_property
    def users(self) -> UsersResourceWithStreamingResponse:
        return UsersResourceWithStreamingResponse(self._admin.users)

    @cached_property
    def training_datasets(self) -> TrainingDatasetsResourceWithStreamingResponse:
        return TrainingDatasetsResourceWithStreamingResponse(self._admin.training_datasets)


class AsyncAdminResourceWithStreamingResponse:
    def __init__(self, admin: AsyncAdminResource) -> None:
        self._admin = admin

    @cached_property
    def entity(self) -> AsyncEntityResourceWithStreamingResponse:
        return AsyncEntityResourceWithStreamingResponse(self._admin.entity)

    @cached_property
    def human_llm(self) -> AsyncHumanLlmResourceWithStreamingResponse:
        return AsyncHumanLlmResourceWithStreamingResponse(self._admin.human_llm)

    @cached_property
    def users(self) -> AsyncUsersResourceWithStreamingResponse:
        return AsyncUsersResourceWithStreamingResponse(self._admin.users)

    @cached_property
    def training_datasets(self) -> AsyncTrainingDatasetsResourceWithStreamingResponse:
        return AsyncTrainingDatasetsResourceWithStreamingResponse(self._admin.training_datasets)
