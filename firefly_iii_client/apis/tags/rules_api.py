# coding: utf-8

"""
    Firefly III API Client

    This is the Python client for Firefly III API  # noqa: E501

    The version of the OpenAPI document: 2.0.5
    Contact: james@firefly-iii.org
    Generated by: https://openapi-generator.tech
"""

from firefly_iii_client.paths.v1_rules_id.delete import DeleteRule
from firefly_iii_client.paths.v1_rules_id_trigger.post import FireRule
from firefly_iii_client.paths.v1_rules_id.get import GetRule
from firefly_iii_client.paths.v1_rules.get import ListRule
from firefly_iii_client.paths.v1_rules.post import StoreRule
from firefly_iii_client.paths.v1_rules_id_test.get import TestRule
from firefly_iii_client.paths.v1_rules_id.put import UpdateRule


class RulesApi(
    DeleteRule,
    FireRule,
    GetRule,
    ListRule,
    StoreRule,
    TestRule,
    UpdateRule,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
