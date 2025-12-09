# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, TypeAlias, TypedDict

__all__ = ["RealtimeAudioFormatsParam", "AudioPcm", "AudioPcmu", "AudioPcma"]


class AudioPcm(TypedDict, total=False):
    """The PCM audio format. Only a 24kHz sample rate is supported."""

    rate: Literal[24000]
    """The sample rate of the audio. Always `24000`."""

    type: Literal["audio/pcm"]
    """The audio format. Always `audio/pcm`."""


class AudioPcmu(TypedDict, total=False):
    """The G.711 μ-law format."""

    type: Literal["audio/pcmu"]
    """The audio format. Always `audio/pcmu`."""


class AudioPcma(TypedDict, total=False):
    """The G.711 A-law format."""

    type: Literal["audio/pcma"]
    """The audio format. Always `audio/pcma`."""


RealtimeAudioFormatsParam: TypeAlias = Union[AudioPcm, AudioPcmu, AudioPcma]
