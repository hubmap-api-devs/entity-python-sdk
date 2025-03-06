# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypeAlias

from .donor import Donor
from .sample import Sample

__all__ = ["AncestorRetrieveResponse", "AncestorRetrieveResponseItem"]

AncestorRetrieveResponseItem: TypeAlias = Union[Donor, Sample, "Dataset"]

AncestorRetrieveResponse: TypeAlias = List[AncestorRetrieveResponseItem]

from .dataset import Dataset
