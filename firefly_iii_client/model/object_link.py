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


class ObjectLink(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class _0(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        rel = schemas.StrSchema
                        uri = schemas.StrSchema
                        __annotations__ = {
                            "rel": rel,
                            "uri": uri,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["rel"]) -> MetaOapg.properties.rel: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["uri"]) -> MetaOapg.properties.uri: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["rel", "uri", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["rel"]) -> typing.Union[MetaOapg.properties.rel, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["uri"]) -> typing.Union[MetaOapg.properties.uri, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["rel", "uri", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    rel: typing.Union[MetaOapg.properties.rel, str, schemas.Unset] = schemas.unset,
                    uri: typing.Union[MetaOapg.properties.uri, str, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> '_0':
                    return super().__new__(
                        cls,
                        *_args,
                        rel=rel,
                        uri=uri,
                        _configuration=_configuration,
                        **kwargs,
                    )
            self = schemas.StrSchema
            __annotations__ = {
                "0": _0,
                "self": self,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["0"]) -> MetaOapg.properties._0: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["self"]) -> MetaOapg.properties.self: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["0", "self", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["0"]) -> typing.Union[MetaOapg.properties._0, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["self"]) -> typing.Union[MetaOapg.properties.self, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["0", "self", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        self: typing.Union[MetaOapg.properties.self, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ObjectLink':
        return super().__new__(
            cls,
            *_args,
            self=self,
            _configuration=_configuration,
            **kwargs,
        )
