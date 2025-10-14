# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["FileCitationBodyParam"]


class FileCitationBodyParam(TypedDict, total=False):
    file_id: Required[str]
    """The ID of the file."""

    filename: Required[str]
    """The filename of the file cited."""

    index: Required[int]
    """The index of the file in the list of files."""

    type: Required[Literal["file_citation"]]
    """The type of the file citation. Always `file_citation`."""
