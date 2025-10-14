# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CostsResult", "Amount"]


class Amount(BaseModel):
    currency: Optional[str] = None
    """Lowercase ISO-4217 currency e.g. "usd" """

    value: Optional[float] = None
    """The numeric value of the cost."""


class CostsResult(BaseModel):
    object: Literal["organization.costs.result"]

    amount: Optional[Amount] = None
    """The monetary value in its associated currency."""

    line_item: Optional[str] = None
    """
    When `group_by=line_item`, this field provides the line item of the grouped
    costs result.
    """

    project_id: Optional[str] = None
    """
    When `group_by=project_id`, this field provides the project ID of the grouped
    costs result.
    """
