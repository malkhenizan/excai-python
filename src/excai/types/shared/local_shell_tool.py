# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["LocalShellTool"]


class LocalShellTool(BaseModel):
    type: Literal["local_shell"]
    """The type of the local shell tool. Always `local_shell`."""
