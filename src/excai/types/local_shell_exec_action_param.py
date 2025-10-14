# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["LocalShellExecActionParam"]


class LocalShellExecActionParam(TypedDict, total=False):
    command: Required[SequenceNotStr[str]]
    """The command to run."""

    env: Required[Dict[str, str]]
    """Environment variables to set for the command."""

    type: Required[Literal["exec"]]
    """The type of the local shell action. Always `exec`."""

    timeout_ms: Optional[int]
    """Optional timeout in milliseconds for the command."""

    user: Optional[str]
    """Optional user to run the command as."""

    working_directory: Optional[str]
    """Optional working directory to run the command in."""
