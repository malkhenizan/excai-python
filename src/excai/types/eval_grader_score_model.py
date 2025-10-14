# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .grader_score_model import GraderScoreModel

__all__ = ["EvalGraderScoreModel"]


class EvalGraderScoreModel(GraderScoreModel):
    pass_threshold: Optional[float] = None
    """The threshold for the score."""
