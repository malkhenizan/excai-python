# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["InputAudio"]


class InputAudio(TypedDict, total=False):
    input_audio: Required[InputAudio]

    type: Required[Literal["input_audio"]]
    """The type of the input item. Always `input_audio`."""
