# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .eval_grader_python import EvalGraderPython
from .eval_grader_score_model import EvalGraderScoreModel
from .shared.grader_label_model import GraderLabelModel
from .shared.grader_string_check import GraderStringCheck
from .eval_grader_text_similarity import EvalGraderTextSimilarity
from .eval_logs_data_source_config import EvalLogsDataSourceConfig
from .eval_custom_data_source_config import EvalCustomDataSourceConfig
from .eval_stored_completions_data_source_config import EvalStoredCompletionsDataSourceConfig

__all__ = ["EvalUpdateResponse", "DataSourceConfig", "TestingCriterion"]

DataSourceConfig: TypeAlias = Annotated[
    Union[EvalCustomDataSourceConfig, EvalLogsDataSourceConfig, EvalStoredCompletionsDataSourceConfig],
    PropertyInfo(discriminator="type"),
]

TestingCriterion: TypeAlias = Union[
    GraderLabelModel, GraderStringCheck, EvalGraderTextSimilarity, EvalGraderPython, EvalGraderScoreModel
]


class EvalUpdateResponse(BaseModel):
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
