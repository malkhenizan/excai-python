# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from .fine_tune_dpo_method_param import FineTuneDpoMethodParam
from .fine_tune_supervised_method_param import FineTuneSupervisedMethodParam

__all__ = ["FineTuneMethodParam"]


class FineTuneMethodParam(TypedDict, total=False):
    dpo: FineTuneDpoMethodParam
    """Configuration for the DPO fine-tuning method."""

    supervised: FineTuneSupervisedMethodParam
    """Configuration for the supervised fine-tuning method."""

    type: Literal["supervised", "dpo"]
    """The type of method. Is either `supervised` or `dpo`."""
