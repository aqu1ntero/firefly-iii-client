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

from firefly_iii_client.models.webhook_attempt import WebhookAttempt

class TestWebhookAttempt(unittest.TestCase):
    """WebhookAttempt unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookAttempt:
        """Test WebhookAttempt
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookAttempt`
        """
        model = WebhookAttempt()
        if include_optional:
            return WebhookAttempt(
                created_at = '2018-09-17T12:46:47+01:00',
                logs = 'Page not found',
                response = 'Page not found',
                status_code = 404,
                updated_at = '2018-09-17T12:46:47+01:00',
                webhook_message_id = '5'
            )
        else:
            return WebhookAttempt(
        )
        """

    def testWebhookAttempt(self):
        """Test WebhookAttempt"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
