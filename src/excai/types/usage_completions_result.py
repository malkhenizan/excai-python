# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["UsageCompletionsResult"]


class UsageCompletionsResult(BaseModel):
    input_tokens: int
    """The aggregated number of text input tokens used, including cached tokens.

    For customers subscribe to scale tier, this includes scale tier tokens.
    """

    num_model_requests: int
    """The count of requests made to the model."""

    object: Literal["organization.usage.completions.result"]

    output_tokens: int
    """The aggregated number of text output tokens used.

    For customers subscribe to scale tier, this includes scale tier tokens.
    """

    api_key_id: Optional[str] = None
    """
    When `group_by=api_key_id`, this field provides the API key ID of the grouped
    usage result.
    """

    batch: Optional[bool] = None
    """
    When `group_by=batch`, this field tells whether the grouped usage result is
    batch or not.
    """

    input_audio_tokens: Optional[int] = None
    """The aggregated number of audio input tokens used, including cached tokens."""

    input_cached_tokens: Optional[int] = None
    """
    The aggregated number of text input tokens that has been cached from previous
    requests. For customers subscribe to scale tier, this includes scale tier
    tokens.
    """

    model: Optional[str] = None
    """
    When `group_by=model`, this field provides the model name of the grouped usage
    result.
    """

    output_audio_tokens: Optional[int] = None
    """The aggregated number of audio output tokens used."""

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
