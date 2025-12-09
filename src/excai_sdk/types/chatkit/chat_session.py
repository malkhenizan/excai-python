# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "ChatSession",
    "ChatkitConfiguration",
    "ChatkitConfigurationAutomaticThreadTitling",
    "ChatkitConfigurationFileUpload",
    "ChatkitConfigurationHistory",
    "RateLimits",
    "Workflow",
    "WorkflowTracing",
]


class ChatkitConfigurationAutomaticThreadTitling(BaseModel):
    """Automatic thread titling preferences."""

    enabled: bool
    """Whether automatic thread titling is enabled."""


class ChatkitConfigurationFileUpload(BaseModel):
    """Upload settings for the session."""

    enabled: bool
    """Indicates if uploads are enabled for the session."""

    max_file_size: Optional[int] = None
    """Maximum upload size in megabytes."""

    max_files: Optional[int] = None
    """Maximum number of uploads allowed during the session."""


class ChatkitConfigurationHistory(BaseModel):
    """History retention configuration."""

    enabled: bool
    """Indicates if chat history is persisted for the session."""

    recent_threads: Optional[int] = None
    """Number of prior threads surfaced in history views.

    Defaults to null when all history is retained.
    """


class ChatkitConfiguration(BaseModel):
    """Resolved ChatKit feature configuration for the session."""

    automatic_thread_titling: ChatkitConfigurationAutomaticThreadTitling
    """Automatic thread titling preferences."""

    file_upload: ChatkitConfigurationFileUpload
    """Upload settings for the session."""

    history: ChatkitConfigurationHistory
    """History retention configuration."""


class RateLimits(BaseModel):
    """Resolved rate limit values."""

    max_requests_per_1_minute: int
    """Maximum allowed requests per one-minute window."""


class WorkflowTracing(BaseModel):
    """Tracing settings applied to the workflow."""

    enabled: bool
    """Indicates whether tracing is enabled."""


class Workflow(BaseModel):
    """Workflow metadata for the session."""

    id: str
    """Identifier of the workflow backing the session."""

    state_variables: Optional[Dict[str, Union[str, bool, float]]] = None
    """State variable key-value pairs applied when invoking the workflow.

    Defaults to null when no overrides were provided.
    """

    tracing: WorkflowTracing
    """Tracing settings applied to the workflow."""

    version: Optional[str] = None
    """Specific workflow version used for the session.

    Defaults to null when using the latest deployment.
    """


class ChatSession(BaseModel):
    """Represents a ChatKit session and its resolved configuration."""

    id: str
    """Identifier for the ChatKit session."""

    chatkit_configuration: ChatkitConfiguration
    """Resolved ChatKit feature configuration for the session."""

    client_secret: str
    """Ephemeral client secret that authenticates session requests."""

    expires_at: int
    """Unix timestamp (in seconds) for when the session expires."""

    max_requests_per_1_minute: int
    """Convenience copy of the per-minute request limit."""

    object: Literal["chatkit.session"]
    """Type discriminator that is always `chatkit.session`."""

    rate_limits: RateLimits
    """Resolved rate limit values."""

    status: Literal["active", "expired", "cancelled"]
    """Current lifecycle state of the session."""

    user: str
    """User identifier associated with the session."""

    workflow: Workflow
    """Workflow metadata for the session."""
