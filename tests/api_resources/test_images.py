# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from excai import ExCai, AsyncExCai
from excai.types import (
    ImageCreateEditResponse,
    ImageCreateVariationResponse,
    ImageCreateGenerationResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestImages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_edit(self, client: ExCai) -> None:
        image = client.images.create_edit(
            image=b"raw file contents",
            prompt="A cute baby sea otter wearing a beret",
        )
        assert_matches_type(ImageCreateEditResponse, image, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_edit_with_all_params(self, client: ExCai) -> None:
        image = client.images.create_edit(
            image=b"raw file contents",
            prompt="A cute baby sea otter wearing a beret",
            mask=b"raw file contents",
            model="gpt-image-1",
            n=1,
            quality="high",
            response_format="url",
            size="1024x1024",
            user="user-1234",
        )
        assert_matches_type(ImageCreateEditResponse, image, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_edit(self, client: ExCai) -> None:
        response = client.images.with_raw_response.create_edit(
            image=b"raw file contents",
            prompt="A cute baby sea otter wearing a beret",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = response.parse()
        assert_matches_type(ImageCreateEditResponse, image, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_edit(self, client: ExCai) -> None:
        with client.images.with_streaming_response.create_edit(
            image=b"raw file contents",
            prompt="A cute baby sea otter wearing a beret",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = response.parse()
            assert_matches_type(ImageCreateEditResponse, image, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_generation(self, client: ExCai) -> None:
        image = client.images.create_generation(
            prompt="A cute baby sea otter",
        )
        assert_matches_type(ImageCreateGenerationResponse, image, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_generation_with_all_params(self, client: ExCai) -> None:
        image = client.images.create_generation(
            prompt="A cute baby sea otter",
            background="transparent",
            model="gpt-image-1",
            moderation="low",
            n=1,
            output_compression=100,
            output_format="png",
            quality="medium",
            response_format="url",
            size="1024x1024",
            style="vivid",
            user="user-1234",
        )
        assert_matches_type(ImageCreateGenerationResponse, image, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_generation(self, client: ExCai) -> None:
        response = client.images.with_raw_response.create_generation(
            prompt="A cute baby sea otter",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = response.parse()
        assert_matches_type(ImageCreateGenerationResponse, image, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_generation(self, client: ExCai) -> None:
        with client.images.with_streaming_response.create_generation(
            prompt="A cute baby sea otter",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = response.parse()
            assert_matches_type(ImageCreateGenerationResponse, image, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_variation(self, client: ExCai) -> None:
        image = client.images.create_variation(
            image=b"raw file contents",
        )
        assert_matches_type(ImageCreateVariationResponse, image, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_variation_with_all_params(self, client: ExCai) -> None:
        image = client.images.create_variation(
            image=b"raw file contents",
            model="dall-e-2",
            n=1,
            response_format="url",
            size="1024x1024",
            user="user-1234",
        )
        assert_matches_type(ImageCreateVariationResponse, image, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_variation(self, client: ExCai) -> None:
        response = client.images.with_raw_response.create_variation(
            image=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = response.parse()
        assert_matches_type(ImageCreateVariationResponse, image, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_variation(self, client: ExCai) -> None:
        with client.images.with_streaming_response.create_variation(
            image=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = response.parse()
            assert_matches_type(ImageCreateVariationResponse, image, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncImages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_edit(self, async_client: AsyncExCai) -> None:
        image = await async_client.images.create_edit(
            image=b"raw file contents",
            prompt="A cute baby sea otter wearing a beret",
        )
        assert_matches_type(ImageCreateEditResponse, image, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_edit_with_all_params(self, async_client: AsyncExCai) -> None:
        image = await async_client.images.create_edit(
            image=b"raw file contents",
            prompt="A cute baby sea otter wearing a beret",
            mask=b"raw file contents",
            model="gpt-image-1",
            n=1,
            quality="high",
            response_format="url",
            size="1024x1024",
            user="user-1234",
        )
        assert_matches_type(ImageCreateEditResponse, image, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_edit(self, async_client: AsyncExCai) -> None:
        response = await async_client.images.with_raw_response.create_edit(
            image=b"raw file contents",
            prompt="A cute baby sea otter wearing a beret",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = await response.parse()
        assert_matches_type(ImageCreateEditResponse, image, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_edit(self, async_client: AsyncExCai) -> None:
        async with async_client.images.with_streaming_response.create_edit(
            image=b"raw file contents",
            prompt="A cute baby sea otter wearing a beret",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = await response.parse()
            assert_matches_type(ImageCreateEditResponse, image, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_generation(self, async_client: AsyncExCai) -> None:
        image = await async_client.images.create_generation(
            prompt="A cute baby sea otter",
        )
        assert_matches_type(ImageCreateGenerationResponse, image, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_generation_with_all_params(self, async_client: AsyncExCai) -> None:
        image = await async_client.images.create_generation(
            prompt="A cute baby sea otter",
            background="transparent",
            model="gpt-image-1",
            moderation="low",
            n=1,
            output_compression=100,
            output_format="png",
            quality="medium",
            response_format="url",
            size="1024x1024",
            style="vivid",
            user="user-1234",
        )
        assert_matches_type(ImageCreateGenerationResponse, image, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_generation(self, async_client: AsyncExCai) -> None:
        response = await async_client.images.with_raw_response.create_generation(
            prompt="A cute baby sea otter",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = await response.parse()
        assert_matches_type(ImageCreateGenerationResponse, image, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_generation(self, async_client: AsyncExCai) -> None:
        async with async_client.images.with_streaming_response.create_generation(
            prompt="A cute baby sea otter",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = await response.parse()
            assert_matches_type(ImageCreateGenerationResponse, image, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_variation(self, async_client: AsyncExCai) -> None:
        image = await async_client.images.create_variation(
            image=b"raw file contents",
        )
        assert_matches_type(ImageCreateVariationResponse, image, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_variation_with_all_params(self, async_client: AsyncExCai) -> None:
        image = await async_client.images.create_variation(
            image=b"raw file contents",
            model="dall-e-2",
            n=1,
            response_format="url",
            size="1024x1024",
            user="user-1234",
        )
        assert_matches_type(ImageCreateVariationResponse, image, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_variation(self, async_client: AsyncExCai) -> None:
        response = await async_client.images.with_raw_response.create_variation(
            image=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = await response.parse()
        assert_matches_type(ImageCreateVariationResponse, image, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_variation(self, async_client: AsyncExCai) -> None:
        async with async_client.images.with_streaming_response.create_variation(
            image=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = await response.parse()
            assert_matches_type(ImageCreateVariationResponse, image, path=["response"])

        assert cast(Any, response.is_closed) is True
