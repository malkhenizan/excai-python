# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .grader_python import GraderPython
from .grader_score_model import GraderScoreModel
from .grader_text_similarity import GraderTextSimilarity
from ..shared.grader_label_model import GraderLabelModel
from ..shared.grader_string_check import GraderStringCheck

__all__ = ["GraderMulti", "Graders"]

Graders: TypeAlias = Union[GraderStringCheck, GraderTextSimilarity, GraderPython, GraderScoreModel, GraderLabelModel]


class GraderMulti(BaseModel):
    calculate_output: str
    """A formula to calculate the output based on grader results."""

    graders: Graders
    """
    A StringCheckGrader object that performs a string comparison between input and
    reference using a specified operation.
    """

    name: str
    """The name of the grader."""

    type: Literal["multi"]
    """The object type, which is always `multi`."""
