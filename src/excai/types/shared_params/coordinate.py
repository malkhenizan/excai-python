# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["Coordinate"]


class Coordinate(TypedDict, total=False):
    x: Required[int]
    """The x-coordinate."""

    y: Required[int]
    """The y-coordinate."""
