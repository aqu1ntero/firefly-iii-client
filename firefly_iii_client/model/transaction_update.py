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


class TransactionUpdate(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            apply_rules = schemas.BoolSchema
            fire_webhooks = schemas.BoolSchema
            
            
            class group_title(
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
                ) -> 'group_title':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class transactions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['TransactionSplitUpdate']:
                        return TransactionSplitUpdate
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['TransactionSplitUpdate'], typing.List['TransactionSplitUpdate']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'transactions':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'TransactionSplitUpdate':
                    return super().__getitem__(i)
            __annotations__ = {
                "apply_rules": apply_rules,
                "fire_webhooks": fire_webhooks,
                "group_title": group_title,
                "transactions": transactions,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["apply_rules"]) -> MetaOapg.properties.apply_rules: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fire_webhooks"]) -> MetaOapg.properties.fire_webhooks: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["group_title"]) -> MetaOapg.properties.group_title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transactions"]) -> MetaOapg.properties.transactions: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["apply_rules", "fire_webhooks", "group_title", "transactions", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["apply_rules"]) -> typing.Union[MetaOapg.properties.apply_rules, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fire_webhooks"]) -> typing.Union[MetaOapg.properties.fire_webhooks, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["group_title"]) -> typing.Union[MetaOapg.properties.group_title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transactions"]) -> typing.Union[MetaOapg.properties.transactions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["apply_rules", "fire_webhooks", "group_title", "transactions", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        apply_rules: typing.Union[MetaOapg.properties.apply_rules, bool, schemas.Unset] = schemas.unset,
        fire_webhooks: typing.Union[MetaOapg.properties.fire_webhooks, bool, schemas.Unset] = schemas.unset,
        group_title: typing.Union[MetaOapg.properties.group_title, None, str, schemas.Unset] = schemas.unset,
        transactions: typing.Union[MetaOapg.properties.transactions, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TransactionUpdate':
        return super().__new__(
            cls,
            *_args,
            apply_rules=apply_rules,
            fire_webhooks=fire_webhooks,
            group_title=group_title,
            transactions=transactions,
            _configuration=_configuration,
            **kwargs,
        )

from firefly_iii_client.model.transaction_split_update import TransactionSplitUpdate
