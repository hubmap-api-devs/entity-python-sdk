# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, TypedDict

from .file_param import FileParam
from .person_param import PersonParam

__all__ = ["PublicationParam", "Antibody"]


class Antibody(TypedDict, total=False):
    antibody_name: str
    """The name of the antibody."""

    channel_id: str
    """The assay specific identifier for the channel corresponding to the antibody."""

    conjugated_cat_number: str
    """An antibody may be conjugated to a fluorescent tag or a metal tag for detection.

    Conjugated antibodies may be purchased from commercial providers. Blank if not
    applicable.
    """

    conjugated_tag: str
    """An antibody may be conjugated to a fluorescent tag or a metal tag for detection.

    Conjugated antibodies may be purchased from commercial providers. Blank if not
    applicable.
    """

    dilution: str
    """The dilition ratio, e.g. 1/200 for the antibody. Blank if not applicable."""

    lot_number: str
    """The antibody lot number from the vendor."""

    rr_id: str
    """
    The unique antibody identifier from the Antibody Registry
    (https://antibodyregistry.org).
    """

    uniprot_accession_number: str
    """
    The unique identifier for the target protein in the UniProt database
    (https://www.uniprot.org).
    """


class PublicationParam(TypedDict, total=False):
    antibodies: Iterable[Antibody]
    """A list of antibodies used in the assay that created the dataset"""

    associated_collection: object
    """The associated collection for a given publication"""

    associated_collection_uuid: str
    """The uuid of the associated collection for a given publication."""

    calculated_metadata: object
    """Calculated metadata outputted from the processing pipeline."""

    contacts: Iterable[PersonParam]
    """
    A list of the people who are the main contacts to get information about the
    entity.
    """

    contains_human_genetic_sequences: bool
    """True if the data contains any human genetic sequence information.

    Can only be set at CREATE/POST time
    """

    creators: Iterable[PersonParam]
    """
    A list of the people who created the entity with full name, email, ORCID iD,
    institution, etc.. This is analogus to the author list on a publication.
    """

    data_types: List[
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
    """The data or assay types contained in this dataset as a json array of strings.

    Each is an assay code from
    [assay types](https://github.com/hubmapconsortium/search-api/blob/main/src/search-schema/data/definitions/enums/assay_types.yaml).
    """

    dbgap_sra_experiment_url: str
    """A URL linking the dataset to the associated uploaded data at dbGaP."""

    dbgap_study_url: str
    """A URL linking the dataset to the particular study on dbGap it belongs to"""

    description: str
    """Free text description of the dataset"""

    error_message: str
    """
    An open text field that holds the last error message that arose from pipeline
    validation or analysis.
    """

    files: Iterable[FileParam]
    """A list of files associated with the dataset."""

    group_uuid: str
    """The uuid of globus group which the user who created this entity is a member of.

    This is required on Create/POST if the user creating the Donor is a member of
    more than one write group. This property cannot be set via PUT (only on
    Create/POST).
    """

    ingest_metadata: object
    """Information associated with running the ingest and processing pipelines."""

    issue: int
    """The issue number of the journal that it was published in."""

    metadata: object
    """Metadata associated with the ingested experimental data."""

    omap_doi: str
    """A DOI pointing to an Organ Mapping Antibody Panel relevant to this publication"""

    pages_or_article_num: str
    """
    The pages or the article number in the publication journal e.g., “23”, “23-49”,
    “e1003424”.
    """

    previous_revision_uuid: str
    """The uuid of previous revision dataset. Can only be set at Create/POST time."""

    publication_date: str
    """The date of publication"""

    publication_doi: str
    """The doi of the publication. (##.####/[alpha-numeric-string])"""

    publication_url: str
    """
    he URL at the publishers server for print/pre-print
    (http(s)://[alpha-numeric-string].[alpha-numeric-string].[...])
    """

    publication_venue: str
    """The venue of the publication, journal, conference, preprint server, etc..."""

    registered_doi: str
    """The doi of a the registered entity.

    e.g. 10.35079/hbm289.pcbm.487. This is set during the publication process and
    currently available for certain Collections and Datasets.
    """

    retraction_reason: str
    """Information recorded about why a the dataset was retracted."""

    status: Literal["New", "Processing", "QA", "Published", "Error", "Hold", "Invalid"]
    """One of: New|Processing|QA|Published|Error|Hold|Invalid"""

    sub_status: str
    """A sub-status provided to further define the status.

    The only current allowable value is "Retracted"
    """

    thumbnail_file_to_add: str
    """Just a temporary file id.

    Provide as a json object with an temp_file_id like
    {"temp_file_id":"dzevgd6xjs4d5grmcp4n"}
    """

    thumbnail_file_to_remove: str
    """The thumbnail image file previously uploaded to delete.

    Provide as a string of the file_uuid like: "c35002f9c3d49f8b77e1e2cd4a01803d"
    """

    title: str
    """The Publication title."""

    volume: int
    """The volume number of a journal that it was published in."""
