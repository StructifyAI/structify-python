# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Dict, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        chat,
        code,
        jobs,
        user,
        wiki,
        admin,
        match,
        nango,
        slack,
        teams,
        polars,
        scrape,
        server,
        sandbox,
        sources,
        datasets,
        entities,
        external,
        projects,
        sessions,
        workflow,
        documents,
        structure,
        connectors,
        public_sessions,
        connector_catalog,
        workflow_schedule,
    )
    from .resources.chat import ChatResource, AsyncChatResource
    from .resources.code import CodeResource, AsyncCodeResource
    from .resources.jobs import JobsResource, AsyncJobsResource
    from .resources.wiki import WikiResource, AsyncWikiResource
    from .resources.match import MatchResource, AsyncMatchResource
    from .resources.nango import NangoResource, AsyncNangoResource
    from .resources.slack import SlackResource, AsyncSlackResource
    from .resources.teams import TeamsResource, AsyncTeamsResource
    from .resources.polars import PolarsResource
    from .resources.scrape import ScrapeResource, AsyncScrapeResource
    from .resources.server import ServerResource, AsyncServerResource
    from .resources.sandbox import SandboxResource, AsyncSandboxResource
    from .resources.sources import SourcesResource, AsyncSourcesResource
    from .resources.entities import EntitiesResource, AsyncEntitiesResource
    from .resources.projects import ProjectsResource, AsyncProjectsResource
    from .resources.sessions import SessionsResource, AsyncSessionsResource
    from .resources.workflow import WorkflowResource, AsyncWorkflowResource
    from .resources.documents import DocumentsResource, AsyncDocumentsResource
    from .resources.structure import StructureResource, AsyncStructureResource
    from .resources.user.user import UserResource, AsyncUserResource
    from .resources.admin.admin import AdminResource, AsyncAdminResource
    from .resources.public_sessions import PublicSessionsResource, AsyncPublicSessionsResource
    from .resources.datasets.datasets import DatasetsResource, AsyncDatasetsResource
    from .resources.external.external import ExternalResource, AsyncExternalResource
    from .resources.workflow_schedule import WorkflowScheduleResource, AsyncWorkflowScheduleResource
    from .resources.connectors.connectors import ConnectorsResource, AsyncConnectorsResource
    from .resources.connector_catalog.connector_catalog import ConnectorCatalogResource, AsyncConnectorCatalogResource

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Structify",
    "AsyncStructify",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "production": "https://api.structify.ai",
    "development": "http://localhost:8080",
}


class Structify(SyncAPIClient):
    # client options
    api_key: str | None
    session_token: str | None

    _environment: Literal["production", "development"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        session_token: str | None = None,
        environment: Literal["production", "development"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
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
        """Construct a new synchronous Structify client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `STRUCTIFY_API_TOKEN`
        - `session_token` from `STRUCTIFY_SESSION_TOKEN`
        """
        if api_key is None:
            api_key = os.environ.get("STRUCTIFY_API_TOKEN")
        self.api_key = api_key

        if session_token is None:
            session_token = os.environ.get("STRUCTIFY_SESSION_TOKEN")
        self.session_token = session_token

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

    @cached_property
    def user(self) -> UserResource:
        from .resources.user import UserResource

        return UserResource(self)

    @cached_property
    def chat(self) -> ChatResource:
        from .resources.chat import ChatResource

        return ChatResource(self)

    @cached_property
    def teams(self) -> TeamsResource:
        from .resources.teams import TeamsResource

        return TeamsResource(self)

    @cached_property
    def wiki(self) -> WikiResource:
        from .resources.wiki import WikiResource

        return WikiResource(self)

    @cached_property
    def polars(self) -> PolarsResource:
        from .resources.polars import PolarsResource

        return PolarsResource(self)

    @cached_property
    def projects(self) -> ProjectsResource:
        from .resources.projects import ProjectsResource

        return ProjectsResource(self)

    @cached_property
    def admin(self) -> AdminResource:
        from .resources.admin import AdminResource

        return AdminResource(self)

    @cached_property
    def datasets(self) -> DatasetsResource:
        from .resources.datasets import DatasetsResource

        return DatasetsResource(self)

    @cached_property
    def documents(self) -> DocumentsResource:
        from .resources.documents import DocumentsResource

        return DocumentsResource(self)

    @cached_property
    def jobs(self) -> JobsResource:
        from .resources.jobs import JobsResource

        return JobsResource(self)

    @cached_property
    def match(self) -> MatchResource:
        from .resources.match import MatchResource

        return MatchResource(self)

    @cached_property
    def sessions(self) -> SessionsResource:
        from .resources.sessions import SessionsResource

        return SessionsResource(self)

    @cached_property
    def workflow_schedule(self) -> WorkflowScheduleResource:
        from .resources.workflow_schedule import WorkflowScheduleResource

        return WorkflowScheduleResource(self)

    @cached_property
    def workflow(self) -> WorkflowResource:
        from .resources.workflow import WorkflowResource

        return WorkflowResource(self)

    @cached_property
    def connectors(self) -> ConnectorsResource:
        from .resources.connectors import ConnectorsResource

        return ConnectorsResource(self)

    @cached_property
    def connector_catalog(self) -> ConnectorCatalogResource:
        from .resources.connector_catalog import ConnectorCatalogResource

        return ConnectorCatalogResource(self)

    @cached_property
    def server(self) -> ServerResource:
        from .resources.server import ServerResource

        return ServerResource(self)

    @cached_property
    def sources(self) -> SourcesResource:
        from .resources.sources import SourcesResource

        return SourcesResource(self)

    @cached_property
    def entities(self) -> EntitiesResource:
        from .resources.entities import EntitiesResource

        return EntitiesResource(self)

    @cached_property
    def sandbox(self) -> SandboxResource:
        from .resources.sandbox import SandboxResource

        return SandboxResource(self)

    @cached_property
    def scrape(self) -> ScrapeResource:
        from .resources.scrape import ScrapeResource

        return ScrapeResource(self)

    @cached_property
    def code(self) -> CodeResource:
        from .resources.code import CodeResource

        return CodeResource(self)

    @cached_property
    def structure(self) -> StructureResource:
        from .resources.structure import StructureResource

        return StructureResource(self)

    @cached_property
    def public_sessions(self) -> PublicSessionsResource:
        from .resources.public_sessions import PublicSessionsResource

        return PublicSessionsResource(self)

    @cached_property
    def external(self) -> ExternalResource:
        from .resources.external import ExternalResource

        return ExternalResource(self)

    @cached_property
    def slack(self) -> SlackResource:
        from .resources.slack import SlackResource

        return SlackResource(self)

    @cached_property
    def nango(self) -> NangoResource:
        from .resources.nango import NangoResource

        return NangoResource(self)

    @cached_property
    def with_raw_response(self) -> StructifyWithRawResponse:
        return StructifyWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StructifyWithStreamedResponse:
        return StructifyWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {**self._api_key, **self._session_token}

    @property
    def _api_key(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"api_key": api_key}

    @property
    def _session_token(self) -> dict[str, str]:
        session_token = self.session_token
        if session_token is None:
            return {}
        return {"Authorization": f"Bearer {session_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if self.api_key and headers.get("api_key"):
            return
        if isinstance(custom_headers.get("api_key"), Omit):
            return

        if self.session_token and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected either api_key or session_token to be set. Or for one of the `api_key` or `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        session_token: str | None = None,
        environment: Literal["production", "development"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
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
            session_token=session_token or self.session_token,
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
    # client options
    api_key: str | None
    session_token: str | None

    _environment: Literal["production", "development"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        session_token: str | None = None,
        environment: Literal["production", "development"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
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
        """Construct a new async AsyncStructify client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `STRUCTIFY_API_TOKEN`
        - `session_token` from `STRUCTIFY_SESSION_TOKEN`
        """
        if api_key is None:
            api_key = os.environ.get("STRUCTIFY_API_TOKEN")
        self.api_key = api_key

        if session_token is None:
            session_token = os.environ.get("STRUCTIFY_SESSION_TOKEN")
        self.session_token = session_token

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

    @cached_property
    def user(self) -> AsyncUserResource:
        from .resources.user import AsyncUserResource

        return AsyncUserResource(self)

    @cached_property
    def chat(self) -> AsyncChatResource:
        from .resources.chat import AsyncChatResource

        return AsyncChatResource(self)

    @cached_property
    def teams(self) -> AsyncTeamsResource:
        from .resources.teams import AsyncTeamsResource

        return AsyncTeamsResource(self)

    @cached_property
    def wiki(self) -> AsyncWikiResource:
        from .resources.wiki import AsyncWikiResource

        return AsyncWikiResource(self)

    @cached_property
    def projects(self) -> AsyncProjectsResource:
        from .resources.projects import AsyncProjectsResource

        return AsyncProjectsResource(self)

    @cached_property
    def admin(self) -> AsyncAdminResource:
        from .resources.admin import AsyncAdminResource

        return AsyncAdminResource(self)

    @cached_property
    def datasets(self) -> AsyncDatasetsResource:
        from .resources.datasets import AsyncDatasetsResource

        return AsyncDatasetsResource(self)

    @cached_property
    def documents(self) -> AsyncDocumentsResource:
        from .resources.documents import AsyncDocumentsResource

        return AsyncDocumentsResource(self)

    @cached_property
    def jobs(self) -> AsyncJobsResource:
        from .resources.jobs import AsyncJobsResource

        return AsyncJobsResource(self)

    @cached_property
    def match(self) -> AsyncMatchResource:
        from .resources.match import AsyncMatchResource

        return AsyncMatchResource(self)

    @cached_property
    def sessions(self) -> AsyncSessionsResource:
        from .resources.sessions import AsyncSessionsResource

        return AsyncSessionsResource(self)

    @cached_property
    def workflow_schedule(self) -> AsyncWorkflowScheduleResource:
        from .resources.workflow_schedule import AsyncWorkflowScheduleResource

        return AsyncWorkflowScheduleResource(self)

    @cached_property
    def workflow(self) -> AsyncWorkflowResource:
        from .resources.workflow import AsyncWorkflowResource

        return AsyncWorkflowResource(self)

    @cached_property
    def connectors(self) -> AsyncConnectorsResource:
        from .resources.connectors import AsyncConnectorsResource

        return AsyncConnectorsResource(self)

    @cached_property
    def connector_catalog(self) -> AsyncConnectorCatalogResource:
        from .resources.connector_catalog import AsyncConnectorCatalogResource

        return AsyncConnectorCatalogResource(self)

    @cached_property
    def server(self) -> AsyncServerResource:
        from .resources.server import AsyncServerResource

        return AsyncServerResource(self)

    @cached_property
    def sources(self) -> AsyncSourcesResource:
        from .resources.sources import AsyncSourcesResource

        return AsyncSourcesResource(self)

    @cached_property
    def entities(self) -> AsyncEntitiesResource:
        from .resources.entities import AsyncEntitiesResource

        return AsyncEntitiesResource(self)

    @cached_property
    def sandbox(self) -> AsyncSandboxResource:
        from .resources.sandbox import AsyncSandboxResource

        return AsyncSandboxResource(self)

    @cached_property
    def scrape(self) -> AsyncScrapeResource:
        from .resources.scrape import AsyncScrapeResource

        return AsyncScrapeResource(self)

    @cached_property
    def code(self) -> AsyncCodeResource:
        from .resources.code import AsyncCodeResource

        return AsyncCodeResource(self)

    @cached_property
    def structure(self) -> AsyncStructureResource:
        from .resources.structure import AsyncStructureResource

        return AsyncStructureResource(self)

    @cached_property
    def public_sessions(self) -> AsyncPublicSessionsResource:
        from .resources.public_sessions import AsyncPublicSessionsResource

        return AsyncPublicSessionsResource(self)

    @cached_property
    def external(self) -> AsyncExternalResource:
        from .resources.external import AsyncExternalResource

        return AsyncExternalResource(self)

    @cached_property
    def slack(self) -> AsyncSlackResource:
        from .resources.slack import AsyncSlackResource

        return AsyncSlackResource(self)

    @cached_property
    def nango(self) -> AsyncNangoResource:
        from .resources.nango import AsyncNangoResource

        return AsyncNangoResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncStructifyWithRawResponse:
        return AsyncStructifyWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStructifyWithStreamedResponse:
        return AsyncStructifyWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {**self._api_key, **self._session_token}

    @property
    def _api_key(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"api_key": api_key}

    @property
    def _session_token(self) -> dict[str, str]:
        session_token = self.session_token
        if session_token is None:
            return {}
        return {"Authorization": f"Bearer {session_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if self.api_key and headers.get("api_key"):
            return
        if isinstance(custom_headers.get("api_key"), Omit):
            return

        if self.session_token and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected either api_key or session_token to be set. Or for one of the `api_key` or `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        session_token: str | None = None,
        environment: Literal["production", "development"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
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
            session_token=session_token or self.session_token,
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
    _client: Structify

    def __init__(self, client: Structify) -> None:
        self._client = client

    @cached_property
    def user(self) -> user.UserResourceWithRawResponse:
        from .resources.user import UserResourceWithRawResponse

        return UserResourceWithRawResponse(self._client.user)

    @cached_property
    def chat(self) -> chat.ChatResourceWithRawResponse:
        from .resources.chat import ChatResourceWithRawResponse

        return ChatResourceWithRawResponse(self._client.chat)

    @cached_property
    def teams(self) -> teams.TeamsResourceWithRawResponse:
        from .resources.teams import TeamsResourceWithRawResponse

        return TeamsResourceWithRawResponse(self._client.teams)

    @cached_property
    def wiki(self) -> wiki.WikiResourceWithRawResponse:
        from .resources.wiki import WikiResourceWithRawResponse

        return WikiResourceWithRawResponse(self._client.wiki)

    @cached_property
    def projects(self) -> projects.ProjectsResourceWithRawResponse:
        from .resources.projects import ProjectsResourceWithRawResponse

        return ProjectsResourceWithRawResponse(self._client.projects)

    @cached_property
    def polars(self) -> polars.PolarsResourceWithRawResponse:
        from .resources.polars import PolarsResourceWithRawResponse

        return PolarsResourceWithRawResponse(self._client.polars)

    @cached_property
    def admin(self) -> admin.AdminResourceWithRawResponse:
        from .resources.admin import AdminResourceWithRawResponse

        return AdminResourceWithRawResponse(self._client.admin)

    @cached_property
    def datasets(self) -> datasets.DatasetsResourceWithRawResponse:
        from .resources.datasets import DatasetsResourceWithRawResponse

        return DatasetsResourceWithRawResponse(self._client.datasets)

    @cached_property
    def documents(self) -> documents.DocumentsResourceWithRawResponse:
        from .resources.documents import DocumentsResourceWithRawResponse

        return DocumentsResourceWithRawResponse(self._client.documents)

    @cached_property
    def jobs(self) -> jobs.JobsResourceWithRawResponse:
        from .resources.jobs import JobsResourceWithRawResponse

        return JobsResourceWithRawResponse(self._client.jobs)

    @cached_property
    def match(self) -> match.MatchResourceWithRawResponse:
        from .resources.match import MatchResourceWithRawResponse

        return MatchResourceWithRawResponse(self._client.match)

    @cached_property
    def sessions(self) -> sessions.SessionsResourceWithRawResponse:
        from .resources.sessions import SessionsResourceWithRawResponse

        return SessionsResourceWithRawResponse(self._client.sessions)

    @cached_property
    def workflow_schedule(self) -> workflow_schedule.WorkflowScheduleResourceWithRawResponse:
        from .resources.workflow_schedule import WorkflowScheduleResourceWithRawResponse

        return WorkflowScheduleResourceWithRawResponse(self._client.workflow_schedule)

    @cached_property
    def workflow(self) -> workflow.WorkflowResourceWithRawResponse:
        from .resources.workflow import WorkflowResourceWithRawResponse

        return WorkflowResourceWithRawResponse(self._client.workflow)

    @cached_property
    def connectors(self) -> connectors.ConnectorsResourceWithRawResponse:
        from .resources.connectors import ConnectorsResourceWithRawResponse

        return ConnectorsResourceWithRawResponse(self._client.connectors)

    @cached_property
    def connector_catalog(self) -> connector_catalog.ConnectorCatalogResourceWithRawResponse:
        from .resources.connector_catalog import ConnectorCatalogResourceWithRawResponse

        return ConnectorCatalogResourceWithRawResponse(self._client.connector_catalog)

    @cached_property
    def server(self) -> server.ServerResourceWithRawResponse:
        from .resources.server import ServerResourceWithRawResponse

        return ServerResourceWithRawResponse(self._client.server)

    @cached_property
    def sources(self) -> sources.SourcesResourceWithRawResponse:
        from .resources.sources import SourcesResourceWithRawResponse

        return SourcesResourceWithRawResponse(self._client.sources)

    @cached_property
    def entities(self) -> entities.EntitiesResourceWithRawResponse:
        from .resources.entities import EntitiesResourceWithRawResponse

        return EntitiesResourceWithRawResponse(self._client.entities)

    @cached_property
    def sandbox(self) -> sandbox.SandboxResourceWithRawResponse:
        from .resources.sandbox import SandboxResourceWithRawResponse

        return SandboxResourceWithRawResponse(self._client.sandbox)

    @cached_property
    def scrape(self) -> scrape.ScrapeResourceWithRawResponse:
        from .resources.scrape import ScrapeResourceWithRawResponse

        return ScrapeResourceWithRawResponse(self._client.scrape)

    @cached_property
    def code(self) -> code.CodeResourceWithRawResponse:
        from .resources.code import CodeResourceWithRawResponse

        return CodeResourceWithRawResponse(self._client.code)

    @cached_property
    def structure(self) -> structure.StructureResourceWithRawResponse:
        from .resources.structure import StructureResourceWithRawResponse

        return StructureResourceWithRawResponse(self._client.structure)

    @cached_property
    def public_sessions(self) -> public_sessions.PublicSessionsResourceWithRawResponse:
        from .resources.public_sessions import PublicSessionsResourceWithRawResponse

        return PublicSessionsResourceWithRawResponse(self._client.public_sessions)

    @cached_property
    def external(self) -> external.ExternalResourceWithRawResponse:
        from .resources.external import ExternalResourceWithRawResponse

        return ExternalResourceWithRawResponse(self._client.external)

    @cached_property
    def slack(self) -> slack.SlackResourceWithRawResponse:
        from .resources.slack import SlackResourceWithRawResponse

        return SlackResourceWithRawResponse(self._client.slack)

    @cached_property
    def nango(self) -> nango.NangoResourceWithRawResponse:
        from .resources.nango import NangoResourceWithRawResponse

        return NangoResourceWithRawResponse(self._client.nango)


class AsyncStructifyWithRawResponse:
    _client: AsyncStructify

    def __init__(self, client: AsyncStructify) -> None:
        self._client = client

    @cached_property
    def user(self) -> user.AsyncUserResourceWithRawResponse:
        from .resources.user import AsyncUserResourceWithRawResponse

        return AsyncUserResourceWithRawResponse(self._client.user)

    @cached_property
    def chat(self) -> chat.AsyncChatResourceWithRawResponse:
        from .resources.chat import AsyncChatResourceWithRawResponse

        return AsyncChatResourceWithRawResponse(self._client.chat)

    @cached_property
    def teams(self) -> teams.AsyncTeamsResourceWithRawResponse:
        from .resources.teams import AsyncTeamsResourceWithRawResponse

        return AsyncTeamsResourceWithRawResponse(self._client.teams)

    @cached_property
    def wiki(self) -> wiki.AsyncWikiResourceWithRawResponse:
        from .resources.wiki import AsyncWikiResourceWithRawResponse

        return AsyncWikiResourceWithRawResponse(self._client.wiki)

    @cached_property
    def projects(self) -> projects.AsyncProjectsResourceWithRawResponse:
        from .resources.projects import AsyncProjectsResourceWithRawResponse

        return AsyncProjectsResourceWithRawResponse(self._client.projects)

    @cached_property
    def admin(self) -> admin.AsyncAdminResourceWithRawResponse:
        from .resources.admin import AsyncAdminResourceWithRawResponse

        return AsyncAdminResourceWithRawResponse(self._client.admin)

    @cached_property
    def datasets(self) -> datasets.AsyncDatasetsResourceWithRawResponse:
        from .resources.datasets import AsyncDatasetsResourceWithRawResponse

        return AsyncDatasetsResourceWithRawResponse(self._client.datasets)

    @cached_property
    def documents(self) -> documents.AsyncDocumentsResourceWithRawResponse:
        from .resources.documents import AsyncDocumentsResourceWithRawResponse

        return AsyncDocumentsResourceWithRawResponse(self._client.documents)

    @cached_property
    def jobs(self) -> jobs.AsyncJobsResourceWithRawResponse:
        from .resources.jobs import AsyncJobsResourceWithRawResponse

        return AsyncJobsResourceWithRawResponse(self._client.jobs)

    @cached_property
    def match(self) -> match.AsyncMatchResourceWithRawResponse:
        from .resources.match import AsyncMatchResourceWithRawResponse

        return AsyncMatchResourceWithRawResponse(self._client.match)

    @cached_property
    def sessions(self) -> sessions.AsyncSessionsResourceWithRawResponse:
        from .resources.sessions import AsyncSessionsResourceWithRawResponse

        return AsyncSessionsResourceWithRawResponse(self._client.sessions)

    @cached_property
    def workflow_schedule(self) -> workflow_schedule.AsyncWorkflowScheduleResourceWithRawResponse:
        from .resources.workflow_schedule import AsyncWorkflowScheduleResourceWithRawResponse

        return AsyncWorkflowScheduleResourceWithRawResponse(self._client.workflow_schedule)

    @cached_property
    def workflow(self) -> workflow.AsyncWorkflowResourceWithRawResponse:
        from .resources.workflow import AsyncWorkflowResourceWithRawResponse

        return AsyncWorkflowResourceWithRawResponse(self._client.workflow)

    @cached_property
    def connectors(self) -> connectors.AsyncConnectorsResourceWithRawResponse:
        from .resources.connectors import AsyncConnectorsResourceWithRawResponse

        return AsyncConnectorsResourceWithRawResponse(self._client.connectors)

    @cached_property
    def connector_catalog(self) -> connector_catalog.AsyncConnectorCatalogResourceWithRawResponse:
        from .resources.connector_catalog import AsyncConnectorCatalogResourceWithRawResponse

        return AsyncConnectorCatalogResourceWithRawResponse(self._client.connector_catalog)

    @cached_property
    def server(self) -> server.AsyncServerResourceWithRawResponse:
        from .resources.server import AsyncServerResourceWithRawResponse

        return AsyncServerResourceWithRawResponse(self._client.server)

    @cached_property
    def sources(self) -> sources.AsyncSourcesResourceWithRawResponse:
        from .resources.sources import AsyncSourcesResourceWithRawResponse

        return AsyncSourcesResourceWithRawResponse(self._client.sources)

    @cached_property
    def entities(self) -> entities.AsyncEntitiesResourceWithRawResponse:
        from .resources.entities import AsyncEntitiesResourceWithRawResponse

        return AsyncEntitiesResourceWithRawResponse(self._client.entities)

    @cached_property
    def sandbox(self) -> sandbox.AsyncSandboxResourceWithRawResponse:
        from .resources.sandbox import AsyncSandboxResourceWithRawResponse

        return AsyncSandboxResourceWithRawResponse(self._client.sandbox)

    @cached_property
    def scrape(self) -> scrape.AsyncScrapeResourceWithRawResponse:
        from .resources.scrape import AsyncScrapeResourceWithRawResponse

        return AsyncScrapeResourceWithRawResponse(self._client.scrape)

    @cached_property
    def code(self) -> code.AsyncCodeResourceWithRawResponse:
        from .resources.code import AsyncCodeResourceWithRawResponse

        return AsyncCodeResourceWithRawResponse(self._client.code)

    @cached_property
    def structure(self) -> structure.AsyncStructureResourceWithRawResponse:
        from .resources.structure import AsyncStructureResourceWithRawResponse

        return AsyncStructureResourceWithRawResponse(self._client.structure)

    @cached_property
    def public_sessions(self) -> public_sessions.AsyncPublicSessionsResourceWithRawResponse:
        from .resources.public_sessions import AsyncPublicSessionsResourceWithRawResponse

        return AsyncPublicSessionsResourceWithRawResponse(self._client.public_sessions)

    @cached_property
    def external(self) -> external.AsyncExternalResourceWithRawResponse:
        from .resources.external import AsyncExternalResourceWithRawResponse

        return AsyncExternalResourceWithRawResponse(self._client.external)

    @cached_property
    def slack(self) -> slack.AsyncSlackResourceWithRawResponse:
        from .resources.slack import AsyncSlackResourceWithRawResponse

        return AsyncSlackResourceWithRawResponse(self._client.slack)

    @cached_property
    def nango(self) -> nango.AsyncNangoResourceWithRawResponse:
        from .resources.nango import AsyncNangoResourceWithRawResponse

        return AsyncNangoResourceWithRawResponse(self._client.nango)


class StructifyWithStreamedResponse:
    _client: Structify

    def __init__(self, client: Structify) -> None:
        self._client = client

    @cached_property
    def user(self) -> user.UserResourceWithStreamingResponse:
        from .resources.user import UserResourceWithStreamingResponse

        return UserResourceWithStreamingResponse(self._client.user)

    @cached_property
    def chat(self) -> chat.ChatResourceWithStreamingResponse:
        from .resources.chat import ChatResourceWithStreamingResponse

        return ChatResourceWithStreamingResponse(self._client.chat)

    @cached_property
    def teams(self) -> teams.TeamsResourceWithStreamingResponse:
        from .resources.teams import TeamsResourceWithStreamingResponse

        return TeamsResourceWithStreamingResponse(self._client.teams)

    @cached_property
    def wiki(self) -> wiki.WikiResourceWithStreamingResponse:
        from .resources.wiki import WikiResourceWithStreamingResponse

        return WikiResourceWithStreamingResponse(self._client.wiki)

    @cached_property
    def projects(self) -> projects.ProjectsResourceWithStreamingResponse:
        from .resources.projects import ProjectsResourceWithStreamingResponse

        return ProjectsResourceWithStreamingResponse(self._client.projects)

    @cached_property
    def polars(self) -> polars.PolarsResourceWithStreamingResponse:
        from .resources.polars import PolarsResourceWithStreamingResponse

        return PolarsResourceWithStreamingResponse(self._client.polars)

    @cached_property
    def admin(self) -> admin.AdminResourceWithStreamingResponse:
        from .resources.admin import AdminResourceWithStreamingResponse

        return AdminResourceWithStreamingResponse(self._client.admin)

    @cached_property
    def datasets(self) -> datasets.DatasetsResourceWithStreamingResponse:
        from .resources.datasets import DatasetsResourceWithStreamingResponse

        return DatasetsResourceWithStreamingResponse(self._client.datasets)

    @cached_property
    def documents(self) -> documents.DocumentsResourceWithStreamingResponse:
        from .resources.documents import DocumentsResourceWithStreamingResponse

        return DocumentsResourceWithStreamingResponse(self._client.documents)

    @cached_property
    def jobs(self) -> jobs.JobsResourceWithStreamingResponse:
        from .resources.jobs import JobsResourceWithStreamingResponse

        return JobsResourceWithStreamingResponse(self._client.jobs)

    @cached_property
    def match(self) -> match.MatchResourceWithStreamingResponse:
        from .resources.match import MatchResourceWithStreamingResponse

        return MatchResourceWithStreamingResponse(self._client.match)

    @cached_property
    def sessions(self) -> sessions.SessionsResourceWithStreamingResponse:
        from .resources.sessions import SessionsResourceWithStreamingResponse

        return SessionsResourceWithStreamingResponse(self._client.sessions)

    @cached_property
    def workflow_schedule(self) -> workflow_schedule.WorkflowScheduleResourceWithStreamingResponse:
        from .resources.workflow_schedule import WorkflowScheduleResourceWithStreamingResponse

        return WorkflowScheduleResourceWithStreamingResponse(self._client.workflow_schedule)

    @cached_property
    def workflow(self) -> workflow.WorkflowResourceWithStreamingResponse:
        from .resources.workflow import WorkflowResourceWithStreamingResponse

        return WorkflowResourceWithStreamingResponse(self._client.workflow)

    @cached_property
    def connectors(self) -> connectors.ConnectorsResourceWithStreamingResponse:
        from .resources.connectors import ConnectorsResourceWithStreamingResponse

        return ConnectorsResourceWithStreamingResponse(self._client.connectors)

    @cached_property
    def connector_catalog(self) -> connector_catalog.ConnectorCatalogResourceWithStreamingResponse:
        from .resources.connector_catalog import ConnectorCatalogResourceWithStreamingResponse

        return ConnectorCatalogResourceWithStreamingResponse(self._client.connector_catalog)

    @cached_property
    def server(self) -> server.ServerResourceWithStreamingResponse:
        from .resources.server import ServerResourceWithStreamingResponse

        return ServerResourceWithStreamingResponse(self._client.server)

    @cached_property
    def sources(self) -> sources.SourcesResourceWithStreamingResponse:
        from .resources.sources import SourcesResourceWithStreamingResponse

        return SourcesResourceWithStreamingResponse(self._client.sources)

    @cached_property
    def entities(self) -> entities.EntitiesResourceWithStreamingResponse:
        from .resources.entities import EntitiesResourceWithStreamingResponse

        return EntitiesResourceWithStreamingResponse(self._client.entities)

    @cached_property
    def sandbox(self) -> sandbox.SandboxResourceWithStreamingResponse:
        from .resources.sandbox import SandboxResourceWithStreamingResponse

        return SandboxResourceWithStreamingResponse(self._client.sandbox)

    @cached_property
    def scrape(self) -> scrape.ScrapeResourceWithStreamingResponse:
        from .resources.scrape import ScrapeResourceWithStreamingResponse

        return ScrapeResourceWithStreamingResponse(self._client.scrape)

    @cached_property
    def code(self) -> code.CodeResourceWithStreamingResponse:
        from .resources.code import CodeResourceWithStreamingResponse

        return CodeResourceWithStreamingResponse(self._client.code)

    @cached_property
    def structure(self) -> structure.StructureResourceWithStreamingResponse:
        from .resources.structure import StructureResourceWithStreamingResponse

        return StructureResourceWithStreamingResponse(self._client.structure)

    @cached_property
    def public_sessions(self) -> public_sessions.PublicSessionsResourceWithStreamingResponse:
        from .resources.public_sessions import PublicSessionsResourceWithStreamingResponse

        return PublicSessionsResourceWithStreamingResponse(self._client.public_sessions)

    @cached_property
    def external(self) -> external.ExternalResourceWithStreamingResponse:
        from .resources.external import ExternalResourceWithStreamingResponse

        return ExternalResourceWithStreamingResponse(self._client.external)

    @cached_property
    def slack(self) -> slack.SlackResourceWithStreamingResponse:
        from .resources.slack import SlackResourceWithStreamingResponse

        return SlackResourceWithStreamingResponse(self._client.slack)

    @cached_property
    def nango(self) -> nango.NangoResourceWithStreamingResponse:
        from .resources.nango import NangoResourceWithStreamingResponse

        return NangoResourceWithStreamingResponse(self._client.nango)


class AsyncStructifyWithStreamedResponse:
    _client: AsyncStructify

    def __init__(self, client: AsyncStructify) -> None:
        self._client = client

    @cached_property
    def user(self) -> user.AsyncUserResourceWithStreamingResponse:
        from .resources.user import AsyncUserResourceWithStreamingResponse

        return AsyncUserResourceWithStreamingResponse(self._client.user)

    @cached_property
    def chat(self) -> chat.AsyncChatResourceWithStreamingResponse:
        from .resources.chat import AsyncChatResourceWithStreamingResponse

        return AsyncChatResourceWithStreamingResponse(self._client.chat)

    @cached_property
    def teams(self) -> teams.AsyncTeamsResourceWithStreamingResponse:
        from .resources.teams import AsyncTeamsResourceWithStreamingResponse

        return AsyncTeamsResourceWithStreamingResponse(self._client.teams)

    @cached_property
    def wiki(self) -> wiki.AsyncWikiResourceWithStreamingResponse:
        from .resources.wiki import AsyncWikiResourceWithStreamingResponse

        return AsyncWikiResourceWithStreamingResponse(self._client.wiki)

    @cached_property
    def projects(self) -> projects.AsyncProjectsResourceWithStreamingResponse:
        from .resources.projects import AsyncProjectsResourceWithStreamingResponse

        return AsyncProjectsResourceWithStreamingResponse(self._client.projects)

    @cached_property
    def admin(self) -> admin.AsyncAdminResourceWithStreamingResponse:
        from .resources.admin import AsyncAdminResourceWithStreamingResponse

        return AsyncAdminResourceWithStreamingResponse(self._client.admin)

    @cached_property
    def datasets(self) -> datasets.AsyncDatasetsResourceWithStreamingResponse:
        from .resources.datasets import AsyncDatasetsResourceWithStreamingResponse

        return AsyncDatasetsResourceWithStreamingResponse(self._client.datasets)

    @cached_property
    def documents(self) -> documents.AsyncDocumentsResourceWithStreamingResponse:
        from .resources.documents import AsyncDocumentsResourceWithStreamingResponse

        return AsyncDocumentsResourceWithStreamingResponse(self._client.documents)

    @cached_property
    def jobs(self) -> jobs.AsyncJobsResourceWithStreamingResponse:
        from .resources.jobs import AsyncJobsResourceWithStreamingResponse

        return AsyncJobsResourceWithStreamingResponse(self._client.jobs)

    @cached_property
    def match(self) -> match.AsyncMatchResourceWithStreamingResponse:
        from .resources.match import AsyncMatchResourceWithStreamingResponse

        return AsyncMatchResourceWithStreamingResponse(self._client.match)

    @cached_property
    def sessions(self) -> sessions.AsyncSessionsResourceWithStreamingResponse:
        from .resources.sessions import AsyncSessionsResourceWithStreamingResponse

        return AsyncSessionsResourceWithStreamingResponse(self._client.sessions)

    @cached_property
    def workflow_schedule(self) -> workflow_schedule.AsyncWorkflowScheduleResourceWithStreamingResponse:
        from .resources.workflow_schedule import AsyncWorkflowScheduleResourceWithStreamingResponse

        return AsyncWorkflowScheduleResourceWithStreamingResponse(self._client.workflow_schedule)

    @cached_property
    def workflow(self) -> workflow.AsyncWorkflowResourceWithStreamingResponse:
        from .resources.workflow import AsyncWorkflowResourceWithStreamingResponse

        return AsyncWorkflowResourceWithStreamingResponse(self._client.workflow)

    @cached_property
    def connectors(self) -> connectors.AsyncConnectorsResourceWithStreamingResponse:
        from .resources.connectors import AsyncConnectorsResourceWithStreamingResponse

        return AsyncConnectorsResourceWithStreamingResponse(self._client.connectors)

    @cached_property
    def connector_catalog(self) -> connector_catalog.AsyncConnectorCatalogResourceWithStreamingResponse:
        from .resources.connector_catalog import AsyncConnectorCatalogResourceWithStreamingResponse

        return AsyncConnectorCatalogResourceWithStreamingResponse(self._client.connector_catalog)

    @cached_property
    def server(self) -> server.AsyncServerResourceWithStreamingResponse:
        from .resources.server import AsyncServerResourceWithStreamingResponse

        return AsyncServerResourceWithStreamingResponse(self._client.server)

    @cached_property
    def sources(self) -> sources.AsyncSourcesResourceWithStreamingResponse:
        from .resources.sources import AsyncSourcesResourceWithStreamingResponse

        return AsyncSourcesResourceWithStreamingResponse(self._client.sources)

    @cached_property
    def entities(self) -> entities.AsyncEntitiesResourceWithStreamingResponse:
        from .resources.entities import AsyncEntitiesResourceWithStreamingResponse

        return AsyncEntitiesResourceWithStreamingResponse(self._client.entities)

    @cached_property
    def sandbox(self) -> sandbox.AsyncSandboxResourceWithStreamingResponse:
        from .resources.sandbox import AsyncSandboxResourceWithStreamingResponse

        return AsyncSandboxResourceWithStreamingResponse(self._client.sandbox)

    @cached_property
    def scrape(self) -> scrape.AsyncScrapeResourceWithStreamingResponse:
        from .resources.scrape import AsyncScrapeResourceWithStreamingResponse

        return AsyncScrapeResourceWithStreamingResponse(self._client.scrape)

    @cached_property
    def code(self) -> code.AsyncCodeResourceWithStreamingResponse:
        from .resources.code import AsyncCodeResourceWithStreamingResponse

        return AsyncCodeResourceWithStreamingResponse(self._client.code)

    @cached_property
    def structure(self) -> structure.AsyncStructureResourceWithStreamingResponse:
        from .resources.structure import AsyncStructureResourceWithStreamingResponse

        return AsyncStructureResourceWithStreamingResponse(self._client.structure)

    @cached_property
    def public_sessions(self) -> public_sessions.AsyncPublicSessionsResourceWithStreamingResponse:
        from .resources.public_sessions import AsyncPublicSessionsResourceWithStreamingResponse

        return AsyncPublicSessionsResourceWithStreamingResponse(self._client.public_sessions)

    @cached_property
    def external(self) -> external.AsyncExternalResourceWithStreamingResponse:
        from .resources.external import AsyncExternalResourceWithStreamingResponse

        return AsyncExternalResourceWithStreamingResponse(self._client.external)

    @cached_property
    def slack(self) -> slack.AsyncSlackResourceWithStreamingResponse:
        from .resources.slack import AsyncSlackResourceWithStreamingResponse

        return AsyncSlackResourceWithStreamingResponse(self._client.slack)

    @cached_property
    def nango(self) -> nango.AsyncNangoResourceWithStreamingResponse:
        from .resources.nango import AsyncNangoResourceWithStreamingResponse

        return AsyncNangoResourceWithStreamingResponse(self._client.nango)


Client = Structify

AsyncClient = AsyncStructify
