# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["InputAudioParam", "InputAudio"]


class InputAudio(TypedDict, total=False):
    data: Required[str]
    """Base64-encoded audio data."""

    format: Required[Literal["mp3", "wav"]]
    """The format of the audio data. Currently supported formats are `mp3` and `wav`."""


class InputAudioParam(TypedDict, total=False):
    type: Required[Literal["input_audio"]]
    """The type of the input item. Always `input_audio`."""

    input_audio: Annotated[InputAudio, PropertyInfo(alias="input_audio_")]
