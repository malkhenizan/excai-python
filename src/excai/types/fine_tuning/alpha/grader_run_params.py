# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

from ...grader_multi_param import GraderMultiParam
from ...grader_python_param import GraderPythonParam
from ...grader_score_model_param import GraderScoreModelParam
from ...grader_text_similarity_param import GraderTextSimilarityParam
from ...shared_params.grader_string_check import GraderStringCheck

__all__ = ["GraderRunParams", "Grader"]


class GraderRunParams(TypedDict, total=False):
    grader: Required[Grader]
    """The grader used for the fine-tuning job."""

    model_sample: Required[str]
    """The model sample to be evaluated.

    This value will be used to populate the `sample` namespace. See
    [the guide](https://platform.excai.com/docs/guides/graders) for more details.
    The `output_json` variable will be populated if the model sample is a valid JSON
    string.
    """

    item: object
    """The dataset item provided to the grader.

    This will be used to populate the `item` namespace. See
    [the guide](https://platform.excai.com/docs/guides/graders) for more details.
    """


Grader: TypeAlias = Union[
    GraderStringCheck, GraderTextSimilarityParam, GraderPythonParam, GraderScoreModelParam, GraderMultiParam
]
