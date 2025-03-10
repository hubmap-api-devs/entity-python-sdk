# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from entity_python_sdk import EntityPythonSDK, AsyncEntityPythonSDK
from entity_python_sdk.types import (
    Entity,
    Instanceof,
    EntityListTupletsResponse,
    EntityListUploadsResponse,
    EntityListSiblingsResponse,
    EntityListCollectionsResponse,
    EntityListEntityTypesResponse,
    EntityListAncestorOrgansResponse,
    EntityCreateMultipleSamplesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEntities:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: EntityPythonSDK) -> None:
        entity = client.entities.retrieve(
            "id",
        )
        assert_matches_type(Entity, entity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: EntityPythonSDK) -> None:
        response = client.entities.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(Entity, entity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: EntityPythonSDK) -> None:
        with client.entities.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(Entity, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: EntityPythonSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.entities.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update_overload_1(self, client: EntityPythonSDK) -> None:
        entity = client.entities.update(
            id="id",
        )
        assert entity is None

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params_overload_1(self, client: EntityPythonSDK) -> None:
        entity = client.entities.update(
            id="id",
            contacts=[
                {
                    "affiliation": "affiliation",
                    "first_name": "first_name",
                    "last_name": "last_name",
                    "middle_name_or_initial": "middle_name_or_initial",
                    "orcid_id": "orcid_id",
                }
            ],
            creators=[
                {
                    "affiliation": "affiliation",
                    "first_name": "first_name",
                    "last_name": "last_name",
                    "middle_name_or_initial": "middle_name_or_initial",
                    "orcid_id": "orcid_id",
                }
            ],
            description="description",
            group_uuid="group_uuid",
            image_files_to_add=["string"],
            image_files_to_remove=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            lab_donor_id="lab_donor_id",
            label="label",
            metadata={
                "living_donor_data": [
                    {
                        "code": "code",
                        "concept_id": "concept_id",
                        "data_type": "Nominal",
                        "data_value": "data_value",
                        "end_datetime": 0,
                        "graph_version": "graph_version",
                        "grouping_code": "grouping_code",
                        "grouping_concept": "grouping_concept",
                        "grouping_concept_preferred_term": "grouping_concept_preferred_term",
                        "grouping_sab": "grouping_sab",
                        "numeric_operator": "EQ",
                        "preferred_term": "preferred_term",
                        "sab": "sab",
                        "start_datetime": 0,
                        "units": "units",
                    }
                ],
                "organ_donor_data": [
                    {
                        "code": "code",
                        "concept_id": "concept_id",
                        "data_type": "Nominal",
                        "data_value": "data_value",
                        "end_datetime": 0,
                        "graph_version": "graph_version",
                        "grouping_code": "grouping_code",
                        "grouping_concept": "grouping_concept",
                        "grouping_concept_preferred_term": "grouping_concept_preferred_term",
                        "grouping_sab": "grouping_sab",
                        "numeric_operator": "EQ",
                        "preferred_term": "preferred_term",
                        "sab": "sab",
                        "start_datetime": 0,
                        "units": "units",
                    }
                ],
            },
            protocol_url="protocol_url",
            registered_doi="registered_doi",
        )
        assert entity is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_overload_1(self, client: EntityPythonSDK) -> None:
        response = client.entities.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert entity is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_overload_1(self, client: EntityPythonSDK) -> None:
        with client.entities.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert entity is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update_overload_1(self, client: EntityPythonSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.entities.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update_overload_2(self, client: EntityPythonSDK) -> None:
        entity = client.entities.update(
            id="id",
        )
        assert entity is None

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params_overload_2(self, client: EntityPythonSDK) -> None:
        entity = client.entities.update(
            id="id",
            contacts=[
                {
                    "affiliation": "affiliation",
                    "first_name": "first_name",
                    "last_name": "last_name",
                    "middle_name_or_initial": "middle_name_or_initial",
                    "orcid_id": "orcid_id",
                }
            ],
            creators=[
                {
                    "affiliation": "affiliation",
                    "first_name": "first_name",
                    "last_name": "last_name",
                    "middle_name_or_initial": "middle_name_or_initial",
                    "orcid_id": "orcid_id",
                }
            ],
            data_access_level="consortium",
            description="description",
            direct_ancestor={
                "contacts": [
                    {
                        "affiliation": "affiliation",
                        "first_name": "first_name",
                        "last_name": "last_name",
                        "middle_name_or_initial": "middle_name_or_initial",
                        "orcid_id": "orcid_id",
                    }
                ],
                "creators": [
                    {
                        "affiliation": "affiliation",
                        "first_name": "first_name",
                        "last_name": "last_name",
                        "middle_name_or_initial": "middle_name_or_initial",
                        "orcid_id": "orcid_id",
                    }
                ],
                "description": "description",
                "group_uuid": "group_uuid",
                "image_files_to_add": ["string"],
                "image_files_to_remove": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "lab_donor_id": "lab_donor_id",
                "label": "label",
                "metadata": {
                    "living_donor_data": [
                        {
                            "code": "code",
                            "concept_id": "concept_id",
                            "data_type": "Nominal",
                            "data_value": "data_value",
                            "end_datetime": 0,
                            "graph_version": "graph_version",
                            "grouping_code": "grouping_code",
                            "grouping_concept": "grouping_concept",
                            "grouping_concept_preferred_term": "grouping_concept_preferred_term",
                            "grouping_sab": "grouping_sab",
                            "numeric_operator": "EQ",
                            "preferred_term": "preferred_term",
                            "sab": "sab",
                            "start_datetime": 0,
                            "units": "units",
                        }
                    ],
                    "organ_donor_data": [
                        {
                            "code": "code",
                            "concept_id": "concept_id",
                            "data_type": "Nominal",
                            "data_value": "data_value",
                            "end_datetime": 0,
                            "graph_version": "graph_version",
                            "grouping_code": "grouping_code",
                            "grouping_concept": "grouping_concept",
                            "grouping_concept_preferred_term": "grouping_concept_preferred_term",
                            "grouping_sab": "grouping_sab",
                            "numeric_operator": "EQ",
                            "preferred_term": "preferred_term",
                            "sab": "sab",
                            "start_datetime": 0,
                            "units": "units",
                        }
                    ],
                },
                "protocol_url": "protocol_url",
                "registered_doi": "registered_doi",
            },
            direct_ancestor_uuid="direct_ancestor_uuid",
            group_uuid="group_uuid",
            image_files_to_add=["string"],
            image_files_to_remove=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            lab_tissue_sample_id="lab_tissue_sample_id",
            metadata={
                "cold_ischemia_time_unit": "cold_ischemia_time_unit",
                "cold_ischemia_time_value": 0,
                "health_status": "cancer",
                "organ_condition": "healthy",
                "pathologist_report": "pathologist_report",
                "perfusion_solution": "UWS",
                "procedure_date": "procedure_date",
                "sample_id": "sample_id",
                "specimen_preservation_temperature": "specimen_preservation_temperature",
                "specimen_quality_criteria": "specimen_quality_criteria",
                "specimen_tumor_distance_unit": "specimen_tumor_distance_unit",
                "specimen_tumor_distance_value": "specimen_tumor_distance_value",
                "vital_state": "living",
                "warm_ischemia_time_unit": "warm_ischemia_time_unit",
                "warm_ischemia_time_value": 0,
            },
            metadata_files_to_add=["string"],
            metadata_files_to_remove=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            organ="AO",
            organ_other="organ_other",
            protocol_url="protocol_url",
            registered_doi="registered_doi",
            rui_location={},
            sample_category="organ",
            submission_id="submission_id",
            visit="visit",
        )
        assert entity is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_overload_2(self, client: EntityPythonSDK) -> None:
        response = client.entities.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert entity is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_overload_2(self, client: EntityPythonSDK) -> None:
        with client.entities.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert entity is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update_overload_2(self, client: EntityPythonSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.entities.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update_overload_3(self, client: EntityPythonSDK) -> None:
        entity = client.entities.update(
            id="id",
        )
        assert entity is None

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params_overload_3(self, client: EntityPythonSDK) -> None:
        entity = client.entities.update(
            id="id",
            antibodies=[
                {
                    "antibody_name": "antibody_name",
                    "channel_id": "channel_id",
                    "conjugated_cat_number": "conjugated_cat_number",
                    "conjugated_tag": "conjugated_tag",
                    "dilution": "dilution",
                    "lot_number": "lot_number",
                    "rr_id": "rr_id",
                    "uniprot_accession_number": "uniprot_accession_number",
                }
            ],
            calculated_metadata={},
            contacts=[
                {
                    "affiliation": "affiliation",
                    "first_name": "first_name",
                    "last_name": "last_name",
                    "middle_name_or_initial": "middle_name_or_initial",
                    "orcid_id": "orcid_id",
                }
            ],
            contains_human_genetic_sequences=True,
            creation_action="creation_action",
            creators=[
                {
                    "affiliation": "affiliation",
                    "first_name": "first_name",
                    "last_name": "last_name",
                    "middle_name_or_initial": "middle_name_or_initial",
                    "orcid_id": "orcid_id",
                }
            ],
            data_types=["AF"],
            dbgap_sra_experiment_url="dbgap_sra_experiment_url",
            dbgap_study_url="dbgap_study_url",
            description="description",
            error_message="error_message",
            files=[
                {
                    "description": "description",
                    "file_uuid": "file_uuid",
                    "filename": "filename",
                }
            ],
            group_uuid="group_uuid",
            ingest_metadata={},
            intended_dataset_type="intended_dataset_type",
            intended_organ="intended_organ",
            metadata={},
            previous_revision_uuid="previous_revision_uuid",
            previous_revision_uuids=["string"],
            registered_doi="registered_doi",
            retraction_reason="retraction_reason",
            status="New",
            sub_status="sub_status",
            thumbnail_file_to_add="thumbnail_file_to_add",
            thumbnail_file_to_remove="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            title="title",
        )
        assert entity is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_overload_3(self, client: EntityPythonSDK) -> None:
        response = client.entities.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert entity is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_overload_3(self, client: EntityPythonSDK) -> None:
        with client.entities.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert entity is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update_overload_3(self, client: EntityPythonSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.entities.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update_overload_4(self, client: EntityPythonSDK) -> None:
        entity = client.entities.update(
            id="id",
        )
        assert entity is None

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params_overload_4(self, client: EntityPythonSDK) -> None:
        entity = client.entities.update(
            id="id",
            dataset_uuids_to_link=["string"],
            dataset_uuids_to_unlink=["string"],
            description="description",
            group_uuid="group_uuid",
            status="status",
            title="title",
            validation_message="validation_message",
        )
        assert entity is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_overload_4(self, client: EntityPythonSDK) -> None:
        response = client.entities.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert entity is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_overload_4(self, client: EntityPythonSDK) -> None:
        with client.entities.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert entity is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update_overload_4(self, client: EntityPythonSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.entities.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update_overload_5(self, client: EntityPythonSDK) -> None:
        entity = client.entities.update(
            id="id",
        )
        assert entity is None

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params_overload_5(self, client: EntityPythonSDK) -> None:
        entity = client.entities.update(
            id="id",
            antibodies=[
                {
                    "antibody_name": "antibody_name",
                    "channel_id": "channel_id",
                    "conjugated_cat_number": "conjugated_cat_number",
                    "conjugated_tag": "conjugated_tag",
                    "dilution": "dilution",
                    "lot_number": "lot_number",
                    "rr_id": "rr_id",
                    "uniprot_accession_number": "uniprot_accession_number",
                }
            ],
            associated_collection={},
            associated_collection_uuid="associated_collection_uuid",
            calculated_metadata={},
            contacts=[
                {
                    "affiliation": "affiliation",
                    "first_name": "first_name",
                    "last_name": "last_name",
                    "middle_name_or_initial": "middle_name_or_initial",
                    "orcid_id": "orcid_id",
                }
            ],
            contains_human_genetic_sequences=True,
            creators=[
                {
                    "affiliation": "affiliation",
                    "first_name": "first_name",
                    "last_name": "last_name",
                    "middle_name_or_initial": "middle_name_or_initial",
                    "orcid_id": "orcid_id",
                }
            ],
            data_types=["AF"],
            dbgap_sra_experiment_url="dbgap_sra_experiment_url",
            dbgap_study_url="dbgap_study_url",
            description="description",
            error_message="error_message",
            files=[
                {
                    "description": "description",
                    "file_uuid": "file_uuid",
                    "filename": "filename",
                }
            ],
            group_uuid="group_uuid",
            ingest_metadata={},
            issue=0,
            metadata={},
            omap_doi="omap_doi",
            pages_or_article_num="pages_or_article_num",
            previous_revision_uuid="previous_revision_uuid",
            publication_date="publication_date",
            publication_doi="publication_doi",
            publication_url="publication_url",
            publication_venue="publication_venue",
            registered_doi="registered_doi",
            retraction_reason="retraction_reason",
            status="New",
            sub_status="sub_status",
            thumbnail_file_to_add="thumbnail_file_to_add",
            thumbnail_file_to_remove="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            title="title",
            volume=0,
        )
        assert entity is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_overload_5(self, client: EntityPythonSDK) -> None:
        response = client.entities.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert entity is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_overload_5(self, client: EntityPythonSDK) -> None:
        with client.entities.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert entity is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update_overload_5(self, client: EntityPythonSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.entities.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update_overload_6(self, client: EntityPythonSDK) -> None:
        entity = client.entities.update(
            id="id",
        )
        assert entity is None

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params_overload_6(self, client: EntityPythonSDK) -> None:
        entity = client.entities.update(
            id="id",
            contacts=[
                {
                    "affiliation": "affiliation",
                    "first_name": "first_name",
                    "last_name": "last_name",
                    "middle_name_or_initial": "middle_name_or_initial",
                    "orcid_id": "orcid_id",
                }
            ],
            contributors=[
                {
                    "affiliation": "affiliation",
                    "first_name": "first_name",
                    "last_name": "last_name",
                    "middle_name_or_initial": "middle_name_or_initial",
                    "orcid_id": "orcid_id",
                }
            ],
            registered_doi="registered_doi",
            title="title",
        )
        assert entity is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_overload_6(self, client: EntityPythonSDK) -> None:
        response = client.entities.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert entity is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_overload_6(self, client: EntityPythonSDK) -> None:
        with client.entities.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert entity is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update_overload_6(self, client: EntityPythonSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.entities.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update_overload_7(self, client: EntityPythonSDK) -> None:
        entity = client.entities.update(
            id="id",
        )
        assert entity is None

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params_overload_7(self, client: EntityPythonSDK) -> None:
        entity = client.entities.update(
            id="id",
            contacts=[
                {
                    "affiliation": "affiliation",
                    "first_name": "first_name",
                    "last_name": "last_name",
                    "middle_name_or_initial": "middle_name_or_initial",
                    "orcid_id": "orcid_id",
                }
            ],
            contributors=[
                {
                    "affiliation": "affiliation",
                    "first_name": "first_name",
                    "last_name": "last_name",
                    "middle_name_or_initial": "middle_name_or_initial",
                    "orcid_id": "orcid_id",
                }
            ],
            registered_doi="registered_doi",
            title="title",
        )
        assert entity is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_overload_7(self, client: EntityPythonSDK) -> None:
        response = client.entities.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert entity is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_overload_7(self, client: EntityPythonSDK) -> None:
        with client.entities.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert entity is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update_overload_7(self, client: EntityPythonSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.entities.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_create_multiple_samples(self, client: EntityPythonSDK) -> None:
        entity = client.entities.create_multiple_samples(
            "count",
        )
        assert_matches_type(EntityCreateMultipleSamplesResponse, entity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_multiple_samples(self, client: EntityPythonSDK) -> None:
        response = client.entities.with_raw_response.create_multiple_samples(
            "count",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntityCreateMultipleSamplesResponse, entity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_multiple_samples(self, client: EntityPythonSDK) -> None:
        with client.entities.with_streaming_response.create_multiple_samples(
            "count",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(EntityCreateMultipleSamplesResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create_multiple_samples(self, client: EntityPythonSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `count` but received ''"):
            client.entities.with_raw_response.create_multiple_samples(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get_globus_url(self, client: EntityPythonSDK) -> None:
        entity = client.entities.get_globus_url(
            "id",
        )
        assert_matches_type(str, entity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_globus_url(self, client: EntityPythonSDK) -> None:
        response = client.entities.with_raw_response.get_globus_url(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(str, entity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_globus_url(self, client: EntityPythonSDK) -> None:
        with client.entities.with_streaming_response.get_globus_url(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(str, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get_globus_url(self, client: EntityPythonSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.entities.with_raw_response.get_globus_url(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_is_instance_of(self, client: EntityPythonSDK) -> None:
        entity = client.entities.is_instance_of(
            type="type",
            id="id",
        )
        assert_matches_type(Instanceof, entity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_is_instance_of(self, client: EntityPythonSDK) -> None:
        response = client.entities.with_raw_response.is_instance_of(
            type="type",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(Instanceof, entity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_is_instance_of(self, client: EntityPythonSDK) -> None:
        with client.entities.with_streaming_response.is_instance_of(
            type="type",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(Instanceof, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_is_instance_of(self, client: EntityPythonSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.entities.with_raw_response.is_instance_of(
                type="type",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `type` but received ''"):
            client.entities.with_raw_response.is_instance_of(
                type="",
                id="id",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list_ancestor_organs(self, client: EntityPythonSDK) -> None:
        entity = client.entities.list_ancestor_organs(
            "id",
        )
        assert_matches_type(EntityListAncestorOrgansResponse, entity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_ancestor_organs(self, client: EntityPythonSDK) -> None:
        response = client.entities.with_raw_response.list_ancestor_organs(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntityListAncestorOrgansResponse, entity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_ancestor_organs(self, client: EntityPythonSDK) -> None:
        with client.entities.with_streaming_response.list_ancestor_organs(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(EntityListAncestorOrgansResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list_ancestor_organs(self, client: EntityPythonSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.entities.with_raw_response.list_ancestor_organs(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list_collections(self, client: EntityPythonSDK) -> None:
        entity = client.entities.list_collections(
            id="id",
        )
        assert_matches_type(EntityListCollectionsResponse, entity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_collections_with_all_params(self, client: EntityPythonSDK) -> None:
        entity = client.entities.list_collections(
            id="id",
            property="uuid",
        )
        assert_matches_type(EntityListCollectionsResponse, entity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_collections(self, client: EntityPythonSDK) -> None:
        response = client.entities.with_raw_response.list_collections(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntityListCollectionsResponse, entity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_collections(self, client: EntityPythonSDK) -> None:
        with client.entities.with_streaming_response.list_collections(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(EntityListCollectionsResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list_collections(self, client: EntityPythonSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.entities.with_raw_response.list_collections(
                id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list_entity_types(self, client: EntityPythonSDK) -> None:
        entity = client.entities.list_entity_types()
        assert_matches_type(EntityListEntityTypesResponse, entity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_entity_types(self, client: EntityPythonSDK) -> None:
        response = client.entities.with_raw_response.list_entity_types()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntityListEntityTypesResponse, entity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_entity_types(self, client: EntityPythonSDK) -> None:
        with client.entities.with_streaming_response.list_entity_types() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(EntityListEntityTypesResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_siblings(self, client: EntityPythonSDK) -> None:
        entity = client.entities.list_siblings(
            id="id",
        )
        assert_matches_type(EntityListSiblingsResponse, entity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_siblings_with_all_params(self, client: EntityPythonSDK) -> None:
        entity = client.entities.list_siblings(
            id="id",
            include_old_revisions="true",
            property_key="uuid",
            status="new",
        )
        assert_matches_type(EntityListSiblingsResponse, entity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_siblings(self, client: EntityPythonSDK) -> None:
        response = client.entities.with_raw_response.list_siblings(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntityListSiblingsResponse, entity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_siblings(self, client: EntityPythonSDK) -> None:
        with client.entities.with_streaming_response.list_siblings(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(EntityListSiblingsResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list_siblings(self, client: EntityPythonSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.entities.with_raw_response.list_siblings(
                id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list_tuplets(self, client: EntityPythonSDK) -> None:
        entity = client.entities.list_tuplets(
            id="id",
        )
        assert_matches_type(EntityListTupletsResponse, entity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_tuplets_with_all_params(self, client: EntityPythonSDK) -> None:
        entity = client.entities.list_tuplets(
            id="id",
            property_key="uuid",
            status="new",
        )
        assert_matches_type(EntityListTupletsResponse, entity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_tuplets(self, client: EntityPythonSDK) -> None:
        response = client.entities.with_raw_response.list_tuplets(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntityListTupletsResponse, entity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_tuplets(self, client: EntityPythonSDK) -> None:
        with client.entities.with_streaming_response.list_tuplets(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(EntityListTupletsResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list_tuplets(self, client: EntityPythonSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.entities.with_raw_response.list_tuplets(
                id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list_uploads(self, client: EntityPythonSDK) -> None:
        entity = client.entities.list_uploads(
            id="id",
        )
        assert_matches_type(EntityListUploadsResponse, entity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_uploads_with_all_params(self, client: EntityPythonSDK) -> None:
        entity = client.entities.list_uploads(
            id="id",
            property="uuid",
        )
        assert_matches_type(EntityListUploadsResponse, entity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_uploads(self, client: EntityPythonSDK) -> None:
        response = client.entities.with_raw_response.list_uploads(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntityListUploadsResponse, entity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_uploads(self, client: EntityPythonSDK) -> None:
        with client.entities.with_streaming_response.list_uploads(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(EntityListUploadsResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list_uploads(self, client: EntityPythonSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.entities.with_raw_response.list_uploads(
                id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_provenance(self, client: EntityPythonSDK) -> None:
        entity = client.entities.retrieve_provenance(
            "id",
        )
        assert entity is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_provenance(self, client: EntityPythonSDK) -> None:
        response = client.entities.with_raw_response.retrieve_provenance(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert entity is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_provenance(self, client: EntityPythonSDK) -> None:
        with client.entities.with_streaming_response.retrieve_provenance(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert entity is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve_provenance(self, client: EntityPythonSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.entities.with_raw_response.retrieve_provenance(
                "",
            )


class TestAsyncEntities:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncEntityPythonSDK) -> None:
        entity = await async_client.entities.retrieve(
            "id",
        )
        assert_matches_type(Entity, entity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncEntityPythonSDK) -> None:
        response = await async_client.entities.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(Entity, entity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncEntityPythonSDK) -> None:
        async with async_client.entities.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(Entity, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncEntityPythonSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.entities.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncEntityPythonSDK) -> None:
        entity = await async_client.entities.update(
            id="id",
        )
        assert entity is None

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params_overload_1(self, async_client: AsyncEntityPythonSDK) -> None:
        entity = await async_client.entities.update(
            id="id",
            contacts=[
                {
                    "affiliation": "affiliation",
                    "first_name": "first_name",
                    "last_name": "last_name",
                    "middle_name_or_initial": "middle_name_or_initial",
                    "orcid_id": "orcid_id",
                }
            ],
            creators=[
                {
                    "affiliation": "affiliation",
                    "first_name": "first_name",
                    "last_name": "last_name",
                    "middle_name_or_initial": "middle_name_or_initial",
                    "orcid_id": "orcid_id",
                }
            ],
            description="description",
            group_uuid="group_uuid",
            image_files_to_add=["string"],
            image_files_to_remove=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            lab_donor_id="lab_donor_id",
            label="label",
            metadata={
                "living_donor_data": [
                    {
                        "code": "code",
                        "concept_id": "concept_id",
                        "data_type": "Nominal",
                        "data_value": "data_value",
                        "end_datetime": 0,
                        "graph_version": "graph_version",
                        "grouping_code": "grouping_code",
                        "grouping_concept": "grouping_concept",
                        "grouping_concept_preferred_term": "grouping_concept_preferred_term",
                        "grouping_sab": "grouping_sab",
                        "numeric_operator": "EQ",
                        "preferred_term": "preferred_term",
                        "sab": "sab",
                        "start_datetime": 0,
                        "units": "units",
                    }
                ],
                "organ_donor_data": [
                    {
                        "code": "code",
                        "concept_id": "concept_id",
                        "data_type": "Nominal",
                        "data_value": "data_value",
                        "end_datetime": 0,
                        "graph_version": "graph_version",
                        "grouping_code": "grouping_code",
                        "grouping_concept": "grouping_concept",
                        "grouping_concept_preferred_term": "grouping_concept_preferred_term",
                        "grouping_sab": "grouping_sab",
                        "numeric_operator": "EQ",
                        "preferred_term": "preferred_term",
                        "sab": "sab",
                        "start_datetime": 0,
                        "units": "units",
                    }
                ],
            },
            protocol_url="protocol_url",
            registered_doi="registered_doi",
        )
        assert entity is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncEntityPythonSDK) -> None:
        response = await async_client.entities.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert entity is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncEntityPythonSDK) -> None:
        async with async_client.entities.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert entity is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update_overload_1(self, async_client: AsyncEntityPythonSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.entities.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncEntityPythonSDK) -> None:
        entity = await async_client.entities.update(
            id="id",
        )
        assert entity is None

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params_overload_2(self, async_client: AsyncEntityPythonSDK) -> None:
        entity = await async_client.entities.update(
            id="id",
            contacts=[
                {
                    "affiliation": "affiliation",
                    "first_name": "first_name",
                    "last_name": "last_name",
                    "middle_name_or_initial": "middle_name_or_initial",
                    "orcid_id": "orcid_id",
                }
            ],
            creators=[
                {
                    "affiliation": "affiliation",
                    "first_name": "first_name",
                    "last_name": "last_name",
                    "middle_name_or_initial": "middle_name_or_initial",
                    "orcid_id": "orcid_id",
                }
            ],
            data_access_level="consortium",
            description="description",
            direct_ancestor={
                "contacts": [
                    {
                        "affiliation": "affiliation",
                        "first_name": "first_name",
                        "last_name": "last_name",
                        "middle_name_or_initial": "middle_name_or_initial",
                        "orcid_id": "orcid_id",
                    }
                ],
                "creators": [
                    {
                        "affiliation": "affiliation",
                        "first_name": "first_name",
                        "last_name": "last_name",
                        "middle_name_or_initial": "middle_name_or_initial",
                        "orcid_id": "orcid_id",
                    }
                ],
                "description": "description",
                "group_uuid": "group_uuid",
                "image_files_to_add": ["string"],
                "image_files_to_remove": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "lab_donor_id": "lab_donor_id",
                "label": "label",
                "metadata": {
                    "living_donor_data": [
                        {
                            "code": "code",
                            "concept_id": "concept_id",
                            "data_type": "Nominal",
                            "data_value": "data_value",
                            "end_datetime": 0,
                            "graph_version": "graph_version",
                            "grouping_code": "grouping_code",
                            "grouping_concept": "grouping_concept",
                            "grouping_concept_preferred_term": "grouping_concept_preferred_term",
                            "grouping_sab": "grouping_sab",
                            "numeric_operator": "EQ",
                            "preferred_term": "preferred_term",
                            "sab": "sab",
                            "start_datetime": 0,
                            "units": "units",
                        }
                    ],
                    "organ_donor_data": [
                        {
                            "code": "code",
                            "concept_id": "concept_id",
                            "data_type": "Nominal",
                            "data_value": "data_value",
                            "end_datetime": 0,
                            "graph_version": "graph_version",
                            "grouping_code": "grouping_code",
                            "grouping_concept": "grouping_concept",
                            "grouping_concept_preferred_term": "grouping_concept_preferred_term",
                            "grouping_sab": "grouping_sab",
                            "numeric_operator": "EQ",
                            "preferred_term": "preferred_term",
                            "sab": "sab",
                            "start_datetime": 0,
                            "units": "units",
                        }
                    ],
                },
                "protocol_url": "protocol_url",
                "registered_doi": "registered_doi",
            },
            direct_ancestor_uuid="direct_ancestor_uuid",
            group_uuid="group_uuid",
            image_files_to_add=["string"],
            image_files_to_remove=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            lab_tissue_sample_id="lab_tissue_sample_id",
            metadata={
                "cold_ischemia_time_unit": "cold_ischemia_time_unit",
                "cold_ischemia_time_value": 0,
                "health_status": "cancer",
                "organ_condition": "healthy",
                "pathologist_report": "pathologist_report",
                "perfusion_solution": "UWS",
                "procedure_date": "procedure_date",
                "sample_id": "sample_id",
                "specimen_preservation_temperature": "specimen_preservation_temperature",
                "specimen_quality_criteria": "specimen_quality_criteria",
                "specimen_tumor_distance_unit": "specimen_tumor_distance_unit",
                "specimen_tumor_distance_value": "specimen_tumor_distance_value",
                "vital_state": "living",
                "warm_ischemia_time_unit": "warm_ischemia_time_unit",
                "warm_ischemia_time_value": 0,
            },
            metadata_files_to_add=["string"],
            metadata_files_to_remove=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            organ="AO",
            organ_other="organ_other",
            protocol_url="protocol_url",
            registered_doi="registered_doi",
            rui_location={},
            sample_category="organ",
            submission_id="submission_id",
            visit="visit",
        )
        assert entity is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncEntityPythonSDK) -> None:
        response = await async_client.entities.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert entity is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncEntityPythonSDK) -> None:
        async with async_client.entities.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert entity is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update_overload_2(self, async_client: AsyncEntityPythonSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.entities.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_overload_3(self, async_client: AsyncEntityPythonSDK) -> None:
        entity = await async_client.entities.update(
            id="id",
        )
        assert entity is None

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params_overload_3(self, async_client: AsyncEntityPythonSDK) -> None:
        entity = await async_client.entities.update(
            id="id",
            antibodies=[
                {
                    "antibody_name": "antibody_name",
                    "channel_id": "channel_id",
                    "conjugated_cat_number": "conjugated_cat_number",
                    "conjugated_tag": "conjugated_tag",
                    "dilution": "dilution",
                    "lot_number": "lot_number",
                    "rr_id": "rr_id",
                    "uniprot_accession_number": "uniprot_accession_number",
                }
            ],
            calculated_metadata={},
            contacts=[
                {
                    "affiliation": "affiliation",
                    "first_name": "first_name",
                    "last_name": "last_name",
                    "middle_name_or_initial": "middle_name_or_initial",
                    "orcid_id": "orcid_id",
                }
            ],
            contains_human_genetic_sequences=True,
            creation_action="creation_action",
            creators=[
                {
                    "affiliation": "affiliation",
                    "first_name": "first_name",
                    "last_name": "last_name",
                    "middle_name_or_initial": "middle_name_or_initial",
                    "orcid_id": "orcid_id",
                }
            ],
            data_types=["AF"],
            dbgap_sra_experiment_url="dbgap_sra_experiment_url",
            dbgap_study_url="dbgap_study_url",
            description="description",
            error_message="error_message",
            files=[
                {
                    "description": "description",
                    "file_uuid": "file_uuid",
                    "filename": "filename",
                }
            ],
            group_uuid="group_uuid",
            ingest_metadata={},
            intended_dataset_type="intended_dataset_type",
            intended_organ="intended_organ",
            metadata={},
            previous_revision_uuid="previous_revision_uuid",
            previous_revision_uuids=["string"],
            registered_doi="registered_doi",
            retraction_reason="retraction_reason",
            status="New",
            sub_status="sub_status",
            thumbnail_file_to_add="thumbnail_file_to_add",
            thumbnail_file_to_remove="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            title="title",
        )
        assert entity is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_overload_3(self, async_client: AsyncEntityPythonSDK) -> None:
        response = await async_client.entities.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert entity is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_overload_3(self, async_client: AsyncEntityPythonSDK) -> None:
        async with async_client.entities.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert entity is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update_overload_3(self, async_client: AsyncEntityPythonSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.entities.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_overload_4(self, async_client: AsyncEntityPythonSDK) -> None:
        entity = await async_client.entities.update(
            id="id",
        )
        assert entity is None

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params_overload_4(self, async_client: AsyncEntityPythonSDK) -> None:
        entity = await async_client.entities.update(
            id="id",
            dataset_uuids_to_link=["string"],
            dataset_uuids_to_unlink=["string"],
            description="description",
            group_uuid="group_uuid",
            status="status",
            title="title",
            validation_message="validation_message",
        )
        assert entity is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_overload_4(self, async_client: AsyncEntityPythonSDK) -> None:
        response = await async_client.entities.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert entity is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_overload_4(self, async_client: AsyncEntityPythonSDK) -> None:
        async with async_client.entities.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert entity is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update_overload_4(self, async_client: AsyncEntityPythonSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.entities.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_overload_5(self, async_client: AsyncEntityPythonSDK) -> None:
        entity = await async_client.entities.update(
            id="id",
        )
        assert entity is None

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params_overload_5(self, async_client: AsyncEntityPythonSDK) -> None:
        entity = await async_client.entities.update(
            id="id",
            antibodies=[
                {
                    "antibody_name": "antibody_name",
                    "channel_id": "channel_id",
                    "conjugated_cat_number": "conjugated_cat_number",
                    "conjugated_tag": "conjugated_tag",
                    "dilution": "dilution",
                    "lot_number": "lot_number",
                    "rr_id": "rr_id",
                    "uniprot_accession_number": "uniprot_accession_number",
                }
            ],
            associated_collection={},
            associated_collection_uuid="associated_collection_uuid",
            calculated_metadata={},
            contacts=[
                {
                    "affiliation": "affiliation",
                    "first_name": "first_name",
                    "last_name": "last_name",
                    "middle_name_or_initial": "middle_name_or_initial",
                    "orcid_id": "orcid_id",
                }
            ],
            contains_human_genetic_sequences=True,
            creators=[
                {
                    "affiliation": "affiliation",
                    "first_name": "first_name",
                    "last_name": "last_name",
                    "middle_name_or_initial": "middle_name_or_initial",
                    "orcid_id": "orcid_id",
                }
            ],
            data_types=["AF"],
            dbgap_sra_experiment_url="dbgap_sra_experiment_url",
            dbgap_study_url="dbgap_study_url",
            description="description",
            error_message="error_message",
            files=[
                {
                    "description": "description",
                    "file_uuid": "file_uuid",
                    "filename": "filename",
                }
            ],
            group_uuid="group_uuid",
            ingest_metadata={},
            issue=0,
            metadata={},
            omap_doi="omap_doi",
            pages_or_article_num="pages_or_article_num",
            previous_revision_uuid="previous_revision_uuid",
            publication_date="publication_date",
            publication_doi="publication_doi",
            publication_url="publication_url",
            publication_venue="publication_venue",
            registered_doi="registered_doi",
            retraction_reason="retraction_reason",
            status="New",
            sub_status="sub_status",
            thumbnail_file_to_add="thumbnail_file_to_add",
            thumbnail_file_to_remove="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            title="title",
            volume=0,
        )
        assert entity is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_overload_5(self, async_client: AsyncEntityPythonSDK) -> None:
        response = await async_client.entities.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert entity is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_overload_5(self, async_client: AsyncEntityPythonSDK) -> None:
        async with async_client.entities.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert entity is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update_overload_5(self, async_client: AsyncEntityPythonSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.entities.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_overload_6(self, async_client: AsyncEntityPythonSDK) -> None:
        entity = await async_client.entities.update(
            id="id",
        )
        assert entity is None

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params_overload_6(self, async_client: AsyncEntityPythonSDK) -> None:
        entity = await async_client.entities.update(
            id="id",
            contacts=[
                {
                    "affiliation": "affiliation",
                    "first_name": "first_name",
                    "last_name": "last_name",
                    "middle_name_or_initial": "middle_name_or_initial",
                    "orcid_id": "orcid_id",
                }
            ],
            contributors=[
                {
                    "affiliation": "affiliation",
                    "first_name": "first_name",
                    "last_name": "last_name",
                    "middle_name_or_initial": "middle_name_or_initial",
                    "orcid_id": "orcid_id",
                }
            ],
            registered_doi="registered_doi",
            title="title",
        )
        assert entity is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_overload_6(self, async_client: AsyncEntityPythonSDK) -> None:
        response = await async_client.entities.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert entity is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_overload_6(self, async_client: AsyncEntityPythonSDK) -> None:
        async with async_client.entities.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert entity is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update_overload_6(self, async_client: AsyncEntityPythonSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.entities.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_overload_7(self, async_client: AsyncEntityPythonSDK) -> None:
        entity = await async_client.entities.update(
            id="id",
        )
        assert entity is None

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params_overload_7(self, async_client: AsyncEntityPythonSDK) -> None:
        entity = await async_client.entities.update(
            id="id",
            contacts=[
                {
                    "affiliation": "affiliation",
                    "first_name": "first_name",
                    "last_name": "last_name",
                    "middle_name_or_initial": "middle_name_or_initial",
                    "orcid_id": "orcid_id",
                }
            ],
            contributors=[
                {
                    "affiliation": "affiliation",
                    "first_name": "first_name",
                    "last_name": "last_name",
                    "middle_name_or_initial": "middle_name_or_initial",
                    "orcid_id": "orcid_id",
                }
            ],
            registered_doi="registered_doi",
            title="title",
        )
        assert entity is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_overload_7(self, async_client: AsyncEntityPythonSDK) -> None:
        response = await async_client.entities.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert entity is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_overload_7(self, async_client: AsyncEntityPythonSDK) -> None:
        async with async_client.entities.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert entity is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update_overload_7(self, async_client: AsyncEntityPythonSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.entities.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_multiple_samples(self, async_client: AsyncEntityPythonSDK) -> None:
        entity = await async_client.entities.create_multiple_samples(
            "count",
        )
        assert_matches_type(EntityCreateMultipleSamplesResponse, entity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_multiple_samples(self, async_client: AsyncEntityPythonSDK) -> None:
        response = await async_client.entities.with_raw_response.create_multiple_samples(
            "count",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(EntityCreateMultipleSamplesResponse, entity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_multiple_samples(self, async_client: AsyncEntityPythonSDK) -> None:
        async with async_client.entities.with_streaming_response.create_multiple_samples(
            "count",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(EntityCreateMultipleSamplesResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create_multiple_samples(self, async_client: AsyncEntityPythonSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `count` but received ''"):
            await async_client.entities.with_raw_response.create_multiple_samples(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_globus_url(self, async_client: AsyncEntityPythonSDK) -> None:
        entity = await async_client.entities.get_globus_url(
            "id",
        )
        assert_matches_type(str, entity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_globus_url(self, async_client: AsyncEntityPythonSDK) -> None:
        response = await async_client.entities.with_raw_response.get_globus_url(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(str, entity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_globus_url(self, async_client: AsyncEntityPythonSDK) -> None:
        async with async_client.entities.with_streaming_response.get_globus_url(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(str, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get_globus_url(self, async_client: AsyncEntityPythonSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.entities.with_raw_response.get_globus_url(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_is_instance_of(self, async_client: AsyncEntityPythonSDK) -> None:
        entity = await async_client.entities.is_instance_of(
            type="type",
            id="id",
        )
        assert_matches_type(Instanceof, entity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_is_instance_of(self, async_client: AsyncEntityPythonSDK) -> None:
        response = await async_client.entities.with_raw_response.is_instance_of(
            type="type",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(Instanceof, entity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_is_instance_of(self, async_client: AsyncEntityPythonSDK) -> None:
        async with async_client.entities.with_streaming_response.is_instance_of(
            type="type",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(Instanceof, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_is_instance_of(self, async_client: AsyncEntityPythonSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.entities.with_raw_response.is_instance_of(
                type="type",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `type` but received ''"):
            await async_client.entities.with_raw_response.is_instance_of(
                type="",
                id="id",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_ancestor_organs(self, async_client: AsyncEntityPythonSDK) -> None:
        entity = await async_client.entities.list_ancestor_organs(
            "id",
        )
        assert_matches_type(EntityListAncestorOrgansResponse, entity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_ancestor_organs(self, async_client: AsyncEntityPythonSDK) -> None:
        response = await async_client.entities.with_raw_response.list_ancestor_organs(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(EntityListAncestorOrgansResponse, entity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_ancestor_organs(self, async_client: AsyncEntityPythonSDK) -> None:
        async with async_client.entities.with_streaming_response.list_ancestor_organs(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(EntityListAncestorOrgansResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list_ancestor_organs(self, async_client: AsyncEntityPythonSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.entities.with_raw_response.list_ancestor_organs(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_collections(self, async_client: AsyncEntityPythonSDK) -> None:
        entity = await async_client.entities.list_collections(
            id="id",
        )
        assert_matches_type(EntityListCollectionsResponse, entity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_collections_with_all_params(self, async_client: AsyncEntityPythonSDK) -> None:
        entity = await async_client.entities.list_collections(
            id="id",
            property="uuid",
        )
        assert_matches_type(EntityListCollectionsResponse, entity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_collections(self, async_client: AsyncEntityPythonSDK) -> None:
        response = await async_client.entities.with_raw_response.list_collections(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(EntityListCollectionsResponse, entity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_collections(self, async_client: AsyncEntityPythonSDK) -> None:
        async with async_client.entities.with_streaming_response.list_collections(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(EntityListCollectionsResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list_collections(self, async_client: AsyncEntityPythonSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.entities.with_raw_response.list_collections(
                id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_entity_types(self, async_client: AsyncEntityPythonSDK) -> None:
        entity = await async_client.entities.list_entity_types()
        assert_matches_type(EntityListEntityTypesResponse, entity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_entity_types(self, async_client: AsyncEntityPythonSDK) -> None:
        response = await async_client.entities.with_raw_response.list_entity_types()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(EntityListEntityTypesResponse, entity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_entity_types(self, async_client: AsyncEntityPythonSDK) -> None:
        async with async_client.entities.with_streaming_response.list_entity_types() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(EntityListEntityTypesResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_siblings(self, async_client: AsyncEntityPythonSDK) -> None:
        entity = await async_client.entities.list_siblings(
            id="id",
        )
        assert_matches_type(EntityListSiblingsResponse, entity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_siblings_with_all_params(self, async_client: AsyncEntityPythonSDK) -> None:
        entity = await async_client.entities.list_siblings(
            id="id",
            include_old_revisions="true",
            property_key="uuid",
            status="new",
        )
        assert_matches_type(EntityListSiblingsResponse, entity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_siblings(self, async_client: AsyncEntityPythonSDK) -> None:
        response = await async_client.entities.with_raw_response.list_siblings(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(EntityListSiblingsResponse, entity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_siblings(self, async_client: AsyncEntityPythonSDK) -> None:
        async with async_client.entities.with_streaming_response.list_siblings(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(EntityListSiblingsResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list_siblings(self, async_client: AsyncEntityPythonSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.entities.with_raw_response.list_siblings(
                id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_tuplets(self, async_client: AsyncEntityPythonSDK) -> None:
        entity = await async_client.entities.list_tuplets(
            id="id",
        )
        assert_matches_type(EntityListTupletsResponse, entity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_tuplets_with_all_params(self, async_client: AsyncEntityPythonSDK) -> None:
        entity = await async_client.entities.list_tuplets(
            id="id",
            property_key="uuid",
            status="new",
        )
        assert_matches_type(EntityListTupletsResponse, entity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_tuplets(self, async_client: AsyncEntityPythonSDK) -> None:
        response = await async_client.entities.with_raw_response.list_tuplets(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(EntityListTupletsResponse, entity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_tuplets(self, async_client: AsyncEntityPythonSDK) -> None:
        async with async_client.entities.with_streaming_response.list_tuplets(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(EntityListTupletsResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list_tuplets(self, async_client: AsyncEntityPythonSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.entities.with_raw_response.list_tuplets(
                id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_uploads(self, async_client: AsyncEntityPythonSDK) -> None:
        entity = await async_client.entities.list_uploads(
            id="id",
        )
        assert_matches_type(EntityListUploadsResponse, entity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_uploads_with_all_params(self, async_client: AsyncEntityPythonSDK) -> None:
        entity = await async_client.entities.list_uploads(
            id="id",
            property="uuid",
        )
        assert_matches_type(EntityListUploadsResponse, entity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_uploads(self, async_client: AsyncEntityPythonSDK) -> None:
        response = await async_client.entities.with_raw_response.list_uploads(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(EntityListUploadsResponse, entity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_uploads(self, async_client: AsyncEntityPythonSDK) -> None:
        async with async_client.entities.with_streaming_response.list_uploads(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(EntityListUploadsResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list_uploads(self, async_client: AsyncEntityPythonSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.entities.with_raw_response.list_uploads(
                id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_provenance(self, async_client: AsyncEntityPythonSDK) -> None:
        entity = await async_client.entities.retrieve_provenance(
            "id",
        )
        assert entity is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_provenance(self, async_client: AsyncEntityPythonSDK) -> None:
        response = await async_client.entities.with_raw_response.retrieve_provenance(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert entity is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_provenance(self, async_client: AsyncEntityPythonSDK) -> None:
        async with async_client.entities.with_streaming_response.retrieve_provenance(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert entity is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve_provenance(self, async_client: AsyncEntityPythonSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.entities.with_raw_response.retrieve_provenance(
                "",
            )
