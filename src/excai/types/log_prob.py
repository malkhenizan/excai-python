# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .top_log_prob import TopLogProb

__all__ = ["LogProb"]


class LogProb(BaseModel):
    token: str

    bytes: List[int]

    logprob: float

    top_logprobs: List[TopLogProb]
