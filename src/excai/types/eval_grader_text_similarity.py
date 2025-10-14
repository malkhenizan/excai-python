# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .grader_text_similarity import GraderTextSimilarity

__all__ = ["EvalGraderTextSimilarity"]


class EvalGraderTextSimilarity(GraderTextSimilarity):
    pass_threshold: float
    """The threshold for the score."""
