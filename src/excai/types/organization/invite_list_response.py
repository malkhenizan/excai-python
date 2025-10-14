# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["InviteListResponse", "Data", "DataProject"]


class DataProject(BaseModel):
    id: Optional[str] = None
    """Project's public ID"""

    role: Optional[Literal["member", "owner"]] = None
    """Project membership role"""


class Data(BaseModel):
    id: str
    """The identifier, which can be referenced in API endpoints"""

    email: str
    """The email address of the individual to whom the invite was sent"""

    expires_at: int
    """The Unix timestamp (in seconds) of when the invite expires."""

    invited_at: int
    """The Unix timestamp (in seconds) of when the invite was sent."""

    object: Literal["organization.invite"]
    """The object type, which is always `organization.invite`"""

    role: Literal["owner", "reader"]
    """`owner` or `reader`"""

    status: Literal["accepted", "expired", "pending"]
    """`accepted`,`expired`, or `pending`"""

    accepted_at: Optional[int] = None
    """The Unix timestamp (in seconds) of when the invite was accepted."""

    projects: Optional[List[DataProject]] = None
    """The projects that were granted membership upon acceptance of the invite."""


class InviteListResponse(BaseModel):
    data: List[Data]

    object: Literal["list"]
    """The object type, which is always `list`"""

    first_id: Optional[str] = None
    """The first `invite_id` in the retrieved `list`"""

    has_more: Optional[bool] = None
    """
    The `has_more` property is used for pagination to indicate there are additional
    results.
    """

    last_id: Optional[str] = None
    """The last `invite_id` in the retrieved `list`"""
