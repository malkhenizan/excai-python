# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["ServiceAccountListResponse", "Data"]


class Data(BaseModel):
    id: str
    """The identifier, which can be referenced in API endpoints"""

    created_at: int
    """The Unix timestamp (in seconds) of when the service account was created"""

    name: str
    """The name of the service account"""

    object: Literal["organization.project.service_account"]
    """The object type, which is always `organization.project.service_account`"""

    role: Literal["owner", "member"]
    """`owner` or `member`"""


class ServiceAccountListResponse(BaseModel):
    data: List[Data]

    first_id: str

    has_more: bool

    last_id: str

    object: Literal["list"]
