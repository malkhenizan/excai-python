# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .fine_tune_supervised_hyperparameters import FineTuneSupervisedHyperparameters

__all__ = ["FineTuneSupervisedMethod"]


class FineTuneSupervisedMethod(BaseModel):
    hyperparameters: Optional[FineTuneSupervisedHyperparameters] = None
    """The hyperparameters used for the fine-tuning job."""
