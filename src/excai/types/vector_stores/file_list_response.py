# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from ..other_chunking_strategy_response_param import OtherChunkingStrategyResponseParam
from ..static_chunking_strategy_response_param import StaticChunkingStrategyResponseParam

__all__ = ["FileListResponse", "Data", "DataLastError", "DataChunkingStrategy"]


class DataLastError(BaseModel):
    code: Literal["server_error", "unsupported_file", "invalid_file"]
    """One of `server_error` or `rate_limit_exceeded`."""

    message: str
    """A human-readable description of the error."""


DataChunkingStrategy: TypeAlias = Union[StaticChunkingStrategyResponseParam, OtherChunkingStrategyResponseParam]


class Data(BaseModel):
    id: str
    """The identifier, which can be referenced in API endpoints."""

    created_at: int
    """The Unix timestamp (in seconds) for when the vector store file was created."""

    last_error: Optional[DataLastError] = None
    """The last error associated with this vector store file.

    Will be `null` if there are no errors.
    """

    object: Literal["vector_store.file"]
    """The object type, which is always `vector_store.file`."""

    status: Literal["in_progress", "completed", "cancelled", "failed"]
    """
    The status of the vector store file, which can be either `in_progress`,
    `completed`, `cancelled`, or `failed`. The status `completed` indicates that the
    vector store file is ready for use.
    """

    usage_bytes: int
    """The total vector store usage in bytes.

    Note that this may be different from the original file size.
    """

    vector_store_id: str
    """
    The ID of the [vector store](/docs/api-reference/vector-stores/object) that the
    [File](/docs/api-reference/files) is attached to.
    """

    attributes: Optional[Dict[str, Union[str, float, bool]]] = None
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard. Keys are
    strings with a maximum length of 64 characters. Values are strings with a
    maximum length of 512 characters, booleans, or numbers.
    """

    chunking_strategy: Optional[DataChunkingStrategy] = None
    """The strategy used to chunk the file."""


class FileListResponse(BaseModel):
    data: List[Data]

    first_id: str

    has_more: bool

    last_id: str

    object: str
