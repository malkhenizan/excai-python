# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

from ...grader_multi_param import GraderMultiParam
from ...grader_python_param import GraderPythonParam
from ...grader_score_model_param import GraderScoreModelParam
from ...grader_text_similarity_param import GraderTextSimilarityParam
from ...shared_params.grader_string_check import GraderStringCheck

__all__ = ["GraderValidateParams", "Grader"]


class GraderValidateParams(TypedDict, total=False):
    grader: Required[Grader]
    """The grader used for the fine-tuning job."""


Grader: TypeAlias = Union[
    GraderStringCheck, GraderTextSimilarityParam, GraderPythonParam, GraderScoreModelParam, GraderMultiParam
]
