# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.supported_entity_type_list_response import SupportedEntityTypeListResponse

__all__ = ["SupportedEntityTypesResource", "AsyncSupportedEntityTypesResource"]


class SupportedEntityTypesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SupportedEntityTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/entity-python-sdk-python#accessing-raw-response-data-eg-headers
        """
        return SupportedEntityTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SupportedEntityTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/entity-python-sdk-python#with_streaming_response
        """
        return SupportedEntityTypesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SupportedEntityTypeListResponse:
        """Get a list of all the available entity types defined in the schema yaml"""
        return self._get(
            "/entity-types",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SupportedEntityTypeListResponse,
        )


class AsyncSupportedEntityTypesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSupportedEntityTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/entity-python-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSupportedEntityTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSupportedEntityTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/entity-python-sdk-python#with_streaming_response
        """
        return AsyncSupportedEntityTypesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SupportedEntityTypeListResponse:
        """Get a list of all the available entity types defined in the schema yaml"""
        return await self._get(
            "/entity-types",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SupportedEntityTypeListResponse,
        )


class SupportedEntityTypesResourceWithRawResponse:
    def __init__(self, supported_entity_types: SupportedEntityTypesResource) -> None:
        self._supported_entity_types = supported_entity_types

        self.list = to_raw_response_wrapper(
            supported_entity_types.list,
        )


class AsyncSupportedEntityTypesResourceWithRawResponse:
    def __init__(self, supported_entity_types: AsyncSupportedEntityTypesResource) -> None:
        self._supported_entity_types = supported_entity_types

        self.list = async_to_raw_response_wrapper(
            supported_entity_types.list,
        )


class SupportedEntityTypesResourceWithStreamingResponse:
    def __init__(self, supported_entity_types: SupportedEntityTypesResource) -> None:
        self._supported_entity_types = supported_entity_types

        self.list = to_streamed_response_wrapper(
            supported_entity_types.list,
        )


class AsyncSupportedEntityTypesResourceWithStreamingResponse:
    def __init__(self, supported_entity_types: AsyncSupportedEntityTypesResource) -> None:
        self._supported_entity_types = supported_entity_types

        self.list = async_to_streamed_response_wrapper(
            supported_entity_types.list,
        )
