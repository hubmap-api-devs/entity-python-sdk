# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypeAlias

from .sample import Sample

__all__ = ["DescendantRetrieveResponse", "DescendantRetrieveResponseItem"]

DescendantRetrieveResponseItem: TypeAlias = Union[Sample, "Dataset"]

DescendantRetrieveResponse: TypeAlias = List[DescendantRetrieveResponseItem]

from .dataset import Dataset
