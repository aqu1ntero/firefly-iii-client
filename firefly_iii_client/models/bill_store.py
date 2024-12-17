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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from firefly_iii_client.models.bill_repeat_frequency import BillRepeatFrequency
from typing import Optional, Set
from typing_extensions import Self

class BillStore(BaseModel):
    """
    BillStore
    """ # noqa: E501
    active: Optional[StrictBool] = Field(default=None, description="If the bill is active.")
    amount_max: StrictStr
    amount_min: StrictStr
    currency_code: Optional[StrictStr] = Field(default=None, description="Use either currency_id or currency_code")
    currency_id: Optional[StrictStr] = Field(default=None, description="Use either currency_id or currency_code")
    var_date: datetime = Field(alias="date")
    end_date: Optional[datetime] = Field(default=None, description="The date after which this bill is no longer valid or applicable")
    extension_date: Optional[datetime] = Field(default=None, description="The date before which the bill must be renewed (or cancelled)")
    name: StrictStr
    notes: Optional[StrictStr] = None
    object_group_id: Optional[StrictStr] = Field(default=None, description="The group ID of the group this object is part of. NULL if no group.")
    object_group_title: Optional[StrictStr] = Field(default=None, description="The name of the group. NULL if no group.")
    repeat_freq: BillRepeatFrequency
    skip: Optional[StrictInt] = Field(default=None, description="How often the bill must be skipped. 1 means a bi-monthly bill.")
    __properties: ClassVar[List[str]] = ["active", "amount_max", "amount_min", "currency_code", "currency_id", "date", "end_date", "extension_date", "name", "notes", "object_group_id", "object_group_title", "repeat_freq", "skip"]

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
        """Create an instance of BillStore from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if notes (nullable) is None
        # and model_fields_set contains the field
        if self.notes is None and "notes" in self.model_fields_set:
            _dict['notes'] = None

        # set to None if object_group_id (nullable) is None
        # and model_fields_set contains the field
        if self.object_group_id is None and "object_group_id" in self.model_fields_set:
            _dict['object_group_id'] = None

        # set to None if object_group_title (nullable) is None
        # and model_fields_set contains the field
        if self.object_group_title is None and "object_group_title" in self.model_fields_set:
            _dict['object_group_title'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BillStore from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "active": obj.get("active"),
            "amount_max": obj.get("amount_max"),
            "amount_min": obj.get("amount_min"),
            "currency_code": obj.get("currency_code"),
            "currency_id": obj.get("currency_id"),
            "date": obj.get("date"),
            "end_date": obj.get("end_date"),
            "extension_date": obj.get("extension_date"),
            "name": obj.get("name"),
            "notes": obj.get("notes"),
            "object_group_id": obj.get("object_group_id"),
            "object_group_title": obj.get("object_group_title"),
            "repeat_freq": obj.get("repeat_freq"),
            "skip": obj.get("skip")
        })
        return _obj


