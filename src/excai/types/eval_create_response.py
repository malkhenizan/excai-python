# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .eval_python_grader import EvalPythonGrader
from .eval_label_model_grader import EvalLabelModelGrader
from .eval_score_model_grader import EvalScoreModelGrader
from .eval_string_check_grader import EvalStringCheckGrader
from .eval_text_similarity_grader import EvalTextSimilarityGrader
from .eval_custom_data_source_config import EvalCustomDataSourceConfig
from .eval_stored_completions_data_source_config import EvalStoredCompletionsDataSourceConfig

__all__ = ["EvalCreateResponse", "DataSourceConfig", "TestingCriterion"]

DataSourceConfig: TypeAlias = Union[EvalCustomDataSourceConfig, EvalStoredCompletionsDataSourceConfig]

TestingCriterion: TypeAlias = Union[
    EvalLabelModelGrader, EvalStringCheckGrader, EvalTextSimilarityGrader, EvalPythonGrader, EvalScoreModelGrader
]


class EvalCreateResponse(BaseModel):
    id: str
    """Unique identifier for the evaluation."""

    created_at: int
    """The Unix timestamp (in seconds) for when the eval was created."""

    data_source_config: DataSourceConfig
    """Configuration of data sources used in runs of the evaluation."""

    metadata: Optional[Dict[str, str]] = None
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings with
    a maximum length of 512 characters.
    """

    name: str
    """The name of the evaluation."""

    object: Literal["eval"]
    """The object type."""

    testing_criteria: List[TestingCriterion]
    """A list of testing criteria."""
