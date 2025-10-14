# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CodeInterpreterOutputImage"]


class CodeInterpreterOutputImage(BaseModel):
    type: Literal["image"]
    """The type of the output. Always 'image'."""

    url: str
    """The URL of the image output from the code interpreter."""
