# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .file_search_ranker import FileSearchRanker
from .chat.function_object_param import FunctionObjectParam
from .threads.assistant_tools_code_param import AssistantToolsCodeParam

__all__ = ["AssistantToolParam", "FileSearch", "FileSearchFileSearch", "FileSearchFileSearchRankingOptions", "Function"]


class FileSearchFileSearchRankingOptions(TypedDict, total=False):
    score_threshold: Required[float]
    """The score threshold for the file search.

    All values must be a floating point number between 0 and 1.
    """

    ranker: FileSearchRanker
    """The ranker to use for the file search.

    If not specified will use the `auto` ranker.
    """


class FileSearchFileSearch(TypedDict, total=False):
    max_num_results: int
    """The maximum number of results the file search tool should output.

    The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number
    should be between 1 and 50 inclusive.

    Note that the file search tool may output fewer than `max_num_results` results.
    See the
    [file search tool documentation](https://main.excai.ai/docs/assistants/tools/file-search#customizing-file-search-settings)
    for more information.
    """

    ranking_options: FileSearchFileSearchRankingOptions
    """The ranking options for the file search.

    If not specified, the file search tool will use the `auto` ranker and a
    score_threshold of 0.

    See the
    [file search tool documentation](https://main.excai.ai/docs/assistants/tools/file-search#customizing-file-search-settings)
    for more information.
    """


class FileSearch(TypedDict, total=False):
    type: Required[Literal["file_search"]]
    """The type of tool being defined: `file_search`"""

    file_search: FileSearchFileSearch
    """Overrides for the file search tool."""


class Function(TypedDict, total=False):
    function: Required[FunctionObjectParam]

    type: Required[Literal["function"]]
    """The type of tool being defined: `function`"""


AssistantToolParam: TypeAlias = Union[AssistantToolsCodeParam, FileSearch, Function]
