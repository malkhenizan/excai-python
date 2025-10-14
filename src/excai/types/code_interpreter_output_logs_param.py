# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CodeInterpreterOutputLogsParam"]


class CodeInterpreterOutputLogsParam(TypedDict, total=False):
    logs: Required[str]
    """The logs output from the code interpreter."""

    type: Required[Literal["logs"]]
    """The type of the output. Always 'logs'."""
