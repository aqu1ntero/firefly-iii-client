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


class ChartDataSet(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            currency_code = schemas.StrSchema
            currency_decimal_places = schemas.Int32Schema
            currency_id = schemas.StrSchema
            currency_symbol = schemas.StrSchema
            end_date = schemas.DateTimeSchema
            
            
            class entries(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ChartDataPoint']:
                        return ChartDataPoint
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['ChartDataPoint'], typing.List['ChartDataPoint']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'entries':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ChartDataPoint':
                    return super().__getitem__(i)
            label = schemas.StrSchema
            start_date = schemas.DateTimeSchema
            type = schemas.StrSchema
            yAxisID = schemas.Int32Schema
            __annotations__ = {
                "currency_code": currency_code,
                "currency_decimal_places": currency_decimal_places,
                "currency_id": currency_id,
                "currency_symbol": currency_symbol,
                "end_date": end_date,
                "entries": entries,
                "label": label,
                "start_date": start_date,
                "type": type,
                "yAxisID": yAxisID,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency_code"]) -> MetaOapg.properties.currency_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency_decimal_places"]) -> MetaOapg.properties.currency_decimal_places: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency_id"]) -> MetaOapg.properties.currency_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency_symbol"]) -> MetaOapg.properties.currency_symbol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["end_date"]) -> MetaOapg.properties.end_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entries"]) -> MetaOapg.properties.entries: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["label"]) -> MetaOapg.properties.label: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start_date"]) -> MetaOapg.properties.start_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["yAxisID"]) -> MetaOapg.properties.yAxisID: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["currency_code", "currency_decimal_places", "currency_id", "currency_symbol", "end_date", "entries", "label", "start_date", "type", "yAxisID", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency_code"]) -> typing.Union[MetaOapg.properties.currency_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency_decimal_places"]) -> typing.Union[MetaOapg.properties.currency_decimal_places, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency_id"]) -> typing.Union[MetaOapg.properties.currency_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency_symbol"]) -> typing.Union[MetaOapg.properties.currency_symbol, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["end_date"]) -> typing.Union[MetaOapg.properties.end_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entries"]) -> typing.Union[MetaOapg.properties.entries, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["label"]) -> typing.Union[MetaOapg.properties.label, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start_date"]) -> typing.Union[MetaOapg.properties.start_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["yAxisID"]) -> typing.Union[MetaOapg.properties.yAxisID, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["currency_code", "currency_decimal_places", "currency_id", "currency_symbol", "end_date", "entries", "label", "start_date", "type", "yAxisID", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        currency_code: typing.Union[MetaOapg.properties.currency_code, str, schemas.Unset] = schemas.unset,
        currency_decimal_places: typing.Union[MetaOapg.properties.currency_decimal_places, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        currency_id: typing.Union[MetaOapg.properties.currency_id, str, schemas.Unset] = schemas.unset,
        currency_symbol: typing.Union[MetaOapg.properties.currency_symbol, str, schemas.Unset] = schemas.unset,
        end_date: typing.Union[MetaOapg.properties.end_date, str, datetime, schemas.Unset] = schemas.unset,
        entries: typing.Union[MetaOapg.properties.entries, list, tuple, schemas.Unset] = schemas.unset,
        label: typing.Union[MetaOapg.properties.label, str, schemas.Unset] = schemas.unset,
        start_date: typing.Union[MetaOapg.properties.start_date, str, datetime, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        yAxisID: typing.Union[MetaOapg.properties.yAxisID, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ChartDataSet':
        return super().__new__(
            cls,
            *_args,
            currency_code=currency_code,
            currency_decimal_places=currency_decimal_places,
            currency_id=currency_id,
            currency_symbol=currency_symbol,
            end_date=end_date,
            entries=entries,
            label=label,
            start_date=start_date,
            type=type,
            yAxisID=yAxisID,
            _configuration=_configuration,
            **kwargs,
        )

from firefly_iii_client.model.chart_data_point import ChartDataPoint
