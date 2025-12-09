# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .reasoning_text_content import ReasoningTextContent

__all__ = ["ReasoningItem", "Summary"]


class Summary(BaseModel):
    """A summary text from the model."""

    text: str
    """A summary of the reasoning output from the model so far."""

    type: Literal["summary_text"]
    """The type of the object. Always `summary_text`."""


class ReasoningItem(BaseModel):
    """
    A description of the chain of thought used by a reasoning model while generating
    a response. Be sure to include these items in your `input` to the Responses API
    for subsequent turns of a conversation if you are manually
    [managing context](https://main.excai.ai/docs/guides/conversation-state).
    """

    id: str
    """The unique identifier of the reasoning content."""

    summary: List[Summary]
    """Reasoning summary content."""

    type: Literal["reasoning"]
    """The type of the object. Always `reasoning`."""

    content: Optional[List[ReasoningTextContent]] = None
    """Reasoning text content."""

    encrypted_content: Optional[str] = None
    """
    The encrypted content of the reasoning item - populated when a response is
    generated with `reasoning.encrypted_content` in the `include` parameter.
    """

    status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    """The status of the item.

    One of `in_progress`, `completed`, or `incomplete`. Populated when items are
    returned via API.
    """
