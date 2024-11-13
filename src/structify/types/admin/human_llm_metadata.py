# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ..._models import BaseModel

__all__ = ["HumanLlmMetadata"]


class HumanLlmMetadata(BaseModel):
    dataset_name: str

    entity_name: str

    property_name: str

    user_email: str
