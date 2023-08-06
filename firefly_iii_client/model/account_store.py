# coding: utf-8

"""
    Firefly III API Client

    This is the Python client for Firefly III API  # noqa: E501

    The version of the OpenAPI document: 2.0.5
    Contact: james@firefly-iii.org
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from firefly_iii_client import schemas  # noqa: F401


class AccountStore(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "name",
            "type",
        }
        
        class properties:
            name = schemas.StrSchema
        
            @staticmethod
            def type() -> typing.Type['ShortAccountTypeProperty']:
                return ShortAccountTypeProperty
            
            
            class account_number(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'string'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'account_number':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def account_role() -> typing.Type['AccountRoleProperty']:
                return AccountRoleProperty
            active = schemas.BoolSchema
            
            
            class bic(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'string'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'bic':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def credit_card_type() -> typing.Type['CreditCardType']:
                return CreditCardType
            currency_code = schemas.StrSchema
            currency_id = schemas.StrSchema
            
            
            class iban(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'iban'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'iban':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            include_net_worth = schemas.BoolSchema
            
            
            class interest(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'string'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'interest':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def interest_period() -> typing.Type['InterestPeriod']:
                return InterestPeriod
            
            
            class latitude(
                schemas.Float64Base,
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'double'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'latitude':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def liability_direction() -> typing.Type['LiabilityDirection']:
                return LiabilityDirection
        
            @staticmethod
            def liability_type() -> typing.Type['LiabilityType']:
                return LiabilityType
            
            
            class longitude(
                schemas.Float64Base,
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'double'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'longitude':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class monthly_payment_date(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'monthly_payment_date':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class notes(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'string'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'notes':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            opening_balance = schemas.StrSchema
            
            
            class opening_balance_date(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'opening_balance_date':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            order = schemas.Int32Schema
            virtual_balance = schemas.StrSchema
            
            
            class zoom_level(
                schemas.Int32Base,
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'int32'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'zoom_level':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "name": name,
                "type": type,
                "account_number": account_number,
                "account_role": account_role,
                "active": active,
                "bic": bic,
                "credit_card_type": credit_card_type,
                "currency_code": currency_code,
                "currency_id": currency_id,
                "iban": iban,
                "include_net_worth": include_net_worth,
                "interest": interest,
                "interest_period": interest_period,
                "latitude": latitude,
                "liability_direction": liability_direction,
                "liability_type": liability_type,
                "longitude": longitude,
                "monthly_payment_date": monthly_payment_date,
                "notes": notes,
                "opening_balance": opening_balance,
                "opening_balance_date": opening_balance_date,
                "order": order,
                "virtual_balance": virtual_balance,
                "zoom_level": zoom_level,
            }
    
    name: MetaOapg.properties.name
    type: 'ShortAccountTypeProperty'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'ShortAccountTypeProperty': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account_number"]) -> MetaOapg.properties.account_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account_role"]) -> 'AccountRoleProperty': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["active"]) -> MetaOapg.properties.active: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bic"]) -> MetaOapg.properties.bic: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["credit_card_type"]) -> 'CreditCardType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency_code"]) -> MetaOapg.properties.currency_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency_id"]) -> MetaOapg.properties.currency_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["iban"]) -> MetaOapg.properties.iban: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["include_net_worth"]) -> MetaOapg.properties.include_net_worth: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["interest"]) -> MetaOapg.properties.interest: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["interest_period"]) -> 'InterestPeriod': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["latitude"]) -> MetaOapg.properties.latitude: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["liability_direction"]) -> 'LiabilityDirection': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["liability_type"]) -> 'LiabilityType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["longitude"]) -> MetaOapg.properties.longitude: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["monthly_payment_date"]) -> MetaOapg.properties.monthly_payment_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notes"]) -> MetaOapg.properties.notes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["opening_balance"]) -> MetaOapg.properties.opening_balance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["opening_balance_date"]) -> MetaOapg.properties.opening_balance_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["order"]) -> MetaOapg.properties.order: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["virtual_balance"]) -> MetaOapg.properties.virtual_balance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["zoom_level"]) -> MetaOapg.properties.zoom_level: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "type", "account_number", "account_role", "active", "bic", "credit_card_type", "currency_code", "currency_id", "iban", "include_net_worth", "interest", "interest_period", "latitude", "liability_direction", "liability_type", "longitude", "monthly_payment_date", "notes", "opening_balance", "opening_balance_date", "order", "virtual_balance", "zoom_level", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> 'ShortAccountTypeProperty': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account_number"]) -> typing.Union[MetaOapg.properties.account_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account_role"]) -> typing.Union['AccountRoleProperty', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["active"]) -> typing.Union[MetaOapg.properties.active, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bic"]) -> typing.Union[MetaOapg.properties.bic, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["credit_card_type"]) -> typing.Union['CreditCardType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency_code"]) -> typing.Union[MetaOapg.properties.currency_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency_id"]) -> typing.Union[MetaOapg.properties.currency_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["iban"]) -> typing.Union[MetaOapg.properties.iban, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["include_net_worth"]) -> typing.Union[MetaOapg.properties.include_net_worth, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["interest"]) -> typing.Union[MetaOapg.properties.interest, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["interest_period"]) -> typing.Union['InterestPeriod', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["latitude"]) -> typing.Union[MetaOapg.properties.latitude, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["liability_direction"]) -> typing.Union['LiabilityDirection', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["liability_type"]) -> typing.Union['LiabilityType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["longitude"]) -> typing.Union[MetaOapg.properties.longitude, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["monthly_payment_date"]) -> typing.Union[MetaOapg.properties.monthly_payment_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notes"]) -> typing.Union[MetaOapg.properties.notes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["opening_balance"]) -> typing.Union[MetaOapg.properties.opening_balance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["opening_balance_date"]) -> typing.Union[MetaOapg.properties.opening_balance_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["order"]) -> typing.Union[MetaOapg.properties.order, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["virtual_balance"]) -> typing.Union[MetaOapg.properties.virtual_balance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["zoom_level"]) -> typing.Union[MetaOapg.properties.zoom_level, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "type", "account_number", "account_role", "active", "bic", "credit_card_type", "currency_code", "currency_id", "iban", "include_net_worth", "interest", "interest_period", "latitude", "liability_direction", "liability_type", "longitude", "monthly_payment_date", "notes", "opening_balance", "opening_balance_date", "order", "virtual_balance", "zoom_level", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        type: 'ShortAccountTypeProperty',
        account_number: typing.Union[MetaOapg.properties.account_number, None, str, schemas.Unset] = schemas.unset,
        account_role: typing.Union['AccountRoleProperty', schemas.Unset] = schemas.unset,
        active: typing.Union[MetaOapg.properties.active, bool, schemas.Unset] = schemas.unset,
        bic: typing.Union[MetaOapg.properties.bic, None, str, schemas.Unset] = schemas.unset,
        credit_card_type: typing.Union['CreditCardType', schemas.Unset] = schemas.unset,
        currency_code: typing.Union[MetaOapg.properties.currency_code, str, schemas.Unset] = schemas.unset,
        currency_id: typing.Union[MetaOapg.properties.currency_id, str, schemas.Unset] = schemas.unset,
        iban: typing.Union[MetaOapg.properties.iban, None, str, schemas.Unset] = schemas.unset,
        include_net_worth: typing.Union[MetaOapg.properties.include_net_worth, bool, schemas.Unset] = schemas.unset,
        interest: typing.Union[MetaOapg.properties.interest, None, str, schemas.Unset] = schemas.unset,
        interest_period: typing.Union['InterestPeriod', schemas.Unset] = schemas.unset,
        latitude: typing.Union[MetaOapg.properties.latitude, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        liability_direction: typing.Union['LiabilityDirection', schemas.Unset] = schemas.unset,
        liability_type: typing.Union['LiabilityType', schemas.Unset] = schemas.unset,
        longitude: typing.Union[MetaOapg.properties.longitude, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        monthly_payment_date: typing.Union[MetaOapg.properties.monthly_payment_date, None, str, datetime, schemas.Unset] = schemas.unset,
        notes: typing.Union[MetaOapg.properties.notes, None, str, schemas.Unset] = schemas.unset,
        opening_balance: typing.Union[MetaOapg.properties.opening_balance, str, schemas.Unset] = schemas.unset,
        opening_balance_date: typing.Union[MetaOapg.properties.opening_balance_date, None, str, datetime, schemas.Unset] = schemas.unset,
        order: typing.Union[MetaOapg.properties.order, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        virtual_balance: typing.Union[MetaOapg.properties.virtual_balance, str, schemas.Unset] = schemas.unset,
        zoom_level: typing.Union[MetaOapg.properties.zoom_level, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AccountStore':
        return super().__new__(
            cls,
            *_args,
            name=name,
            type=type,
            account_number=account_number,
            account_role=account_role,
            active=active,
            bic=bic,
            credit_card_type=credit_card_type,
            currency_code=currency_code,
            currency_id=currency_id,
            iban=iban,
            include_net_worth=include_net_worth,
            interest=interest,
            interest_period=interest_period,
            latitude=latitude,
            liability_direction=liability_direction,
            liability_type=liability_type,
            longitude=longitude,
            monthly_payment_date=monthly_payment_date,
            notes=notes,
            opening_balance=opening_balance,
            opening_balance_date=opening_balance_date,
            order=order,
            virtual_balance=virtual_balance,
            zoom_level=zoom_level,
            _configuration=_configuration,
            **kwargs,
        )

from firefly_iii_client.model.account_role_property import AccountRoleProperty
from firefly_iii_client.model.credit_card_type import CreditCardType
from firefly_iii_client.model.interest_period import InterestPeriod
from firefly_iii_client.model.liability_direction import LiabilityDirection
from firefly_iii_client.model.liability_type import LiabilityType
from firefly_iii_client.model.short_account_type_property import ShortAccountTypeProperty
