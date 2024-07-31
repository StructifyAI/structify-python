# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Dict, Union, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import resources, _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, StructifyError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "resources",
    "Structify",
    "AsyncStructify",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "production": "https://api.structify.ai",
    "deployment": "http://localhost:8080",
}


class Structify(SyncAPIClient):
    user: resources.UserResource
    admin: resources.AdminResource
    datasets: resources.DatasetsResource
    documents: resources.DocumentsResource
    runs: resources.RunsResource
    server: resources.ServerResource
    sources: resources.SourcesResource
    structure: resources.StructureResource
    usage: resources.UsageResource
    with_raw_response: StructifyWithRawResponse
    with_streaming_response: StructifyWithStreamedResponse

    # client options
    api_key: str

    _environment: Literal["production", "deployment"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "deployment"] | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | None | NotGiven = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous structify client instance.

        This automatically infers the `api_key` argument from the `STRUCTIFY_API_TOKEN` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("STRUCTIFY_API_TOKEN")
        if api_key is None:
            raise StructifyError(
                "The api_key client option must be set either by passing api_key to the client or by setting the STRUCTIFY_API_TOKEN environment variable"
            )
        self.api_key = api_key

        self._environment = environment

        base_url_env = os.environ.get("STRUCTIFY_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `STRUCTIFY_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.user = resources.UserResource(self)
        self.admin = resources.AdminResource(self)
        self.datasets = resources.DatasetsResource(self)
        self.documents = resources.DocumentsResource(self)
        self.runs = resources.RunsResource(self)
        self.server = resources.ServerResource(self)
        self.sources = resources.SourcesResource(self)
        self.structure = resources.StructureResource(self)
        self.usage = resources.UsageResource(self)
        self.with_raw_response = StructifyWithRawResponse(self)
        self.with_streaming_response = StructifyWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"api_key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "deployment"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncStructify(AsyncAPIClient):
    user: resources.AsyncUserResource
    admin: resources.AsyncAdminResource
    datasets: resources.AsyncDatasetsResource
    documents: resources.AsyncDocumentsResource
    runs: resources.AsyncRunsResource
    server: resources.AsyncServerResource
    sources: resources.AsyncSourcesResource
    structure: resources.AsyncStructureResource
    usage: resources.AsyncUsageResource
    with_raw_response: AsyncStructifyWithRawResponse
    with_streaming_response: AsyncStructifyWithStreamedResponse

    # client options
    api_key: str

    _environment: Literal["production", "deployment"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "deployment"] | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | None | NotGiven = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async structify client instance.

        This automatically infers the `api_key` argument from the `STRUCTIFY_API_TOKEN` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("STRUCTIFY_API_TOKEN")
        if api_key is None:
            raise StructifyError(
                "The api_key client option must be set either by passing api_key to the client or by setting the STRUCTIFY_API_TOKEN environment variable"
            )
        self.api_key = api_key

        self._environment = environment

        base_url_env = os.environ.get("STRUCTIFY_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `STRUCTIFY_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.user = resources.AsyncUserResource(self)
        self.admin = resources.AsyncAdminResource(self)
        self.datasets = resources.AsyncDatasetsResource(self)
        self.documents = resources.AsyncDocumentsResource(self)
        self.runs = resources.AsyncRunsResource(self)
        self.server = resources.AsyncServerResource(self)
        self.sources = resources.AsyncSourcesResource(self)
        self.structure = resources.AsyncStructureResource(self)
        self.usage = resources.AsyncUsageResource(self)
        self.with_raw_response = AsyncStructifyWithRawResponse(self)
        self.with_streaming_response = AsyncStructifyWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"api_key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "deployment"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class StructifyWithRawResponse:
    def __init__(self, client: Structify) -> None:
        self.user = resources.UserResourceWithRawResponse(client.user)
        self.admin = resources.AdminResourceWithRawResponse(client.admin)
        self.datasets = resources.DatasetsResourceWithRawResponse(client.datasets)
        self.documents = resources.DocumentsResourceWithRawResponse(client.documents)
        self.runs = resources.RunsResourceWithRawResponse(client.runs)
        self.server = resources.ServerResourceWithRawResponse(client.server)
        self.sources = resources.SourcesResourceWithRawResponse(client.sources)
        self.structure = resources.StructureResourceWithRawResponse(client.structure)
        self.usage = resources.UsageResourceWithRawResponse(client.usage)


class AsyncStructifyWithRawResponse:
    def __init__(self, client: AsyncStructify) -> None:
        self.user = resources.AsyncUserResourceWithRawResponse(client.user)
        self.admin = resources.AsyncAdminResourceWithRawResponse(client.admin)
        self.datasets = resources.AsyncDatasetsResourceWithRawResponse(client.datasets)
        self.documents = resources.AsyncDocumentsResourceWithRawResponse(client.documents)
        self.runs = resources.AsyncRunsResourceWithRawResponse(client.runs)
        self.server = resources.AsyncServerResourceWithRawResponse(client.server)
        self.sources = resources.AsyncSourcesResourceWithRawResponse(client.sources)
        self.structure = resources.AsyncStructureResourceWithRawResponse(client.structure)
        self.usage = resources.AsyncUsageResourceWithRawResponse(client.usage)


class StructifyWithStreamedResponse:
    def __init__(self, client: Structify) -> None:
        self.user = resources.UserResourceWithStreamingResponse(client.user)
        self.admin = resources.AdminResourceWithStreamingResponse(client.admin)
        self.datasets = resources.DatasetsResourceWithStreamingResponse(client.datasets)
        self.documents = resources.DocumentsResourceWithStreamingResponse(client.documents)
        self.runs = resources.RunsResourceWithStreamingResponse(client.runs)
        self.server = resources.ServerResourceWithStreamingResponse(client.server)
        self.sources = resources.SourcesResourceWithStreamingResponse(client.sources)
        self.structure = resources.StructureResourceWithStreamingResponse(client.structure)
        self.usage = resources.UsageResourceWithStreamingResponse(client.usage)


class AsyncStructifyWithStreamedResponse:
    def __init__(self, client: AsyncStructify) -> None:
        self.user = resources.AsyncUserResourceWithStreamingResponse(client.user)
        self.admin = resources.AsyncAdminResourceWithStreamingResponse(client.admin)
        self.datasets = resources.AsyncDatasetsResourceWithStreamingResponse(client.datasets)
        self.documents = resources.AsyncDocumentsResourceWithStreamingResponse(client.documents)
        self.runs = resources.AsyncRunsResourceWithStreamingResponse(client.runs)
        self.server = resources.AsyncServerResourceWithStreamingResponse(client.server)
        self.sources = resources.AsyncSourcesResourceWithStreamingResponse(client.sources)
        self.structure = resources.AsyncStructureResourceWithStreamingResponse(client.structure)
        self.usage = resources.AsyncUsageResourceWithStreamingResponse(client.usage)


Client = Structify

AsyncClient = AsyncStructify
