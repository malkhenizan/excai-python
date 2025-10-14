# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import TypeAlias

from ...._models import BaseModel
from ...grader_multi import GraderMulti
from ...grader_python import GraderPython
from ...grader_score_model import GraderScoreModel
from ...grader_text_similarity import GraderTextSimilarity
from ...shared.grader_string_check import GraderStringCheck

__all__ = ["GraderValidateResponse", "Grader"]

Grader: TypeAlias = Union[GraderStringCheck, GraderTextSimilarity, GraderPython, GraderScoreModel, GraderMulti]


class GraderValidateResponse(BaseModel):
    grader: Optional[Grader] = None
    """The grader used for the fine-tuning job."""
