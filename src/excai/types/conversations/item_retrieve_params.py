# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ItemRetrieveParams"]


class ItemRetrieveParams(TypedDict, total=False):
    conversation_id: Required[str]

    include: List[
        Literal[
            "code_interpreter_call.outputs",
            "computer_call_output.output.image_url",
            "file_search_call.results",
            "message.input_image.image_url",
            "message.output_text.logprobs",
            "reasoning.encrypted_content",
        ]
    ]
    """Additional fields to include in the response.

    See the `include` parameter for
    [listing Conversation items above](https://platform.excai.com/docs/api-reference/conversations/list-items#conversations_list_items-include)
    for more information.
    """
