# coding: utf-8

"""
    Firefly III API Client

    This is the Python client for Firefly III API  # noqa: E501

    OpenAPI spec version: 0.9.0
    Contact: thegrumpydictator@gmail.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from firefly_iii_client.api_client import ApiClient


class CurrencyExchangeRatesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_exchange_rate(self, **kwargs):  # noqa: E501
        """Get an exchange rate.  # noqa: E501

        Get an exchange rate. If Firefly III doesn't know the rate it will set the rate to 1.0.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_exchange_rate(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str _from: The source currency code. If omitted, defaults to EUR.
        :param str to: The destination currency code. If omitted, defaults to USD.
        :param date date: The date you want to know the exchange rate on.
        :param float amount: The amount in the source currency. If added, Firefly III will calculate the amount in the destination currency.
        :return: ExchangeRate
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_exchange_rate_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_exchange_rate_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_exchange_rate_with_http_info(self, **kwargs):  # noqa: E501
        """Get an exchange rate.  # noqa: E501

        Get an exchange rate. If Firefly III doesn't know the rate it will set the rate to 1.0.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_exchange_rate_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str _from: The source currency code. If omitted, defaults to EUR.
        :param str to: The destination currency code. If omitted, defaults to USD.
        :param date date: The date you want to know the exchange rate on.
        :param float amount: The amount in the source currency. If added, Firefly III will calculate the amount in the destination currency.
        :return: ExchangeRate
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['_from', 'to', 'date', 'amount']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_exchange_rate" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if '_from' in local_var_params:
            query_params.append(('from', local_var_params['_from']))  # noqa: E501
        if 'to' in local_var_params:
            query_params.append(('to', local_var_params['to']))  # noqa: E501
        if 'date' in local_var_params:
            query_params.append(('date', local_var_params['date']))  # noqa: E501
        if 'amount' in local_var_params:
            query_params.append(('amount', local_var_params['amount']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['firefly_iii_auth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/cer', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ExchangeRate',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)