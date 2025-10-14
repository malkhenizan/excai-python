# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel
from ..usage_time_bucket import UsageTimeBucket

__all__ = ["UsageVectorStoresResponse"]


class UsageVectorStoresResponse(BaseModel):
    data: List[UsageTimeBucket]

    has_more: bool

    next_page: str

    object: Literal["page"]
