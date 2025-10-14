# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["CodeInterpreterToolAuto"]


class CodeInterpreterToolAuto(TypedDict, total=False):
    type: Required[Literal["auto"]]
    """Always `auto`."""

    file_ids: SequenceNotStr[str]
    """An optional list of uploaded files to make available to your code."""
