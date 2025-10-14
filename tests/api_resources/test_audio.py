# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from excai import ExCai, AsyncExCai
from excai.types import (
    AudioTranslateAudioResponse,
    AudioTranscribeAudioResponse,
)
from tests.utils import assert_matches_type
from excai._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAudio:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_generate_audio(self, client: ExCai, respx_mock: MockRouter) -> None:
        respx_mock.post("/audio/speech").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        audio = client.audio.generate_audio(
            input="input",
            model="string",
            voice="ash",
        )
        assert audio.is_closed
        assert audio.json() == {"foo": "bar"}
        assert cast(Any, audio.is_closed) is True
        assert isinstance(audio, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_generate_audio_with_all_params(self, client: ExCai, respx_mock: MockRouter) -> None:
        respx_mock.post("/audio/speech").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        audio = client.audio.generate_audio(
            input="input",
            model="string",
            voice="ash",
            instructions="instructions",
            response_format="mp3",
            speed=0.25,
            stream_format="sse",
        )
        assert audio.is_closed
        assert audio.json() == {"foo": "bar"}
        assert cast(Any, audio.is_closed) is True
        assert isinstance(audio, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_generate_audio(self, client: ExCai, respx_mock: MockRouter) -> None:
        respx_mock.post("/audio/speech").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        audio = client.audio.with_raw_response.generate_audio(
            input="input",
            model="string",
            voice="ash",
        )

        assert audio.is_closed is True
        assert audio.http_request.headers.get("X-Stainless-Lang") == "python"
        assert audio.json() == {"foo": "bar"}
        assert isinstance(audio, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_generate_audio(self, client: ExCai, respx_mock: MockRouter) -> None:
        respx_mock.post("/audio/speech").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.audio.with_streaming_response.generate_audio(
            input="input",
            model="string",
            voice="ash",
        ) as audio:
            assert not audio.is_closed
            assert audio.http_request.headers.get("X-Stainless-Lang") == "python"

            assert audio.json() == {"foo": "bar"}
            assert cast(Any, audio.is_closed) is True
            assert isinstance(audio, StreamedBinaryAPIResponse)

        assert cast(Any, audio.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_transcribe_audio(self, client: ExCai) -> None:
        audio = client.audio.transcribe_audio(
            file=b"raw file contents",
            model="gpt-4o-transcribe",
        )
        assert_matches_type(AudioTranscribeAudioResponse, audio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_transcribe_audio_with_all_params(self, client: ExCai) -> None:
        audio = client.audio.transcribe_audio(
            file=b"raw file contents",
            model="gpt-4o-transcribe",
            chunking_strategy="auto",
            include=["logprobs"],
            language="language",
            prompt="prompt",
            response_format="json",
            stream=True,
            temperature=0,
            timestamp_granularities=["word"],
        )
        assert_matches_type(AudioTranscribeAudioResponse, audio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_transcribe_audio(self, client: ExCai) -> None:
        response = client.audio.with_raw_response.transcribe_audio(
            file=b"raw file contents",
            model="gpt-4o-transcribe",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audio = response.parse()
        assert_matches_type(AudioTranscribeAudioResponse, audio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_transcribe_audio(self, client: ExCai) -> None:
        with client.audio.with_streaming_response.transcribe_audio(
            file=b"raw file contents",
            model="gpt-4o-transcribe",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audio = response.parse()
            assert_matches_type(AudioTranscribeAudioResponse, audio, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_translate_audio(self, client: ExCai) -> None:
        audio = client.audio.translate_audio(
            file=b"raw file contents",
            model="whisper-1",
        )
        assert_matches_type(AudioTranslateAudioResponse, audio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_translate_audio_with_all_params(self, client: ExCai) -> None:
        audio = client.audio.translate_audio(
            file=b"raw file contents",
            model="whisper-1",
            prompt="prompt",
            response_format="json",
            temperature=0,
        )
        assert_matches_type(AudioTranslateAudioResponse, audio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_translate_audio(self, client: ExCai) -> None:
        response = client.audio.with_raw_response.translate_audio(
            file=b"raw file contents",
            model="whisper-1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audio = response.parse()
        assert_matches_type(AudioTranslateAudioResponse, audio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_translate_audio(self, client: ExCai) -> None:
        with client.audio.with_streaming_response.translate_audio(
            file=b"raw file contents",
            model="whisper-1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audio = response.parse()
            assert_matches_type(AudioTranslateAudioResponse, audio, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAudio:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_generate_audio(self, async_client: AsyncExCai, respx_mock: MockRouter) -> None:
        respx_mock.post("/audio/speech").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        audio = await async_client.audio.generate_audio(
            input="input",
            model="string",
            voice="ash",
        )
        assert audio.is_closed
        assert await audio.json() == {"foo": "bar"}
        assert cast(Any, audio.is_closed) is True
        assert isinstance(audio, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_generate_audio_with_all_params(
        self, async_client: AsyncExCai, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/audio/speech").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        audio = await async_client.audio.generate_audio(
            input="input",
            model="string",
            voice="ash",
            instructions="instructions",
            response_format="mp3",
            speed=0.25,
            stream_format="sse",
        )
        assert audio.is_closed
        assert await audio.json() == {"foo": "bar"}
        assert cast(Any, audio.is_closed) is True
        assert isinstance(audio, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_generate_audio(self, async_client: AsyncExCai, respx_mock: MockRouter) -> None:
        respx_mock.post("/audio/speech").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        audio = await async_client.audio.with_raw_response.generate_audio(
            input="input",
            model="string",
            voice="ash",
        )

        assert audio.is_closed is True
        assert audio.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await audio.json() == {"foo": "bar"}
        assert isinstance(audio, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_generate_audio(self, async_client: AsyncExCai, respx_mock: MockRouter) -> None:
        respx_mock.post("/audio/speech").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.audio.with_streaming_response.generate_audio(
            input="input",
            model="string",
            voice="ash",
        ) as audio:
            assert not audio.is_closed
            assert audio.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await audio.json() == {"foo": "bar"}
            assert cast(Any, audio.is_closed) is True
            assert isinstance(audio, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, audio.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_transcribe_audio(self, async_client: AsyncExCai) -> None:
        audio = await async_client.audio.transcribe_audio(
            file=b"raw file contents",
            model="gpt-4o-transcribe",
        )
        assert_matches_type(AudioTranscribeAudioResponse, audio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_transcribe_audio_with_all_params(self, async_client: AsyncExCai) -> None:
        audio = await async_client.audio.transcribe_audio(
            file=b"raw file contents",
            model="gpt-4o-transcribe",
            chunking_strategy="auto",
            include=["logprobs"],
            language="language",
            prompt="prompt",
            response_format="json",
            stream=True,
            temperature=0,
            timestamp_granularities=["word"],
        )
        assert_matches_type(AudioTranscribeAudioResponse, audio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_transcribe_audio(self, async_client: AsyncExCai) -> None:
        response = await async_client.audio.with_raw_response.transcribe_audio(
            file=b"raw file contents",
            model="gpt-4o-transcribe",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audio = await response.parse()
        assert_matches_type(AudioTranscribeAudioResponse, audio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_transcribe_audio(self, async_client: AsyncExCai) -> None:
        async with async_client.audio.with_streaming_response.transcribe_audio(
            file=b"raw file contents",
            model="gpt-4o-transcribe",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audio = await response.parse()
            assert_matches_type(AudioTranscribeAudioResponse, audio, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_translate_audio(self, async_client: AsyncExCai) -> None:
        audio = await async_client.audio.translate_audio(
            file=b"raw file contents",
            model="whisper-1",
        )
        assert_matches_type(AudioTranslateAudioResponse, audio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_translate_audio_with_all_params(self, async_client: AsyncExCai) -> None:
        audio = await async_client.audio.translate_audio(
            file=b"raw file contents",
            model="whisper-1",
            prompt="prompt",
            response_format="json",
            temperature=0,
        )
        assert_matches_type(AudioTranslateAudioResponse, audio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_translate_audio(self, async_client: AsyncExCai) -> None:
        response = await async_client.audio.with_raw_response.translate_audio(
            file=b"raw file contents",
            model="whisper-1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audio = await response.parse()
        assert_matches_type(AudioTranslateAudioResponse, audio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_translate_audio(self, async_client: AsyncExCai) -> None:
        async with async_client.audio.with_streaming_response.translate_audio(
            file=b"raw file contents",
            model="whisper-1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audio = await response.parse()
            assert_matches_type(AudioTranslateAudioResponse, audio, path=["response"])

        assert cast(Any, response.is_closed) is True
