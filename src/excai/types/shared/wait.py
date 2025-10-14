# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Wait"]


class Wait(BaseModel):
    type: Literal["wait"]
    """Specifies the event type.

    For a wait action, this property is always set to `wait`.
    """
