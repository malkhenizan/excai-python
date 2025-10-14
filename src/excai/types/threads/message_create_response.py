# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "MessageCreateResponse",
    "Attachment",
    "AttachmentTool",
    "AttachmentToolAssistantToolsCode",
    "AttachmentToolAssistantToolsFileSearchTypeOnly",
    "Content",
    "ContentImageFile",
    "ContentImageFileImageFile",
    "ContentImageURL",
    "ContentImageURLImageURL",
    "ContentText",
    "ContentTextText",
    "ContentTextTextAnnotation",
    "ContentTextTextAnnotationFileCitation",
    "ContentTextTextAnnotationFileCitationFileCitation",
    "ContentTextTextAnnotationFilePath",
    "ContentTextTextAnnotationFilePathFilePath",
    "ContentRefusal",
    "IncompleteDetails",
]


class AttachmentToolAssistantToolsCode(BaseModel):
    type: Literal["code_interpreter"]
    """The type of tool being defined: `code_interpreter`"""


class AttachmentToolAssistantToolsFileSearchTypeOnly(BaseModel):
    type: Literal["file_search"]
    """The type of tool being defined: `file_search`"""


AttachmentTool: TypeAlias = Union[AttachmentToolAssistantToolsCode, AttachmentToolAssistantToolsFileSearchTypeOnly]


class Attachment(BaseModel):
    file_id: Optional[str] = None
    """The ID of the file to attach to the message."""

    tools: Optional[List[AttachmentTool]] = None
    """The tools to add this file to."""


class ContentImageFileImageFile(BaseModel):
    file_id: str
    """
    The [File](https://platform.excai.com/docs/api-reference/files) ID of the image
    in the message content. Set `purpose="vision"` when uploading the File if you
    need to later display the file content.
    """

    detail: Optional[Literal["auto", "low", "high"]] = None
    """Specifies the detail level of the image if specified by the user.

    `low` uses fewer tokens, you can opt in to high resolution using `high`.
    """


class ContentImageFile(BaseModel):
    image_file: ContentImageFileImageFile

    type: Literal["image_file"]
    """Always `image_file`."""


class ContentImageURLImageURL(BaseModel):
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


class ContentImageURL(BaseModel):
    image_url: ContentImageURLImageURL

    type: Literal["image_url"]
    """The type of the content part."""


class ContentTextTextAnnotationFileCitationFileCitation(BaseModel):
    file_id: str
    """The ID of the specific File the citation is from."""


class ContentTextTextAnnotationFileCitation(BaseModel):
    end_index: int

    file_citation: ContentTextTextAnnotationFileCitationFileCitation

    start_index: int

    text: str
    """The text in the message content that needs to be replaced."""

    type: Literal["file_citation"]
    """Always `file_citation`."""


class ContentTextTextAnnotationFilePathFilePath(BaseModel):
    file_id: str
    """The ID of the file that was generated."""


class ContentTextTextAnnotationFilePath(BaseModel):
    end_index: int

    file_path: ContentTextTextAnnotationFilePathFilePath

    start_index: int

    text: str
    """The text in the message content that needs to be replaced."""

    type: Literal["file_path"]
    """Always `file_path`."""


ContentTextTextAnnotation: TypeAlias = Annotated[
    Union[ContentTextTextAnnotationFileCitation, ContentTextTextAnnotationFilePath], PropertyInfo(discriminator="type")
]


class ContentTextText(BaseModel):
    annotations: List[ContentTextTextAnnotation]

    value: str
    """The data that makes up the text."""


class ContentText(BaseModel):
    text: ContentTextText

    type: Literal["text"]
    """Always `text`."""


class ContentRefusal(BaseModel):
    refusal: str

    type: Literal["refusal"]
    """Always `refusal`."""


Content: TypeAlias = Annotated[
    Union[ContentImageFile, ContentImageURL, ContentText, ContentRefusal], PropertyInfo(discriminator="type")
]


class IncompleteDetails(BaseModel):
    reason: Literal["content_filter", "max_tokens", "run_cancelled", "run_expired", "run_failed"]
    """The reason the message is incomplete."""


class MessageCreateResponse(BaseModel):
    id: str
    """The identifier, which can be referenced in API endpoints."""

    assistant_id: Optional[str] = None
    """
    If applicable, the ID of the
    [assistant](https://platform.excai.com/docs/api-reference/assistants) that
    authored this message.
    """

    attachments: Optional[List[Attachment]] = None
    """A list of files attached to the message, and the tools they were added to."""

    completed_at: Optional[int] = None
    """The Unix timestamp (in seconds) for when the message was completed."""

    content: List[Content]
    """The content of the message in array of text and/or images."""

    created_at: int
    """The Unix timestamp (in seconds) for when the message was created."""

    incomplete_at: Optional[int] = None
    """The Unix timestamp (in seconds) for when the message was marked as incomplete."""

    incomplete_details: Optional[IncompleteDetails] = None
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
