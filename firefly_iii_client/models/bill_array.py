# coding: utf-8

"""
    Firefly III API Client

    This is the Python client for Firefly III API  # noqa: E501

    The version of the OpenAPI document: 0.10.0
    Contact: thegrumpydictator@gmail.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class BillArray(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'data': 'list[Bill]',
        'meta': 'Meta'
    }

    attribute_map = {
        'data': 'data',
        'meta': 'meta'
    }

    def __init__(self, data=None, meta=None):  # noqa: E501
        """BillArray - a model defined in OpenAPI"""  # noqa: E501

        self._data = None
        self._meta = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if meta is not None:
            self.meta = meta

    @property
    def data(self):
        """Gets the data of this BillArray.  # noqa: E501


        :return: The data of this BillArray.  # noqa: E501
        :rtype: list[Bill]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this BillArray.


        :param data: The data of this BillArray.  # noqa: E501
        :type: list[Bill]
        """

        self._data = data

    @property
    def meta(self):
        """Gets the meta of this BillArray.  # noqa: E501


        :return: The meta of this BillArray.  # noqa: E501
        :rtype: Meta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this BillArray.


        :param meta: The meta of this BillArray.  # noqa: E501
        :type: Meta
        """

        self._meta = meta

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BillArray):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
