# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .grader_python_param import GraderPythonParam

__all__ = ["EvalGraderPythonParam"]


class EvalGraderPythonParam(GraderPythonParam, total=False):
    pass_threshold: float
    """The threshold for the score."""
