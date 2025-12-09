# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ComputerToolCallSafetyCheck"]


class ComputerToolCallSafetyCheck(BaseModel):
    """A pending safety check for the computer call."""

    id: str
    """The ID of the pending safety check."""

    code: str
    """The type of the pending safety check."""

    message: str
    """Details about the pending safety check."""
