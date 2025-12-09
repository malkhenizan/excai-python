# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .function_tool_call import FunctionToolCall

__all__ = ["FunctionToolCallResource"]


class FunctionToolCallResource(FunctionToolCall):
    """A tool call to run a function.

    See the
    [function calling guide](https://main.excai.ai/docs/guides/function-calling) for more information.
    """

    id: str  # type: ignore
    """The unique ID of the function tool call."""
