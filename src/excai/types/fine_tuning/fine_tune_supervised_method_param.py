# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .fine_tune_supervised_hyperparameters_param import FineTuneSupervisedHyperparametersParam

__all__ = ["FineTuneSupervisedMethodParam"]


class FineTuneSupervisedMethodParam(TypedDict, total=False):
    hyperparameters: FineTuneSupervisedHyperparametersParam
    """The hyperparameters used for the fine-tuning job."""
