# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .fine_tuning.alpha.grader_python_script import GraderPythonScript

__all__ = ["GraderPythonEval"]


class GraderPythonEval(GraderPythonScript):
    """A PythonGrader object that runs a python script on the input."""

    pass_threshold: Optional[float] = None
    """The threshold for the score."""
