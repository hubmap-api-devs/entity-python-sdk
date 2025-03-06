# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .donor import Donor
from .sample import Sample

__all__ = ["EntityUpdateResponse"]

EntityUpdateResponse: TypeAlias = Union[Donor, Sample, "Dataset"]

from .dataset import Dataset
