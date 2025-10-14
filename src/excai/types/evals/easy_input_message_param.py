# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..shared_params.input_file_content import InputFileContent
from ..shared_params.input_text_content import InputTextContent
from ..shared_params.input_image_content import InputImageContent

__all__ = ["EasyInputMessageParam", "ContentInputMessageContentList"]

ContentInputMessageContentList: TypeAlias = Union[InputTextContent, InputImageContent, InputFileContent]


class EasyInputMessageParam(TypedDict, total=False):
    content: Required[Union[str, Iterable[ContentInputMessageContentList]]]
    """
    Text, image, or audio input to the model, used to generate a response. Can also
    contain previous assistant responses.
    """

    role: Required[Literal["user", "assistant", "system", "developer"]]
    """The role of the message input.

    One of `user`, `assistant`, `system`, or `developer`.
    """

    type: Literal["message"]
    """The type of the message input. Always `message`."""
