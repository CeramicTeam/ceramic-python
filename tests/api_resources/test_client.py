# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from ceramic import Ceramic, AsyncCeramic
from tests.utils import assert_matches_type
from ceramic.types import SearchResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClient:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search(self, client: Ceramic) -> None:
        client_ = client.search(
            query="California rental laws",
        )
        assert_matches_type(SearchResponse, client_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: Ceramic) -> None:
        client_ = client.search(
            query="California rental laws",
            max_description_length=1,
            max_results=1,
        )
        assert_matches_type(SearchResponse, client_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: Ceramic) -> None:
        response = client.with_raw_response.search(
            query="California rental laws",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(SearchResponse, client_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: Ceramic) -> None:
        with client.with_streaming_response.search(
            query="California rental laws",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(SearchResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncClient:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncCeramic) -> None:
        client = await async_client.search(
            query="California rental laws",
        )
        assert_matches_type(SearchResponse, client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncCeramic) -> None:
        client = await async_client.search(
            query="California rental laws",
            max_description_length=1,
            max_results=1,
        )
        assert_matches_type(SearchResponse, client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncCeramic) -> None:
        response = await async_client.with_raw_response.search(
            query="California rental laws",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(SearchResponse, client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncCeramic) -> None:
        async with async_client.with_streaming_response.search(
            query="California rental laws",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(SearchResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True
