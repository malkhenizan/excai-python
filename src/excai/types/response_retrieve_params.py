# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["ResponseRetrieveParams"]


class ResponseRetrieveParams(TypedDict, total=False):
    include: List[
        Literal["file_search_call.results", "message.input_image.image_url", "computer_call_output.output.image_url"]
    ]
    """Additional fields to include in the response.

    See the `include` parameter for Response creation above for more information.
    """
