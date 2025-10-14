# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["InputAudio"]


class InputAudio(BaseModel):
    type: Literal["input_audio"]
    """The type of the input item. Always `input_audio`."""

    input_audio: Optional[InputAudio] = FieldInfo(alias="input_audio_", default=None)
