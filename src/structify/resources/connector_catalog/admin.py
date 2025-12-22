# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.connector_catalog import (
    admin_create_catalog_params,
    admin_update_catalog_params,
    admin_create_auth_method_params,
    admin_update_auth_method_params,
    admin_create_credential_field_params,
    admin_update_credential_field_params,
    admin_batch_create_credential_fields_params,
)
from ...types.connector_auth_method import ConnectorAuthMethod
from ...types.connector_credential_field import ConnectorCredentialField
from ...types.connector_catalog.connector_catalog import ConnectorCatalog
from ...types.connector_catalog.admin_list_nango_pending_response import AdminListNangoPendingResponse
from ...types.connector_catalog.create_credential_field_request_param import CreateCredentialFieldRequestParam
from ...types.connector_catalog.admin_batch_create_credential_fields_response import (
    AdminBatchCreateCredentialFieldsResponse,
)

__all__ = ["AdminResource", "AsyncAdminResource"]


class AdminResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AdminResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
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

    def batch_create_credential_fields(
        self,
        *,
        fields: Iterable[CreateCredentialFieldRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdminBatchCreateCredentialFieldsResponse:
        """
        Batch create connector credential fields

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/admin/connector-catalog/credential-fields/batch",
            body=maybe_transform(
                {"fields": fields}, admin_batch_create_credential_fields_params.AdminBatchCreateCredentialFieldsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdminBatchCreateCredentialFieldsResponse,
        )

    def create_auth_method(
        self,
        *,
        auth_type: Literal["credentials", "oauth_nango"],
        connector_catalog_id: str,
        is_active: bool,
        priority: int,
        label: Optional[str] | Omit = omit,
        nango_integration_key: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorAuthMethod:
        """
        Create a new connector auth method

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/admin/connector-catalog/auth-methods",
            body=maybe_transform(
                {
                    "auth_type": auth_type,
                    "connector_catalog_id": connector_catalog_id,
                    "is_active": is_active,
                    "priority": priority,
                    "label": label,
                    "nango_integration_key": nango_integration_key,
                },
                admin_create_auth_method_params.AdminCreateAuthMethodParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectorAuthMethod,
        )

    def create_catalog(
        self,
        *,
        name: str,
        slug: str,
        categories: SequenceNotStr[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        logo_path: Optional[str] | Omit = omit,
        priority: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorCatalog:
        """
        Create a new connector catalog entry

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/admin/connector-catalog",
            body=maybe_transform(
                {
                    "name": name,
                    "slug": slug,
                    "categories": categories,
                    "description": description,
                    "logo_path": logo_path,
                    "priority": priority,
                },
                admin_create_catalog_params.AdminCreateCatalogParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectorCatalog,
        )

    def create_credential_field(
        self,
        *,
        auth_method_id: str,
        display_order: int,
        field_type: str,
        is_optional: bool,
        name: str,
        default_value: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        label: Optional[str] | Omit = omit,
        options: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorCredentialField:
        """
        Create a new connector credential field

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/admin/connector-catalog/credential-fields",
            body=maybe_transform(
                {
                    "auth_method_id": auth_method_id,
                    "display_order": display_order,
                    "field_type": field_type,
                    "is_optional": is_optional,
                    "name": name,
                    "default_value": default_value,
                    "description": description,
                    "label": label,
                    "options": options,
                },
                admin_create_credential_field_params.AdminCreateCredentialFieldParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectorCredentialField,
        )

    def delete_credential_field(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a connector credential field

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/admin/connector-catalog/credential-fields/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list_nango_pending(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdminListNangoPendingResponse:
        """List Nango integrations that are not yet in the connector catalog"""
        return self._get(
            "/admin/connector-catalog/nango-pending",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdminListNangoPendingResponse,
        )

    def update_auth_method(
        self,
        id: str,
        *,
        is_active: Optional[bool] | Omit = omit,
        label: Optional[str] | Omit = omit,
        priority: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorAuthMethod:
        """
        Update a connector auth method

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/admin/connector-catalog/auth-methods/{id}",
            body=maybe_transform(
                {
                    "is_active": is_active,
                    "label": label,
                    "priority": priority,
                },
                admin_update_auth_method_params.AdminUpdateAuthMethodParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectorAuthMethod,
        )

    def update_catalog(
        self,
        id: str,
        *,
        categories: Optional[SequenceNotStr[str]] | Omit = omit,
        description: Optional[str] | Omit = omit,
        logo_path: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        priority: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorCatalog:
        """
        Update a connector catalog entry

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/admin/connector-catalog/{id}",
            body=maybe_transform(
                {
                    "categories": categories,
                    "description": description,
                    "logo_path": logo_path,
                    "name": name,
                    "priority": priority,
                },
                admin_update_catalog_params.AdminUpdateCatalogParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectorCatalog,
        )

    def update_credential_field(
        self,
        id: str,
        *,
        default_value: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        display_order: Optional[int] | Omit = omit,
        field_type: Optional[str] | Omit = omit,
        is_optional: Optional[bool] | Omit = omit,
        label: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        options: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorCredentialField:
        """
        Update a connector credential field

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/admin/connector-catalog/credential-fields/{id}",
            body=maybe_transform(
                {
                    "default_value": default_value,
                    "description": description,
                    "display_order": display_order,
                    "field_type": field_type,
                    "is_optional": is_optional,
                    "label": label,
                    "name": name,
                    "options": options,
                },
                admin_update_credential_field_params.AdminUpdateCredentialFieldParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectorCredentialField,
        )


class AsyncAdminResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAdminResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
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

    async def batch_create_credential_fields(
        self,
        *,
        fields: Iterable[CreateCredentialFieldRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdminBatchCreateCredentialFieldsResponse:
        """
        Batch create connector credential fields

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/admin/connector-catalog/credential-fields/batch",
            body=await async_maybe_transform(
                {"fields": fields}, admin_batch_create_credential_fields_params.AdminBatchCreateCredentialFieldsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdminBatchCreateCredentialFieldsResponse,
        )

    async def create_auth_method(
        self,
        *,
        auth_type: Literal["credentials", "oauth_nango"],
        connector_catalog_id: str,
        is_active: bool,
        priority: int,
        label: Optional[str] | Omit = omit,
        nango_integration_key: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorAuthMethod:
        """
        Create a new connector auth method

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/admin/connector-catalog/auth-methods",
            body=await async_maybe_transform(
                {
                    "auth_type": auth_type,
                    "connector_catalog_id": connector_catalog_id,
                    "is_active": is_active,
                    "priority": priority,
                    "label": label,
                    "nango_integration_key": nango_integration_key,
                },
                admin_create_auth_method_params.AdminCreateAuthMethodParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectorAuthMethod,
        )

    async def create_catalog(
        self,
        *,
        name: str,
        slug: str,
        categories: SequenceNotStr[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        logo_path: Optional[str] | Omit = omit,
        priority: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorCatalog:
        """
        Create a new connector catalog entry

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/admin/connector-catalog",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "slug": slug,
                    "categories": categories,
                    "description": description,
                    "logo_path": logo_path,
                    "priority": priority,
                },
                admin_create_catalog_params.AdminCreateCatalogParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectorCatalog,
        )

    async def create_credential_field(
        self,
        *,
        auth_method_id: str,
        display_order: int,
        field_type: str,
        is_optional: bool,
        name: str,
        default_value: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        label: Optional[str] | Omit = omit,
        options: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorCredentialField:
        """
        Create a new connector credential field

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/admin/connector-catalog/credential-fields",
            body=await async_maybe_transform(
                {
                    "auth_method_id": auth_method_id,
                    "display_order": display_order,
                    "field_type": field_type,
                    "is_optional": is_optional,
                    "name": name,
                    "default_value": default_value,
                    "description": description,
                    "label": label,
                    "options": options,
                },
                admin_create_credential_field_params.AdminCreateCredentialFieldParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectorCredentialField,
        )

    async def delete_credential_field(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a connector credential field

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/admin/connector-catalog/credential-fields/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list_nango_pending(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdminListNangoPendingResponse:
        """List Nango integrations that are not yet in the connector catalog"""
        return await self._get(
            "/admin/connector-catalog/nango-pending",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdminListNangoPendingResponse,
        )

    async def update_auth_method(
        self,
        id: str,
        *,
        is_active: Optional[bool] | Omit = omit,
        label: Optional[str] | Omit = omit,
        priority: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorAuthMethod:
        """
        Update a connector auth method

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/admin/connector-catalog/auth-methods/{id}",
            body=await async_maybe_transform(
                {
                    "is_active": is_active,
                    "label": label,
                    "priority": priority,
                },
                admin_update_auth_method_params.AdminUpdateAuthMethodParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectorAuthMethod,
        )

    async def update_catalog(
        self,
        id: str,
        *,
        categories: Optional[SequenceNotStr[str]] | Omit = omit,
        description: Optional[str] | Omit = omit,
        logo_path: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        priority: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorCatalog:
        """
        Update a connector catalog entry

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/admin/connector-catalog/{id}",
            body=await async_maybe_transform(
                {
                    "categories": categories,
                    "description": description,
                    "logo_path": logo_path,
                    "name": name,
                    "priority": priority,
                },
                admin_update_catalog_params.AdminUpdateCatalogParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectorCatalog,
        )

    async def update_credential_field(
        self,
        id: str,
        *,
        default_value: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        display_order: Optional[int] | Omit = omit,
        field_type: Optional[str] | Omit = omit,
        is_optional: Optional[bool] | Omit = omit,
        label: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        options: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorCredentialField:
        """
        Update a connector credential field

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/admin/connector-catalog/credential-fields/{id}",
            body=await async_maybe_transform(
                {
                    "default_value": default_value,
                    "description": description,
                    "display_order": display_order,
                    "field_type": field_type,
                    "is_optional": is_optional,
                    "label": label,
                    "name": name,
                    "options": options,
                },
                admin_update_credential_field_params.AdminUpdateCredentialFieldParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectorCredentialField,
        )


class AdminResourceWithRawResponse:
    def __init__(self, admin: AdminResource) -> None:
        self._admin = admin

        self.batch_create_credential_fields = to_raw_response_wrapper(
            admin.batch_create_credential_fields,
        )
        self.create_auth_method = to_raw_response_wrapper(
            admin.create_auth_method,
        )
        self.create_catalog = to_raw_response_wrapper(
            admin.create_catalog,
        )
        self.create_credential_field = to_raw_response_wrapper(
            admin.create_credential_field,
        )
        self.delete_credential_field = to_raw_response_wrapper(
            admin.delete_credential_field,
        )
        self.list_nango_pending = to_raw_response_wrapper(
            admin.list_nango_pending,
        )
        self.update_auth_method = to_raw_response_wrapper(
            admin.update_auth_method,
        )
        self.update_catalog = to_raw_response_wrapper(
            admin.update_catalog,
        )
        self.update_credential_field = to_raw_response_wrapper(
            admin.update_credential_field,
        )


class AsyncAdminResourceWithRawResponse:
    def __init__(self, admin: AsyncAdminResource) -> None:
        self._admin = admin

        self.batch_create_credential_fields = async_to_raw_response_wrapper(
            admin.batch_create_credential_fields,
        )
        self.create_auth_method = async_to_raw_response_wrapper(
            admin.create_auth_method,
        )
        self.create_catalog = async_to_raw_response_wrapper(
            admin.create_catalog,
        )
        self.create_credential_field = async_to_raw_response_wrapper(
            admin.create_credential_field,
        )
        self.delete_credential_field = async_to_raw_response_wrapper(
            admin.delete_credential_field,
        )
        self.list_nango_pending = async_to_raw_response_wrapper(
            admin.list_nango_pending,
        )
        self.update_auth_method = async_to_raw_response_wrapper(
            admin.update_auth_method,
        )
        self.update_catalog = async_to_raw_response_wrapper(
            admin.update_catalog,
        )
        self.update_credential_field = async_to_raw_response_wrapper(
            admin.update_credential_field,
        )


class AdminResourceWithStreamingResponse:
    def __init__(self, admin: AdminResource) -> None:
        self._admin = admin

        self.batch_create_credential_fields = to_streamed_response_wrapper(
            admin.batch_create_credential_fields,
        )
        self.create_auth_method = to_streamed_response_wrapper(
            admin.create_auth_method,
        )
        self.create_catalog = to_streamed_response_wrapper(
            admin.create_catalog,
        )
        self.create_credential_field = to_streamed_response_wrapper(
            admin.create_credential_field,
        )
        self.delete_credential_field = to_streamed_response_wrapper(
            admin.delete_credential_field,
        )
        self.list_nango_pending = to_streamed_response_wrapper(
            admin.list_nango_pending,
        )
        self.update_auth_method = to_streamed_response_wrapper(
            admin.update_auth_method,
        )
        self.update_catalog = to_streamed_response_wrapper(
            admin.update_catalog,
        )
        self.update_credential_field = to_streamed_response_wrapper(
            admin.update_credential_field,
        )


class AsyncAdminResourceWithStreamingResponse:
    def __init__(self, admin: AsyncAdminResource) -> None:
        self._admin = admin

        self.batch_create_credential_fields = async_to_streamed_response_wrapper(
            admin.batch_create_credential_fields,
        )
        self.create_auth_method = async_to_streamed_response_wrapper(
            admin.create_auth_method,
        )
        self.create_catalog = async_to_streamed_response_wrapper(
            admin.create_catalog,
        )
        self.create_credential_field = async_to_streamed_response_wrapper(
            admin.create_credential_field,
        )
        self.delete_credential_field = async_to_streamed_response_wrapper(
            admin.delete_credential_field,
        )
        self.list_nango_pending = async_to_streamed_response_wrapper(
            admin.list_nango_pending,
        )
        self.update_auth_method = async_to_streamed_response_wrapper(
            admin.update_auth_method,
        )
        self.update_catalog = async_to_streamed_response_wrapper(
            admin.update_catalog,
        )
        self.update_credential_field = async_to_streamed_response_wrapper(
            admin.update_credential_field,
        )
