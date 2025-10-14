# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["InputAudio"]


class InputAudio(BaseModel):
    input_audio: InputAudio

    type: Literal["input_audio"]
    """The type of the input item. Always `input_audio`."""
