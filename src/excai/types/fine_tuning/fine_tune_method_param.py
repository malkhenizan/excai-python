# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .fine_tune_dpo_method_param import FineTuneDpoMethodParam
from .fine_tune_supervised_method_param import FineTuneSupervisedMethodParam
from .fine_tune_reinforcement_method_param import FineTuneReinforcementMethodParam

__all__ = ["FineTuneMethodParam"]


class FineTuneMethodParam(TypedDict, total=False):
    type: Required[Literal["supervised", "dpo", "reinforcement"]]
    """The type of method. Is either `supervised`, `dpo`, or `reinforcement`."""

    dpo: FineTuneDpoMethodParam
    """Configuration for the DPO fine-tuning method."""

    reinforcement: FineTuneReinforcementMethodParam
    """Configuration for the reinforcement fine-tuning method."""

    supervised: FineTuneSupervisedMethodParam
    """Configuration for the supervised fine-tuning method."""
