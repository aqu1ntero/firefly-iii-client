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


class TagAttributes(object):
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
        'date': 'date',
        'description': 'str',
        'latitude': 'str',
        'longitude': 'str',
        'tag': 'str',
        'updated_at': 'datetime',
        'zoom_level': 'str'
    }

    attribute_map = {
        'created_at': 'created_at',
        'date': 'date',
        'description': 'description',
        'latitude': 'latitude',
        'longitude': 'longitude',
        'tag': 'tag',
        'updated_at': 'updated_at',
        'zoom_level': 'zoom_level'
    }

    def __init__(self, created_at=None, date=None, description=None, latitude=None, longitude=None, tag=None, updated_at=None, zoom_level=None):  # noqa: E501
        """TagAttributes - a model defined in OpenAPI"""  # noqa: E501

        self._created_at = None
        self._date = None
        self._description = None
        self._latitude = None
        self._longitude = None
        self._tag = None
        self._updated_at = None
        self._zoom_level = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        self.date = date
        if description is not None:
            self.description = description
        self.latitude = latitude
        self.longitude = longitude
        if tag is not None:
            self.tag = tag
        if updated_at is not None:
            self.updated_at = updated_at
        self.zoom_level = zoom_level

    @property
    def created_at(self):
        """Gets the created_at of this TagAttributes.  # noqa: E501


        :return: The created_at of this TagAttributes.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this TagAttributes.


        :param created_at: The created_at of this TagAttributes.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def date(self):
        """Gets the date of this TagAttributes.  # noqa: E501

        The date to which the tag is applicable.  # noqa: E501

        :return: The date of this TagAttributes.  # noqa: E501
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this TagAttributes.

        The date to which the tag is applicable.  # noqa: E501

        :param date: The date of this TagAttributes.  # noqa: E501
        :type: date
        """

        self._date = date

    @property
    def description(self):
        """Gets the description of this TagAttributes.  # noqa: E501


        :return: The description of this TagAttributes.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TagAttributes.


        :param description: The description of this TagAttributes.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def latitude(self):
        """Gets the latitude of this TagAttributes.  # noqa: E501

        Latitude of the tag's location, if applicable. Can be used to draw a map.  # noqa: E501

        :return: The latitude of this TagAttributes.  # noqa: E501
        :rtype: str
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this TagAttributes.

        Latitude of the tag's location, if applicable. Can be used to draw a map.  # noqa: E501

        :param latitude: The latitude of this TagAttributes.  # noqa: E501
        :type: str
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this TagAttributes.  # noqa: E501

        Latitude of the tag's location, if applicable. Can be used to draw a map.  # noqa: E501

        :return: The longitude of this TagAttributes.  # noqa: E501
        :rtype: str
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this TagAttributes.

        Latitude of the tag's location, if applicable. Can be used to draw a map.  # noqa: E501

        :param longitude: The longitude of this TagAttributes.  # noqa: E501
        :type: str
        """

        self._longitude = longitude

    @property
    def tag(self):
        """Gets the tag of this TagAttributes.  # noqa: E501

        The tag  # noqa: E501

        :return: The tag of this TagAttributes.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this TagAttributes.

        The tag  # noqa: E501

        :param tag: The tag of this TagAttributes.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def updated_at(self):
        """Gets the updated_at of this TagAttributes.  # noqa: E501


        :return: The updated_at of this TagAttributes.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this TagAttributes.


        :param updated_at: The updated_at of this TagAttributes.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def zoom_level(self):
        """Gets the zoom_level of this TagAttributes.  # noqa: E501

        Zoom level for the map, if drawn. This to set the box right. Unfortunately this is a proprietary value because each map provider has different zoom levels.  # noqa: E501

        :return: The zoom_level of this TagAttributes.  # noqa: E501
        :rtype: str
        """
        return self._zoom_level

    @zoom_level.setter
    def zoom_level(self, zoom_level):
        """Sets the zoom_level of this TagAttributes.

        Zoom level for the map, if drawn. This to set the box right. Unfortunately this is a proprietary value because each map provider has different zoom levels.  # noqa: E501

        :param zoom_level: The zoom_level of this TagAttributes.  # noqa: E501
        :type: str
        """

        self._zoom_level = zoom_level

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
        if not isinstance(other, TagAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
