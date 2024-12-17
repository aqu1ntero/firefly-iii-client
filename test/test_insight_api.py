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

from firefly_iii_client.api.insight_api import InsightApi


class TestInsightApi(unittest.TestCase):
    """InsightApi unit test stubs"""

    def setUp(self) -> None:
        self.api = InsightApi()

    def tearDown(self) -> None:
        pass

    def test_insight_expense_asset(self) -> None:
        """Test case for insight_expense_asset

        Insight into expenses, grouped by asset account.
        """
        pass

    def test_insight_expense_bill(self) -> None:
        """Test case for insight_expense_bill

        Insight into expenses, grouped by bill.
        """
        pass

    def test_insight_expense_budget(self) -> None:
        """Test case for insight_expense_budget

        Insight into expenses, grouped by budget.
        """
        pass

    def test_insight_expense_category(self) -> None:
        """Test case for insight_expense_category

        Insight into expenses, grouped by category.
        """
        pass

    def test_insight_expense_expense(self) -> None:
        """Test case for insight_expense_expense

        Insight into expenses, grouped by expense account.
        """
        pass

    def test_insight_expense_no_bill(self) -> None:
        """Test case for insight_expense_no_bill

        Insight into expenses, without bill.
        """
        pass

    def test_insight_expense_no_budget(self) -> None:
        """Test case for insight_expense_no_budget

        Insight into expenses, without budget.
        """
        pass

    def test_insight_expense_no_category(self) -> None:
        """Test case for insight_expense_no_category

        Insight into expenses, without category.
        """
        pass

    def test_insight_expense_no_tag(self) -> None:
        """Test case for insight_expense_no_tag

        Insight into expenses, without tag.
        """
        pass

    def test_insight_expense_tag(self) -> None:
        """Test case for insight_expense_tag

        Insight into expenses, grouped by tag.
        """
        pass

    def test_insight_expense_total(self) -> None:
        """Test case for insight_expense_total

        Insight into total expenses.
        """
        pass

    def test_insight_income_asset(self) -> None:
        """Test case for insight_income_asset

        Insight into income, grouped by asset account.
        """
        pass

    def test_insight_income_category(self) -> None:
        """Test case for insight_income_category

        Insight into income, grouped by category.
        """
        pass

    def test_insight_income_no_category(self) -> None:
        """Test case for insight_income_no_category

        Insight into income, without category.
        """
        pass

    def test_insight_income_no_tag(self) -> None:
        """Test case for insight_income_no_tag

        Insight into income, without tag.
        """
        pass

    def test_insight_income_revenue(self) -> None:
        """Test case for insight_income_revenue

        Insight into income, grouped by revenue account.
        """
        pass

    def test_insight_income_tag(self) -> None:
        """Test case for insight_income_tag

        Insight into income, grouped by tag.
        """
        pass

    def test_insight_income_total(self) -> None:
        """Test case for insight_income_total

        Insight into total income.
        """
        pass

    def test_insight_transfer_category(self) -> None:
        """Test case for insight_transfer_category

        Insight into transfers, grouped by category.
        """
        pass

    def test_insight_transfer_no_category(self) -> None:
        """Test case for insight_transfer_no_category

        Insight into transfers, without category.
        """
        pass

    def test_insight_transfer_no_tag(self) -> None:
        """Test case for insight_transfer_no_tag

        Insight into expenses, without tag.
        """
        pass

    def test_insight_transfer_tag(self) -> None:
        """Test case for insight_transfer_tag

        Insight into transfers, grouped by tag.
        """
        pass

    def test_insight_transfer_total(self) -> None:
        """Test case for insight_transfer_total

        Insight into total transfers.
        """
        pass

    def test_insight_transfers(self) -> None:
        """Test case for insight_transfers

        Insight into transfers, grouped by account.
        """
        pass


if __name__ == '__main__':
    unittest.main()
