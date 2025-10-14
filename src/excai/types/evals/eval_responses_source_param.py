# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["EvalResponsesSourceParam"]


class EvalResponsesSourceParam(TypedDict, total=False):
    type: Required[Literal["responses"]]
    """The type of run data source. Always `responses`."""

    allow_parallel_tool_calls: Optional[bool]
    """Whether to allow parallel tool calls.

    This is a query parameter used to select responses.
    """

    created_after: Optional[int]
    """Only include items created after this timestamp (inclusive).

    This is a query parameter used to select responses.
    """

    created_before: Optional[int]
    """Only include items created before this timestamp (inclusive).

    This is a query parameter used to select responses.
    """

    has_tool_calls: Optional[bool]
    """Whether the response has tool calls.

    This is a query parameter used to select responses.
    """

    instructions_search: Optional[str]
    """Optional search string for instructions.

    This is a query parameter used to select responses.
    """

    metadata: Optional[object]
    """Metadata filter for the responses.

    This is a query parameter used to select responses.
    """

    model: Optional[str]
    """The name of the model to find responses for.

    This is a query parameter used to select responses.
    """

    reasoning_effort: Optional[Literal["low", "medium", "high"]]
    """Optional reasoning effort parameter.

    This is a query parameter used to select responses.
    """

    temperature: Optional[float]
    """Sampling temperature. This is a query parameter used to select responses."""

    top_p: Optional[float]
    """Nucleus sampling parameter. This is a query parameter used to select responses."""

    users: Optional[SequenceNotStr[str]]
    """List of user identifiers. This is a query parameter used to select responses."""
