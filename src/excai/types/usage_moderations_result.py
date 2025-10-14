# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["UsageModerationsResult"]


class UsageModerationsResult(BaseModel):
    input_tokens: int
    """The aggregated number of input tokens used."""

    num_model_requests: int
    """The count of requests made to the model."""

    object: Literal["organization.usage.moderations.result"]

    api_key_id: Optional[str] = None
    """
    When `group_by=api_key_id`, this field provides the API key ID of the grouped
    usage result.
    """

    model: Optional[str] = None
    """
    When `group_by=model`, this field provides the model name of the grouped usage
    result.
    """

    project_id: Optional[str] = None
    """
    When `group_by=project_id`, this field provides the project ID of the grouped
    usage result.
    """

    user_id: Optional[str] = None
    """
    When `group_by=user_id`, this field provides the user ID of the grouped usage
    result.
    """
