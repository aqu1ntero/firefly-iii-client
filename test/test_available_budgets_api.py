# coding: utf-8

"""
    Firefly III API Client

    This is the Python client for Firefly III API

    The version of the OpenAPI document: 6.1.24
    Contact: james@firefly-iii.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from firefly_iii_client.api.available_budgets_api import AvailableBudgetsApi


class TestAvailableBudgetsApi(unittest.TestCase):
    """AvailableBudgetsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AvailableBudgetsApi()

    def tearDown(self) -> None:
        pass

    def test_get_available_budget(self) -> None:
        """Test case for get_available_budget

        Get a single available budget.
        """
        pass

    def test_list_available_budget(self) -> None:
        """Test case for list_available_budget

        List all available budget amounts.
        """
        pass


if __name__ == '__main__':
    unittest.main()
