# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["APIKeyRetrieveResponse", "Owner", "OwnerServiceAccount", "OwnerUser"]


class OwnerServiceAccount(BaseModel):
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


class OwnerUser(BaseModel):
    id: str
    """The identifier, which can be referenced in API endpoints"""

    added_at: int
    """The Unix timestamp (in seconds) of when the project was added."""

    email: str
    """The email address of the user"""

    name: str
    """The name of the user"""

    object: Literal["organization.project.user"]
    """The object type, which is always `organization.project.user`"""

    role: Literal["owner", "member"]
    """`owner` or `member`"""


class Owner(BaseModel):
    service_account: Optional[OwnerServiceAccount] = None
    """Represents an individual service account in a project."""

    type: Optional[Literal["user", "service_account"]] = None
    """`user` or `service_account`"""

    user: Optional[OwnerUser] = None
    """Represents an individual user in a project."""


class APIKeyRetrieveResponse(BaseModel):
    id: str
    """The identifier, which can be referenced in API endpoints"""

    created_at: int
    """The Unix timestamp (in seconds) of when the API key was created"""

    last_used_at: int
    """The Unix timestamp (in seconds) of when the API key was last used."""

    name: str
    """The name of the API key"""

    object: Literal["organization.project.api_key"]
    """The object type, which is always `organization.project.api_key`"""

    owner: Owner

    redacted_value: str
    """The redacted value of the API key"""
