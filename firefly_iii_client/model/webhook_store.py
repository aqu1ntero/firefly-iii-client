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


class WebhookStore(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "delivery",
            "response",
            "trigger",
            "title",
            "url",
        }
        
        class properties:
        
            @staticmethod
            def delivery() -> typing.Type['WebhookDelivery']:
                return WebhookDelivery
        
            @staticmethod
            def response() -> typing.Type['WebhookResponse']:
                return WebhookResponse
            title = schemas.StrSchema
        
            @staticmethod
            def trigger() -> typing.Type['WebhookTrigger']:
                return WebhookTrigger
            url = schemas.StrSchema
            active = schemas.BoolSchema
            __annotations__ = {
                "delivery": delivery,
                "response": response,
                "title": title,
                "trigger": trigger,
                "url": url,
                "active": active,
            }
    
    delivery: 'WebhookDelivery'
    response: 'WebhookResponse'
    trigger: 'WebhookTrigger'
    title: MetaOapg.properties.title
    url: MetaOapg.properties.url
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["delivery"]) -> 'WebhookDelivery': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["response"]) -> 'WebhookResponse': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trigger"]) -> 'WebhookTrigger': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["active"]) -> MetaOapg.properties.active: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["delivery", "response", "title", "trigger", "url", "active", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["delivery"]) -> 'WebhookDelivery': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["response"]) -> 'WebhookResponse': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trigger"]) -> 'WebhookTrigger': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["active"]) -> typing.Union[MetaOapg.properties.active, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["delivery", "response", "title", "trigger", "url", "active", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        delivery: 'WebhookDelivery',
        response: 'WebhookResponse',
        trigger: 'WebhookTrigger',
        title: typing.Union[MetaOapg.properties.title, str, ],
        url: typing.Union[MetaOapg.properties.url, str, ],
        active: typing.Union[MetaOapg.properties.active, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WebhookStore':
        return super().__new__(
            cls,
            *_args,
            delivery=delivery,
            response=response,
            trigger=trigger,
            title=title,
            url=url,
            active=active,
            _configuration=_configuration,
            **kwargs,
        )

from firefly_iii_client.model.webhook_delivery import WebhookDelivery
from firefly_iii_client.model.webhook_response import WebhookResponse
from firefly_iii_client.model.webhook_trigger import WebhookTrigger
