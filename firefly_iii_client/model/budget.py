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


class Budget(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "name",
        }
        
        class properties:
            name = schemas.StrSchema
            active = schemas.BoolSchema
            
            
            class auto_budget_amount(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'amount'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'auto_budget_amount':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class auto_budget_currency_code(
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
                ) -> 'auto_budget_currency_code':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class auto_budget_currency_id(
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
                ) -> 'auto_budget_currency_id':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def auto_budget_period() -> typing.Type['AutoBudgetPeriod']:
                return AutoBudgetPeriod
        
            @staticmethod
            def auto_budget_type() -> typing.Type['AutoBudgetType']:
                return AutoBudgetType
            created_at = schemas.DateTimeSchema
            
            
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
            order = schemas.Int32Schema
            
            
            class spent(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['BudgetSpent']:
                        return BudgetSpent
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['BudgetSpent'], typing.List['BudgetSpent']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'spent':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'BudgetSpent':
                    return super().__getitem__(i)
            updated_at = schemas.DateTimeSchema
            __annotations__ = {
                "name": name,
                "active": active,
                "auto_budget_amount": auto_budget_amount,
                "auto_budget_currency_code": auto_budget_currency_code,
                "auto_budget_currency_id": auto_budget_currency_id,
                "auto_budget_period": auto_budget_period,
                "auto_budget_type": auto_budget_type,
                "created_at": created_at,
                "notes": notes,
                "order": order,
                "spent": spent,
                "updated_at": updated_at,
            }
    
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["active"]) -> MetaOapg.properties.active: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["auto_budget_amount"]) -> MetaOapg.properties.auto_budget_amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["auto_budget_currency_code"]) -> MetaOapg.properties.auto_budget_currency_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["auto_budget_currency_id"]) -> MetaOapg.properties.auto_budget_currency_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["auto_budget_period"]) -> 'AutoBudgetPeriod': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["auto_budget_type"]) -> 'AutoBudgetType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notes"]) -> MetaOapg.properties.notes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["order"]) -> MetaOapg.properties.order: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["spent"]) -> MetaOapg.properties.spent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "active", "auto_budget_amount", "auto_budget_currency_code", "auto_budget_currency_id", "auto_budget_period", "auto_budget_type", "created_at", "notes", "order", "spent", "updated_at", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["active"]) -> typing.Union[MetaOapg.properties.active, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["auto_budget_amount"]) -> typing.Union[MetaOapg.properties.auto_budget_amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["auto_budget_currency_code"]) -> typing.Union[MetaOapg.properties.auto_budget_currency_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["auto_budget_currency_id"]) -> typing.Union[MetaOapg.properties.auto_budget_currency_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["auto_budget_period"]) -> typing.Union['AutoBudgetPeriod', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["auto_budget_type"]) -> typing.Union['AutoBudgetType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notes"]) -> typing.Union[MetaOapg.properties.notes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["order"]) -> typing.Union[MetaOapg.properties.order, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["spent"]) -> typing.Union[MetaOapg.properties.spent, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> typing.Union[MetaOapg.properties.updated_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "active", "auto_budget_amount", "auto_budget_currency_code", "auto_budget_currency_id", "auto_budget_period", "auto_budget_type", "created_at", "notes", "order", "spent", "updated_at", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        active: typing.Union[MetaOapg.properties.active, bool, schemas.Unset] = schemas.unset,
        auto_budget_amount: typing.Union[MetaOapg.properties.auto_budget_amount, None, str, schemas.Unset] = schemas.unset,
        auto_budget_currency_code: typing.Union[MetaOapg.properties.auto_budget_currency_code, None, str, schemas.Unset] = schemas.unset,
        auto_budget_currency_id: typing.Union[MetaOapg.properties.auto_budget_currency_id, None, str, schemas.Unset] = schemas.unset,
        auto_budget_period: typing.Union['AutoBudgetPeriod', schemas.Unset] = schemas.unset,
        auto_budget_type: typing.Union['AutoBudgetType', schemas.Unset] = schemas.unset,
        created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, schemas.Unset] = schemas.unset,
        notes: typing.Union[MetaOapg.properties.notes, None, str, schemas.Unset] = schemas.unset,
        order: typing.Union[MetaOapg.properties.order, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        spent: typing.Union[MetaOapg.properties.spent, list, tuple, schemas.Unset] = schemas.unset,
        updated_at: typing.Union[MetaOapg.properties.updated_at, str, datetime, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Budget':
        return super().__new__(
            cls,
            *_args,
            name=name,
            active=active,
            auto_budget_amount=auto_budget_amount,
            auto_budget_currency_code=auto_budget_currency_code,
            auto_budget_currency_id=auto_budget_currency_id,
            auto_budget_period=auto_budget_period,
            auto_budget_type=auto_budget_type,
            created_at=created_at,
            notes=notes,
            order=order,
            spent=spent,
            updated_at=updated_at,
            _configuration=_configuration,
            **kwargs,
        )

from firefly_iii_client.model.auto_budget_period import AutoBudgetPeriod
from firefly_iii_client.model.auto_budget_type import AutoBudgetType
from firefly_iii_client.model.budget_spent import BudgetSpent
