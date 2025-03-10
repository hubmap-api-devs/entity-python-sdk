# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from entity_python_sdk import EntityPythonSDK, AsyncEntityPythonSDK
from entity_python_sdk.types import SupportedEntityTypeListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSupportedEntityTypes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: EntityPythonSDK) -> None:
        supported_entity_type = client.supported_entity_types.list()
        assert_matches_type(SupportedEntityTypeListResponse, supported_entity_type, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: EntityPythonSDK) -> None:
        response = client.supported_entity_types.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        supported_entity_type = response.parse()
        assert_matches_type(SupportedEntityTypeListResponse, supported_entity_type, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: EntityPythonSDK) -> None:
        with client.supported_entity_types.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            supported_entity_type = response.parse()
            assert_matches_type(SupportedEntityTypeListResponse, supported_entity_type, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSupportedEntityTypes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncEntityPythonSDK) -> None:
        supported_entity_type = await async_client.supported_entity_types.list()
        assert_matches_type(SupportedEntityTypeListResponse, supported_entity_type, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncEntityPythonSDK) -> None:
        response = await async_client.supported_entity_types.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        supported_entity_type = await response.parse()
        assert_matches_type(SupportedEntityTypeListResponse, supported_entity_type, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncEntityPythonSDK) -> None:
        async with async_client.supported_entity_types.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            supported_entity_type = await response.parse()
            assert_matches_type(SupportedEntityTypeListResponse, supported_entity_type, path=["response"])

        assert cast(Any, response.is_closed) is True
