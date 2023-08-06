# coding: utf-8

"""
    Firefly III API Client

    This is the Python client for Firefly III API  # noqa: E501

    The version of the OpenAPI document: 2.0.5
    Contact: james@firefly-iii.org
    Generated by: https://openapi-generator.tech
"""

from firefly_iii_client.paths.v1_about.get import GetAbout
from firefly_iii_client.paths.v1_cron_cli_token.get import GetCron
from firefly_iii_client.paths.v1_about_user.get import GetCurrentUser


class AboutApi(
    GetAbout,
    GetCron,
    GetCurrentUser,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
