# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .file_path import FilePath
from .url_citation_body import URLCitationBody
from .file_citation_body import FileCitationBody

__all__ = ["OutputTextContent", "Annotation"]

Annotation: TypeAlias = Union[FileCitationBody, URLCitationBody, FilePath]


class OutputTextContent(TypedDict, total=False):
    annotations: Required[Iterable[Annotation]]
    """The annotations of the text output."""

    text: Required[str]
    """The text output from the model."""

    type: Required[Literal["output_text"]]
    """The type of the output text. Always `output_text`."""
