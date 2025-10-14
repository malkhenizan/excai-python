# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .grader_python import GraderPython

__all__ = ["EvalGraderPython"]


class EvalGraderPython(GraderPython):
    pass_threshold: Optional[float] = None
    """The threshold for the score."""
