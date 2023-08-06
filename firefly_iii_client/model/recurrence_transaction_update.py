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


class RecurrenceTransactionUpdate(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "id",
        }
        
        class properties:
            id = schemas.StrSchema
            amount = schemas.StrSchema
            
            
            class bill_id(
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
                ) -> 'bill_id':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            budget_id = schemas.StrSchema
            category_id = schemas.StrSchema
            currency_code = schemas.StrSchema
            currency_id = schemas.StrSchema
            description = schemas.StrSchema
            destination_id = schemas.StrSchema
            
            
            class foreign_amount(
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
                ) -> 'foreign_amount':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class foreign_currency_id(
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
                ) -> 'foreign_currency_id':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class piggy_bank_id(
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
                ) -> 'piggy_bank_id':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            source_id = schemas.StrSchema
            
            
            class tags(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tags':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "id": id,
                "amount": amount,
                "bill_id": bill_id,
                "budget_id": budget_id,
                "category_id": category_id,
                "currency_code": currency_code,
                "currency_id": currency_id,
                "description": description,
                "destination_id": destination_id,
                "foreign_amount": foreign_amount,
                "foreign_currency_id": foreign_currency_id,
                "piggy_bank_id": piggy_bank_id,
                "source_id": source_id,
                "tags": tags,
            }
    
    id: MetaOapg.properties.id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bill_id"]) -> MetaOapg.properties.bill_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["budget_id"]) -> MetaOapg.properties.budget_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["category_id"]) -> MetaOapg.properties.category_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency_code"]) -> MetaOapg.properties.currency_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency_id"]) -> MetaOapg.properties.currency_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["destination_id"]) -> MetaOapg.properties.destination_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["foreign_amount"]) -> MetaOapg.properties.foreign_amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["foreign_currency_id"]) -> MetaOapg.properties.foreign_currency_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["piggy_bank_id"]) -> MetaOapg.properties.piggy_bank_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["source_id"]) -> MetaOapg.properties.source_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tags"]) -> MetaOapg.properties.tags: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "amount", "bill_id", "budget_id", "category_id", "currency_code", "currency_id", "description", "destination_id", "foreign_amount", "foreign_currency_id", "piggy_bank_id", "source_id", "tags", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> typing.Union[MetaOapg.properties.amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bill_id"]) -> typing.Union[MetaOapg.properties.bill_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["budget_id"]) -> typing.Union[MetaOapg.properties.budget_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["category_id"]) -> typing.Union[MetaOapg.properties.category_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency_code"]) -> typing.Union[MetaOapg.properties.currency_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency_id"]) -> typing.Union[MetaOapg.properties.currency_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["destination_id"]) -> typing.Union[MetaOapg.properties.destination_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["foreign_amount"]) -> typing.Union[MetaOapg.properties.foreign_amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["foreign_currency_id"]) -> typing.Union[MetaOapg.properties.foreign_currency_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["piggy_bank_id"]) -> typing.Union[MetaOapg.properties.piggy_bank_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source_id"]) -> typing.Union[MetaOapg.properties.source_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tags"]) -> typing.Union[MetaOapg.properties.tags, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "amount", "bill_id", "budget_id", "category_id", "currency_code", "currency_id", "description", "destination_id", "foreign_amount", "foreign_currency_id", "piggy_bank_id", "source_id", "tags", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        amount: typing.Union[MetaOapg.properties.amount, str, schemas.Unset] = schemas.unset,
        bill_id: typing.Union[MetaOapg.properties.bill_id, None, str, schemas.Unset] = schemas.unset,
        budget_id: typing.Union[MetaOapg.properties.budget_id, str, schemas.Unset] = schemas.unset,
        category_id: typing.Union[MetaOapg.properties.category_id, str, schemas.Unset] = schemas.unset,
        currency_code: typing.Union[MetaOapg.properties.currency_code, str, schemas.Unset] = schemas.unset,
        currency_id: typing.Union[MetaOapg.properties.currency_id, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        destination_id: typing.Union[MetaOapg.properties.destination_id, str, schemas.Unset] = schemas.unset,
        foreign_amount: typing.Union[MetaOapg.properties.foreign_amount, None, str, schemas.Unset] = schemas.unset,
        foreign_currency_id: typing.Union[MetaOapg.properties.foreign_currency_id, None, str, schemas.Unset] = schemas.unset,
        piggy_bank_id: typing.Union[MetaOapg.properties.piggy_bank_id, None, str, schemas.Unset] = schemas.unset,
        source_id: typing.Union[MetaOapg.properties.source_id, str, schemas.Unset] = schemas.unset,
        tags: typing.Union[MetaOapg.properties.tags, list, tuple, None, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RecurrenceTransactionUpdate':
        return super().__new__(
            cls,
            *_args,
            id=id,
            amount=amount,
            bill_id=bill_id,
            budget_id=budget_id,
            category_id=category_id,
            currency_code=currency_code,
            currency_id=currency_id,
            description=description,
            destination_id=destination_id,
            foreign_amount=foreign_amount,
            foreign_currency_id=foreign_currency_id,
            piggy_bank_id=piggy_bank_id,
            source_id=source_id,
            tags=tags,
            _configuration=_configuration,
            **kwargs,
        )
