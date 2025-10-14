# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .drag_param import DragParam
from .move_param import MoveParam
from .type_param import TypeParam
from .wait_param import WaitParam
from .click_param import ClickParam
from .scroll_param import ScrollParam
from .key_press_param import KeyPressParam
from .screenshot_param import ScreenshotParam
from .double_click_param import DoubleClickParam
from .computer_tool_call_safety_check_param import ComputerToolCallSafetyCheckParam

__all__ = ["ComputerToolCallParam", "Action"]

Action: TypeAlias = Union[
    ClickParam,
    DoubleClickParam,
    DragParam,
    KeyPressParam,
    MoveParam,
    ScreenshotParam,
    ScrollParam,
    TypeParam,
    WaitParam,
]


class ComputerToolCallParam(TypedDict, total=False):
    id: Required[str]
    """The unique ID of the computer call."""

    action: Required[Action]
    """A click action."""

    call_id: Required[str]
    """An identifier used when responding to the tool call with output."""

    pending_safety_checks: Required[Iterable[ComputerToolCallSafetyCheckParam]]
    """The pending safety checks for the computer call."""

    status: Required[Literal["in_progress", "completed", "incomplete"]]
    """The status of the item.

    One of `in_progress`, `completed`, or `incomplete`. Populated when items are
    returned via API.
    """

    type: Required[Literal["computer_call"]]
    """The type of the computer call. Always `computer_call`."""
