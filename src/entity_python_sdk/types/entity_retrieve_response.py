# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .file import File
from .donor import Donor
from .person import Person
from .sample import Sample
from .upload import Upload
from .dataset import Dataset
from .._compat import PYDANTIC_V2
from .._models import BaseModel
from .collection import Collection

__all__ = [
    "EntityRetrieveResponse",
    "EntitiesDonor",
    "EntitiesSample",
    "DatasetsDataset",
    "EntitiesUpload",
    "EntitiesCollection",
    "UnionMember5",
    "UnionMember5Antibody",
    "UnionMember5DirectAncestor",
    "UnionMember6",
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


class UnionMember5Antibody(BaseModel):
    antibody_name: Optional[str] = None
    """The name of the antibody."""

    channel_id: Optional[str] = None
    """The assay specific identifier for the channel corresponding to the antibody."""

    conjugated_cat_number: Optional[str] = None
    """An antibody may be conjugated to a fluorescent tag or a metal tag for detection.

    Conjugated antibodies may be purchased from commercial providers. Blank if not
    applicable.
    """

    conjugated_tag: Optional[str] = None
    """An antibody may be conjugated to a fluorescent tag or a metal tag for detection.

    Conjugated antibodies may be purchased from commercial providers. Blank if not
    applicable.
    """

    dilution: Optional[str] = None
    """The dilition ratio, e.g. 1/200 for the antibody. Blank if not applicable."""

    lot_number: Optional[str] = None
    """The antibody lot number from the vendor."""

    rr_id: Optional[str] = None
    """
    The unique antibody identifier from the Antibody Registry
    (https://antibodyregistry.org).
    """

    uniprot_accession_number: Optional[str] = None
    """
    The unique identifier for the target protein in the UniProt database
    (https://www.uniprot.org).
    """


UnionMember5DirectAncestor: TypeAlias = Union[Sample, "Dataset"]


class UnionMember5(BaseModel):
    entity_type: Literal["Donor", "Sample", "Dataset", "Upload", "Collection", "Publication", "Epicollection"]
    """One of the normalized entity types: Dataset, Collection, Sample, Donor"""

    antibodies: Optional[List[UnionMember5Antibody]] = None
    """A list of antibodies used in the assay that created the dataset"""

    associated_collection: Optional[object] = None
    """The associated collection for a given publication"""

    calculated_metadata: Optional[object] = None
    """Calculated metadata outputted from the processing pipeline."""

    collections: Optional[List["Collection"]] = None
    """A list of collections that this dataset belongs to."""

    contacts: Optional[List[Person]] = None
    """
    A list of the people who are the main contacts to get information about the
    entity.
    """

    contains_human_genetic_sequences: Optional[bool] = None
    """True if the data contains any human genetic sequence information.

    Can only be set at CREATE/POST time
    """

    contributors: Optional[List[Person]] = None
    """A list of people who contributed to the creation of this dataset.

    Returned as an array of contributor where the structure of a contributor is
    """

    created_by_user_displayname: Optional[str] = None
    """The name of the person or process authenticated when creating the object"""

    created_by_user_email: Optional[str] = None
    """
    The email address of the person or process authenticated when creating the
    object.
    """

    created_by_user_sub: Optional[str] = None
    """
    The subject id as provided by the authorization mechanism for the person or
    process authenticated when creating the object.
    """

    created_timestamp: Optional[int] = None
    """The timestamp of when the node was created.

    The format is an integer representing milliseconds since midnight Jan 1, 1970
    """

    creators: Optional[List[Person]] = None
    """
    A list of the people who created the entity with full name, email, ORCID iD,
    institution, etc.. This is analogus to the author list on a publication.
    """

    data_access_level: Optional[Literal["public", "consortium"]] = None
    """One of the values: public, consortium."""

    data_types: Optional[
        List[
            Literal[
                "AF",
                "ATACseq-bulk",
                "bulk_atacseq",
                "cell-dive",
                "CODEX",
                "codex_cytokit",
                "DART-FISH",
                "image_pyramid",
                "IMC",
                "3D-IMC",
                "lc-ms_label-free",
                "lc-ms_labeled",
                "lc-ms-ms_label-free",
                "lc-ms-ms_labeled",
                "LC-MS-untargeted",
                "Lightsheet",
                "MALDI-IMS-neg",
                "MALDI-IMS-pos",
                "MxIF",
                "PAS",
                "bulk-RNA",
                "salmon_rnaseq_bulk",
                "SNAREseq",
                "sc_atac_seq_snare_lab",
                "sc_atac_seq_snare",
                "scRNA-Seq-10x",
                "salmon_rnaseq_10x",
                "sc_rna_seq_snare_lab",
                "salmon_rnaseq_snareseq",
                "sciATACseq",
                "sc_atac_seq_sci",
                "sciRNAseq",
                "salmon_rnaseq_sciseq",
                "seqFish",
                "seqFish_lab_processed",
                "snATACseq",
                "sn_atac_seq",
                "snRNAseq",
                "salmon_sn_rnaseq_10x",
                "Slide-seq",
                "Targeted-Shotgun-LC-MS",
                "TMT-LC-MS",
                "WGS",
            ]
        ]
    ] = None
    """The data or assay types contained in this dataset as a json array of strings.

    Each is an assay code from
    [assay types](https://github.com/hubmapconsortium/search-api/blob/main/src/search-schema/data/definitions/enums/assay_types.yaml).
    """

    dbgap_sra_experiment_url: Optional[str] = None
    """A URL linking the dataset to the associated uploaded data at dbGaP."""

    dbgap_study_url: Optional[str] = None
    """A URL linking the dataset to the particular study on dbGap it belongs to"""

    description: Optional[str] = None
    """Free text description of the dataset"""

    direct_ancestors: Optional[List[UnionMember5DirectAncestor]] = None
    """
    A list of direct parent ancensters (one level above) that the Dataset was
    derived from.
    """

    doi_url: Optional[str] = None
    """The url from the doi registry for this entity.

    e.g. https://doi.org/10.35079/hbm289.pcbm.487
    """

    error_message: Optional[str] = None
    """
    An open text field that holds the last error message that arose from pipeline
    validation or analysis.
    """

    files: Optional[List[File]] = None
    """A list of files associated with the dataset."""

    group_name: Optional[str] = None
    """
    The displayname of globus group which the user who created this entity is a
    member of
    """

    group_uuid: Optional[str] = None
    """The uuid of globus group which the user who created this entity is a member of.

    This is required on Create/POST if the user creating the Donor is a member of
    more than one write group. This property cannot be set via PUT (only on
    Create/POST).
    """

    hubmap_id: Optional[str] = None
    """
    A HuBMAP Consortium wide unique identifier randomly generated in the format
    HBM###.ABCD.### for every entity.
    """

    ingest_metadata: Optional[object] = None
    """Information associated with running the ingest and processing pipelines."""

    issue: Optional[int] = None
    """The issue number of the journal that it was published in."""

    last_modified_timestamp: Optional[int] = None
    """The timestamp of when the object was last modified.

    The format is an integer representing milliseconds since midnight, Jan 1, 1970
    """

    last_modified_user_displayname: Optional[str] = None
    """
    The name of the person or process which authenticated when the object was last
    modified.
    """

    last_modified_user_email: Optional[str] = None
    """
    The email address of the person or process which authenticated when the object
    was last modified.
    """

    last_modified_user_sub: Optional[str] = None
    """
    The subject id of the user who last modified the entity as provided by the
    authorization mechanism for the person or process authenticated when the object
    was modified.
    """

    local_directory_rel_path: Optional[str] = None
    """
    The path on the local HIVE file system, relative to the base data directory,
    where the data is stored.
    """

    metadata: Optional[object] = None
    """Metadata associated with the ingested experimental data."""

    next_revision_uuid: Optional[str] = None
    """The uuid of next revision dataset"""

    omap_doi: Optional[str] = None
    """A DOI pointing to an Organ Mapping Antibody Panel relevant to this publication"""

    pages_or_article_num: Optional[str] = None
    """
    The pages or the article number in the publication journal e.g., “23”, “23-49”,
    “e1003424”.
    """

    previous_revision_uuid: Optional[str] = None
    """The uuid of previous revision dataset. Can only be set at Create/POST time."""

    publication_date: Optional[str] = None
    """The date of publication"""

    publication_doi: Optional[str] = None
    """The doi of the publication. (##.####/[alpha-numeric-string])"""

    publication_url: Optional[str] = None
    """
    he URL at the publishers server for print/pre-print
    (http(s)://[alpha-numeric-string].[alpha-numeric-string].[...])
    """

    publication_venue: Optional[str] = None
    """The venue of the publication, journal, conference, preprint server, etc..."""

    published_timestamp: Optional[int] = None
    """The timestamp of when the dataset was published.

    The format is an integer representing milliseconds since midnight, Jan 1, 1970.
    """

    published_user_displayname: Optional[str] = None
    """The name of the authenticated user or process that published the data."""

    published_user_email: Optional[str] = None
    """
    The email address of the user who published the provided by the authorization
    mechanism for the person or process authenticated when published.
    """

    published_user_sub: Optional[str] = None
    """
    The subject id for the user who published the data as provided by the
    authorization mechanism for the person or process authenticated when the dataset
    was published.
    """

    registered_doi: Optional[str] = None
    """The doi of a the registered entity.

    e.g. 10.35079/hbm289.pcbm.487. This is set during the publication process and
    currently available for certain Collections and Datasets.
    """

    retraction_reason: Optional[str] = None
    """Information recorded about why a the dataset was retracted."""

    status: Optional[Literal["New", "Processing", "QA", "Published", "Error", "Hold", "Invalid"]] = None
    """One of: New|Processing|QA|Published|Error|Hold|Invalid"""

    sub_status: Optional[str] = None
    """A sub-status provided to further define the status.

    The only current allowable value is "Retracted"
    """

    thumbnail_file: Optional[object] = None
    """The dataset thumbnail file detail.

    Stored in db as a stringfied json, e.g., {"filename": "thumbnail.jpg",
    "file_uuid": "c35002f9c3d49f8b77e1e2cd4a01803d"}
    """

    title: Optional[str] = None
    """The Publication title."""

    upload: Optional[List["Upload"]] = None
    """The Data Upload that this dataset is associated with."""

    uuid: Optional[str] = None
    """The HuBMAP unique identifier, intended for internal software use only.

    This is a 32 digit hexadecimal uuid e.g. 461bbfdc353a2673e381f632510b0f17
    """

    volume: Optional[int] = None
    """The volume number of a journal that it was published in."""


class UnionMember6(BaseModel):
    entity_type: Literal["Donor", "Sample", "Dataset", "Upload", "Collection", "Publication", "Epicollection"]
    """One of the normalized entity types: Dataset, Collection, Sample, Donor"""

    contacts: Optional[List[Person]] = None
    """
    A list of the people who are the main contacts to get information about the
    entity.
    """

    contributors: Optional[List[Person]] = None
    """
    A list of the people who created the entity with full name, email, ORCID iD,
    institution, etc.. This is analogus to the author list on a publication.
    """

    created_by_user_displayname: Optional[str] = None
    """The name of the person or process authenticated when creating the object"""

    created_by_user_email: Optional[str] = None
    """
    The email address of the person or process authenticated when creating the
    object.
    """

    created_by_user_sub: Optional[str] = None
    """
    The subject id as provided by the authorization mechanism for the person or
    process authenticated when creating the object.
    """

    created_timestamp: Optional[int] = None
    """The timestamp of when the node was created.

    The format is an integer representing milliseconds since midnight Jan 1, 1970
    """

    datasets: Optional[List["Dataset"]] = None
    """The datasets that are contained in the Collection."""

    doi_url: Optional[str] = None
    """The url from the doi registry for this entity.

    e.g. https://doi.org/10.35079/hbm289.pcbm.487
    """

    hubmap_id: Optional[str] = None
    """
    A HuBMAP Consortium wide unique identifier randomly generated in the format
    HBM###.ABCD.### for every entity.
    """

    last_modified_timestamp: Optional[int] = None
    """The timestamp of when the object was last modified.

    The format is an integer representing milliseconds since midnight, Jan 1, 1970
    """

    last_modified_user_displayname: Optional[str] = None
    """
    The name of the person or process which authenticated when the object was last
    modified.
    """

    last_modified_user_email: Optional[str] = None
    """
    The email address of the person or process which authenticated when the object
    was last modified.
    """

    last_modified_user_sub: Optional[str] = None
    """
    The subject id of the user who last modified the entity as provided by the
    authorization mechanism for the person or process authenticated when the object
    was modified.
    """

    registered_doi: Optional[str] = None
    """The doi of a the registered entity.

    e.g. 10.35079/hbm289.pcbm.487. This is set during the publication process and
    currently available for certain Collections and Datasets.
    """

    title: Optional[str] = None
    """The title of the Collection"""

    uuid: Optional[str] = None
    """The HuBMAP unique identifier, intended for internal software use only.

    This is a 32 digit hexadecimal uuid e.g. 461bbfdc353a2673e381f632510b0f17
    """


EntityRetrieveResponse: TypeAlias = Union[
    EntitiesDonor, EntitiesSample, DatasetsDataset, EntitiesUpload, EntitiesCollection, UnionMember5, UnionMember6
]

from .upload import Upload
from .dataset import Dataset
from .collection import Collection

if PYDANTIC_V2:
    UnionMember5.model_rebuild()
    UnionMember5Antibody.model_rebuild()
    UnionMember6.model_rebuild()
else:
    UnionMember5.update_forward_refs()  # type: ignore
    UnionMember5Antibody.update_forward_refs()  # type: ignore
    UnionMember6.update_forward_refs()  # type: ignore
