# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .function import Function
from ..._models import BaseModel

__all__ = ["ChatCompletionTool"]


class ChatCompletionTool(BaseModel):
    """A function tool that can be used to generate a response."""

    function: Function

    type: Literal["function"]
    """The type of the tool. Currently, only `function` is supported."""
