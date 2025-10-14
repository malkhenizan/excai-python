# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .image import Image
from .._models import BaseModel
from .image_gen_usage import ImageGenUsage

__all__ = ["ImageCreateImageResponse"]


class ImageCreateImageResponse(BaseModel):
    created: int
    """The Unix timestamp (in seconds) of when the image was created."""

    background: Optional[Literal["transparent", "opaque"]] = None
    """The background parameter used for the image generation.

    Either `transparent` or `opaque`.
    """

    data: Optional[List[Image]] = None
    """The list of generated images."""

    output_format: Optional[Literal["png", "webp", "jpeg"]] = None
    """The output format of the image generation. Either `png`, `webp`, or `jpeg`."""

    quality: Optional[Literal["low", "medium", "high"]] = None
    """The quality of the image generated. Either `low`, `medium`, or `high`."""

    size: Optional[Literal["1024x1024", "1024x1536", "1536x1024"]] = None
    """The size of the image generated.

    Either `1024x1024`, `1024x1536`, or `1536x1024`.
    """

    usage: Optional[ImageGenUsage] = None
    """For `gpt-image-1` only, the token usage information for the image generation."""
