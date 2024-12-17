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

from firefly_iii_client.models.category_earned import CategoryEarned

class TestCategoryEarned(unittest.TestCase):
    """CategoryEarned unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CategoryEarned:
        """Test CategoryEarned
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CategoryEarned`
        """
        model = CategoryEarned()
        if include_optional:
            return CategoryEarned(
                currency_code = 'USD',
                currency_decimal_places = 2,
                currency_id = '5',
                currency_symbol = '$',
                sum = '123.45'
            )
        else:
            return CategoryEarned(
        )
        """

    def testCategoryEarned(self):
        """Test CategoryEarned"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
