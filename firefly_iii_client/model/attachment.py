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


class Attachment(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "filename",
            "attachable_id",
            "attachable_type",
        }
        
        class properties:
            attachable_id = schemas.StrSchema
        
            @staticmethod
            def attachable_type() -> typing.Type['AttachableType']:
                return AttachableType
            filename = schemas.StrSchema
            created_at = schemas.DateTimeSchema
            download_url = schemas.StrSchema
            md5 = schemas.StrSchema
            mime = schemas.StrSchema
            
            
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
            size = schemas.Int32Schema
            title = schemas.StrSchema
            updated_at = schemas.DateTimeSchema
            upload_url = schemas.StrSchema
            __annotations__ = {
                "attachable_id": attachable_id,
                "attachable_type": attachable_type,
                "filename": filename,
                "created_at": created_at,
                "download_url": download_url,
                "md5": md5,
                "mime": mime,
                "notes": notes,
                "size": size,
                "title": title,
                "updated_at": updated_at,
                "upload_url": upload_url,
            }
    
    filename: MetaOapg.properties.filename
    attachable_id: MetaOapg.properties.attachable_id
    attachable_type: 'AttachableType'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attachable_id"]) -> MetaOapg.properties.attachable_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attachable_type"]) -> 'AttachableType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["filename"]) -> MetaOapg.properties.filename: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["download_url"]) -> MetaOapg.properties.download_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["md5"]) -> MetaOapg.properties.md5: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mime"]) -> MetaOapg.properties.mime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notes"]) -> MetaOapg.properties.notes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["size"]) -> MetaOapg.properties.size: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["upload_url"]) -> MetaOapg.properties.upload_url: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["attachable_id", "attachable_type", "filename", "created_at", "download_url", "md5", "mime", "notes", "size", "title", "updated_at", "upload_url", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attachable_id"]) -> MetaOapg.properties.attachable_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attachable_type"]) -> 'AttachableType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["filename"]) -> MetaOapg.properties.filename: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["download_url"]) -> typing.Union[MetaOapg.properties.download_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["md5"]) -> typing.Union[MetaOapg.properties.md5, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mime"]) -> typing.Union[MetaOapg.properties.mime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notes"]) -> typing.Union[MetaOapg.properties.notes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["size"]) -> typing.Union[MetaOapg.properties.size, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> typing.Union[MetaOapg.properties.updated_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["upload_url"]) -> typing.Union[MetaOapg.properties.upload_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["attachable_id", "attachable_type", "filename", "created_at", "download_url", "md5", "mime", "notes", "size", "title", "updated_at", "upload_url", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        filename: typing.Union[MetaOapg.properties.filename, str, ],
        attachable_id: typing.Union[MetaOapg.properties.attachable_id, str, ],
        attachable_type: 'AttachableType',
        created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, schemas.Unset] = schemas.unset,
        download_url: typing.Union[MetaOapg.properties.download_url, str, schemas.Unset] = schemas.unset,
        md5: typing.Union[MetaOapg.properties.md5, str, schemas.Unset] = schemas.unset,
        mime: typing.Union[MetaOapg.properties.mime, str, schemas.Unset] = schemas.unset,
        notes: typing.Union[MetaOapg.properties.notes, None, str, schemas.Unset] = schemas.unset,
        size: typing.Union[MetaOapg.properties.size, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        updated_at: typing.Union[MetaOapg.properties.updated_at, str, datetime, schemas.Unset] = schemas.unset,
        upload_url: typing.Union[MetaOapg.properties.upload_url, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Attachment':
        return super().__new__(
            cls,
            *_args,
            filename=filename,
            attachable_id=attachable_id,
            attachable_type=attachable_type,
            created_at=created_at,
            download_url=download_url,
            md5=md5,
            mime=mime,
            notes=notes,
            size=size,
            title=title,
            updated_at=updated_at,
            upload_url=upload_url,
            _configuration=_configuration,
            **kwargs,
        )

from firefly_iii_client.model.attachable_type import AttachableType
