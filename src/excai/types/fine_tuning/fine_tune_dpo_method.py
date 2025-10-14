# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .fine_tune_dpo_hyperparameters import FineTuneDpoHyperparameters

__all__ = ["FineTuneDpoMethod"]


class FineTuneDpoMethod(BaseModel):
    hyperparameters: Optional[FineTuneDpoHyperparameters] = None
    """The hyperparameters used for the DPO fine-tuning job."""
