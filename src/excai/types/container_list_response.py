# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ContainerListResponse", "Data", "DataExpiresAfter"]


class DataExpiresAfter(BaseModel):
    anchor: Optional[Literal["last_active_at"]] = None
    """The reference point for the expiration."""

    minutes: Optional[int] = None
    """The number of minutes after the anchor before the container expires."""


class Data(BaseModel):
    id: str
    """Unique identifier for the container."""

    created_at: int
    """Unix timestamp (in seconds) when the container was created."""

    name: str
    """Name of the container."""

    object: str
    """The type of this object."""

    status: str
    """Status of the container (e.g., active, deleted)."""

    expires_after: Optional[DataExpiresAfter] = None
    """
    The container will expire after this time period. The anchor is the reference
    point for the expiration. The minutes is the number of minutes after the anchor
    before the container expires.
    """


class ContainerListResponse(BaseModel):
    data: List[Data]
    """A list of containers."""

    first_id: str
    """The ID of the first container in the list."""

    has_more: bool
    """Whether there are more containers available."""

    last_id: str
    """The ID of the last container in the list."""

    object: Literal["list"]
    """The type of object returned, must be 'list'."""
