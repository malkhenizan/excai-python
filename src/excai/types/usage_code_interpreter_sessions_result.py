# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["UsageCodeInterpreterSessionsResult"]


class UsageCodeInterpreterSessionsResult(BaseModel):
    object: Literal["organization.usage.code_interpreter_sessions.result"]

    num_sessions: Optional[int] = None
    """The number of code interpreter sessions."""

    project_id: Optional[str] = None
    """
    When `group_by=project_id`, this field provides the project ID of the grouped
    usage result.
    """
