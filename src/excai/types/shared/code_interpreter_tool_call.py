# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "CodeInterpreterToolCall",
    "Result",
    "ResultCodeInterpreterTextOutput",
    "ResultCodeInterpreterFileOutput",
    "ResultCodeInterpreterFileOutputFile",
]


class ResultCodeInterpreterTextOutput(BaseModel):
    logs: str
    """The logs of the code interpreter tool call."""

    type: Literal["logs"]
    """The type of the code interpreter text output. Always `logs`."""


class ResultCodeInterpreterFileOutputFile(BaseModel):
    file_id: str
    """The ID of the file."""

    mime_type: str
    """The MIME type of the file."""


class ResultCodeInterpreterFileOutput(BaseModel):
    files: List[ResultCodeInterpreterFileOutputFile]

    type: Literal["files"]
    """The type of the code interpreter file output. Always `files`."""


Result: TypeAlias = Union[ResultCodeInterpreterTextOutput, ResultCodeInterpreterFileOutput]


class CodeInterpreterToolCall(BaseModel):
    id: str
    """The unique ID of the code interpreter tool call."""

    code: str
    """The code to run."""

    results: List[Result]
    """The results of the code interpreter tool call."""

    status: Literal["in_progress", "interpreting", "completed"]
    """The status of the code interpreter tool call."""

    type: Literal["code_interpreter_call"]
    """The type of the code interpreter tool call. Always `code_interpreter_call`."""
