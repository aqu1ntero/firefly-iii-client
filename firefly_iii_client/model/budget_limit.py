"""
    Firefly III API Client

    This is the Python client for Firefly III API  # noqa: E501

    The version of the OpenAPI document: 1.5.2
    Contact: james@firefly-iii.org
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from firefly_iii_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from firefly_iii_client.exceptions import ApiAttributeError



class BudgetLimit(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'amount': (str,),  # noqa: E501
            'budget_id': (str,),  # noqa: E501
            'end': (datetime,),  # noqa: E501
            'start': (datetime,),  # noqa: E501
            'created_at': (datetime,),  # noqa: E501
            'currency_code': (str,),  # noqa: E501
            'currency_decimal_places': (int,),  # noqa: E501
            'currency_id': (str,),  # noqa: E501
            'currency_symbol': (str,),  # noqa: E501
            'period': (str, none_type,),  # noqa: E501
            'spent': (str, none_type,),  # noqa: E501
            'updated_at': (datetime,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'amount': 'amount',  # noqa: E501
        'budget_id': 'budget_id',  # noqa: E501
        'end': 'end',  # noqa: E501
        'start': 'start',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
        'currency_code': 'currency_code',  # noqa: E501
        'currency_decimal_places': 'currency_decimal_places',  # noqa: E501
        'currency_id': 'currency_id',  # noqa: E501
        'currency_symbol': 'currency_symbol',  # noqa: E501
        'period': 'period',  # noqa: E501
        'spent': 'spent',  # noqa: E501
        'updated_at': 'updated_at',  # noqa: E501
    }

    read_only_vars = {
        'budget_id',  # noqa: E501
        'created_at',  # noqa: E501
        'currency_decimal_places',  # noqa: E501
        'currency_symbol',  # noqa: E501
        'period',  # noqa: E501
        'spent',  # noqa: E501
        'updated_at',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, amount, budget_id, end, start, *args, **kwargs):  # noqa: E501
        """BudgetLimit - a model defined in OpenAPI

        Args:
            amount (str):
            budget_id (str): The budget ID of the associated budget.
            end (datetime): End date of the budget limit.
            start (datetime): Start date of the budget limit.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            created_at (datetime): [optional]  # noqa: E501
            currency_code (str): Use either currency_id or currency_code. Defaults to the user's default currency.. [optional]  # noqa: E501
            currency_decimal_places (int): [optional]  # noqa: E501
            currency_id (str): Use either currency_id or currency_code. Defaults to the user's default currency.. [optional]  # noqa: E501
            currency_symbol (str): [optional]  # noqa: E501
            period (str, none_type): Period of the budget limit. Only used when auto-generated by auto-budget.. [optional]  # noqa: E501
            spent (str, none_type): [optional]  # noqa: E501
            updated_at (datetime): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.amount = amount
        self.budget_id = budget_id
        self.end = end
        self.start = start
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, amount, end, start, *args, **kwargs):  # noqa: E501
        """BudgetLimit - a model defined in OpenAPI

        Args:
            amount (str):
            end (datetime): End date of the budget limit.
            start (datetime): Start date of the budget limit.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            created_at (datetime): [optional]  # noqa: E501
            currency_code (str): Use either currency_id or currency_code. Defaults to the user's default currency.. [optional]  # noqa: E501
            currency_decimal_places (int): [optional]  # noqa: E501
            currency_id (str): Use either currency_id or currency_code. Defaults to the user's default currency.. [optional]  # noqa: E501
            currency_symbol (str): [optional]  # noqa: E501
            period (str, none_type): Period of the budget limit. Only used when auto-generated by auto-budget.. [optional]  # noqa: E501
            spent (str, none_type): [optional]  # noqa: E501
            updated_at (datetime): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.amount = amount
        self.end = end
        self.start = start
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
