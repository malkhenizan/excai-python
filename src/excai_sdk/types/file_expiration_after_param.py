# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["FileExpirationAfterParam"]


class FileExpirationAfterParam(TypedDict, total=False):
    """The expiration policy for a file.

    By default, files with `purpose=batch` expire after 30 days and all other files are persisted until they are manually deleted.
    """

    anchor: Required[Literal["created_at"]]
    """Anchor timestamp after which the expiration policy applies.

    Supported anchors: `created_at`.
    """

    seconds: Required[int]
    """The number of seconds after the anchor time that the file will expire.

    Must be between 3600 (1 hour) and 2592000 (30 days).
    """
