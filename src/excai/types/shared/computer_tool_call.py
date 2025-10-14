# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal, TypeAlias

from .drag import Drag
from .move import Move
from .type import Type
from .wait import Wait
from .click import Click
from .scroll import Scroll
from ..._models import BaseModel
from .key_press import KeyPress
from .screenshot import Screenshot
from .double_click import DoubleClick
from .computer_tool_call_safety_check import ComputerToolCallSafetyCheck

__all__ = ["ComputerToolCall", "Action"]

Action: TypeAlias = Union[Click, DoubleClick, Drag, KeyPress, Move, Screenshot, Scroll, Type, Wait]


class ComputerToolCall(BaseModel):
    id: str
    """The unique ID of the computer call."""

    action: Action
    """A click action."""

    call_id: str
    """An identifier used when responding to the tool call with output."""

    pending_safety_checks: List[ComputerToolCallSafetyCheck]
    """The pending safety checks for the computer call."""

    status: Literal["in_progress", "completed", "incomplete"]
    """The status of the item.

    One of `in_progress`, `completed`, or `incomplete`. Populated when items are
    returned via API.
    """

    type: Literal["computer_call"]
    """The type of the computer call. Always `computer_call`."""
