# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables

@pulumi.input_type
class VaultNotificationArgs:
    events: pulumi.Input[List[pulumi.Input[str]]] = pulumi.input_property("events")
    """
    You can configure a vault to publish a notification for `ArchiveRetrievalCompleted` and `InventoryRetrievalCompleted` events.
    """
    sns_topic: pulumi.Input[str] = pulumi.input_property("snsTopic")
    """
    The SNS Topic ARN.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, events: pulumi.Input[List[pulumi.Input[str]]], sns_topic: pulumi.Input[str]) -> None:
        """
        :param pulumi.Input[List[pulumi.Input[str]]] events: You can configure a vault to publish a notification for `ArchiveRetrievalCompleted` and `InventoryRetrievalCompleted` events.
        :param pulumi.Input[str] sns_topic: The SNS Topic ARN.
        """
        __self__.events = events
        __self__.sns_topic = sns_topic

