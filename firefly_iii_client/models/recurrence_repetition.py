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


class RecurrenceRepetition(object):
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
        'created_at': 'datetime',
        'description': 'str',
        'id': 'int',
        'moment': 'str',
        'occurrences': 'list[date]',
        'skip': 'int',
        'type': 'str',
        'updated_at': 'datetime',
        'weekend': 'int'
    }

    attribute_map = {
        'created_at': 'created_at',
        'description': 'description',
        'id': 'id',
        'moment': 'moment',
        'occurrences': 'occurrences',
        'skip': 'skip',
        'type': 'type',
        'updated_at': 'updated_at',
        'weekend': 'weekend'
    }

    def __init__(self, created_at=None, description=None, id=None, moment=None, occurrences=None, skip=None, type=None, updated_at=None, weekend=None):  # noqa: E501
        """RecurrenceRepetition - a model defined in OpenAPI"""  # noqa: E501

        self._created_at = None
        self._description = None
        self._id = None
        self._moment = None
        self._occurrences = None
        self._skip = None
        self._type = None
        self._updated_at = None
        self._weekend = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if moment is not None:
            self.moment = moment
        if occurrences is not None:
            self.occurrences = occurrences
        if skip is not None:
            self.skip = skip
        if type is not None:
            self.type = type
        if updated_at is not None:
            self.updated_at = updated_at
        if weekend is not None:
            self.weekend = weekend

    @property
    def created_at(self):
        """Gets the created_at of this RecurrenceRepetition.  # noqa: E501


        :return: The created_at of this RecurrenceRepetition.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this RecurrenceRepetition.


        :param created_at: The created_at of this RecurrenceRepetition.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def description(self):
        """Gets the description of this RecurrenceRepetition.  # noqa: E501

        Auto-generated repetition description.  # noqa: E501

        :return: The description of this RecurrenceRepetition.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RecurrenceRepetition.

        Auto-generated repetition description.  # noqa: E501

        :param description: The description of this RecurrenceRepetition.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this RecurrenceRepetition.  # noqa: E501


        :return: The id of this RecurrenceRepetition.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RecurrenceRepetition.


        :param id: The id of this RecurrenceRepetition.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def moment(self):
        """Gets the moment of this RecurrenceRepetition.  # noqa: E501

        Information that defined the type of repetition. - For 'daily', this is empty. - For 'weekly', it is day of the week between 1 and 7 (Monday - Sunday). - For 'ndom', it is '1,2' or '4,5' or something else, where the first number is the week in the month, and the second number is the day in the week (between 1 and 7). Effectively, this means: the 2nd Wednesday of the month - For 'monthly' it is the day of the month (1 - 31) - For yearly, it is a full date, ie '2018-09-17'. The year you use does not matter.   # noqa: E501

        :return: The moment of this RecurrenceRepetition.  # noqa: E501
        :rtype: str
        """
        return self._moment

    @moment.setter
    def moment(self, moment):
        """Sets the moment of this RecurrenceRepetition.

        Information that defined the type of repetition. - For 'daily', this is empty. - For 'weekly', it is day of the week between 1 and 7 (Monday - Sunday). - For 'ndom', it is '1,2' or '4,5' or something else, where the first number is the week in the month, and the second number is the day in the week (between 1 and 7). Effectively, this means: the 2nd Wednesday of the month - For 'monthly' it is the day of the month (1 - 31) - For yearly, it is a full date, ie '2018-09-17'. The year you use does not matter.   # noqa: E501

        :param moment: The moment of this RecurrenceRepetition.  # noqa: E501
        :type: str
        """

        self._moment = moment

    @property
    def occurrences(self):
        """Gets the occurrences of this RecurrenceRepetition.  # noqa: E501

        Array of future dates when the repetition will apply to. Auto generated.  # noqa: E501

        :return: The occurrences of this RecurrenceRepetition.  # noqa: E501
        :rtype: list[date]
        """
        return self._occurrences

    @occurrences.setter
    def occurrences(self, occurrences):
        """Sets the occurrences of this RecurrenceRepetition.

        Array of future dates when the repetition will apply to. Auto generated.  # noqa: E501

        :param occurrences: The occurrences of this RecurrenceRepetition.  # noqa: E501
        :type: list[date]
        """

        self._occurrences = occurrences

    @property
    def skip(self):
        """Gets the skip of this RecurrenceRepetition.  # noqa: E501

        How many occurrences to skip. 0 means skip nothing. 1 means every other.  # noqa: E501

        :return: The skip of this RecurrenceRepetition.  # noqa: E501
        :rtype: int
        """
        return self._skip

    @skip.setter
    def skip(self, skip):
        """Sets the skip of this RecurrenceRepetition.

        How many occurrences to skip. 0 means skip nothing. 1 means every other.  # noqa: E501

        :param skip: The skip of this RecurrenceRepetition.  # noqa: E501
        :type: int
        """

        self._skip = skip

    @property
    def type(self):
        """Gets the type of this RecurrenceRepetition.  # noqa: E501

        The type of the repetition. ndom means: the n-th weekday of the month, where you can also specify which day of the week.  # noqa: E501

        :return: The type of this RecurrenceRepetition.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RecurrenceRepetition.

        The type of the repetition. ndom means: the n-th weekday of the month, where you can also specify which day of the week.  # noqa: E501

        :param type: The type of this RecurrenceRepetition.  # noqa: E501
        :type: str
        """
        allowed_values = ["daily", "weekly", "ndom", "monthly", "yearly"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def updated_at(self):
        """Gets the updated_at of this RecurrenceRepetition.  # noqa: E501


        :return: The updated_at of this RecurrenceRepetition.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this RecurrenceRepetition.


        :param updated_at: The updated_at of this RecurrenceRepetition.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def weekend(self):
        """Gets the weekend of this RecurrenceRepetition.  # noqa: E501

        How to respond when the recurring transaction falls in the weekend. Possible values: 1. Do nothing, just create it 2. Create no transaction. 3. Skip to the previous Friday. 4. Skip to the next Monday.   # noqa: E501

        :return: The weekend of this RecurrenceRepetition.  # noqa: E501
        :rtype: int
        """
        return self._weekend

    @weekend.setter
    def weekend(self, weekend):
        """Sets the weekend of this RecurrenceRepetition.

        How to respond when the recurring transaction falls in the weekend. Possible values: 1. Do nothing, just create it 2. Create no transaction. 3. Skip to the previous Friday. 4. Skip to the next Monday.   # noqa: E501

        :param weekend: The weekend of this RecurrenceRepetition.  # noqa: E501
        :type: int
        """

        self._weekend = weekend

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
        if not isinstance(other, RecurrenceRepetition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
