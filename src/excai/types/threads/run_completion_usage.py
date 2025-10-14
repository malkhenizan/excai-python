# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["RunCompletionUsage"]


class RunCompletionUsage(BaseModel):
    completion_tokens: int
    """Number of completion tokens used over the course of the run."""

    prompt_tokens: int
    """Number of prompt tokens used over the course of the run."""

    total_tokens: int
    """Total number of tokens used (prompt + completion)."""
