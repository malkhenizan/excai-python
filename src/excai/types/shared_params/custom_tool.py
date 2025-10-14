# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["CustomTool", "Format", "FormatText", "FormatGrammar"]


class FormatText(TypedDict, total=False):
    type: Required[Literal["text"]]
    """Unconstrained text format. Always `text`."""


class FormatGrammar(TypedDict, total=False):
    definition: Required[str]
    """The grammar definition."""

    syntax: Required[Literal["lark", "regex"]]
    """The syntax of the grammar definition. One of `lark` or `regex`."""

    type: Required[Literal["grammar"]]
    """Grammar format. Always `grammar`."""


Format: TypeAlias = Union[FormatText, FormatGrammar]


class CustomTool(TypedDict, total=False):
    name: Required[str]
    """The name of the custom tool, used to identify it in tool calls."""

    type: Required[Literal["custom"]]
    """The type of the custom tool. Always `custom`."""

    description: str
    """Optional description of the custom tool, used to provide more context."""

    format: Format
    """The input format for the custom tool. Default is unconstrained text."""
