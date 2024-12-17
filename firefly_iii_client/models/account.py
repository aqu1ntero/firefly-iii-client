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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from firefly_iii_client.models.account_role_property import AccountRoleProperty
from firefly_iii_client.models.credit_card_type_property import CreditCardTypeProperty
from firefly_iii_client.models.interest_period_property import InterestPeriodProperty
from firefly_iii_client.models.liability_direction_property import LiabilityDirectionProperty
from firefly_iii_client.models.liability_type_property import LiabilityTypeProperty
from firefly_iii_client.models.short_account_type_property import ShortAccountTypeProperty
from typing import Optional, Set
from typing_extensions import Self

class Account(BaseModel):
    """
    Account
    """ # noqa: E501
    account_number: Optional[StrictStr] = None
    account_role: Optional[AccountRoleProperty] = None
    active: Optional[StrictBool] = Field(default=True, description="If omitted, defaults to true.")
    bic: Optional[StrictStr] = None
    created_at: Optional[datetime] = None
    credit_card_type: Optional[CreditCardTypeProperty] = None
    currency_code: Optional[StrictStr] = Field(default=None, description="Use either currency_id or currency_code. Defaults to the user's default currency.")
    currency_decimal_places: Optional[StrictInt] = None
    currency_id: Optional[StrictStr] = Field(default=None, description="Use either currency_id or currency_code. Defaults to the user's default currency.")
    currency_symbol: Optional[StrictStr] = None
    current_balance: Optional[StrictStr] = None
    current_balance_date: Optional[datetime] = Field(default=None, description="The timestamp for this date is always 23:59:59, to indicate it's the balance at the very END of that particular day.")
    current_debt: Optional[StrictStr] = Field(default=None, description="Represents the current debt for liabilities.")
    iban: Optional[StrictStr] = None
    include_net_worth: Optional[StrictBool] = Field(default=True, description="If omitted, defaults to true.")
    interest: Optional[StrictStr] = Field(default=None, description="Mandatory when type is liability. Interest percentage.")
    interest_period: Optional[InterestPeriodProperty] = None
    latitude: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Latitude of the accounts's location, if applicable. Can be used to draw a map.")
    liability_direction: Optional[LiabilityDirectionProperty] = None
    liability_type: Optional[LiabilityTypeProperty] = None
    longitude: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Latitude of the accounts's location, if applicable. Can be used to draw a map.")
    monthly_payment_date: Optional[datetime] = Field(default=None, description="Mandatory when the account_role is ccAsset. Moment at which CC payment installments are asked for by the bank.")
    name: StrictStr
    notes: Optional[StrictStr] = None
    opening_balance: Optional[StrictStr] = Field(default=None, description="Represents the opening balance, the initial amount this account holds.")
    opening_balance_date: Optional[datetime] = Field(default=None, description="Represents the date of the opening balance.")
    order: Optional[StrictInt] = Field(default=None, description="Order of the account. Is NULL if account is not asset or liability.")
    type: ShortAccountTypeProperty
    updated_at: Optional[datetime] = None
    virtual_balance: Optional[StrictStr] = None
    zoom_level: Optional[StrictInt] = Field(default=None, description="Zoom level for the map, if drawn. This to set the box right. Unfortunately this is a proprietary value because each map provider has different zoom levels.")
    __properties: ClassVar[List[str]] = ["account_number", "account_role", "active", "bic", "created_at", "credit_card_type", "currency_code", "currency_decimal_places", "currency_id", "currency_symbol", "current_balance", "current_balance_date", "current_debt", "iban", "include_net_worth", "interest", "interest_period", "latitude", "liability_direction", "liability_type", "longitude", "monthly_payment_date", "name", "notes", "opening_balance", "opening_balance_date", "order", "type", "updated_at", "virtual_balance", "zoom_level"]

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
        """Create an instance of Account from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "created_at",
            "currency_decimal_places",
            "currency_symbol",
            "current_balance",
            "current_balance_date",
            "updated_at",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if account_number (nullable) is None
        # and model_fields_set contains the field
        if self.account_number is None and "account_number" in self.model_fields_set:
            _dict['account_number'] = None

        # set to None if account_role (nullable) is None
        # and model_fields_set contains the field
        if self.account_role is None and "account_role" in self.model_fields_set:
            _dict['account_role'] = None

        # set to None if bic (nullable) is None
        # and model_fields_set contains the field
        if self.bic is None and "bic" in self.model_fields_set:
            _dict['bic'] = None

        # set to None if credit_card_type (nullable) is None
        # and model_fields_set contains the field
        if self.credit_card_type is None and "credit_card_type" in self.model_fields_set:
            _dict['credit_card_type'] = None

        # set to None if current_debt (nullable) is None
        # and model_fields_set contains the field
        if self.current_debt is None and "current_debt" in self.model_fields_set:
            _dict['current_debt'] = None

        # set to None if iban (nullable) is None
        # and model_fields_set contains the field
        if self.iban is None and "iban" in self.model_fields_set:
            _dict['iban'] = None

        # set to None if interest (nullable) is None
        # and model_fields_set contains the field
        if self.interest is None and "interest" in self.model_fields_set:
            _dict['interest'] = None

        # set to None if interest_period (nullable) is None
        # and model_fields_set contains the field
        if self.interest_period is None and "interest_period" in self.model_fields_set:
            _dict['interest_period'] = None

        # set to None if latitude (nullable) is None
        # and model_fields_set contains the field
        if self.latitude is None and "latitude" in self.model_fields_set:
            _dict['latitude'] = None

        # set to None if liability_direction (nullable) is None
        # and model_fields_set contains the field
        if self.liability_direction is None and "liability_direction" in self.model_fields_set:
            _dict['liability_direction'] = None

        # set to None if liability_type (nullable) is None
        # and model_fields_set contains the field
        if self.liability_type is None and "liability_type" in self.model_fields_set:
            _dict['liability_type'] = None

        # set to None if longitude (nullable) is None
        # and model_fields_set contains the field
        if self.longitude is None and "longitude" in self.model_fields_set:
            _dict['longitude'] = None

        # set to None if monthly_payment_date (nullable) is None
        # and model_fields_set contains the field
        if self.monthly_payment_date is None and "monthly_payment_date" in self.model_fields_set:
            _dict['monthly_payment_date'] = None

        # set to None if notes (nullable) is None
        # and model_fields_set contains the field
        if self.notes is None and "notes" in self.model_fields_set:
            _dict['notes'] = None

        # set to None if opening_balance_date (nullable) is None
        # and model_fields_set contains the field
        if self.opening_balance_date is None and "opening_balance_date" in self.model_fields_set:
            _dict['opening_balance_date'] = None

        # set to None if order (nullable) is None
        # and model_fields_set contains the field
        if self.order is None and "order" in self.model_fields_set:
            _dict['order'] = None

        # set to None if zoom_level (nullable) is None
        # and model_fields_set contains the field
        if self.zoom_level is None and "zoom_level" in self.model_fields_set:
            _dict['zoom_level'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Account from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "account_number": obj.get("account_number"),
            "account_role": obj.get("account_role"),
            "active": obj.get("active") if obj.get("active") is not None else True,
            "bic": obj.get("bic"),
            "created_at": obj.get("created_at"),
            "credit_card_type": obj.get("credit_card_type"),
            "currency_code": obj.get("currency_code"),
            "currency_decimal_places": obj.get("currency_decimal_places"),
            "currency_id": obj.get("currency_id"),
            "currency_symbol": obj.get("currency_symbol"),
            "current_balance": obj.get("current_balance"),
            "current_balance_date": obj.get("current_balance_date"),
            "current_debt": obj.get("current_debt"),
            "iban": obj.get("iban"),
            "include_net_worth": obj.get("include_net_worth") if obj.get("include_net_worth") is not None else True,
            "interest": obj.get("interest"),
            "interest_period": obj.get("interest_period"),
            "latitude": obj.get("latitude"),
            "liability_direction": obj.get("liability_direction"),
            "liability_type": obj.get("liability_type"),
            "longitude": obj.get("longitude"),
            "monthly_payment_date": obj.get("monthly_payment_date"),
            "name": obj.get("name"),
            "notes": obj.get("notes"),
            "opening_balance": obj.get("opening_balance"),
            "opening_balance_date": obj.get("opening_balance_date"),
            "order": obj.get("order"),
            "type": obj.get("type"),
            "updated_at": obj.get("updated_at"),
            "virtual_balance": obj.get("virtual_balance"),
            "zoom_level": obj.get("zoom_level")
        })
        return _obj


