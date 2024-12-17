# coding: utf-8

"""
    Firefly III API Client

    This is the Python client for Firefly III API

    The version of the OpenAPI document: 6.1.24
    Contact: james@firefly-iii.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class WebhookAttempt(BaseModel):
    """
    WebhookAttempt
    """ # noqa: E501
    created_at: Optional[datetime] = None
    logs: Optional[StrictStr] = Field(default=None, description="Internal log for this attempt. May contain sensitive user data.")
    response: Optional[StrictStr] = Field(default=None, description="Webhook receiver response for this attempt, if any. May contain sensitive user data.")
    status_code: Optional[StrictInt] = Field(default=None, description="The HTTP status code of the error, if any.")
    updated_at: Optional[datetime] = None
    webhook_message_id: Optional[StrictStr] = Field(default=None, description="The ID of the webhook message this attempt belongs to.")
    __properties: ClassVar[List[str]] = ["created_at", "logs", "response", "status_code", "updated_at", "webhook_message_id"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of WebhookAttempt from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "created_at",
            "updated_at",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if logs (nullable) is None
        # and model_fields_set contains the field
        if self.logs is None and "logs" in self.model_fields_set:
            _dict['logs'] = None

        # set to None if response (nullable) is None
        # and model_fields_set contains the field
        if self.response is None and "response" in self.model_fields_set:
            _dict['response'] = None

        # set to None if status_code (nullable) is None
        # and model_fields_set contains the field
        if self.status_code is None and "status_code" in self.model_fields_set:
            _dict['status_code'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WebhookAttempt from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created_at": obj.get("created_at"),
            "logs": obj.get("logs"),
            "response": obj.get("response"),
            "status_code": obj.get("status_code"),
            "updated_at": obj.get("updated_at"),
            "webhook_message_id": obj.get("webhook_message_id")
        })
        return _obj


