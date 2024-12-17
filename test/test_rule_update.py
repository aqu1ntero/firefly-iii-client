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

from firefly_iii_client.models.rule_update import RuleUpdate

class TestRuleUpdate(unittest.TestCase):
    """RuleUpdate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RuleUpdate:
        """Test RuleUpdate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RuleUpdate`
        """
        model = RuleUpdate()
        if include_optional:
            return RuleUpdate(
                actions = [
                    firefly_iii_client.models.rule_action_update.RuleActionUpdate(
                        active = True, 
                        order = 5, 
                        stop_processing = False, 
                        type = 'set_category', 
                        value = 'Daily groceries', )
                    ],
                active = True,
                description = 'First rule description',
                order = 5,
                rule_group_id = '81',
                stop_processing = False,
                strict = True,
                title = 'First rule title.',
                trigger = 'store-journal',
                triggers = [
                    firefly_iii_client.models.rule_trigger_update.RuleTriggerUpdate(
                        active = True, 
                        order = 5, 
                        stop_processing = False, 
                        type = 'user_action', 
                        value = 'tag1', )
                    ]
            )
        else:
            return RuleUpdate(
        )
        """

    def testRuleUpdate(self):
        """Test RuleUpdate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
