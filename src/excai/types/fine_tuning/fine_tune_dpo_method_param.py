# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .fine_tune_dpo_hyperparameters_param import FineTuneDpoHyperparametersParam

__all__ = ["FineTuneDpoMethodParam"]


class FineTuneDpoMethodParam(TypedDict, total=False):
    hyperparameters: FineTuneDpoHyperparametersParam
    """The hyperparameters used for the DPO fine-tuning job."""
