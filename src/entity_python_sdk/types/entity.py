# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from .donor import Donor
from .sample import Sample
from .upload import Upload
from .dataset import Dataset
from .collection import Collection
from .publication import Publication
from .epicollection import Epicollection

__all__ = [
    "Entity",
    "EntitiesDonor",
    "EntitiesSample",
    "DatasetsDataset",
    "EntitiesUpload",
    "EntitiesCollection",
    "EntitiesPublication",
    "EntitiesEpicollection",
]


class EntitiesDonor(Donor):
    entity_type: Optional[
        Literal["Donor", "Sample", "Dataset", "Upload", "Collection", "Publication", "Epicollection"]
    ] = None  # type: ignore
    """the type of entity"""


class EntitiesSample(Sample):
    entity_type: Optional[
        Literal["Donor", "Sample", "Dataset", "Upload", "Collection", "Publication", "Epicollection"]
    ] = None  # type: ignore
    """the type of entity"""


class DatasetsDataset(Dataset):
    entity_type: Optional[
        Literal["Donor", "Sample", "Dataset", "Upload", "Collection", "Publication", "Epicollection"]
    ] = None  # type: ignore
    """the type of entity"""


class EntitiesUpload(Upload):
    entity_type: Optional[
        Literal["Donor", "Sample", "Dataset", "Upload", "Collection", "Publication", "Epicollection"]
    ] = None  # type: ignore
    """the type of entity"""


class EntitiesCollection(Collection):
    entity_type: Optional[
        Literal["Donor", "Sample", "Dataset", "Upload", "Collection", "Publication", "Epicollection"]
    ] = None  # type: ignore
    """the type of entity"""


class EntitiesPublication(Publication):
    entity_type: Optional[
        Literal["Donor", "Sample", "Dataset", "Upload", "Collection", "Publication", "Epicollection"]
    ] = None  # type: ignore
    """the type of entity"""


class EntitiesEpicollection(Epicollection):
    entity_type: Optional[
        Literal["Donor", "Sample", "Dataset", "Upload", "Collection", "Publication", "Epicollection"]
    ] = None  # type: ignore
    """the type of entity"""


Entity: TypeAlias = Union[
    EntitiesDonor,
    EntitiesSample,
    DatasetsDataset,
    EntitiesUpload,
    EntitiesCollection,
    EntitiesPublication,
    EntitiesEpicollection,
]
