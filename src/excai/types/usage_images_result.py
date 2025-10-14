# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["UsageImagesResult"]


class UsageImagesResult(BaseModel):
    images: int
    """The number of images processed."""

    num_model_requests: int
    """The count of requests made to the model."""

    object: Literal["organization.usage.images.result"]

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

    size: Optional[str] = None
    """
    When `group_by=size`, this field provides the image size of the grouped usage
    result.
    """

    source: Optional[str] = None
    """
    When `group_by=source`, this field provides the source of the grouped usage
    result, possible values are `image.generation`, `image.edit`, `image.variation`.
    """

    user_id: Optional[str] = None
    """
    When `group_by=user_id`, this field provides the user ID of the grouped usage
    result.
    """
