# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "MessageListResponse",
    "Data",
    "DataAttachment",
    "DataAttachmentTool",
    "DataAttachmentToolAssistantToolsCode",
    "DataAttachmentToolAssistantToolsFileSearchTypeOnly",
    "DataContent",
    "DataContentMessageContentImageFileObject",
    "DataContentMessageContentImageFileObjectImageFile",
    "DataContentMessageContentImageURLObject",
    "DataContentMessageContentImageURLObjectImageURL",
    "DataContentMessageContentTextObject",
    "DataContentMessageContentTextObjectText",
    "DataContentMessageContentTextObjectTextAnnotation",
    "DataContentMessageContentTextObjectTextAnnotationMessageContentTextAnnotationsFileCitationObject",
    "DataContentMessageContentTextObjectTextAnnotationMessageContentTextAnnotationsFileCitationObjectFileCitation",
    "DataContentMessageContentTextObjectTextAnnotationMessageContentTextAnnotationsFilePathObject",
    "DataContentMessageContentTextObjectTextAnnotationMessageContentTextAnnotationsFilePathObjectFilePath",
    "DataContentMessageContentRefusalObject",
    "DataIncompleteDetails",
]


class DataAttachmentToolAssistantToolsCode(BaseModel):
    type: Literal["code_interpreter"]
    """The type of tool being defined: `code_interpreter`"""


class DataAttachmentToolAssistantToolsFileSearchTypeOnly(BaseModel):
    type: Literal["file_search"]
    """The type of tool being defined: `file_search`"""


DataAttachmentTool: TypeAlias = Union[
    DataAttachmentToolAssistantToolsCode, DataAttachmentToolAssistantToolsFileSearchTypeOnly
]


class DataAttachment(BaseModel):
    file_id: Optional[str] = None
    """The ID of the file to attach to the message."""

    tools: Optional[List[DataAttachmentTool]] = None
    """The tools to add this file to."""


class DataContentMessageContentImageFileObjectImageFile(BaseModel):
    file_id: str
    """The [File](/docs/api-reference/files) ID of the image in the message content.

    Set `purpose="vision"` when uploading the File if you need to later display the
    file content.
    """

    detail: Optional[Literal["auto", "low", "high"]] = None
    """Specifies the detail level of the image if specified by the user.

    `low` uses fewer tokens, you can opt in to high resolution using `high`.
    """


class DataContentMessageContentImageFileObject(BaseModel):
    image_file: DataContentMessageContentImageFileObjectImageFile

    type: Literal["image_file"]
    """Always `image_file`."""


class DataContentMessageContentImageURLObjectImageURL(BaseModel):
    url: str
    """
    The external URL of the image, must be a supported image types: jpeg, jpg, png,
    gif, webp.
    """

    detail: Optional[Literal["auto", "low", "high"]] = None
    """Specifies the detail level of the image.

    `low` uses fewer tokens, you can opt in to high resolution using `high`. Default
    value is `auto`
    """


class DataContentMessageContentImageURLObject(BaseModel):
    image_url: DataContentMessageContentImageURLObjectImageURL

    type: Literal["image_url"]
    """The type of the content part."""


class DataContentMessageContentTextObjectTextAnnotationMessageContentTextAnnotationsFileCitationObjectFileCitation(
    BaseModel
):
    file_id: str
    """The ID of the specific File the citation is from."""


class DataContentMessageContentTextObjectTextAnnotationMessageContentTextAnnotationsFileCitationObject(BaseModel):
    end_index: int

    file_citation: (
        DataContentMessageContentTextObjectTextAnnotationMessageContentTextAnnotationsFileCitationObjectFileCitation
    )

    start_index: int

    text: str
    """The text in the message content that needs to be replaced."""

    type: Literal["file_citation"]
    """Always `file_citation`."""


class DataContentMessageContentTextObjectTextAnnotationMessageContentTextAnnotationsFilePathObjectFilePath(BaseModel):
    file_id: str
    """The ID of the file that was generated."""


class DataContentMessageContentTextObjectTextAnnotationMessageContentTextAnnotationsFilePathObject(BaseModel):
    end_index: int

    file_path: DataContentMessageContentTextObjectTextAnnotationMessageContentTextAnnotationsFilePathObjectFilePath

    start_index: int

    text: str
    """The text in the message content that needs to be replaced."""

    type: Literal["file_path"]
    """Always `file_path`."""


DataContentMessageContentTextObjectTextAnnotation: TypeAlias = Union[
    DataContentMessageContentTextObjectTextAnnotationMessageContentTextAnnotationsFileCitationObject,
    DataContentMessageContentTextObjectTextAnnotationMessageContentTextAnnotationsFilePathObject,
]


class DataContentMessageContentTextObjectText(BaseModel):
    annotations: List[DataContentMessageContentTextObjectTextAnnotation]

    value: str
    """The data that makes up the text."""


class DataContentMessageContentTextObject(BaseModel):
    text: DataContentMessageContentTextObjectText

    type: Literal["text"]
    """Always `text`."""


class DataContentMessageContentRefusalObject(BaseModel):
    refusal: str

    type: Literal["refusal"]
    """Always `refusal`."""


DataContent: TypeAlias = Union[
    DataContentMessageContentImageFileObject,
    DataContentMessageContentImageURLObject,
    DataContentMessageContentTextObject,
    DataContentMessageContentRefusalObject,
]


class DataIncompleteDetails(BaseModel):
    reason: Literal["content_filter", "max_tokens", "run_cancelled", "run_expired", "run_failed"]
    """The reason the message is incomplete."""


class Data(BaseModel):
    id: str
    """The identifier, which can be referenced in API endpoints."""

    assistant_id: Optional[str] = None
    """
    If applicable, the ID of the [assistant](/docs/api-reference/assistants) that
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
    The ID of the [run](/docs/api-reference/runs) associated with the creation of
    this message. Value is `null` when messages are created manually using the
    create message or create thread endpoints.
    """

    status: Literal["in_progress", "incomplete", "completed"]
    """
    The status of the message, which can be either `in_progress`, `incomplete`, or
    `completed`.
    """

    thread_id: str
    """The [thread](/docs/api-reference/threads) ID that this message belongs to."""


class MessageListResponse(BaseModel):
    data: List[Data]

    first_id: str

    has_more: bool

    last_id: str

    object: str
