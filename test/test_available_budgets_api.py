# coding: utf-8

"""
    Firefly III API Client

    This is the Python client for Firefly III API  # noqa: E501

    OpenAPI spec version: 0.9.0
    Contact: thegrumpydictator@gmail.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import firefly_iii_client
from firefly_iii_client.api.available_budgets_api import AvailableBudgetsApi  # noqa: E501
from firefly_iii_client.rest import ApiException


class TestAvailableBudgetsApi(unittest.TestCase):
    """AvailableBudgetsApi unit test stubs"""

    def setUp(self):
        self.api = firefly_iii_client.api.available_budgets_api.AvailableBudgetsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_available_budget(self):
        """Test case for delete_available_budget

        Delete an available budget.  # noqa: E501
        """
        pass

    def test_get_available_budget(self):
        """Test case for get_available_budget

        Get a single available budget.  # noqa: E501
        """
        pass

    def test_get_available_budgets(self):
        """Test case for get_available_budgets

        List all available budget amounts.  # noqa: E501
        """
        pass

    def test_store_available_budget(self):
        """Test case for store_available_budget

        Store a new available budget  # noqa: E501
        """
        pass

    def test_update_available_budget(self):
        """Test case for update_available_budget

        Update existing available budget, to change for example the date range of the amount or the amount itself.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()