# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["FileSearchRankingOptions"]


class FileSearchRankingOptions(BaseModel):
    score_threshold: float
    """The score threshold for the file search.

    All values must be a floating point number between 0 and 1.
    """

    ranker: Optional[Literal["auto", "default_2024_08_21"]] = None
    """The ranker to use for the file search.

    If not specified will use the `auto` ranker.
    """
