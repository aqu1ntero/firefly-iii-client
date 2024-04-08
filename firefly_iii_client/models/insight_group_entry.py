# coding: utf-8

"""
    Firefly III API Client

    This is the Python client for Firefly III API

    The version of the OpenAPI document: 2.0.12
    Contact: james@firefly-iii.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class InsightGroupEntry(BaseModel):
    """
    InsightGroupEntry
    """ # noqa: E501
    currency_code: Optional[StrictStr] = Field(default=None, description="The currency code of the expenses listed for this account.")
    currency_id: Optional[StrictStr] = Field(default=None, description="The currency ID of the expenses listed for this account.")
    difference: Optional[StrictStr] = Field(default=None, description="The amount spent or earned between start date and end date, a number defined as a string, for this object and all asset accounts.")
    difference_float: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The amount spent or earned between start date and end date, a number as a float, for this object and all asset accounts. May have rounding errors.")
    id: Optional[StrictStr] = Field(default=None, description="This ID is a reference to the original object.")
    name: Optional[StrictStr] = Field(default=None, description="This is the name of the object.")
    __properties: ClassVar[List[str]] = ["currency_code", "currency_id", "difference", "difference_float", "id", "name"]

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
        """Create an instance of InsightGroupEntry from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InsightGroupEntry from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "currency_code": obj.get("currency_code"),
            "currency_id": obj.get("currency_id"),
            "difference": obj.get("difference"),
            "difference_float": obj.get("difference_float"),
            "id": obj.get("id"),
            "name": obj.get("name")
        })
        return _obj

