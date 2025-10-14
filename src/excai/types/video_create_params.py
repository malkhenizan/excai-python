# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .._types import FileTypes

__all__ = ["VideoCreateParams"]


class VideoCreateParams(TypedDict, total=False):
    prompt: Required[str]
    """Text prompt that describes the video to generate."""

    input_reference: FileTypes
    """Optional image reference that guides generation."""

    model: Literal["sora-2", "sora-2-pro"]
    """The video generation model to use. Defaults to `sora-2`."""

    seconds: Literal["4", "8", "12"]
    """Clip duration in seconds. Defaults to 4 seconds."""

    size: Literal["720x1280", "1280x720", "1024x1792", "1792x1024"]
    """Output resolution formatted as width x height. Defaults to 720x1280."""
