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

from firefly_iii_client.models.insight_transfer_entry import InsightTransferEntry

class TestInsightTransferEntry(unittest.TestCase):
    """InsightTransferEntry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InsightTransferEntry:
        """Test InsightTransferEntry
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InsightTransferEntry`
        """
        model = InsightTransferEntry()
        if include_optional:
            return InsightTransferEntry(
                currency_code = 'EUR',
                currency_id = '5',
                difference = '-123.45',
                difference_float = -123.45,
                id = '123',
                var_in = '123.45',
                in_float = 123.45,
                name = 'Land lord',
                out = '123.45',
                out_float = 123.45
            )
        else:
            return InsightTransferEntry(
        )
        """

    def testInsightTransferEntry(self):
        """Test InsightTransferEntry"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
