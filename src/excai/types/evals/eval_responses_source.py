# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["EvalResponsesSource"]


class EvalResponsesSource(BaseModel):
    type: Literal["responses"]
    """The type of run data source. Always `responses`."""

    allow_parallel_tool_calls: Optional[bool] = None
    """Whether to allow parallel tool calls.

    This is a query parameter used to select responses.
    """

    created_after: Optional[int] = None
    """Only include items created after this timestamp (inclusive).

    This is a query parameter used to select responses.
    """

    created_before: Optional[int] = None
    """Only include items created before this timestamp (inclusive).

    This is a query parameter used to select responses.
    """

    has_tool_calls: Optional[bool] = None
    """Whether the response has tool calls.

    This is a query parameter used to select responses.
    """

    instructions_search: Optional[str] = None
    """Optional search string for instructions.

    This is a query parameter used to select responses.
    """

    metadata: Optional[object] = None
    """Metadata filter for the responses.

    This is a query parameter used to select responses.
    """

    model: Optional[str] = None
    """The name of the model to find responses for.

    This is a query parameter used to select responses.
    """

    reasoning_effort: Optional[Literal["low", "medium", "high"]] = None
    """Optional reasoning effort parameter.

    This is a query parameter used to select responses.
    """

    temperature: Optional[float] = None
    """Sampling temperature. This is a query parameter used to select responses."""

    top_p: Optional[float] = None
    """Nucleus sampling parameter. This is a query parameter used to select responses."""

    users: Optional[List[str]] = None
    """List of user identifiers. This is a query parameter used to select responses."""
