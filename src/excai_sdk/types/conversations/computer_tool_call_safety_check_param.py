# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ComputerToolCallSafetyCheckParam"]


class ComputerToolCallSafetyCheckParam(TypedDict, total=False):
    """A pending safety check for the computer call."""

    id: Required[str]
    """The ID of the pending safety check."""

    code: Required[str]
    """The type of the pending safety check."""

    message: Required[str]
    """Details about the pending safety check."""
