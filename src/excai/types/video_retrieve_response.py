# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .error_2 import Error2
from .._models import BaseModel

__all__ = ["VideoRetrieveResponse"]


class VideoRetrieveResponse(BaseModel):
    id: str
    """Unique identifier for the video job."""

    completed_at: Optional[int] = None
    """Unix timestamp (seconds) for when the job completed, if finished."""

    created_at: int
    """Unix timestamp (seconds) for when the job was created."""

    error: Optional[Error2] = None
    """Error payload that explains why generation failed, if applicable."""

    expires_at: Optional[int] = None
    """Unix timestamp (seconds) for when the downloadable assets expire, if set."""

    model: Literal["sora-2", "sora-2-pro"]
    """The video generation model that produced the job."""

    object: Literal["video"]
    """The object type, which is always `video`."""

    progress: int
    """Approximate completion percentage for the generation task."""

    remixed_from_video_id: Optional[str] = None
    """Identifier of the source video if this video is a remix."""

    seconds: Literal["4", "8", "12"]
    """Duration of the generated clip in seconds."""

    size: Literal["720x1280", "1280x720", "1024x1792", "1792x1024"]
    """The resolution of the generated video."""

    status: Literal["queued", "in_progress", "completed", "failed"]
    """Current lifecycle status of the video job."""
