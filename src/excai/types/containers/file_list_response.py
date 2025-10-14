# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["FileListResponse", "Data"]


class Data(BaseModel):
    id: str
    """Unique identifier for the file."""

    bytes: int
    """Size of the file in bytes."""

    container_id: str
    """The container this file belongs to."""

    created_at: int
    """Unix timestamp (in seconds) when the file was created."""

    object: Literal["container.file"]
    """The type of this object (`container.file`)."""

    path: str
    """Path of the file in the container."""

    source: str
    """Source of the file (e.g., `user`, `assistant`)."""


class FileListResponse(BaseModel):
    data: List[Data]
    """A list of container files."""

    first_id: str
    """The ID of the first file in the list."""

    has_more: bool
    """Whether there are more files available."""

    last_id: str
    """The ID of the last file in the list."""

    object: Literal["list"]
    """The type of object returned, must be 'list'."""
