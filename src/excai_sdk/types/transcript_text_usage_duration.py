# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TranscriptTextUsageDuration"]


class TranscriptTextUsageDuration(BaseModel):
    """Usage statistics for models billed by audio input duration."""

    seconds: float
    """Duration of the input audio in seconds."""

    type: Literal["duration"]
    """The type of the usage object. Always `duration` for this variant."""
