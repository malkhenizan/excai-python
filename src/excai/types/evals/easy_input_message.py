# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from ..shared.input_file_content import InputFileContent
from ..shared.input_text_content import InputTextContent
from ..shared.input_image_content import InputImageContent

__all__ = ["EasyInputMessage", "ContentInputMessageContentList"]

ContentInputMessageContentList: TypeAlias = Union[InputTextContent, InputImageContent, InputFileContent]


class EasyInputMessage(BaseModel):
    content: Union[str, List[ContentInputMessageContentList]]
    """
    Text, image, or audio input to the model, used to generate a response. Can also
    contain previous assistant responses.
    """

    role: Literal["user", "assistant", "system", "developer"]
    """The role of the message input.

    One of `user`, `assistant`, `system`, or `developer`.
    """

    type: Optional[Literal["message"]] = None
    """The type of the message input. Always `message`."""
