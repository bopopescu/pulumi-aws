# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables


class GetOutpostsResult:
    """
    A collection of values returned by getOutposts.
    """
    # pylint: disable=no-self-argument
    def __init__(__self__, arns=None, availability_zone=None, availability_zone_id=None, id=None, ids=None, site_id=None) -> None:
        if arns and not isinstance(arns, list):
            raise TypeError("Expected argument 'arns' to be a list")
        __self__.arns = arns
        """
        Set of Amazon Resource Names (ARNs).
        """
        if availability_zone and not isinstance(availability_zone, str):
            raise TypeError("Expected argument 'availability_zone' to be a str")
        __self__.availability_zone = availability_zone
        if availability_zone_id and not isinstance(availability_zone_id, str):
            raise TypeError("Expected argument 'availability_zone_id' to be a str")
        __self__.availability_zone_id = availability_zone_id
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        __self__.ids = ids
        """
        Set of identifiers.
        """
        if site_id and not isinstance(site_id, str):
            raise TypeError("Expected argument 'site_id' to be a str")
        __self__.site_id = site_id


class AwaitableGetOutpostsResult(GetOutpostsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOutpostsResult(
            arns=self.arns,
            availability_zone=self.availability_zone,
            availability_zone_id=self.availability_zone_id,
            id=self.id,
            ids=self.ids,
            site_id=self.site_id)


def get_outposts(availability_zone=None, availability_zone_id=None, site_id=None, opts=None):
    """
    Provides details about multiple Outposts.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.outposts.get_outposts(site_id=data["aws_outposts_site"]["id"])
    ```


    :param str availability_zone: Availability Zone name.
    :param str availability_zone_id: Availability Zone identifier.
    :param str site_id: Site identifier.
    """
    __args__ = dict()
    __args__['availabilityZone'] = availability_zone
    __args__['availabilityZoneId'] = availability_zone_id
    __args__['siteId'] = site_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:outposts/getOutposts:getOutposts', __args__, opts=opts).value

    return AwaitableGetOutpostsResult(
        arns=__ret__.get('arns'),
        availability_zone=__ret__.get('availabilityZone'),
        availability_zone_id=__ret__.get('availabilityZoneId'),
        id=__ret__.get('id'),
        ids=__ret__.get('ids'),
        site_id=__ret__.get('siteId'))
