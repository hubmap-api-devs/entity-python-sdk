# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypeAlias

from .sample import Sample

__all__ = ["ChildRetrieveResponse", "ChildRetrieveResponseItem"]

ChildRetrieveResponseItem: TypeAlias = Union[Sample, "Dataset"]

ChildRetrieveResponse: TypeAlias = List[ChildRetrieveResponseItem]

from .dataset import Dataset
