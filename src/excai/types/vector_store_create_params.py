# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "VectorStoreCreateParams",
    "ChunkingStrategy",
    "ChunkingStrategyAutoChunkingStrategyRequestParam",
    "ChunkingStrategyStaticChunkingStrategyRequestParam",
    "ChunkingStrategyStaticChunkingStrategyRequestParamStatic",
    "ExpiresAfter",
]


class VectorStoreCreateParams(TypedDict, total=False):
    chunking_strategy: ChunkingStrategy
    """The chunking strategy used to chunk the file(s).

    If not set, will use the `auto` strategy. Only applicable if `file_ids` is
    non-empty.
    """

    expires_after: ExpiresAfter
    """The expiration policy for a vector store."""

    file_ids: SequenceNotStr[str]
    """A list of [File](/docs/api-reference/files) IDs that the vector store should
    use.

    Useful for tools like `file_search` that can access files.
    """

    metadata: Optional[Dict[str, str]]
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings with
    a maximum length of 512 characters.
    """

    name: str
    """The name of the vector store."""


class ChunkingStrategyAutoChunkingStrategyRequestParam(TypedDict, total=False):
    type: Required[Literal["auto"]]
    """Always `auto`."""


class ChunkingStrategyStaticChunkingStrategyRequestParamStatic(TypedDict, total=False):
    chunk_overlap_tokens: Required[int]
    """The number of tokens that overlap between chunks. The default value is `400`.

    Note that the overlap must not exceed half of `max_chunk_size_tokens`.
    """

    max_chunk_size_tokens: Required[int]
    """The maximum number of tokens in each chunk.

    The default value is `800`. The minimum value is `100` and the maximum value is
    `4096`.
    """


class ChunkingStrategyStaticChunkingStrategyRequestParam(TypedDict, total=False):
    static: Required[ChunkingStrategyStaticChunkingStrategyRequestParamStatic]

    type: Required[Literal["static"]]
    """Always `static`."""


ChunkingStrategy: TypeAlias = Union[
    ChunkingStrategyAutoChunkingStrategyRequestParam, ChunkingStrategyStaticChunkingStrategyRequestParam
]


class ExpiresAfter(TypedDict, total=False):
    anchor: Required[Literal["last_active_at"]]
    """Anchor timestamp after which the expiration policy applies.

    Supported anchors: `last_active_at`.
    """

    days: Required[int]
    """The number of days after the anchor time that the vector store will expire."""
