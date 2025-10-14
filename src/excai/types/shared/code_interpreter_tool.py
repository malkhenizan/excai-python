# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .code_interpreter_tool_auto import CodeInterpreterToolAuto

__all__ = ["CodeInterpreterTool", "Container"]

Container: TypeAlias = Union[str, CodeInterpreterToolAuto]


class CodeInterpreterTool(BaseModel):
    container: Container
    """The code interpreter container.

    Can be a container ID or an object that specifies uploaded file IDs to make
    available to your code.
    """

    type: Literal["code_interpreter"]
    """The type of the code interpreter tool. Always `code_interpreter`."""
