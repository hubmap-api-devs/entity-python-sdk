# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypeAlias

from .donor import Donor
from .sample import Sample

__all__ = ["ParentRetrieveResponse", "ParentRetrieveResponseItem"]

ParentRetrieveResponseItem: TypeAlias = Union[Donor, Sample, "Dataset"]

ParentRetrieveResponse: TypeAlias = List[ParentRetrieveResponseItem]

from .dataset import Dataset
