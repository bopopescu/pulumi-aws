# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class GetParameterResult:
    """
    A collection of values returned by getParameter.
    """
    def __init__(__self__, arn=None, name=None, type=None, value=None, version=None, with_decryption=None, id=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        __self__.arn = arn
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        __self__.type = type
        if value and not isinstance(value, str):
            raise TypeError("Expected argument 'value' to be a str")
        __self__.value = value
        if version and not isinstance(version, float):
            raise TypeError("Expected argument 'version' to be a float")
        __self__.version = version
        if with_decryption and not isinstance(with_decryption, bool):
            raise TypeError("Expected argument 'with_decryption' to be a bool")
        __self__.with_decryption = with_decryption
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

async def get_parameter(name=None,with_decryption=None,opts=None):
    """
    Provides an SSM Parameter data source.

    > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/ssm_parameter.html.markdown.
    """
    __args__ = dict()

    __args__['name'] = name
    __args__['withDecryption'] = with_decryption
    __ret__ = await pulumi.runtime.invoke('aws:ssm/getParameter:getParameter', __args__, opts=opts)

    return GetParameterResult(
        arn=__ret__.get('arn'),
        name=__ret__.get('name'),
        type=__ret__.get('type'),
        value=__ret__.get('value'),
        version=__ret__.get('version'),
        with_decryption=__ret__.get('withDecryption'),
        id=__ret__.get('id'))
