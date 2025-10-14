# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .grader_python_param import GraderPythonParam
from .grader_score_model_param import GraderScoreModelParam
from .grader_text_similarity_param import GraderTextSimilarityParam
from .shared_params.grader_label_model import GraderLabelModel
from .shared_params.grader_string_check import GraderStringCheck

__all__ = ["GraderMultiParam", "Graders"]

Graders: TypeAlias = Union[
    GraderStringCheck, GraderTextSimilarityParam, GraderPythonParam, GraderScoreModelParam, GraderLabelModel
]


class GraderMultiParam(TypedDict, total=False):
    calculate_output: Required[str]
    """A formula to calculate the output based on grader results."""

    graders: Required[Graders]
    """
    A StringCheckGrader object that performs a string comparison between input and
    reference using a specified operation.
    """

    name: Required[str]
    """The name of the grader."""

    type: Required[Literal["multi"]]
    """The object type, which is always `multi`."""
