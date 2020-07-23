# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables


class GetEventCategoriesResult:
    """
    A collection of values returned by getEventCategories.
    """
    # pylint: disable=no-self-argument
    def __init__(__self__, event_categories=None, id=None, source_type=None) -> None:
        if event_categories and not isinstance(event_categories, list):
            raise TypeError("Expected argument 'event_categories' to be a list")
        __self__.event_categories = event_categories
        """
        A list of the event categories.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if source_type and not isinstance(source_type, str):
            raise TypeError("Expected argument 'source_type' to be a str")
        __self__.source_type = source_type


class AwaitableGetEventCategoriesResult(GetEventCategoriesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEventCategoriesResult(
            event_categories=self.event_categories,
            id=self.id,
            source_type=self.source_type)


def get_event_categories(source_type=None, opts=None):
    """
    ## Example Usage

    List the event categories of all the RDS resources.

    ```python
    import pulumi
    import pulumi_aws as aws

    example_event_categories = aws.rds.get_event_categories()
    pulumi.export("example", example_event_categories.event_categories)
    ```

    List the event categories specific to the RDS resource `db-snapshot`.

    ```python
    import pulumi
    import pulumi_aws as aws

    example_event_categories = aws.rds.get_event_categories(source_type="db-snapshot")
    pulumi.export("example", example_event_categories.event_categories)
    ```


    :param str source_type: The type of source that will be generating the events. Valid options are db-instance, db-security-group, db-parameter-group, db-snapshot, db-cluster or db-cluster-snapshot.
    """
    __args__ = dict()
    __args__['sourceType'] = source_type
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:rds/getEventCategories:getEventCategories', __args__, opts=opts).value

    return AwaitableGetEventCategoriesResult(
        event_categories=__ret__.get('eventCategories'),
        id=__ret__.get('id'),
        source_type=__ret__.get('sourceType'))
