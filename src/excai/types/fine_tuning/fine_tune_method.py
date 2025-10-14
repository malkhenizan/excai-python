# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .fine_tune_dpo_method import FineTuneDpoMethod
from .fine_tune_supervised_method import FineTuneSupervisedMethod
from .fine_tune_reinforcement_method import FineTuneReinforcementMethod

__all__ = ["FineTuneMethod"]


class FineTuneMethod(BaseModel):
    type: Literal["supervised", "dpo", "reinforcement"]
    """The type of method. Is either `supervised`, `dpo`, or `reinforcement`."""

    dpo: Optional[FineTuneDpoMethod] = None
    """Configuration for the DPO fine-tuning method."""

    reinforcement: Optional[FineTuneReinforcementMethod] = None
    """Configuration for the reinforcement fine-tuning method."""

    supervised: Optional[FineTuneSupervisedMethod] = None
    """Configuration for the supervised fine-tuning method."""
