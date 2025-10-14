# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .message_content_text_annotations_file_path_object import MessageContentTextAnnotationsFilePathObject
from .message_content_text_annotations_file_citation_object import MessageContentTextAnnotationsFileCitationObject

__all__ = ["MessageContentTextObject", "Text", "TextAnnotation"]

TextAnnotation: TypeAlias = Union[
    MessageContentTextAnnotationsFileCitationObject, MessageContentTextAnnotationsFilePathObject
]


class Text(BaseModel):
    annotations: List[TextAnnotation]

    value: str
    """The data that makes up the text."""


class MessageContentTextObject(BaseModel):
    text: Text

    type: Literal["text"]
    """Always `text`."""
