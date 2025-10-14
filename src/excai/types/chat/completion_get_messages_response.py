# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .chat_completion_response_message import ChatCompletionResponseMessage

__all__ = [
    "CompletionGetMessagesResponse",
    "Data",
    "DataContentPart",
    "DataContentPartChatCompletionRequestMessageContentPartText",
    "DataContentPartChatCompletionRequestMessageContentPartImage",
    "DataContentPartChatCompletionRequestMessageContentPartImageImageURL",
]


class DataContentPartChatCompletionRequestMessageContentPartText(BaseModel):
    text: str
    """The text content."""

    type: Literal["text"]
    """The type of the content part."""


class DataContentPartChatCompletionRequestMessageContentPartImageImageURL(BaseModel):
    url: str
    """Either a URL of the image or the base64 encoded image data."""

    detail: Optional[Literal["auto", "low", "high"]] = None
    """Specifies the detail level of the image.

    Learn more in the
    [Vision guide](https://platform.excai.com/docs/guides/vision#low-or-high-fidelity-image-understanding).
    """


class DataContentPartChatCompletionRequestMessageContentPartImage(BaseModel):
    image_url: DataContentPartChatCompletionRequestMessageContentPartImageImageURL

    type: Literal["image_url"]
    """The type of the content part."""


DataContentPart: TypeAlias = Union[
    DataContentPartChatCompletionRequestMessageContentPartText,
    DataContentPartChatCompletionRequestMessageContentPartImage,
]


class Data(ChatCompletionResponseMessage):
    id: str
    """The identifier of the chat message."""

    content_parts: Optional[List[DataContentPart]] = None
    """
    If a content parts array was provided, this is an array of `text` and
    `image_url` parts. Otherwise, null.
    """


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
