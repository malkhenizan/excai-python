# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel
from .chat.metadata import Metadata
from .grader_python_eval import GraderPythonEval
from .grader_score_eval_model import GraderScoreEvalModel
from .grader_string_check_eval import GraderStringCheckEval
from .grader_text_similarity_eval import GraderTextSimilarityEval

__all__ = [
    "Eval",
    "DataSourceConfig",
    "DataSourceConfigCustom",
    "DataSourceConfigLogs",
    "DataSourceConfigStoredCompletions",
    "TestingCriterion",
]


class DataSourceConfigCustom(BaseModel):
    """
    A CustomDataSourceConfig which specifies the schema of your `item` and optionally `sample` namespaces.
    The response schema defines the shape of the data that will be:
    - Used to define your testing criteria and
    - What data is required when creating a run
    """

    schema_: Dict[str, object] = FieldInfo(alias="schema")
    """
    The json schema for the run data source items. Learn how to build JSON schemas
    [here](https://json-schema.org/).
    """

    type: Literal["custom"]
    """The type of data source. Always `custom`."""


class DataSourceConfigLogs(BaseModel):
    """
    A LogsDataSourceConfig which specifies the metadata property of your logs query.
    This is usually metadata like `usecase=chatbot` or `prompt-version=v2`, etc.
    The schema returned by this data source config is used to defined what variables are available in your evals.
    `item` and `sample` are both defined when using this data source config.
    """

    schema_: Dict[str, object] = FieldInfo(alias="schema")
    """
    The json schema for the run data source items. Learn how to build JSON schemas
    [here](https://json-schema.org/).
    """

    type: Literal["logs"]
    """The type of data source. Always `logs`."""

    metadata: Optional[Metadata] = None
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings with
    a maximum length of 512 characters.
    """


class DataSourceConfigStoredCompletions(BaseModel):
    """Deprecated in favor of LogsDataSourceConfig."""

    schema_: Dict[str, object] = FieldInfo(alias="schema")
    """
    The json schema for the run data source items. Learn how to build JSON schemas
    [here](https://json-schema.org/).
    """

    type: Literal["stored_completions"]
    """The type of data source. Always `stored_completions`."""

    metadata: Optional[Metadata] = None
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings with
    a maximum length of 512 characters.
    """


DataSourceConfig: TypeAlias = Annotated[
    Union[DataSourceConfigCustom, DataSourceConfigLogs, DataSourceConfigStoredCompletions],
    PropertyInfo(discriminator="type"),
]

TestingCriterion: TypeAlias = Union[
    GraderStringCheckEval, GraderTextSimilarityEval, GraderPythonEval, GraderScoreEvalModel
]


class Eval(BaseModel):
    """
    An Eval object with a data source config and testing criteria.
    An Eval represents a task to be done for your LLM integration.
    Like:
     - Improve the quality of my chatbot
     - See how well my chatbot handles customer support
     - Check if o4-mini is better at my usecase than openai/gpt-oss-120b
    """

    id: str
    """Unique identifier for the evaluation."""

    created_at: int
    """The Unix timestamp (in seconds) for when the eval was created."""

    data_source_config: DataSourceConfig
    """Configuration of data sources used in runs of the evaluation."""

    metadata: Optional[Metadata] = None
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
