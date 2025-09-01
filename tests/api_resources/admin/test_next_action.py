# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify._utils import parse_datetime
from structify.types.admin import (
    ActionTrainingDataEntry,
    ActionTrainingDataResponse,
    DeleteActionTrainingDataResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNextAction:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_add_training_datum(self, client: Structify) -> None:
        next_action = client.admin.next_action.add_training_datum(
            input={
                "all_steps": [{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
                "descriptor": {
                    "description": "description",
                    "name": "name",
                    "relationships": [
                        {
                            "description": "description",
                            "name": "name",
                            "source_table": "source_table",
                            "target_table": "target_table",
                        }
                    ],
                    "tables": [
                        {
                            "description": "description",
                            "name": "name",
                            "properties": [
                                {
                                    "description": "description",
                                    "name": "name",
                                }
                            ],
                        }
                    ],
                },
                "extraction_criteria": [{"relationship_name": "relationship_name"}],
                "previous_actions": [
                    {
                        "selected_step": {
                            "info": {"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                            "llm_input": {
                                "decoding_params": {"parameters": [{"max_tokens": 0}]},
                                "messages": [
                                    {
                                        "content": [{"text": "Text"}],
                                        "role": "user",
                                    }
                                ],
                                "metadata": {
                                    "dataset_descriptor": {
                                        "description": "description",
                                        "name": "name",
                                        "relationships": [
                                            {
                                                "description": "description",
                                                "name": "name",
                                                "source_table": "source_table",
                                                "target_table": "target_table",
                                            }
                                        ],
                                        "tables": [
                                            {
                                                "description": "description",
                                                "name": "name",
                                                "properties": [
                                                    {
                                                        "description": "description",
                                                        "name": "name",
                                                    }
                                                ],
                                            }
                                        ],
                                    },
                                    "extracted_entities": [
                                        {
                                            "entities": [
                                                {
                                                    "id": 0,
                                                    "properties": {"foo": "string"},
                                                    "type": "type",
                                                }
                                            ]
                                        }
                                    ],
                                    "extraction_criteria": [{"relationship_name": "relationship_name"}],
                                    "formatter_specific": {"image_meta": {"image": "image"}},
                                    "tool_metadata": [
                                        {
                                            "description": "description",
                                            "name": "Exit",
                                            "regex_validator": "regex_validator",
                                        }
                                    ],
                                },
                            },
                            "llm_output": "llm_output",
                            "step_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        }
                    }
                ],
                "seeded_kg": {
                    "entities": [
                        {
                            "id": 0,
                            "properties": {"foo": "string"},
                            "type": "type",
                        }
                    ]
                },
            },
            label="label",
            output={
                "selected_step": {
                    "info": {"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    "llm_input": {
                        "decoding_params": {"parameters": [{"max_tokens": 0}]},
                        "messages": [
                            {
                                "content": [{"text": "Text"}],
                                "role": "user",
                            }
                        ],
                        "metadata": {
                            "dataset_descriptor": {
                                "description": "description",
                                "name": "name",
                                "relationships": [
                                    {
                                        "description": "description",
                                        "name": "name",
                                        "source_table": "source_table",
                                        "target_table": "target_table",
                                    }
                                ],
                                "tables": [
                                    {
                                        "description": "description",
                                        "name": "name",
                                        "properties": [
                                            {
                                                "description": "description",
                                                "name": "name",
                                            }
                                        ],
                                    }
                                ],
                            },
                            "extracted_entities": [
                                {
                                    "entities": [
                                        {
                                            "id": 0,
                                            "properties": {"foo": "string"},
                                            "type": "type",
                                        }
                                    ]
                                }
                            ],
                            "extraction_criteria": [{"relationship_name": "relationship_name"}],
                            "formatter_specific": {"image_meta": {"image": "image"}},
                            "tool_metadata": [
                                {
                                    "description": "description",
                                    "name": "Exit",
                                    "regex_validator": "regex_validator",
                                }
                            ],
                        },
                    },
                    "llm_output": "llm_output",
                    "step_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            },
        )
        assert next_action is None

    @parametrize
    def test_method_add_training_datum_with_all_params(self, client: Structify) -> None:
        next_action = client.admin.next_action.add_training_datum(
            input={
                "all_steps": [
                    {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "action_name": "action_name",
                        "metadata": {"foo": "string"},
                    }
                ],
                "descriptor": {
                    "description": "description",
                    "name": "name",
                    "relationships": [
                        {
                            "description": "description",
                            "name": "name",
                            "source_table": "source_table",
                            "target_table": "target_table",
                            "merge_strategy": {
                                "source_cardinality_given_target_match": 0,
                                "target_cardinality_given_source_match": 0,
                            },
                            "properties": [
                                {
                                    "description": "description",
                                    "name": "name",
                                    "merge_strategy": "Unique",
                                    "prop_type": "String",
                                }
                            ],
                        }
                    ],
                    "tables": [
                        {
                            "description": "description",
                            "name": "name",
                            "properties": [
                                {
                                    "description": "description",
                                    "name": "name",
                                    "merge_strategy": "Unique",
                                    "prop_type": "String",
                                }
                            ],
                            "expected_cardinality": 0,
                            "primary_column": "primary_column",
                        }
                    ],
                    "llm_override_field": "llm_override_field",
                },
                "extraction_criteria": [{"relationship_name": "relationship_name"}],
                "previous_actions": [
                    {
                        "selected_step": {
                            "info": {
                                "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                                "action_name": "action_name",
                                "metadata": {"foo": "string"},
                            },
                            "llm_input": {
                                "decoding_params": {"parameters": [{"max_tokens": 0}]},
                                "messages": [
                                    {
                                        "content": [{"text": "Text"}],
                                        "role": "user",
                                    }
                                ],
                                "metadata": {
                                    "dataset_descriptor": {
                                        "description": "description",
                                        "name": "name",
                                        "relationships": [
                                            {
                                                "description": "description",
                                                "name": "name",
                                                "source_table": "source_table",
                                                "target_table": "target_table",
                                                "merge_strategy": {
                                                    "source_cardinality_given_target_match": 0,
                                                    "target_cardinality_given_source_match": 0,
                                                },
                                                "properties": [
                                                    {
                                                        "description": "description",
                                                        "name": "name",
                                                        "merge_strategy": "Unique",
                                                        "prop_type": "String",
                                                    }
                                                ],
                                            }
                                        ],
                                        "tables": [
                                            {
                                                "description": "description",
                                                "name": "name",
                                                "properties": [
                                                    {
                                                        "description": "description",
                                                        "name": "name",
                                                        "merge_strategy": "Unique",
                                                        "prop_type": "String",
                                                    }
                                                ],
                                                "expected_cardinality": 0,
                                                "primary_column": "primary_column",
                                            }
                                        ],
                                        "llm_override_field": "llm_override_field",
                                    },
                                    "extracted_entities": [
                                        {
                                            "entities": [
                                                {
                                                    "id": 0,
                                                    "properties": {"foo": "string"},
                                                    "type": "type",
                                                }
                                            ],
                                            "relationships": [
                                                {
                                                    "source": 0,
                                                    "target": 0,
                                                    "type": "type",
                                                    "properties": {"foo": "string"},
                                                }
                                            ],
                                        }
                                    ],
                                    "extraction_criteria": [{"relationship_name": "relationship_name"}],
                                    "formatter_specific": {
                                        "image_meta": {
                                            "image": "image",
                                            "document_name": "document_name",
                                            "document_page": 0,
                                            "ocr_content": "ocr_content",
                                        }
                                    },
                                    "tool_metadata": [
                                        {
                                            "description": "description",
                                            "name": "Exit",
                                            "regex_validator": "regex_validator",
                                        }
                                    ],
                                    "qa_potentially_sus_response": "qa_potentially_sus_response",
                                },
                            },
                            "llm_output": "llm_output",
                            "step_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        }
                    }
                ],
                "seeded_kg": {
                    "entities": [
                        {
                            "id": 0,
                            "properties": {"foo": "string"},
                            "type": "type",
                        }
                    ],
                    "relationships": [
                        {
                            "source": 0,
                            "target": 0,
                            "type": "type",
                            "properties": {"foo": "string"},
                        }
                    ],
                },
            },
            label="label",
            output={
                "selected_step": {
                    "info": {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "action_name": "action_name",
                        "metadata": {"foo": "string"},
                    },
                    "llm_input": {
                        "decoding_params": {"parameters": [{"max_tokens": 0}]},
                        "messages": [
                            {
                                "content": [{"text": "Text"}],
                                "role": "user",
                            }
                        ],
                        "metadata": {
                            "dataset_descriptor": {
                                "description": "description",
                                "name": "name",
                                "relationships": [
                                    {
                                        "description": "description",
                                        "name": "name",
                                        "source_table": "source_table",
                                        "target_table": "target_table",
                                        "merge_strategy": {
                                            "source_cardinality_given_target_match": 0,
                                            "target_cardinality_given_source_match": 0,
                                        },
                                        "properties": [
                                            {
                                                "description": "description",
                                                "name": "name",
                                                "merge_strategy": "Unique",
                                                "prop_type": "String",
                                            }
                                        ],
                                    }
                                ],
                                "tables": [
                                    {
                                        "description": "description",
                                        "name": "name",
                                        "properties": [
                                            {
                                                "description": "description",
                                                "name": "name",
                                                "merge_strategy": "Unique",
                                                "prop_type": "String",
                                            }
                                        ],
                                        "expected_cardinality": 0,
                                        "primary_column": "primary_column",
                                    }
                                ],
                                "llm_override_field": "llm_override_field",
                            },
                            "extracted_entities": [
                                {
                                    "entities": [
                                        {
                                            "id": 0,
                                            "properties": {"foo": "string"},
                                            "type": "type",
                                        }
                                    ],
                                    "relationships": [
                                        {
                                            "source": 0,
                                            "target": 0,
                                            "type": "type",
                                            "properties": {"foo": "string"},
                                        }
                                    ],
                                }
                            ],
                            "extraction_criteria": [{"relationship_name": "relationship_name"}],
                            "formatter_specific": {
                                "image_meta": {
                                    "image": "image",
                                    "document_name": "document_name",
                                    "document_page": 0,
                                    "ocr_content": "ocr_content",
                                }
                            },
                            "tool_metadata": [
                                {
                                    "description": "description",
                                    "name": "Exit",
                                    "regex_validator": "regex_validator",
                                }
                            ],
                            "qa_potentially_sus_response": "qa_potentially_sus_response",
                        },
                    },
                    "llm_output": "llm_output",
                    "step_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            },
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert next_action is None

    @parametrize
    def test_raw_response_add_training_datum(self, client: Structify) -> None:
        response = client.admin.next_action.with_raw_response.add_training_datum(
            input={
                "all_steps": [{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
                "descriptor": {
                    "description": "description",
                    "name": "name",
                    "relationships": [
                        {
                            "description": "description",
                            "name": "name",
                            "source_table": "source_table",
                            "target_table": "target_table",
                        }
                    ],
                    "tables": [
                        {
                            "description": "description",
                            "name": "name",
                            "properties": [
                                {
                                    "description": "description",
                                    "name": "name",
                                }
                            ],
                        }
                    ],
                },
                "extraction_criteria": [{"relationship_name": "relationship_name"}],
                "previous_actions": [
                    {
                        "selected_step": {
                            "info": {"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                            "llm_input": {
                                "decoding_params": {"parameters": [{"max_tokens": 0}]},
                                "messages": [
                                    {
                                        "content": [{"text": "Text"}],
                                        "role": "user",
                                    }
                                ],
                                "metadata": {
                                    "dataset_descriptor": {
                                        "description": "description",
                                        "name": "name",
                                        "relationships": [
                                            {
                                                "description": "description",
                                                "name": "name",
                                                "source_table": "source_table",
                                                "target_table": "target_table",
                                            }
                                        ],
                                        "tables": [
                                            {
                                                "description": "description",
                                                "name": "name",
                                                "properties": [
                                                    {
                                                        "description": "description",
                                                        "name": "name",
                                                    }
                                                ],
                                            }
                                        ],
                                    },
                                    "extracted_entities": [
                                        {
                                            "entities": [
                                                {
                                                    "id": 0,
                                                    "properties": {"foo": "string"},
                                                    "type": "type",
                                                }
                                            ]
                                        }
                                    ],
                                    "extraction_criteria": [{"relationship_name": "relationship_name"}],
                                    "formatter_specific": {"image_meta": {"image": "image"}},
                                    "tool_metadata": [
                                        {
                                            "description": "description",
                                            "name": "Exit",
                                            "regex_validator": "regex_validator",
                                        }
                                    ],
                                },
                            },
                            "llm_output": "llm_output",
                            "step_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        }
                    }
                ],
                "seeded_kg": {
                    "entities": [
                        {
                            "id": 0,
                            "properties": {"foo": "string"},
                            "type": "type",
                        }
                    ]
                },
            },
            label="label",
            output={
                "selected_step": {
                    "info": {"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    "llm_input": {
                        "decoding_params": {"parameters": [{"max_tokens": 0}]},
                        "messages": [
                            {
                                "content": [{"text": "Text"}],
                                "role": "user",
                            }
                        ],
                        "metadata": {
                            "dataset_descriptor": {
                                "description": "description",
                                "name": "name",
                                "relationships": [
                                    {
                                        "description": "description",
                                        "name": "name",
                                        "source_table": "source_table",
                                        "target_table": "target_table",
                                    }
                                ],
                                "tables": [
                                    {
                                        "description": "description",
                                        "name": "name",
                                        "properties": [
                                            {
                                                "description": "description",
                                                "name": "name",
                                            }
                                        ],
                                    }
                                ],
                            },
                            "extracted_entities": [
                                {
                                    "entities": [
                                        {
                                            "id": 0,
                                            "properties": {"foo": "string"},
                                            "type": "type",
                                        }
                                    ]
                                }
                            ],
                            "extraction_criteria": [{"relationship_name": "relationship_name"}],
                            "formatter_specific": {"image_meta": {"image": "image"}},
                            "tool_metadata": [
                                {
                                    "description": "description",
                                    "name": "Exit",
                                    "regex_validator": "regex_validator",
                                }
                            ],
                        },
                    },
                    "llm_output": "llm_output",
                    "step_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        next_action = response.parse()
        assert next_action is None

    @parametrize
    def test_streaming_response_add_training_datum(self, client: Structify) -> None:
        with client.admin.next_action.with_streaming_response.add_training_datum(
            input={
                "all_steps": [{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
                "descriptor": {
                    "description": "description",
                    "name": "name",
                    "relationships": [
                        {
                            "description": "description",
                            "name": "name",
                            "source_table": "source_table",
                            "target_table": "target_table",
                        }
                    ],
                    "tables": [
                        {
                            "description": "description",
                            "name": "name",
                            "properties": [
                                {
                                    "description": "description",
                                    "name": "name",
                                }
                            ],
                        }
                    ],
                },
                "extraction_criteria": [{"relationship_name": "relationship_name"}],
                "previous_actions": [
                    {
                        "selected_step": {
                            "info": {"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                            "llm_input": {
                                "decoding_params": {"parameters": [{"max_tokens": 0}]},
                                "messages": [
                                    {
                                        "content": [{"text": "Text"}],
                                        "role": "user",
                                    }
                                ],
                                "metadata": {
                                    "dataset_descriptor": {
                                        "description": "description",
                                        "name": "name",
                                        "relationships": [
                                            {
                                                "description": "description",
                                                "name": "name",
                                                "source_table": "source_table",
                                                "target_table": "target_table",
                                            }
                                        ],
                                        "tables": [
                                            {
                                                "description": "description",
                                                "name": "name",
                                                "properties": [
                                                    {
                                                        "description": "description",
                                                        "name": "name",
                                                    }
                                                ],
                                            }
                                        ],
                                    },
                                    "extracted_entities": [
                                        {
                                            "entities": [
                                                {
                                                    "id": 0,
                                                    "properties": {"foo": "string"},
                                                    "type": "type",
                                                }
                                            ]
                                        }
                                    ],
                                    "extraction_criteria": [{"relationship_name": "relationship_name"}],
                                    "formatter_specific": {"image_meta": {"image": "image"}},
                                    "tool_metadata": [
                                        {
                                            "description": "description",
                                            "name": "Exit",
                                            "regex_validator": "regex_validator",
                                        }
                                    ],
                                },
                            },
                            "llm_output": "llm_output",
                            "step_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        }
                    }
                ],
                "seeded_kg": {
                    "entities": [
                        {
                            "id": 0,
                            "properties": {"foo": "string"},
                            "type": "type",
                        }
                    ]
                },
            },
            label="label",
            output={
                "selected_step": {
                    "info": {"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    "llm_input": {
                        "decoding_params": {"parameters": [{"max_tokens": 0}]},
                        "messages": [
                            {
                                "content": [{"text": "Text"}],
                                "role": "user",
                            }
                        ],
                        "metadata": {
                            "dataset_descriptor": {
                                "description": "description",
                                "name": "name",
                                "relationships": [
                                    {
                                        "description": "description",
                                        "name": "name",
                                        "source_table": "source_table",
                                        "target_table": "target_table",
                                    }
                                ],
                                "tables": [
                                    {
                                        "description": "description",
                                        "name": "name",
                                        "properties": [
                                            {
                                                "description": "description",
                                                "name": "name",
                                            }
                                        ],
                                    }
                                ],
                            },
                            "extracted_entities": [
                                {
                                    "entities": [
                                        {
                                            "id": 0,
                                            "properties": {"foo": "string"},
                                            "type": "type",
                                        }
                                    ]
                                }
                            ],
                            "extraction_criteria": [{"relationship_name": "relationship_name"}],
                            "formatter_specific": {"image_meta": {"image": "image"}},
                            "tool_metadata": [
                                {
                                    "description": "description",
                                    "name": "Exit",
                                    "regex_validator": "regex_validator",
                                }
                            ],
                        },
                    },
                    "llm_output": "llm_output",
                    "step_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            next_action = response.parse()
            assert next_action is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete_training_data(self, client: Structify) -> None:
        next_action = client.admin.next_action.delete_training_data(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DeleteActionTrainingDataResponse, next_action, path=["response"])

    @parametrize
    def test_raw_response_delete_training_data(self, client: Structify) -> None:
        response = client.admin.next_action.with_raw_response.delete_training_data(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        next_action = response.parse()
        assert_matches_type(DeleteActionTrainingDataResponse, next_action, path=["response"])

    @parametrize
    def test_streaming_response_delete_training_data(self, client: Structify) -> None:
        with client.admin.next_action.with_streaming_response.delete_training_data(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            next_action = response.parse()
            assert_matches_type(DeleteActionTrainingDataResponse, next_action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_batched_training_data(self, client: Structify) -> None:
        next_action = client.admin.next_action.get_batched_training_data(
            job_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(ActionTrainingDataResponse, next_action, path=["response"])

    @parametrize
    def test_raw_response_get_batched_training_data(self, client: Structify) -> None:
        response = client.admin.next_action.with_raw_response.get_batched_training_data(
            job_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        next_action = response.parse()
        assert_matches_type(ActionTrainingDataResponse, next_action, path=["response"])

    @parametrize
    def test_streaming_response_get_batched_training_data(self, client: Structify) -> None:
        with client.admin.next_action.with_streaming_response.get_batched_training_data(
            job_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            next_action = response.parse()
            assert_matches_type(ActionTrainingDataResponse, next_action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_training_data(self, client: Structify) -> None:
        next_action = client.admin.next_action.get_training_data()
        assert_matches_type(ActionTrainingDataResponse, next_action, path=["response"])

    @parametrize
    def test_method_get_training_data_with_all_params(self, client: Structify) -> None:
        next_action = client.admin.next_action.get_training_data(
            from_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            offset=0,
            status="HumanLLMLabel",
            to_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ActionTrainingDataResponse, next_action, path=["response"])

    @parametrize
    def test_raw_response_get_training_data(self, client: Structify) -> None:
        response = client.admin.next_action.with_raw_response.get_training_data()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        next_action = response.parse()
        assert_matches_type(ActionTrainingDataResponse, next_action, path=["response"])

    @parametrize
    def test_streaming_response_get_training_data(self, client: Structify) -> None:
        with client.admin.next_action.with_streaming_response.get_training_data() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            next_action = response.parse()
            assert_matches_type(ActionTrainingDataResponse, next_action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_training_datum(self, client: Structify) -> None:
        next_action = client.admin.next_action.get_training_datum(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ActionTrainingDataEntry, next_action, path=["response"])

    @parametrize
    def test_raw_response_get_training_datum(self, client: Structify) -> None:
        response = client.admin.next_action.with_raw_response.get_training_datum(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        next_action = response.parse()
        assert_matches_type(ActionTrainingDataEntry, next_action, path=["response"])

    @parametrize
    def test_streaming_response_get_training_datum(self, client: Structify) -> None:
        with client.admin.next_action.with_streaming_response.get_training_datum(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            next_action = response.parse()
            assert_matches_type(ActionTrainingDataEntry, next_action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_label_training_datum(self, client: Structify) -> None:
        next_action = client.admin.next_action.label_training_datum(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            label="label",
            output={
                "selected_step": {
                    "info": {"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    "llm_input": {
                        "decoding_params": {"parameters": [{"max_tokens": 0}]},
                        "messages": [
                            {
                                "content": [{"text": "Text"}],
                                "role": "user",
                            }
                        ],
                        "metadata": {
                            "dataset_descriptor": {
                                "description": "description",
                                "name": "name",
                                "relationships": [
                                    {
                                        "description": "description",
                                        "name": "name",
                                        "source_table": "source_table",
                                        "target_table": "target_table",
                                    }
                                ],
                                "tables": [
                                    {
                                        "description": "description",
                                        "name": "name",
                                        "properties": [
                                            {
                                                "description": "description",
                                                "name": "name",
                                            }
                                        ],
                                    }
                                ],
                            },
                            "extracted_entities": [
                                {
                                    "entities": [
                                        {
                                            "id": 0,
                                            "properties": {"foo": "string"},
                                            "type": "type",
                                        }
                                    ]
                                }
                            ],
                            "extraction_criteria": [{"relationship_name": "relationship_name"}],
                            "formatter_specific": {"image_meta": {"image": "image"}},
                            "tool_metadata": [
                                {
                                    "description": "description",
                                    "name": "Exit",
                                    "regex_validator": "regex_validator",
                                }
                            ],
                        },
                    },
                    "llm_output": "llm_output",
                    "step_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            },
        )
        assert next_action is None

    @parametrize
    def test_raw_response_label_training_datum(self, client: Structify) -> None:
        response = client.admin.next_action.with_raw_response.label_training_datum(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            label="label",
            output={
                "selected_step": {
                    "info": {"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    "llm_input": {
                        "decoding_params": {"parameters": [{"max_tokens": 0}]},
                        "messages": [
                            {
                                "content": [{"text": "Text"}],
                                "role": "user",
                            }
                        ],
                        "metadata": {
                            "dataset_descriptor": {
                                "description": "description",
                                "name": "name",
                                "relationships": [
                                    {
                                        "description": "description",
                                        "name": "name",
                                        "source_table": "source_table",
                                        "target_table": "target_table",
                                    }
                                ],
                                "tables": [
                                    {
                                        "description": "description",
                                        "name": "name",
                                        "properties": [
                                            {
                                                "description": "description",
                                                "name": "name",
                                            }
                                        ],
                                    }
                                ],
                            },
                            "extracted_entities": [
                                {
                                    "entities": [
                                        {
                                            "id": 0,
                                            "properties": {"foo": "string"},
                                            "type": "type",
                                        }
                                    ]
                                }
                            ],
                            "extraction_criteria": [{"relationship_name": "relationship_name"}],
                            "formatter_specific": {"image_meta": {"image": "image"}},
                            "tool_metadata": [
                                {
                                    "description": "description",
                                    "name": "Exit",
                                    "regex_validator": "regex_validator",
                                }
                            ],
                        },
                    },
                    "llm_output": "llm_output",
                    "step_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        next_action = response.parse()
        assert next_action is None

    @parametrize
    def test_streaming_response_label_training_datum(self, client: Structify) -> None:
        with client.admin.next_action.with_streaming_response.label_training_datum(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            label="label",
            output={
                "selected_step": {
                    "info": {"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    "llm_input": {
                        "decoding_params": {"parameters": [{"max_tokens": 0}]},
                        "messages": [
                            {
                                "content": [{"text": "Text"}],
                                "role": "user",
                            }
                        ],
                        "metadata": {
                            "dataset_descriptor": {
                                "description": "description",
                                "name": "name",
                                "relationships": [
                                    {
                                        "description": "description",
                                        "name": "name",
                                        "source_table": "source_table",
                                        "target_table": "target_table",
                                    }
                                ],
                                "tables": [
                                    {
                                        "description": "description",
                                        "name": "name",
                                        "properties": [
                                            {
                                                "description": "description",
                                                "name": "name",
                                            }
                                        ],
                                    }
                                ],
                            },
                            "extracted_entities": [
                                {
                                    "entities": [
                                        {
                                            "id": 0,
                                            "properties": {"foo": "string"},
                                            "type": "type",
                                        }
                                    ]
                                }
                            ],
                            "extraction_criteria": [{"relationship_name": "relationship_name"}],
                            "formatter_specific": {"image_meta": {"image": "image"}},
                            "tool_metadata": [
                                {
                                    "description": "description",
                                    "name": "Exit",
                                    "regex_validator": "regex_validator",
                                }
                            ],
                        },
                    },
                    "llm_output": "llm_output",
                    "step_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            next_action = response.parse()
            assert next_action is None

        assert cast(Any, response.is_closed) is True


class TestAsyncNextAction:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_add_training_datum(self, async_client: AsyncStructify) -> None:
        next_action = await async_client.admin.next_action.add_training_datum(
            input={
                "all_steps": [{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
                "descriptor": {
                    "description": "description",
                    "name": "name",
                    "relationships": [
                        {
                            "description": "description",
                            "name": "name",
                            "source_table": "source_table",
                            "target_table": "target_table",
                        }
                    ],
                    "tables": [
                        {
                            "description": "description",
                            "name": "name",
                            "properties": [
                                {
                                    "description": "description",
                                    "name": "name",
                                }
                            ],
                        }
                    ],
                },
                "extraction_criteria": [{"relationship_name": "relationship_name"}],
                "previous_actions": [
                    {
                        "selected_step": {
                            "info": {"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                            "llm_input": {
                                "decoding_params": {"parameters": [{"max_tokens": 0}]},
                                "messages": [
                                    {
                                        "content": [{"text": "Text"}],
                                        "role": "user",
                                    }
                                ],
                                "metadata": {
                                    "dataset_descriptor": {
                                        "description": "description",
                                        "name": "name",
                                        "relationships": [
                                            {
                                                "description": "description",
                                                "name": "name",
                                                "source_table": "source_table",
                                                "target_table": "target_table",
                                            }
                                        ],
                                        "tables": [
                                            {
                                                "description": "description",
                                                "name": "name",
                                                "properties": [
                                                    {
                                                        "description": "description",
                                                        "name": "name",
                                                    }
                                                ],
                                            }
                                        ],
                                    },
                                    "extracted_entities": [
                                        {
                                            "entities": [
                                                {
                                                    "id": 0,
                                                    "properties": {"foo": "string"},
                                                    "type": "type",
                                                }
                                            ]
                                        }
                                    ],
                                    "extraction_criteria": [{"relationship_name": "relationship_name"}],
                                    "formatter_specific": {"image_meta": {"image": "image"}},
                                    "tool_metadata": [
                                        {
                                            "description": "description",
                                            "name": "Exit",
                                            "regex_validator": "regex_validator",
                                        }
                                    ],
                                },
                            },
                            "llm_output": "llm_output",
                            "step_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        }
                    }
                ],
                "seeded_kg": {
                    "entities": [
                        {
                            "id": 0,
                            "properties": {"foo": "string"},
                            "type": "type",
                        }
                    ]
                },
            },
            label="label",
            output={
                "selected_step": {
                    "info": {"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    "llm_input": {
                        "decoding_params": {"parameters": [{"max_tokens": 0}]},
                        "messages": [
                            {
                                "content": [{"text": "Text"}],
                                "role": "user",
                            }
                        ],
                        "metadata": {
                            "dataset_descriptor": {
                                "description": "description",
                                "name": "name",
                                "relationships": [
                                    {
                                        "description": "description",
                                        "name": "name",
                                        "source_table": "source_table",
                                        "target_table": "target_table",
                                    }
                                ],
                                "tables": [
                                    {
                                        "description": "description",
                                        "name": "name",
                                        "properties": [
                                            {
                                                "description": "description",
                                                "name": "name",
                                            }
                                        ],
                                    }
                                ],
                            },
                            "extracted_entities": [
                                {
                                    "entities": [
                                        {
                                            "id": 0,
                                            "properties": {"foo": "string"},
                                            "type": "type",
                                        }
                                    ]
                                }
                            ],
                            "extraction_criteria": [{"relationship_name": "relationship_name"}],
                            "formatter_specific": {"image_meta": {"image": "image"}},
                            "tool_metadata": [
                                {
                                    "description": "description",
                                    "name": "Exit",
                                    "regex_validator": "regex_validator",
                                }
                            ],
                        },
                    },
                    "llm_output": "llm_output",
                    "step_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            },
        )
        assert next_action is None

    @parametrize
    async def test_method_add_training_datum_with_all_params(self, async_client: AsyncStructify) -> None:
        next_action = await async_client.admin.next_action.add_training_datum(
            input={
                "all_steps": [
                    {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "action_name": "action_name",
                        "metadata": {"foo": "string"},
                    }
                ],
                "descriptor": {
                    "description": "description",
                    "name": "name",
                    "relationships": [
                        {
                            "description": "description",
                            "name": "name",
                            "source_table": "source_table",
                            "target_table": "target_table",
                            "merge_strategy": {
                                "source_cardinality_given_target_match": 0,
                                "target_cardinality_given_source_match": 0,
                            },
                            "properties": [
                                {
                                    "description": "description",
                                    "name": "name",
                                    "merge_strategy": "Unique",
                                    "prop_type": "String",
                                }
                            ],
                        }
                    ],
                    "tables": [
                        {
                            "description": "description",
                            "name": "name",
                            "properties": [
                                {
                                    "description": "description",
                                    "name": "name",
                                    "merge_strategy": "Unique",
                                    "prop_type": "String",
                                }
                            ],
                            "expected_cardinality": 0,
                            "primary_column": "primary_column",
                        }
                    ],
                    "llm_override_field": "llm_override_field",
                },
                "extraction_criteria": [{"relationship_name": "relationship_name"}],
                "previous_actions": [
                    {
                        "selected_step": {
                            "info": {
                                "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                                "action_name": "action_name",
                                "metadata": {"foo": "string"},
                            },
                            "llm_input": {
                                "decoding_params": {"parameters": [{"max_tokens": 0}]},
                                "messages": [
                                    {
                                        "content": [{"text": "Text"}],
                                        "role": "user",
                                    }
                                ],
                                "metadata": {
                                    "dataset_descriptor": {
                                        "description": "description",
                                        "name": "name",
                                        "relationships": [
                                            {
                                                "description": "description",
                                                "name": "name",
                                                "source_table": "source_table",
                                                "target_table": "target_table",
                                                "merge_strategy": {
                                                    "source_cardinality_given_target_match": 0,
                                                    "target_cardinality_given_source_match": 0,
                                                },
                                                "properties": [
                                                    {
                                                        "description": "description",
                                                        "name": "name",
                                                        "merge_strategy": "Unique",
                                                        "prop_type": "String",
                                                    }
                                                ],
                                            }
                                        ],
                                        "tables": [
                                            {
                                                "description": "description",
                                                "name": "name",
                                                "properties": [
                                                    {
                                                        "description": "description",
                                                        "name": "name",
                                                        "merge_strategy": "Unique",
                                                        "prop_type": "String",
                                                    }
                                                ],
                                                "expected_cardinality": 0,
                                                "primary_column": "primary_column",
                                            }
                                        ],
                                        "llm_override_field": "llm_override_field",
                                    },
                                    "extracted_entities": [
                                        {
                                            "entities": [
                                                {
                                                    "id": 0,
                                                    "properties": {"foo": "string"},
                                                    "type": "type",
                                                }
                                            ],
                                            "relationships": [
                                                {
                                                    "source": 0,
                                                    "target": 0,
                                                    "type": "type",
                                                    "properties": {"foo": "string"},
                                                }
                                            ],
                                        }
                                    ],
                                    "extraction_criteria": [{"relationship_name": "relationship_name"}],
                                    "formatter_specific": {
                                        "image_meta": {
                                            "image": "image",
                                            "document_name": "document_name",
                                            "document_page": 0,
                                            "ocr_content": "ocr_content",
                                        }
                                    },
                                    "tool_metadata": [
                                        {
                                            "description": "description",
                                            "name": "Exit",
                                            "regex_validator": "regex_validator",
                                        }
                                    ],
                                    "qa_potentially_sus_response": "qa_potentially_sus_response",
                                },
                            },
                            "llm_output": "llm_output",
                            "step_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        }
                    }
                ],
                "seeded_kg": {
                    "entities": [
                        {
                            "id": 0,
                            "properties": {"foo": "string"},
                            "type": "type",
                        }
                    ],
                    "relationships": [
                        {
                            "source": 0,
                            "target": 0,
                            "type": "type",
                            "properties": {"foo": "string"},
                        }
                    ],
                },
            },
            label="label",
            output={
                "selected_step": {
                    "info": {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "action_name": "action_name",
                        "metadata": {"foo": "string"},
                    },
                    "llm_input": {
                        "decoding_params": {"parameters": [{"max_tokens": 0}]},
                        "messages": [
                            {
                                "content": [{"text": "Text"}],
                                "role": "user",
                            }
                        ],
                        "metadata": {
                            "dataset_descriptor": {
                                "description": "description",
                                "name": "name",
                                "relationships": [
                                    {
                                        "description": "description",
                                        "name": "name",
                                        "source_table": "source_table",
                                        "target_table": "target_table",
                                        "merge_strategy": {
                                            "source_cardinality_given_target_match": 0,
                                            "target_cardinality_given_source_match": 0,
                                        },
                                        "properties": [
                                            {
                                                "description": "description",
                                                "name": "name",
                                                "merge_strategy": "Unique",
                                                "prop_type": "String",
                                            }
                                        ],
                                    }
                                ],
                                "tables": [
                                    {
                                        "description": "description",
                                        "name": "name",
                                        "properties": [
                                            {
                                                "description": "description",
                                                "name": "name",
                                                "merge_strategy": "Unique",
                                                "prop_type": "String",
                                            }
                                        ],
                                        "expected_cardinality": 0,
                                        "primary_column": "primary_column",
                                    }
                                ],
                                "llm_override_field": "llm_override_field",
                            },
                            "extracted_entities": [
                                {
                                    "entities": [
                                        {
                                            "id": 0,
                                            "properties": {"foo": "string"},
                                            "type": "type",
                                        }
                                    ],
                                    "relationships": [
                                        {
                                            "source": 0,
                                            "target": 0,
                                            "type": "type",
                                            "properties": {"foo": "string"},
                                        }
                                    ],
                                }
                            ],
                            "extraction_criteria": [{"relationship_name": "relationship_name"}],
                            "formatter_specific": {
                                "image_meta": {
                                    "image": "image",
                                    "document_name": "document_name",
                                    "document_page": 0,
                                    "ocr_content": "ocr_content",
                                }
                            },
                            "tool_metadata": [
                                {
                                    "description": "description",
                                    "name": "Exit",
                                    "regex_validator": "regex_validator",
                                }
                            ],
                            "qa_potentially_sus_response": "qa_potentially_sus_response",
                        },
                    },
                    "llm_output": "llm_output",
                    "step_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            },
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert next_action is None

    @parametrize
    async def test_raw_response_add_training_datum(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.next_action.with_raw_response.add_training_datum(
            input={
                "all_steps": [{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
                "descriptor": {
                    "description": "description",
                    "name": "name",
                    "relationships": [
                        {
                            "description": "description",
                            "name": "name",
                            "source_table": "source_table",
                            "target_table": "target_table",
                        }
                    ],
                    "tables": [
                        {
                            "description": "description",
                            "name": "name",
                            "properties": [
                                {
                                    "description": "description",
                                    "name": "name",
                                }
                            ],
                        }
                    ],
                },
                "extraction_criteria": [{"relationship_name": "relationship_name"}],
                "previous_actions": [
                    {
                        "selected_step": {
                            "info": {"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                            "llm_input": {
                                "decoding_params": {"parameters": [{"max_tokens": 0}]},
                                "messages": [
                                    {
                                        "content": [{"text": "Text"}],
                                        "role": "user",
                                    }
                                ],
                                "metadata": {
                                    "dataset_descriptor": {
                                        "description": "description",
                                        "name": "name",
                                        "relationships": [
                                            {
                                                "description": "description",
                                                "name": "name",
                                                "source_table": "source_table",
                                                "target_table": "target_table",
                                            }
                                        ],
                                        "tables": [
                                            {
                                                "description": "description",
                                                "name": "name",
                                                "properties": [
                                                    {
                                                        "description": "description",
                                                        "name": "name",
                                                    }
                                                ],
                                            }
                                        ],
                                    },
                                    "extracted_entities": [
                                        {
                                            "entities": [
                                                {
                                                    "id": 0,
                                                    "properties": {"foo": "string"},
                                                    "type": "type",
                                                }
                                            ]
                                        }
                                    ],
                                    "extraction_criteria": [{"relationship_name": "relationship_name"}],
                                    "formatter_specific": {"image_meta": {"image": "image"}},
                                    "tool_metadata": [
                                        {
                                            "description": "description",
                                            "name": "Exit",
                                            "regex_validator": "regex_validator",
                                        }
                                    ],
                                },
                            },
                            "llm_output": "llm_output",
                            "step_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        }
                    }
                ],
                "seeded_kg": {
                    "entities": [
                        {
                            "id": 0,
                            "properties": {"foo": "string"},
                            "type": "type",
                        }
                    ]
                },
            },
            label="label",
            output={
                "selected_step": {
                    "info": {"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    "llm_input": {
                        "decoding_params": {"parameters": [{"max_tokens": 0}]},
                        "messages": [
                            {
                                "content": [{"text": "Text"}],
                                "role": "user",
                            }
                        ],
                        "metadata": {
                            "dataset_descriptor": {
                                "description": "description",
                                "name": "name",
                                "relationships": [
                                    {
                                        "description": "description",
                                        "name": "name",
                                        "source_table": "source_table",
                                        "target_table": "target_table",
                                    }
                                ],
                                "tables": [
                                    {
                                        "description": "description",
                                        "name": "name",
                                        "properties": [
                                            {
                                                "description": "description",
                                                "name": "name",
                                            }
                                        ],
                                    }
                                ],
                            },
                            "extracted_entities": [
                                {
                                    "entities": [
                                        {
                                            "id": 0,
                                            "properties": {"foo": "string"},
                                            "type": "type",
                                        }
                                    ]
                                }
                            ],
                            "extraction_criteria": [{"relationship_name": "relationship_name"}],
                            "formatter_specific": {"image_meta": {"image": "image"}},
                            "tool_metadata": [
                                {
                                    "description": "description",
                                    "name": "Exit",
                                    "regex_validator": "regex_validator",
                                }
                            ],
                        },
                    },
                    "llm_output": "llm_output",
                    "step_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        next_action = await response.parse()
        assert next_action is None

    @parametrize
    async def test_streaming_response_add_training_datum(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.next_action.with_streaming_response.add_training_datum(
            input={
                "all_steps": [{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
                "descriptor": {
                    "description": "description",
                    "name": "name",
                    "relationships": [
                        {
                            "description": "description",
                            "name": "name",
                            "source_table": "source_table",
                            "target_table": "target_table",
                        }
                    ],
                    "tables": [
                        {
                            "description": "description",
                            "name": "name",
                            "properties": [
                                {
                                    "description": "description",
                                    "name": "name",
                                }
                            ],
                        }
                    ],
                },
                "extraction_criteria": [{"relationship_name": "relationship_name"}],
                "previous_actions": [
                    {
                        "selected_step": {
                            "info": {"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                            "llm_input": {
                                "decoding_params": {"parameters": [{"max_tokens": 0}]},
                                "messages": [
                                    {
                                        "content": [{"text": "Text"}],
                                        "role": "user",
                                    }
                                ],
                                "metadata": {
                                    "dataset_descriptor": {
                                        "description": "description",
                                        "name": "name",
                                        "relationships": [
                                            {
                                                "description": "description",
                                                "name": "name",
                                                "source_table": "source_table",
                                                "target_table": "target_table",
                                            }
                                        ],
                                        "tables": [
                                            {
                                                "description": "description",
                                                "name": "name",
                                                "properties": [
                                                    {
                                                        "description": "description",
                                                        "name": "name",
                                                    }
                                                ],
                                            }
                                        ],
                                    },
                                    "extracted_entities": [
                                        {
                                            "entities": [
                                                {
                                                    "id": 0,
                                                    "properties": {"foo": "string"},
                                                    "type": "type",
                                                }
                                            ]
                                        }
                                    ],
                                    "extraction_criteria": [{"relationship_name": "relationship_name"}],
                                    "formatter_specific": {"image_meta": {"image": "image"}},
                                    "tool_metadata": [
                                        {
                                            "description": "description",
                                            "name": "Exit",
                                            "regex_validator": "regex_validator",
                                        }
                                    ],
                                },
                            },
                            "llm_output": "llm_output",
                            "step_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        }
                    }
                ],
                "seeded_kg": {
                    "entities": [
                        {
                            "id": 0,
                            "properties": {"foo": "string"},
                            "type": "type",
                        }
                    ]
                },
            },
            label="label",
            output={
                "selected_step": {
                    "info": {"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    "llm_input": {
                        "decoding_params": {"parameters": [{"max_tokens": 0}]},
                        "messages": [
                            {
                                "content": [{"text": "Text"}],
                                "role": "user",
                            }
                        ],
                        "metadata": {
                            "dataset_descriptor": {
                                "description": "description",
                                "name": "name",
                                "relationships": [
                                    {
                                        "description": "description",
                                        "name": "name",
                                        "source_table": "source_table",
                                        "target_table": "target_table",
                                    }
                                ],
                                "tables": [
                                    {
                                        "description": "description",
                                        "name": "name",
                                        "properties": [
                                            {
                                                "description": "description",
                                                "name": "name",
                                            }
                                        ],
                                    }
                                ],
                            },
                            "extracted_entities": [
                                {
                                    "entities": [
                                        {
                                            "id": 0,
                                            "properties": {"foo": "string"},
                                            "type": "type",
                                        }
                                    ]
                                }
                            ],
                            "extraction_criteria": [{"relationship_name": "relationship_name"}],
                            "formatter_specific": {"image_meta": {"image": "image"}},
                            "tool_metadata": [
                                {
                                    "description": "description",
                                    "name": "Exit",
                                    "regex_validator": "regex_validator",
                                }
                            ],
                        },
                    },
                    "llm_output": "llm_output",
                    "step_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            next_action = await response.parse()
            assert next_action is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete_training_data(self, async_client: AsyncStructify) -> None:
        next_action = await async_client.admin.next_action.delete_training_data(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DeleteActionTrainingDataResponse, next_action, path=["response"])

    @parametrize
    async def test_raw_response_delete_training_data(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.next_action.with_raw_response.delete_training_data(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        next_action = await response.parse()
        assert_matches_type(DeleteActionTrainingDataResponse, next_action, path=["response"])

    @parametrize
    async def test_streaming_response_delete_training_data(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.next_action.with_streaming_response.delete_training_data(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            next_action = await response.parse()
            assert_matches_type(DeleteActionTrainingDataResponse, next_action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_batched_training_data(self, async_client: AsyncStructify) -> None:
        next_action = await async_client.admin.next_action.get_batched_training_data(
            job_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(ActionTrainingDataResponse, next_action, path=["response"])

    @parametrize
    async def test_raw_response_get_batched_training_data(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.next_action.with_raw_response.get_batched_training_data(
            job_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        next_action = await response.parse()
        assert_matches_type(ActionTrainingDataResponse, next_action, path=["response"])

    @parametrize
    async def test_streaming_response_get_batched_training_data(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.next_action.with_streaming_response.get_batched_training_data(
            job_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            next_action = await response.parse()
            assert_matches_type(ActionTrainingDataResponse, next_action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_training_data(self, async_client: AsyncStructify) -> None:
        next_action = await async_client.admin.next_action.get_training_data()
        assert_matches_type(ActionTrainingDataResponse, next_action, path=["response"])

    @parametrize
    async def test_method_get_training_data_with_all_params(self, async_client: AsyncStructify) -> None:
        next_action = await async_client.admin.next_action.get_training_data(
            from_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            offset=0,
            status="HumanLLMLabel",
            to_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ActionTrainingDataResponse, next_action, path=["response"])

    @parametrize
    async def test_raw_response_get_training_data(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.next_action.with_raw_response.get_training_data()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        next_action = await response.parse()
        assert_matches_type(ActionTrainingDataResponse, next_action, path=["response"])

    @parametrize
    async def test_streaming_response_get_training_data(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.next_action.with_streaming_response.get_training_data() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            next_action = await response.parse()
            assert_matches_type(ActionTrainingDataResponse, next_action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_training_datum(self, async_client: AsyncStructify) -> None:
        next_action = await async_client.admin.next_action.get_training_datum(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ActionTrainingDataEntry, next_action, path=["response"])

    @parametrize
    async def test_raw_response_get_training_datum(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.next_action.with_raw_response.get_training_datum(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        next_action = await response.parse()
        assert_matches_type(ActionTrainingDataEntry, next_action, path=["response"])

    @parametrize
    async def test_streaming_response_get_training_datum(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.next_action.with_streaming_response.get_training_datum(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            next_action = await response.parse()
            assert_matches_type(ActionTrainingDataEntry, next_action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_label_training_datum(self, async_client: AsyncStructify) -> None:
        next_action = await async_client.admin.next_action.label_training_datum(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            label="label",
            output={
                "selected_step": {
                    "info": {"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    "llm_input": {
                        "decoding_params": {"parameters": [{"max_tokens": 0}]},
                        "messages": [
                            {
                                "content": [{"text": "Text"}],
                                "role": "user",
                            }
                        ],
                        "metadata": {
                            "dataset_descriptor": {
                                "description": "description",
                                "name": "name",
                                "relationships": [
                                    {
                                        "description": "description",
                                        "name": "name",
                                        "source_table": "source_table",
                                        "target_table": "target_table",
                                    }
                                ],
                                "tables": [
                                    {
                                        "description": "description",
                                        "name": "name",
                                        "properties": [
                                            {
                                                "description": "description",
                                                "name": "name",
                                            }
                                        ],
                                    }
                                ],
                            },
                            "extracted_entities": [
                                {
                                    "entities": [
                                        {
                                            "id": 0,
                                            "properties": {"foo": "string"},
                                            "type": "type",
                                        }
                                    ]
                                }
                            ],
                            "extraction_criteria": [{"relationship_name": "relationship_name"}],
                            "formatter_specific": {"image_meta": {"image": "image"}},
                            "tool_metadata": [
                                {
                                    "description": "description",
                                    "name": "Exit",
                                    "regex_validator": "regex_validator",
                                }
                            ],
                        },
                    },
                    "llm_output": "llm_output",
                    "step_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            },
        )
        assert next_action is None

    @parametrize
    async def test_raw_response_label_training_datum(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.next_action.with_raw_response.label_training_datum(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            label="label",
            output={
                "selected_step": {
                    "info": {"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    "llm_input": {
                        "decoding_params": {"parameters": [{"max_tokens": 0}]},
                        "messages": [
                            {
                                "content": [{"text": "Text"}],
                                "role": "user",
                            }
                        ],
                        "metadata": {
                            "dataset_descriptor": {
                                "description": "description",
                                "name": "name",
                                "relationships": [
                                    {
                                        "description": "description",
                                        "name": "name",
                                        "source_table": "source_table",
                                        "target_table": "target_table",
                                    }
                                ],
                                "tables": [
                                    {
                                        "description": "description",
                                        "name": "name",
                                        "properties": [
                                            {
                                                "description": "description",
                                                "name": "name",
                                            }
                                        ],
                                    }
                                ],
                            },
                            "extracted_entities": [
                                {
                                    "entities": [
                                        {
                                            "id": 0,
                                            "properties": {"foo": "string"},
                                            "type": "type",
                                        }
                                    ]
                                }
                            ],
                            "extraction_criteria": [{"relationship_name": "relationship_name"}],
                            "formatter_specific": {"image_meta": {"image": "image"}},
                            "tool_metadata": [
                                {
                                    "description": "description",
                                    "name": "Exit",
                                    "regex_validator": "regex_validator",
                                }
                            ],
                        },
                    },
                    "llm_output": "llm_output",
                    "step_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        next_action = await response.parse()
        assert next_action is None

    @parametrize
    async def test_streaming_response_label_training_datum(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.next_action.with_streaming_response.label_training_datum(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            label="label",
            output={
                "selected_step": {
                    "info": {"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    "llm_input": {
                        "decoding_params": {"parameters": [{"max_tokens": 0}]},
                        "messages": [
                            {
                                "content": [{"text": "Text"}],
                                "role": "user",
                            }
                        ],
                        "metadata": {
                            "dataset_descriptor": {
                                "description": "description",
                                "name": "name",
                                "relationships": [
                                    {
                                        "description": "description",
                                        "name": "name",
                                        "source_table": "source_table",
                                        "target_table": "target_table",
                                    }
                                ],
                                "tables": [
                                    {
                                        "description": "description",
                                        "name": "name",
                                        "properties": [
                                            {
                                                "description": "description",
                                                "name": "name",
                                            }
                                        ],
                                    }
                                ],
                            },
                            "extracted_entities": [
                                {
                                    "entities": [
                                        {
                                            "id": 0,
                                            "properties": {"foo": "string"},
                                            "type": "type",
                                        }
                                    ]
                                }
                            ],
                            "extraction_criteria": [{"relationship_name": "relationship_name"}],
                            "formatter_specific": {"image_meta": {"image": "image"}},
                            "tool_metadata": [
                                {
                                    "description": "description",
                                    "name": "Exit",
                                    "regex_validator": "regex_validator",
                                }
                            ],
                        },
                    },
                    "llm_output": "llm_output",
                    "step_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            next_action = await response.parse()
            assert next_action is None

        assert cast(Any, response.is_closed) is True
