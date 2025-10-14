# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ProjectListResponse", "Data"]


class Data(BaseModel):
    id: str
    """The identifier, which can be referenced in API endpoints"""

    created_at: int
    """The Unix timestamp (in seconds) of when the project was created."""

    name: str
    """The name of the project. This appears in reporting."""

    object: Literal["organization.project"]
    """The object type, which is always `organization.project`"""

    status: Literal["active", "archived"]
    """`active` or `archived`"""

    archived_at: Optional[int] = None
    """The Unix timestamp (in seconds) of when the project was archived or `null`."""


class ProjectListResponse(BaseModel):
    data: List[Data]

    first_id: str

    has_more: bool

    last_id: str

    object: Literal["list"]
