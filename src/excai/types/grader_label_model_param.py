# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr
from .fine_tuning.alpha.eval_item_param import EvalItemParam

__all__ = ["GraderLabelModelParam"]


class GraderLabelModelParam(TypedDict, total=False):
    input: Required[Iterable[EvalItemParam]]

    labels: Required[SequenceNotStr[str]]
    """The labels to assign to each item in the evaluation."""

    model: Required[str]
    """The model to use for the evaluation. Must support structured outputs."""

    name: Required[str]
    """The name of the grader."""

    passing_labels: Required[SequenceNotStr[str]]
    """The labels that indicate a passing result. Must be a subset of labels."""

    type: Required[Literal["label_model"]]
    """The object type, which is always `label_model`."""
