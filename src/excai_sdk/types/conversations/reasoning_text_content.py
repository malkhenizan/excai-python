# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ReasoningTextContent"]


class ReasoningTextContent(BaseModel):
    """Reasoning text from the model."""

    text: str
    """The reasoning text from the model."""

    type: Literal["reasoning_text"]
    """The type of the reasoning text. Always `reasoning_text`."""
