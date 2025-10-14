# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required

from .fine_tuning.grader_text_similarity_param import GraderTextSimilarityParam

__all__ = ["EvalGraderTextSimilarityParam"]


class EvalGraderTextSimilarityParam(GraderTextSimilarityParam, total=False):
    pass_threshold: Required[float]
    """The threshold for the score."""
