# coding: utf-8

"""
    Firefly III API Client

    This is the Python client for Firefly III API  # noqa: E501

    OpenAPI spec version: 0.9.0
    Contact: thegrumpydictator@gmail.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class RuleGroupAttributes(object):
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
        'active': 'bool',
        'created_at': 'datetime',
        'description': 'str',
        'order': 'int',
        'title': 'str',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'active': 'active',
        'created_at': 'created_at',
        'description': 'description',
        'order': 'order',
        'title': 'title',
        'updated_at': 'updated_at'
    }

    def __init__(self, active=None, created_at=None, description=None, order=None, title=None, updated_at=None):  # noqa: E501
        """RuleGroupAttributes - a model defined in OpenAPI"""  # noqa: E501

        self._active = None
        self._created_at = None
        self._description = None
        self._order = None
        self._title = None
        self._updated_at = None
        self.discriminator = None

        if active is not None:
            self.active = active
        if created_at is not None:
            self.created_at = created_at
        if description is not None:
            self.description = description
        if order is not None:
            self.order = order
        if title is not None:
            self.title = title
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def active(self):
        """Gets the active of this RuleGroupAttributes.  # noqa: E501


        :return: The active of this RuleGroupAttributes.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this RuleGroupAttributes.


        :param active: The active of this RuleGroupAttributes.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def created_at(self):
        """Gets the created_at of this RuleGroupAttributes.  # noqa: E501


        :return: The created_at of this RuleGroupAttributes.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this RuleGroupAttributes.


        :param created_at: The created_at of this RuleGroupAttributes.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def description(self):
        """Gets the description of this RuleGroupAttributes.  # noqa: E501


        :return: The description of this RuleGroupAttributes.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RuleGroupAttributes.


        :param description: The description of this RuleGroupAttributes.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def order(self):
        """Gets the order of this RuleGroupAttributes.  # noqa: E501


        :return: The order of this RuleGroupAttributes.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this RuleGroupAttributes.


        :param order: The order of this RuleGroupAttributes.  # noqa: E501
        :type: int
        """

        self._order = order

    @property
    def title(self):
        """Gets the title of this RuleGroupAttributes.  # noqa: E501


        :return: The title of this RuleGroupAttributes.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this RuleGroupAttributes.


        :param title: The title of this RuleGroupAttributes.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def updated_at(self):
        """Gets the updated_at of this RuleGroupAttributes.  # noqa: E501


        :return: The updated_at of this RuleGroupAttributes.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this RuleGroupAttributes.


        :param updated_at: The updated_at of this RuleGroupAttributes.  # noqa: E501
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
        if not isinstance(other, RuleGroupAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other