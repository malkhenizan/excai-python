# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["Coordinate"]


class Coordinate(BaseModel):
    x: int
    """The x-coordinate."""

    y: int
    """The y-coordinate."""
