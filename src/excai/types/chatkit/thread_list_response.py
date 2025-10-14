# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = ["ThreadListResponse", "Data", "DataStatus", "DataStatusActive", "DataStatusLocked", "DataStatusClosed"]


class DataStatusActive(BaseModel):
    type: Literal["active"]
    """Status discriminator that is always `active`."""


class DataStatusLocked(BaseModel):
    reason: Optional[str] = None
    """Reason that the thread was locked. Defaults to null when no reason is recorded."""

    type: Literal["locked"]
    """Status discriminator that is always `locked`."""


class DataStatusClosed(BaseModel):
    reason: Optional[str] = None
    """Reason that the thread was closed. Defaults to null when no reason is recorded."""

    type: Literal["closed"]
    """Status discriminator that is always `closed`."""


DataStatus: TypeAlias = Annotated[
    Union[DataStatusActive, DataStatusLocked, DataStatusClosed], PropertyInfo(discriminator="type")
]


class Data(BaseModel):
    id: str
    """Identifier of the thread."""

    created_at: int
    """Unix timestamp (in seconds) for when the thread was created."""

    object: Literal["chatkit.thread"]
    """Type discriminator that is always `chatkit.thread`."""

    status: DataStatus
    """Current status for the thread. Defaults to `active` for newly created threads."""

    title: Optional[str] = None
    """Optional human-readable title for the thread.

    Defaults to null when no title has been generated.
    """

    user: str
    """Free-form string that identifies your end user who owns the thread."""


class ThreadListResponse(BaseModel):
    data: List[Data]
    """A list of items"""

    first_id: Optional[str] = None
    """The ID of the first item in the list."""

    has_more: bool
    """Whether there are more items available."""

    last_id: Optional[str] = None
    """The ID of the last item in the list."""

    object: Literal["list"]
    """The type of object returned, must be `list`."""
