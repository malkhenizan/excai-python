# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .log_prob_param import LogProbParam
from .file_path_param import FilePathParam
from .url_citation_body_param import URLCitationBodyParam
from .file_citation_body_param import FileCitationBodyParam
from .container_file_citation_body_param import ContainerFileCitationBodyParam

__all__ = ["OutputTextContentParam", "Annotation"]

Annotation: TypeAlias = Union[
    FileCitationBodyParam, URLCitationBodyParam, ContainerFileCitationBodyParam, FilePathParam
]


class OutputTextContentParam(TypedDict, total=False):
    annotations: Required[Iterable[Annotation]]
    """The annotations of the text output."""

    text: Required[str]
    """The text output from the model."""

    type: Required[Literal["output_text"]]
    """The type of the output text. Always `output_text`."""

    logprobs: Iterable[LogProbParam]
