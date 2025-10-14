# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .summary import Summary
from .reasoning_text_content import ReasoningTextContent

__all__ = ["ReasoningItem"]


class ReasoningItem(TypedDict, total=False):
    id: Required[str]
    """The unique identifier of the reasoning content."""

    summary: Required[Iterable[Summary]]
    """Reasoning summary content."""

    type: Required[Literal["reasoning"]]
    """The type of the object. Always `reasoning`."""

    content: Iterable[ReasoningTextContent]
    """Reasoning text content."""

    encrypted_content: Optional[str]
    """
    The encrypted content of the reasoning item - populated when a response is
    generated with `reasoning.encrypted_content` in the `include` parameter.
    """

    status: Literal["in_progress", "completed", "incomplete"]
    """The status of the item.

    One of `in_progress`, `completed`, or `incomplete`. Populated when items are
    returned via API.
    """
