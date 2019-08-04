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


class ChartDataSet(object):
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
        'currency_code': 'str',
        'currency_decimal_places': 'int',
        'currency_id': 'float',
        'currency_symbol': 'str',
        'entries': 'list[ChartDataPoint]',
        'label': 'str',
        'type': 'str',
        'y_axis_id': 'int'
    }

    attribute_map = {
        'currency_code': 'currency_code',
        'currency_decimal_places': 'currency_decimal_places',
        'currency_id': 'currency_id',
        'currency_symbol': 'currency_symbol',
        'entries': 'entries',
        'label': 'label',
        'type': 'type',
        'y_axis_id': 'yAxisID'
    }

    def __init__(self, currency_code=None, currency_decimal_places=None, currency_id=None, currency_symbol=None, entries=None, label=None, type=None, y_axis_id=None):  # noqa: E501
        """ChartDataSet - a model defined in OpenAPI"""  # noqa: E501

        self._currency_code = None
        self._currency_decimal_places = None
        self._currency_id = None
        self._currency_symbol = None
        self._entries = None
        self._label = None
        self._type = None
        self._y_axis_id = None
        self.discriminator = None

        if currency_code is not None:
            self.currency_code = currency_code
        if currency_decimal_places is not None:
            self.currency_decimal_places = currency_decimal_places
        if currency_id is not None:
            self.currency_id = currency_id
        if currency_symbol is not None:
            self.currency_symbol = currency_symbol
        if entries is not None:
            self.entries = entries
        if label is not None:
            self.label = label
        if type is not None:
            self.type = type
        if y_axis_id is not None:
            self.y_axis_id = y_axis_id

    @property
    def currency_code(self):
        """Gets the currency_code of this ChartDataSet.  # noqa: E501


        :return: The currency_code of this ChartDataSet.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this ChartDataSet.


        :param currency_code: The currency_code of this ChartDataSet.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

    @property
    def currency_decimal_places(self):
        """Gets the currency_decimal_places of this ChartDataSet.  # noqa: E501

        Number of decimals for the currency associated to the data in the entries.  # noqa: E501

        :return: The currency_decimal_places of this ChartDataSet.  # noqa: E501
        :rtype: int
        """
        return self._currency_decimal_places

    @currency_decimal_places.setter
    def currency_decimal_places(self, currency_decimal_places):
        """Sets the currency_decimal_places of this ChartDataSet.

        Number of decimals for the currency associated to the data in the entries.  # noqa: E501

        :param currency_decimal_places: The currency_decimal_places of this ChartDataSet.  # noqa: E501
        :type: int
        """

        self._currency_decimal_places = currency_decimal_places

    @property
    def currency_id(self):
        """Gets the currency_id of this ChartDataSet.  # noqa: E501

        The currency ID of the currency associated to the data in the entries.  # noqa: E501

        :return: The currency_id of this ChartDataSet.  # noqa: E501
        :rtype: float
        """
        return self._currency_id

    @currency_id.setter
    def currency_id(self, currency_id):
        """Sets the currency_id of this ChartDataSet.

        The currency ID of the currency associated to the data in the entries.  # noqa: E501

        :param currency_id: The currency_id of this ChartDataSet.  # noqa: E501
        :type: float
        """

        self._currency_id = currency_id

    @property
    def currency_symbol(self):
        """Gets the currency_symbol of this ChartDataSet.  # noqa: E501


        :return: The currency_symbol of this ChartDataSet.  # noqa: E501
        :rtype: str
        """
        return self._currency_symbol

    @currency_symbol.setter
    def currency_symbol(self, currency_symbol):
        """Sets the currency_symbol of this ChartDataSet.


        :param currency_symbol: The currency_symbol of this ChartDataSet.  # noqa: E501
        :type: str
        """

        self._currency_symbol = currency_symbol

    @property
    def entries(self):
        """Gets the entries of this ChartDataSet.  # noqa: E501

        The actual entries for this data set. They 'key' value is the label for the data point. The value is the actual (numerical) value.  # noqa: E501

        :return: The entries of this ChartDataSet.  # noqa: E501
        :rtype: list[ChartDataPoint]
        """
        return self._entries

    @entries.setter
    def entries(self, entries):
        """Sets the entries of this ChartDataSet.

        The actual entries for this data set. They 'key' value is the label for the data point. The value is the actual (numerical) value.  # noqa: E501

        :param entries: The entries of this ChartDataSet.  # noqa: E501
        :type: list[ChartDataPoint]
        """

        self._entries = entries

    @property
    def label(self):
        """Gets the label of this ChartDataSet.  # noqa: E501

        This is the title of the current set. It can refer to an account, a budget or another object (by name).  # noqa: E501

        :return: The label of this ChartDataSet.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ChartDataSet.

        This is the title of the current set. It can refer to an account, a budget or another object (by name).  # noqa: E501

        :param label: The label of this ChartDataSet.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this ChartDataSet.  # noqa: E501

        Indicated the type of chart that is expected to be rendered. You can safely ignore this if you want.  # noqa: E501

        :return: The type of this ChartDataSet.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ChartDataSet.

        Indicated the type of chart that is expected to be rendered. You can safely ignore this if you want.  # noqa: E501

        :param type: The type of this ChartDataSet.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def y_axis_id(self):
        """Gets the y_axis_id of this ChartDataSet.  # noqa: E501

        Used to indicate the Y axis for this data set. Is usually between 0 and 1 (left and right side of the chart).  # noqa: E501

        :return: The y_axis_id of this ChartDataSet.  # noqa: E501
        :rtype: int
        """
        return self._y_axis_id

    @y_axis_id.setter
    def y_axis_id(self, y_axis_id):
        """Sets the y_axis_id of this ChartDataSet.

        Used to indicate the Y axis for this data set. Is usually between 0 and 1 (left and right side of the chart).  # noqa: E501

        :param y_axis_id: The y_axis_id of this ChartDataSet.  # noqa: E501
        :type: int
        """

        self._y_axis_id = y_axis_id

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
        if not isinstance(other, ChartDataSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
