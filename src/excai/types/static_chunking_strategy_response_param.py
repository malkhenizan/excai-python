# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .static_chunking_strategy import StaticChunkingStrategy

__all__ = ["StaticChunkingStrategyResponseParam"]


class StaticChunkingStrategyResponseParam(BaseModel):
    static: StaticChunkingStrategy

    type: Literal["static"]
    """Always `static`."""
