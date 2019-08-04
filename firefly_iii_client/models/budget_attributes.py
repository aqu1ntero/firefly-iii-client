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


class BudgetAttributes(object):
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
        'active': 'str',
        'created_at': 'datetime',
        'name': 'str',
        'order': 'int',
        'spent': 'list[BudgetSpent]',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'active': 'active',
        'created_at': 'created_at',
        'name': 'name',
        'order': 'order',
        'spent': 'spent',
        'updated_at': 'updated_at'
    }

    def __init__(self, active=None, created_at=None, name=None, order=None, spent=None, updated_at=None):  # noqa: E501
        """BudgetAttributes - a model defined in OpenAPI"""  # noqa: E501

        self._active = None
        self._created_at = None
        self._name = None
        self._order = None
        self._spent = None
        self._updated_at = None
        self.discriminator = None

        if active is not None:
            self.active = active
        if created_at is not None:
            self.created_at = created_at
        if name is not None:
            self.name = name
        if order is not None:
            self.order = order
        if spent is not None:
            self.spent = spent
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def active(self):
        """Gets the active of this BudgetAttributes.  # noqa: E501


        :return: The active of this BudgetAttributes.  # noqa: E501
        :rtype: str
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this BudgetAttributes.


        :param active: The active of this BudgetAttributes.  # noqa: E501
        :type: str
        """

        self._active = active

    @property
    def created_at(self):
        """Gets the created_at of this BudgetAttributes.  # noqa: E501


        :return: The created_at of this BudgetAttributes.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this BudgetAttributes.


        :param created_at: The created_at of this BudgetAttributes.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def name(self):
        """Gets the name of this BudgetAttributes.  # noqa: E501


        :return: The name of this BudgetAttributes.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BudgetAttributes.


        :param name: The name of this BudgetAttributes.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def order(self):
        """Gets the order of this BudgetAttributes.  # noqa: E501


        :return: The order of this BudgetAttributes.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this BudgetAttributes.


        :param order: The order of this BudgetAttributes.  # noqa: E501
        :type: int
        """

        self._order = order

    @property
    def spent(self):
        """Gets the spent of this BudgetAttributes.  # noqa: E501

        Information on how much was spent in this budget. Is only filled in when the start and end date are submitted.  # noqa: E501

        :return: The spent of this BudgetAttributes.  # noqa: E501
        :rtype: list[BudgetSpent]
        """
        return self._spent

    @spent.setter
    def spent(self, spent):
        """Sets the spent of this BudgetAttributes.

        Information on how much was spent in this budget. Is only filled in when the start and end date are submitted.  # noqa: E501

        :param spent: The spent of this BudgetAttributes.  # noqa: E501
        :type: list[BudgetSpent]
        """

        self._spent = spent

    @property
    def updated_at(self):
        """Gets the updated_at of this BudgetAttributes.  # noqa: E501


        :return: The updated_at of this BudgetAttributes.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this BudgetAttributes.


        :param updated_at: The updated_at of this BudgetAttributes.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

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
        if not isinstance(other, BudgetAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
