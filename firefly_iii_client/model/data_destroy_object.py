# coding: utf-8

"""
    Firefly III API Client

    This is the Python client for Firefly III API  # noqa: E501

    The version of the OpenAPI document: 2.0.5
    Contact: james@firefly-iii.org
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from firefly_iii_client import schemas  # noqa: F401


class DataDestroyObject(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        enum_value_to_name = {
            "not_assets_liabilities": "NOT_ASSETS_LIABILITIES",
            "budgets": "BUDGETS",
            "bills": "BILLS",
            "piggy_banks": "PIGGY_BANKS",
            "rules": "RULES",
            "recurring": "RECURRING",
            "categories": "CATEGORIES",
            "tags": "TAGS",
            "object_groups": "OBJECT_GROUPS",
            "accounts": "ACCOUNTS",
            "asset_accounts": "ASSET_ACCOUNTS",
            "expense_accounts": "EXPENSE_ACCOUNTS",
            "revenue_accounts": "REVENUE_ACCOUNTS",
            "liabilities": "LIABILITIES",
            "transactions": "TRANSACTIONS",
            "withdrawals": "WITHDRAWALS",
            "deposits": "DEPOSITS",
            "transfers": "TRANSFERS",
        }
    
    @schemas.classproperty
    def NOT_ASSETS_LIABILITIES(cls):
        return cls("not_assets_liabilities")
    
    @schemas.classproperty
    def BUDGETS(cls):
        return cls("budgets")
    
    @schemas.classproperty
    def BILLS(cls):
        return cls("bills")
    
    @schemas.classproperty
    def PIGGY_BANKS(cls):
        return cls("piggy_banks")
    
    @schemas.classproperty
    def RULES(cls):
        return cls("rules")
    
    @schemas.classproperty
    def RECURRING(cls):
        return cls("recurring")
    
    @schemas.classproperty
    def CATEGORIES(cls):
        return cls("categories")
    
    @schemas.classproperty
    def TAGS(cls):
        return cls("tags")
    
    @schemas.classproperty
    def OBJECT_GROUPS(cls):
        return cls("object_groups")
    
    @schemas.classproperty
    def ACCOUNTS(cls):
        return cls("accounts")
    
    @schemas.classproperty
    def ASSET_ACCOUNTS(cls):
        return cls("asset_accounts")
    
    @schemas.classproperty
    def EXPENSE_ACCOUNTS(cls):
        return cls("expense_accounts")
    
    @schemas.classproperty
    def REVENUE_ACCOUNTS(cls):
        return cls("revenue_accounts")
    
    @schemas.classproperty
    def LIABILITIES(cls):
        return cls("liabilities")
    
    @schemas.classproperty
    def TRANSACTIONS(cls):
        return cls("transactions")
    
    @schemas.classproperty
    def WITHDRAWALS(cls):
        return cls("withdrawals")
    
    @schemas.classproperty
    def DEPOSITS(cls):
        return cls("deposits")
    
    @schemas.classproperty
    def TRANSFERS(cls):
        return cls("transfers")
