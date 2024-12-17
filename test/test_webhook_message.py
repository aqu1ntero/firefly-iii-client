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

from firefly_iii_client.models.webhook_message import WebhookMessage

class TestWebhookMessage(unittest.TestCase):
    """WebhookMessage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookMessage:
        """Test WebhookMessage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookMessage`
        """
        model = WebhookMessage()
        if include_optional:
            return WebhookMessage(
                created_at = '2018-09-17T12:46:47+01:00',
                errored = False,
                message = '{some:message}',
                sent = False,
                updated_at = '2018-09-17T12:46:47+01:00',
                uuid = '7a344c02-5b52-46b1-90e6-a437431dcf07',
                webhook_id = '5'
            )
        else:
            return WebhookMessage(
        )
        """

    def testWebhookMessage(self):
        """Test WebhookMessage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
