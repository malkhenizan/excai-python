# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["FileSearchRankingOptions"]


class FileSearchRankingOptions(TypedDict, total=False):
    score_threshold: Required[float]
    """The score threshold for the file search.

    All values must be a floating point number between 0 and 1.
    """

    ranker: Literal["auto", "default_2024_08_21"]
    """The ranker to use for the file search.

    If not specified will use the `auto` ranker.
    """
