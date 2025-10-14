# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel
from .chat_completion_response_message import ChatCompletionResponseMessage

__all__ = ["CompletionGetMessagesResponse", "Data"]


class Data(ChatCompletionResponseMessage):
    id: str
    """The identifier of the chat message."""


class CompletionGetMessagesResponse(BaseModel):
    data: List[Data]
    """An array of chat completion message objects."""

    first_id: str
    """The identifier of the first chat message in the data array."""

    has_more: bool
    """Indicates whether there are more chat messages available."""

    last_id: str
    """The identifier of the last chat message in the data array."""

    object: Literal["list"]
    """The type of this object. It is always set to "list"."""
