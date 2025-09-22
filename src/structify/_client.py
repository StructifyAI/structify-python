# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Dict, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._version import __version__
from .resources import (
    chat,
    code,
    jobs,
    teams,
    polars,
    report,
    scrape,
    server,
    sandbox,
    sources,
    entities,
    external,
    projects,
    sessions,
    documents,
    structure,
    connectors,
    public_sessions,
    workflow_schedule,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, StructifyError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.user import user
from .resources.admin import admin
from .resources.datasets import datasets

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
    user: user.UserResource
    chat: chat.ChatResource
    teams: teams.TeamsResource
    projects: projects.ProjectsResource
    admin: admin.AdminResource
    datasets: datasets.DatasetsResource
    documents: documents.DocumentsResource
    jobs: jobs.JobsResource
    sessions: sessions.SessionsResource
    workflow_schedule: workflow_schedule.WorkflowScheduleResource
    connectors: connectors.ConnectorsResource
    server: server.ServerResource
    sources: sources.SourcesResource
    entities: entities.EntitiesResource
    report: report.ReportResource
    sandbox: sandbox.SandboxResource
    scrape: scrape.ScrapeResource
    code: code.CodeResource
    structure: structure.StructureResource
    public_sessions: public_sessions.PublicSessionsResource
    polars: polars.PolarsResource
    external: external.ExternalResource
    with_raw_response: StructifyWithRawResponse
    with_streaming_response: StructifyWithStreamedResponse

    # client options
    api_key: str

    _environment: Literal["production", "development"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
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

        self.user = user.UserResource(self)
        self.chat = chat.ChatResource(self)
        self.teams = teams.TeamsResource(self)
        self.projects = projects.ProjectsResource(self)
        self.admin = admin.AdminResource(self)
        self.datasets = datasets.DatasetsResource(self)
        self.documents = documents.DocumentsResource(self)
        self.jobs = jobs.JobsResource(self)
        self.sessions = sessions.SessionsResource(self)
        self.workflow_schedule = workflow_schedule.WorkflowScheduleResource(self)
        self.connectors = connectors.ConnectorsResource(self)
        self.server = server.ServerResource(self)
        self.sources = sources.SourcesResource(self)
        self.entities = entities.EntitiesResource(self)
        self.report = report.ReportResource(self)
        self.sandbox = sandbox.SandboxResource(self)
        self.scrape = scrape.ScrapeResource(self)
        self.code = code.CodeResource(self)
        self.structure = structure.StructureResource(self)
        self.public_sessions = public_sessions.PublicSessionsResource(self)
        self.polars = polars.PolarsResource(self)
        self.external = external.ExternalResource(self)
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
    user: user.AsyncUserResource
    chat: chat.AsyncChatResource
    teams: teams.AsyncTeamsResource
    projects: projects.AsyncProjectsResource
    admin: admin.AsyncAdminResource
    datasets: datasets.AsyncDatasetsResource
    documents: documents.AsyncDocumentsResource
    jobs: jobs.AsyncJobsResource
    sessions: sessions.AsyncSessionsResource
    workflow_schedule: workflow_schedule.AsyncWorkflowScheduleResource
    connectors: connectors.AsyncConnectorsResource
    server: server.AsyncServerResource
    sources: sources.AsyncSourcesResource
    entities: entities.AsyncEntitiesResource
    report: report.AsyncReportResource
    sandbox: sandbox.AsyncSandboxResource
    scrape: scrape.AsyncScrapeResource
    code: code.AsyncCodeResource
    structure: structure.AsyncStructureResource
    public_sessions: public_sessions.AsyncPublicSessionsResource
    external: external.AsyncExternalResource
    with_raw_response: AsyncStructifyWithRawResponse
    with_streaming_response: AsyncStructifyWithStreamedResponse

    # client options
    api_key: str

    _environment: Literal["production", "development"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
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

        self.user = user.AsyncUserResource(self)
        self.chat = chat.AsyncChatResource(self)
        self.teams = teams.AsyncTeamsResource(self)
        self.projects = projects.AsyncProjectsResource(self)
        self.admin = admin.AsyncAdminResource(self)
        self.datasets = datasets.AsyncDatasetsResource(self)
        self.documents = documents.AsyncDocumentsResource(self)
        self.jobs = jobs.AsyncJobsResource(self)
        self.sessions = sessions.AsyncSessionsResource(self)
        self.workflow_schedule = workflow_schedule.AsyncWorkflowScheduleResource(self)
        self.connectors = connectors.AsyncConnectorsResource(self)
        self.server = server.AsyncServerResource(self)
        self.sources = sources.AsyncSourcesResource(self)
        self.entities = entities.AsyncEntitiesResource(self)
        self.report = report.AsyncReportResource(self)
        self.sandbox = sandbox.AsyncSandboxResource(self)
        self.scrape = scrape.AsyncScrapeResource(self)
        self.code = code.AsyncCodeResource(self)
        self.structure = structure.AsyncStructureResource(self)
        self.public_sessions = public_sessions.AsyncPublicSessionsResource(self)
        self.external = external.AsyncExternalResource(self)
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
        self.user = user.UserResourceWithRawResponse(client.user)
        self.chat = chat.ChatResourceWithRawResponse(client.chat)
        self.teams = teams.TeamsResourceWithRawResponse(client.teams)
        self.projects = projects.ProjectsResourceWithRawResponse(client.projects)
        self.admin = admin.AdminResourceWithRawResponse(client.admin)
        self.datasets = datasets.DatasetsResourceWithRawResponse(client.datasets)
        self.documents = documents.DocumentsResourceWithRawResponse(client.documents)
        self.jobs = jobs.JobsResourceWithRawResponse(client.jobs)
        self.sessions = sessions.SessionsResourceWithRawResponse(client.sessions)
        self.workflow_schedule = workflow_schedule.WorkflowScheduleResourceWithRawResponse(client.workflow_schedule)
        self.connectors = connectors.ConnectorsResourceWithRawResponse(client.connectors)
        self.server = server.ServerResourceWithRawResponse(client.server)
        self.sources = sources.SourcesResourceWithRawResponse(client.sources)
        self.entities = entities.EntitiesResourceWithRawResponse(client.entities)
        self.report = report.ReportResourceWithRawResponse(client.report)
        self.sandbox = sandbox.SandboxResourceWithRawResponse(client.sandbox)
        self.scrape = scrape.ScrapeResourceWithRawResponse(client.scrape)
        self.code = code.CodeResourceWithRawResponse(client.code)
        self.structure = structure.StructureResourceWithRawResponse(client.structure)
        self.public_sessions = public_sessions.PublicSessionsResourceWithRawResponse(client.public_sessions)
        self.polars = polars.PolarsResourceWithRawResponse(client.polars)
        self.external = external.ExternalResourceWithRawResponse(client.external)


class AsyncStructifyWithRawResponse:
    def __init__(self, client: AsyncStructify) -> None:
        self.user = user.AsyncUserResourceWithRawResponse(client.user)
        self.chat = chat.AsyncChatResourceWithRawResponse(client.chat)
        self.teams = teams.AsyncTeamsResourceWithRawResponse(client.teams)
        self.projects = projects.AsyncProjectsResourceWithRawResponse(client.projects)
        self.admin = admin.AsyncAdminResourceWithRawResponse(client.admin)
        self.datasets = datasets.AsyncDatasetsResourceWithRawResponse(client.datasets)
        self.documents = documents.AsyncDocumentsResourceWithRawResponse(client.documents)
        self.jobs = jobs.AsyncJobsResourceWithRawResponse(client.jobs)
        self.sessions = sessions.AsyncSessionsResourceWithRawResponse(client.sessions)
        self.workflow_schedule = workflow_schedule.AsyncWorkflowScheduleResourceWithRawResponse(
            client.workflow_schedule
        )
        self.connectors = connectors.AsyncConnectorsResourceWithRawResponse(client.connectors)
        self.server = server.AsyncServerResourceWithRawResponse(client.server)
        self.sources = sources.AsyncSourcesResourceWithRawResponse(client.sources)
        self.entities = entities.AsyncEntitiesResourceWithRawResponse(client.entities)
        self.report = report.AsyncReportResourceWithRawResponse(client.report)
        self.sandbox = sandbox.AsyncSandboxResourceWithRawResponse(client.sandbox)
        self.scrape = scrape.AsyncScrapeResourceWithRawResponse(client.scrape)
        self.code = code.AsyncCodeResourceWithRawResponse(client.code)
        self.structure = structure.AsyncStructureResourceWithRawResponse(client.structure)
        self.public_sessions = public_sessions.AsyncPublicSessionsResourceWithRawResponse(client.public_sessions)
        self.external = external.AsyncExternalResourceWithRawResponse(client.external)


class StructifyWithStreamedResponse:
    def __init__(self, client: Structify) -> None:
        self.user = user.UserResourceWithStreamingResponse(client.user)
        self.chat = chat.ChatResourceWithStreamingResponse(client.chat)
        self.teams = teams.TeamsResourceWithStreamingResponse(client.teams)
        self.projects = projects.ProjectsResourceWithStreamingResponse(client.projects)
        self.admin = admin.AdminResourceWithStreamingResponse(client.admin)
        self.datasets = datasets.DatasetsResourceWithStreamingResponse(client.datasets)
        self.documents = documents.DocumentsResourceWithStreamingResponse(client.documents)
        self.jobs = jobs.JobsResourceWithStreamingResponse(client.jobs)
        self.sessions = sessions.SessionsResourceWithStreamingResponse(client.sessions)
        self.workflow_schedule = workflow_schedule.WorkflowScheduleResourceWithStreamingResponse(
            client.workflow_schedule
        )
        self.connectors = connectors.ConnectorsResourceWithStreamingResponse(client.connectors)
        self.server = server.ServerResourceWithStreamingResponse(client.server)
        self.sources = sources.SourcesResourceWithStreamingResponse(client.sources)
        self.entities = entities.EntitiesResourceWithStreamingResponse(client.entities)
        self.report = report.ReportResourceWithStreamingResponse(client.report)
        self.sandbox = sandbox.SandboxResourceWithStreamingResponse(client.sandbox)
        self.scrape = scrape.ScrapeResourceWithStreamingResponse(client.scrape)
        self.code = code.CodeResourceWithStreamingResponse(client.code)
        self.structure = structure.StructureResourceWithStreamingResponse(client.structure)
        self.public_sessions = public_sessions.PublicSessionsResourceWithStreamingResponse(client.public_sessions)
        self.polars = polars.PolarsResourceWithStreamingResponse(client.polars)
        self.external = external.ExternalResourceWithStreamingResponse(client.external)


class AsyncStructifyWithStreamedResponse:
    def __init__(self, client: AsyncStructify) -> None:
        self.user = user.AsyncUserResourceWithStreamingResponse(client.user)
        self.chat = chat.AsyncChatResourceWithStreamingResponse(client.chat)
        self.teams = teams.AsyncTeamsResourceWithStreamingResponse(client.teams)
        self.projects = projects.AsyncProjectsResourceWithStreamingResponse(client.projects)
        self.admin = admin.AsyncAdminResourceWithStreamingResponse(client.admin)
        self.datasets = datasets.AsyncDatasetsResourceWithStreamingResponse(client.datasets)
        self.documents = documents.AsyncDocumentsResourceWithStreamingResponse(client.documents)
        self.jobs = jobs.AsyncJobsResourceWithStreamingResponse(client.jobs)
        self.sessions = sessions.AsyncSessionsResourceWithStreamingResponse(client.sessions)
        self.workflow_schedule = workflow_schedule.AsyncWorkflowScheduleResourceWithStreamingResponse(
            client.workflow_schedule
        )
        self.connectors = connectors.AsyncConnectorsResourceWithStreamingResponse(client.connectors)
        self.server = server.AsyncServerResourceWithStreamingResponse(client.server)
        self.sources = sources.AsyncSourcesResourceWithStreamingResponse(client.sources)
        self.entities = entities.AsyncEntitiesResourceWithStreamingResponse(client.entities)
        self.report = report.AsyncReportResourceWithStreamingResponse(client.report)
        self.sandbox = sandbox.AsyncSandboxResourceWithStreamingResponse(client.sandbox)
        self.scrape = scrape.AsyncScrapeResourceWithStreamingResponse(client.scrape)
        self.code = code.AsyncCodeResourceWithStreamingResponse(client.code)
        self.structure = structure.AsyncStructureResourceWithStreamingResponse(client.structure)
        self.public_sessions = public_sessions.AsyncPublicSessionsResourceWithStreamingResponse(client.public_sessions)
        self.external = external.AsyncExternalResourceWithStreamingResponse(client.external)


Client = Structify

AsyncClient = AsyncStructify
