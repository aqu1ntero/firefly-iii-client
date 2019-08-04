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


class PiggyBankAttributes(object):
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
        'account_id': 'int',
        'account_name': 'str',
        'active': 'bool',
        'created_at': 'datetime',
        'currency_code': 'str',
        'currency_decimal_places': 'int',
        'currency_id': 'int',
        'currency_symbol': 'str',
        'current_amount': 'float',
        'left_to_save': 'float',
        'name': 'str',
        'notes': 'str',
        'order': 'int',
        'percentage': 'float',
        'save_per_month': 'float',
        'start_date': 'date',
        'target_amount': 'float',
        'target_date': 'date',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'account_id': 'account_id',
        'account_name': 'account_name',
        'active': 'active',
        'created_at': 'created_at',
        'currency_code': 'currency_code',
        'currency_decimal_places': 'currency_decimal_places',
        'currency_id': 'currency_id',
        'currency_symbol': 'currency_symbol',
        'current_amount': 'current_amount',
        'left_to_save': 'left_to_save',
        'name': 'name',
        'notes': 'notes',
        'order': 'order',
        'percentage': 'percentage',
        'save_per_month': 'save_per_month',
        'start_date': 'start_date',
        'target_amount': 'target_amount',
        'target_date': 'target_date',
        'updated_at': 'updated_at'
    }

    def __init__(self, account_id=None, account_name=None, active=None, created_at=None, currency_code=None, currency_decimal_places=None, currency_id=None, currency_symbol=None, current_amount=None, left_to_save=None, name=None, notes=None, order=None, percentage=None, save_per_month=None, start_date=None, target_amount=None, target_date=None, updated_at=None):  # noqa: E501
        """PiggyBankAttributes - a model defined in OpenAPI"""  # noqa: E501

        self._account_id = None
        self._account_name = None
        self._active = None
        self._created_at = None
        self._currency_code = None
        self._currency_decimal_places = None
        self._currency_id = None
        self._currency_symbol = None
        self._current_amount = None
        self._left_to_save = None
        self._name = None
        self._notes = None
        self._order = None
        self._percentage = None
        self._save_per_month = None
        self._start_date = None
        self._target_amount = None
        self._target_date = None
        self._updated_at = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if account_name is not None:
            self.account_name = account_name
        if active is not None:
            self.active = active
        if created_at is not None:
            self.created_at = created_at
        if currency_code is not None:
            self.currency_code = currency_code
        if currency_decimal_places is not None:
            self.currency_decimal_places = currency_decimal_places
        if currency_id is not None:
            self.currency_id = currency_id
        if currency_symbol is not None:
            self.currency_symbol = currency_symbol
        if current_amount is not None:
            self.current_amount = current_amount
        if left_to_save is not None:
            self.left_to_save = left_to_save
        if name is not None:
            self.name = name
        if notes is not None:
            self.notes = notes
        if order is not None:
            self.order = order
        if percentage is not None:
            self.percentage = percentage
        if save_per_month is not None:
            self.save_per_month = save_per_month
        if start_date is not None:
            self.start_date = start_date
        if target_amount is not None:
            self.target_amount = target_amount
        if target_date is not None:
            self.target_date = target_date
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def account_id(self):
        """Gets the account_id of this PiggyBankAttributes.  # noqa: E501

        The ID of the asset account this piggy bank is connected to.  # noqa: E501

        :return: The account_id of this PiggyBankAttributes.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this PiggyBankAttributes.

        The ID of the asset account this piggy bank is connected to.  # noqa: E501

        :param account_id: The account_id of this PiggyBankAttributes.  # noqa: E501
        :type: int
        """

        self._account_id = account_id

    @property
    def account_name(self):
        """Gets the account_name of this PiggyBankAttributes.  # noqa: E501

        The name of the asset account this piggy bank is connected to.  # noqa: E501

        :return: The account_name of this PiggyBankAttributes.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this PiggyBankAttributes.

        The name of the asset account this piggy bank is connected to.  # noqa: E501

        :param account_name: The account_name of this PiggyBankAttributes.  # noqa: E501
        :type: str
        """

        self._account_name = account_name

    @property
    def active(self):
        """Gets the active of this PiggyBankAttributes.  # noqa: E501


        :return: The active of this PiggyBankAttributes.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this PiggyBankAttributes.


        :param active: The active of this PiggyBankAttributes.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def created_at(self):
        """Gets the created_at of this PiggyBankAttributes.  # noqa: E501


        :return: The created_at of this PiggyBankAttributes.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this PiggyBankAttributes.


        :param created_at: The created_at of this PiggyBankAttributes.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def currency_code(self):
        """Gets the currency_code of this PiggyBankAttributes.  # noqa: E501


        :return: The currency_code of this PiggyBankAttributes.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this PiggyBankAttributes.


        :param currency_code: The currency_code of this PiggyBankAttributes.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

    @property
    def currency_decimal_places(self):
        """Gets the currency_decimal_places of this PiggyBankAttributes.  # noqa: E501

        Number of decimals supported by the currency  # noqa: E501

        :return: The currency_decimal_places of this PiggyBankAttributes.  # noqa: E501
        :rtype: int
        """
        return self._currency_decimal_places

    @currency_decimal_places.setter
    def currency_decimal_places(self, currency_decimal_places):
        """Sets the currency_decimal_places of this PiggyBankAttributes.

        Number of decimals supported by the currency  # noqa: E501

        :param currency_decimal_places: The currency_decimal_places of this PiggyBankAttributes.  # noqa: E501
        :type: int
        """

        self._currency_decimal_places = currency_decimal_places

    @property
    def currency_id(self):
        """Gets the currency_id of this PiggyBankAttributes.  # noqa: E501


        :return: The currency_id of this PiggyBankAttributes.  # noqa: E501
        :rtype: int
        """
        return self._currency_id

    @currency_id.setter
    def currency_id(self, currency_id):
        """Sets the currency_id of this PiggyBankAttributes.


        :param currency_id: The currency_id of this PiggyBankAttributes.  # noqa: E501
        :type: int
        """

        self._currency_id = currency_id

    @property
    def currency_symbol(self):
        """Gets the currency_symbol of this PiggyBankAttributes.  # noqa: E501


        :return: The currency_symbol of this PiggyBankAttributes.  # noqa: E501
        :rtype: str
        """
        return self._currency_symbol

    @currency_symbol.setter
    def currency_symbol(self, currency_symbol):
        """Sets the currency_symbol of this PiggyBankAttributes.


        :param currency_symbol: The currency_symbol of this PiggyBankAttributes.  # noqa: E501
        :type: str
        """

        self._currency_symbol = currency_symbol

    @property
    def current_amount(self):
        """Gets the current_amount of this PiggyBankAttributes.  # noqa: E501


        :return: The current_amount of this PiggyBankAttributes.  # noqa: E501
        :rtype: float
        """
        return self._current_amount

    @current_amount.setter
    def current_amount(self, current_amount):
        """Sets the current_amount of this PiggyBankAttributes.


        :param current_amount: The current_amount of this PiggyBankAttributes.  # noqa: E501
        :type: float
        """

        self._current_amount = current_amount

    @property
    def left_to_save(self):
        """Gets the left_to_save of this PiggyBankAttributes.  # noqa: E501


        :return: The left_to_save of this PiggyBankAttributes.  # noqa: E501
        :rtype: float
        """
        return self._left_to_save

    @left_to_save.setter
    def left_to_save(self, left_to_save):
        """Sets the left_to_save of this PiggyBankAttributes.


        :param left_to_save: The left_to_save of this PiggyBankAttributes.  # noqa: E501
        :type: float
        """

        self._left_to_save = left_to_save

    @property
    def name(self):
        """Gets the name of this PiggyBankAttributes.  # noqa: E501


        :return: The name of this PiggyBankAttributes.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PiggyBankAttributes.


        :param name: The name of this PiggyBankAttributes.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def notes(self):
        """Gets the notes of this PiggyBankAttributes.  # noqa: E501


        :return: The notes of this PiggyBankAttributes.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this PiggyBankAttributes.


        :param notes: The notes of this PiggyBankAttributes.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def order(self):
        """Gets the order of this PiggyBankAttributes.  # noqa: E501


        :return: The order of this PiggyBankAttributes.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this PiggyBankAttributes.


        :param order: The order of this PiggyBankAttributes.  # noqa: E501
        :type: int
        """

        self._order = order

    @property
    def percentage(self):
        """Gets the percentage of this PiggyBankAttributes.  # noqa: E501


        :return: The percentage of this PiggyBankAttributes.  # noqa: E501
        :rtype: float
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this PiggyBankAttributes.


        :param percentage: The percentage of this PiggyBankAttributes.  # noqa: E501
        :type: float
        """

        self._percentage = percentage

    @property
    def save_per_month(self):
        """Gets the save_per_month of this PiggyBankAttributes.  # noqa: E501


        :return: The save_per_month of this PiggyBankAttributes.  # noqa: E501
        :rtype: float
        """
        return self._save_per_month

    @save_per_month.setter
    def save_per_month(self, save_per_month):
        """Sets the save_per_month of this PiggyBankAttributes.


        :param save_per_month: The save_per_month of this PiggyBankAttributes.  # noqa: E501
        :type: float
        """

        self._save_per_month = save_per_month

    @property
    def start_date(self):
        """Gets the start_date of this PiggyBankAttributes.  # noqa: E501

        The date you started with this piggy bank.  # noqa: E501

        :return: The start_date of this PiggyBankAttributes.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this PiggyBankAttributes.

        The date you started with this piggy bank.  # noqa: E501

        :param start_date: The start_date of this PiggyBankAttributes.  # noqa: E501
        :type: date
        """

        self._start_date = start_date

    @property
    def target_amount(self):
        """Gets the target_amount of this PiggyBankAttributes.  # noqa: E501


        :return: The target_amount of this PiggyBankAttributes.  # noqa: E501
        :rtype: float
        """
        return self._target_amount

    @target_amount.setter
    def target_amount(self, target_amount):
        """Sets the target_amount of this PiggyBankAttributes.


        :param target_amount: The target_amount of this PiggyBankAttributes.  # noqa: E501
        :type: float
        """

        self._target_amount = target_amount

    @property
    def target_date(self):
        """Gets the target_date of this PiggyBankAttributes.  # noqa: E501

        The date you intend to finish saving money.  # noqa: E501

        :return: The target_date of this PiggyBankAttributes.  # noqa: E501
        :rtype: date
        """
        return self._target_date

    @target_date.setter
    def target_date(self, target_date):
        """Sets the target_date of this PiggyBankAttributes.

        The date you intend to finish saving money.  # noqa: E501

        :param target_date: The target_date of this PiggyBankAttributes.  # noqa: E501
        :type: date
        """

        self._target_date = target_date

    @property
    def updated_at(self):
        """Gets the updated_at of this PiggyBankAttributes.  # noqa: E501


        :return: The updated_at of this PiggyBankAttributes.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this PiggyBankAttributes.


        :param updated_at: The updated_at of this PiggyBankAttributes.  # noqa: E501
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
        if not isinstance(other, PiggyBankAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
