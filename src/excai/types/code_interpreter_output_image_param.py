# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CodeInterpreterOutputImageParam"]


class CodeInterpreterOutputImageParam(TypedDict, total=False):
    type: Required[Literal["image"]]
    """The type of the output. Always 'image'."""

    url: Required[str]
    """The URL of the image output from the code interpreter."""
