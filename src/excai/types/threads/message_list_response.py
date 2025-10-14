# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .message_content_text_object import MessageContentTextObject
from ..shared.assistant_tools_code import AssistantToolsCode
from .message_content_refusal_object import MessageContentRefusalObject
from .message_content_image_url_object import MessageContentImageURLObject
from .message_content_image_file_object import MessageContentImageFileObject
from ..assistant_tools_file_search_type_only import AssistantToolsFileSearchTypeOnly

__all__ = [
    "MessageListResponse",
    "Data",
    "DataAttachment",
    "DataAttachmentTool",
    "DataContent",
    "DataIncompleteDetails",
]

DataAttachmentTool: TypeAlias = Union[AssistantToolsCode, AssistantToolsFileSearchTypeOnly]


class DataAttachment(BaseModel):
    file_id: Optional[str] = None
    """The ID of the file to attach to the message."""

    tools: Optional[List[DataAttachmentTool]] = None
    """The tools to add this file to."""


DataContent: TypeAlias = Annotated[
    Union[
        MessageContentImageFileObject,
        MessageContentImageURLObject,
        MessageContentTextObject,
        MessageContentRefusalObject,
    ],
    PropertyInfo(discriminator="type"),
]


class DataIncompleteDetails(BaseModel):
    reason: Literal["content_filter", "max_tokens", "run_cancelled", "run_expired", "run_failed"]
    """The reason the message is incomplete."""


class Data(BaseModel):
    id: str
    """The identifier, which can be referenced in API endpoints."""

    assistant_id: Optional[str] = None
    """
    If applicable, the ID of the
    [assistant](https://platform.excai.com/docs/api-reference/assistants) that
    authored this message.
    """

    attachments: Optional[List[DataAttachment]] = None
    """A list of files attached to the message, and the tools they were added to."""

    completed_at: Optional[int] = None
    """The Unix timestamp (in seconds) for when the message was completed."""

    content: List[DataContent]
    """The content of the message in array of text and/or images."""

    created_at: int
    """The Unix timestamp (in seconds) for when the message was created."""

    incomplete_at: Optional[int] = None
    """The Unix timestamp (in seconds) for when the message was marked as incomplete."""

    incomplete_details: Optional[DataIncompleteDetails] = None
    """On an incomplete message, details about why the message is incomplete."""

    metadata: Optional[Dict[str, str]] = None
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings with
    a maximum length of 512 characters.
    """

    object: Literal["thread.message"]
    """The object type, which is always `thread.message`."""

    role: Literal["user", "assistant"]
    """The entity that produced the message. One of `user` or `assistant`."""

    run_id: Optional[str] = None
    """
    The ID of the [run](https://platform.excai.com/docs/api-reference/runs)
    associated with the creation of this message. Value is `null` when messages are
    created manually using the create message or create thread endpoints.
    """

    status: Literal["in_progress", "incomplete", "completed"]
    """
    The status of the message, which can be either `in_progress`, `incomplete`, or
    `completed`.
    """

    thread_id: str
    """
    The [thread](https://platform.excai.com/docs/api-reference/threads) ID that this
    message belongs to.
    """


class MessageListResponse(BaseModel):
    data: List[Data]

    first_id: str

    has_more: bool

    last_id: str

    object: str
