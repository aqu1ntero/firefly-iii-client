# coding: utf-8

"""
    Firefly III API Client

    This is the Python client for Firefly III API

    The version of the OpenAPI document: 2.0.12
    Contact: james@firefly-iii.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from firefly_iii_client.api.object_groups_api import ObjectGroupsApi


class TestObjectGroupsApi(unittest.TestCase):
    """ObjectGroupsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ObjectGroupsApi()

    def tearDown(self) -> None:
        pass

    def test_delete_object_group(self) -> None:
        """Test case for delete_object_group

        Delete a object group.
        """
        pass

    def test_get_object_group(self) -> None:
        """Test case for get_object_group

        Get a single object group.
        """
        pass

    def test_list_bill_by_object_group(self) -> None:
        """Test case for list_bill_by_object_group

        List all bills with this object group.
        """
        pass

    def test_list_object_groups(self) -> None:
        """Test case for list_object_groups

        List all oject groups.
        """
        pass

    def test_list_piggy_bank_by_object_group(self) -> None:
        """Test case for list_piggy_bank_by_object_group

        List all piggy banks related to the object group.
        """
        pass

    def test_update_object_group(self) -> None:
        """Test case for update_object_group

        Update existing object group.
        """
        pass


if __name__ == '__main__':
    unittest.main()