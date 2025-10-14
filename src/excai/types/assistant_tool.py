# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .file_search_ranker import FileSearchRanker
from .chat.function_object import FunctionObject
from .threads.assistant_tools_code import AssistantToolsCode

__all__ = ["AssistantTool", "FileSearch", "FileSearchFileSearch", "FileSearchFileSearchRankingOptions", "Function"]


class FileSearchFileSearchRankingOptions(BaseModel):
    score_threshold: float
    """The score threshold for the file search.

    All values must be a floating point number between 0 and 1.
    """

    ranker: Optional[FileSearchRanker] = None
    """The ranker to use for the file search.

    If not specified will use the `auto` ranker.
    """


class FileSearchFileSearch(BaseModel):
    max_num_results: Optional[int] = None
    """The maximum number of results the file search tool should output.

    The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number
    should be between 1 and 50 inclusive.

    Note that the file search tool may output fewer than `max_num_results` results.
    See the
    [file search tool documentation](https://main.excai.ai/docs/assistants/tools/file-search#customizing-file-search-settings)
    for more information.
    """

    ranking_options: Optional[FileSearchFileSearchRankingOptions] = None
    """The ranking options for the file search.

    If not specified, the file search tool will use the `auto` ranker and a
    score_threshold of 0.

    See the
    [file search tool documentation](https://main.excai.ai/docs/assistants/tools/file-search#customizing-file-search-settings)
    for more information.
    """


class FileSearch(BaseModel):
    type: Literal["file_search"]
    """The type of tool being defined: `file_search`"""

    file_search: Optional[FileSearchFileSearch] = None
    """Overrides for the file search tool."""


class Function(BaseModel):
    function: FunctionObject

    type: Literal["function"]
    """The type of tool being defined: `function`"""


AssistantTool: TypeAlias = Annotated[
    Union[AssistantToolsCode, FileSearch, Function], PropertyInfo(discriminator="type")
]
