# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .static_chunking_strategy_param import StaticChunkingStrategyParam

__all__ = ["ChunkingStrategyRequestParam", "Auto", "Static"]


class Auto(TypedDict, total=False):
    type: Required[Literal["auto"]]
    """Always `auto`."""


class Static(TypedDict, total=False):
    static: Required[StaticChunkingStrategyParam]

    type: Required[Literal["static"]]
    """Always `static`."""


ChunkingStrategyRequestParam: TypeAlias = Union[Auto, Static]
