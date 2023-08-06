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


class TransactionLink(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "link_type_id",
            "outward_id",
            "inward_id",
        }
        
        class properties:
            inward_id = schemas.StrSchema
            link_type_id = schemas.StrSchema
            outward_id = schemas.StrSchema
            created_at = schemas.DateTimeSchema
            link_type_name = schemas.StrSchema
            
            
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
            updated_at = schemas.DateTimeSchema
            __annotations__ = {
                "inward_id": inward_id,
                "link_type_id": link_type_id,
                "outward_id": outward_id,
                "created_at": created_at,
                "link_type_name": link_type_name,
                "notes": notes,
                "updated_at": updated_at,
            }
    
    link_type_id: MetaOapg.properties.link_type_id
    outward_id: MetaOapg.properties.outward_id
    inward_id: MetaOapg.properties.inward_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["inward_id"]) -> MetaOapg.properties.inward_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["link_type_id"]) -> MetaOapg.properties.link_type_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["outward_id"]) -> MetaOapg.properties.outward_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["link_type_name"]) -> MetaOapg.properties.link_type_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notes"]) -> MetaOapg.properties.notes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["inward_id", "link_type_id", "outward_id", "created_at", "link_type_name", "notes", "updated_at", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["inward_id"]) -> MetaOapg.properties.inward_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["link_type_id"]) -> MetaOapg.properties.link_type_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["outward_id"]) -> MetaOapg.properties.outward_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["link_type_name"]) -> typing.Union[MetaOapg.properties.link_type_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notes"]) -> typing.Union[MetaOapg.properties.notes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> typing.Union[MetaOapg.properties.updated_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["inward_id", "link_type_id", "outward_id", "created_at", "link_type_name", "notes", "updated_at", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        link_type_id: typing.Union[MetaOapg.properties.link_type_id, str, ],
        outward_id: typing.Union[MetaOapg.properties.outward_id, str, ],
        inward_id: typing.Union[MetaOapg.properties.inward_id, str, ],
        created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, schemas.Unset] = schemas.unset,
        link_type_name: typing.Union[MetaOapg.properties.link_type_name, str, schemas.Unset] = schemas.unset,
        notes: typing.Union[MetaOapg.properties.notes, None, str, schemas.Unset] = schemas.unset,
        updated_at: typing.Union[MetaOapg.properties.updated_at, str, datetime, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TransactionLink':
        return super().__new__(
            cls,
            *_args,
            link_type_id=link_type_id,
            outward_id=outward_id,
            inward_id=inward_id,
            created_at=created_at,
            link_type_name=link_type_name,
            notes=notes,
            updated_at=updated_at,
            _configuration=_configuration,
            **kwargs,
        )
