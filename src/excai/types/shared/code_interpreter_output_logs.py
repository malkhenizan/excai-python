# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CodeInterpreterOutputLogs"]


class CodeInterpreterOutputLogs(BaseModel):
    logs: str
    """The logs output from the code interpreter."""

    type: Literal["logs"]
    """The type of the output. Always 'logs'."""
