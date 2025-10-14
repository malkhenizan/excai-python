# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .fine_tuning.grader_score_model_param import GraderScoreModelParam

__all__ = ["EvalGraderScoreModelParam"]


class EvalGraderScoreModelParam(GraderScoreModelParam, total=False):
    pass_threshold: float
    """The threshold for the score."""
