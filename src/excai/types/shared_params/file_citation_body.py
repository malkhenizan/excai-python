# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["FileCitationBody"]


class FileCitationBody(TypedDict, total=False):
    file_id: Required[str]
    """The ID of the file."""

    index: Required[int]
    """The index of the file in the list of files."""

    type: Required[Literal["file_citation"]]
    """The type of the file citation. Always `file_citation`."""
