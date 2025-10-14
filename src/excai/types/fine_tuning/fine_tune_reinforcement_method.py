# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel
from ..grader_multi import GraderMulti
from ..grader_python import GraderPython
from ..grader_score_model import GraderScoreModel
from ..grader_text_similarity import GraderTextSimilarity
from ..shared.grader_string_check import GraderStringCheck
from .fine_tune_reinforcement_hyperparameters import FineTuneReinforcementHyperparameters

__all__ = ["FineTuneReinforcementMethod", "Grader"]

Grader: TypeAlias = Union[GraderStringCheck, GraderTextSimilarity, GraderPython, GraderScoreModel, GraderMulti]


class FineTuneReinforcementMethod(BaseModel):
    grader: Grader
    """The grader used for the fine-tuning job."""

    hyperparameters: Optional[FineTuneReinforcementHyperparameters] = None
    """The hyperparameters used for the reinforcement fine-tuning job."""
