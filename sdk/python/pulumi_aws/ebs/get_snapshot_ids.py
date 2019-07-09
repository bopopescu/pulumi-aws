# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class GetSnapshotIdsResult:
    """
    A collection of values returned by getSnapshotIds.
    """
    def __init__(__self__, filters=None, ids=None, owners=None, restorable_by_user_ids=None, id=None):
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        __self__.filters = filters
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        __self__.ids = ids
        if owners and not isinstance(owners, list):
            raise TypeError("Expected argument 'owners' to be a list")
        __self__.owners = owners
        if restorable_by_user_ids and not isinstance(restorable_by_user_ids, list):
            raise TypeError("Expected argument 'restorable_by_user_ids' to be a list")
        __self__.restorable_by_user_ids = restorable_by_user_ids
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

async def get_snapshot_ids(filters=None,owners=None,restorable_by_user_ids=None,opts=None):
    """
    Use this data source to get a list of EBS Snapshot IDs matching the specified
    criteria.

    > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/ebs_snapshot_ids.html.markdown.
    """
    __args__ = dict()

    __args__['filters'] = filters
    __args__['owners'] = owners
    __args__['restorableByUserIds'] = restorable_by_user_ids
    __ret__ = await pulumi.runtime.invoke('aws:ebs/getSnapshotIds:getSnapshotIds', __args__, opts=opts)

    return GetSnapshotIdsResult(
        filters=__ret__.get('filters'),
        ids=__ret__.get('ids'),
        owners=__ret__.get('owners'),
        restorable_by_user_ids=__ret__.get('restorableByUserIds'),
        id=__ret__.get('id'))
