# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = ["CustomTool", "Format", "FormatText", "FormatGrammar"]


class FormatText(BaseModel):
    type: Literal["text"]
    """Unconstrained text format. Always `text`."""


class FormatGrammar(BaseModel):
    definition: str
    """The grammar definition."""

    syntax: Literal["lark", "regex"]
    """The syntax of the grammar definition. One of `lark` or `regex`."""

    type: Literal["grammar"]
    """Grammar format. Always `grammar`."""


Format: TypeAlias = Annotated[Union[FormatText, FormatGrammar], PropertyInfo(discriminator="type")]


class CustomTool(BaseModel):
    name: str
    """The name of the custom tool, used to identify it in tool calls."""

    type: Literal["custom"]
    """The type of the custom tool. Always `custom`."""

    description: Optional[str] = None
    """Optional description of the custom tool, used to provide more context."""

    format: Optional[Format] = None
    """The input format for the custom tool. Default is unconstrained text."""
