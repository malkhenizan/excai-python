# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["KeyPress"]


class KeyPress(BaseModel):
    keys: List[str]
    """The combination of keys the model is requesting to be pressed.

    This is an array of strings, each representing a key.
    """

    type: Literal["keypress"]
    """Specifies the event type.

    For a keypress action, this property is always set to `keypress`.
    """
