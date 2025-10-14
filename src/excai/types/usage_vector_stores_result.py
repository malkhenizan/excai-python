# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["UsageVectorStoresResult"]


class UsageVectorStoresResult(BaseModel):
    object: Literal["organization.usage.vector_stores.result"]

    usage_bytes: int
    """The vector stores usage in bytes."""

    project_id: Optional[str] = None
    """
    When `group_by=project_id`, this field provides the project ID of the grouped
    usage result.
    """
