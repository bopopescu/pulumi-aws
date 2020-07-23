# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables

@pulumi.input_type
class PlanRuleArgs:
    rule_name: pulumi.Input[str] = pulumi.input_property("ruleName")
    """
    An display name for a backup rule.
    """
    target_vault_name: pulumi.Input[str] = pulumi.input_property("targetVaultName")
    """
    The name of a logical container where backups are stored.
    """
    completion_window: Optional[pulumi.Input[float]] = pulumi.input_property("completionWindow")
    """
    The amount of time AWS Backup attempts a backup before canceling the job and returning an error.
    """
    copy_actions: Optional[pulumi.Input[List[pulumi.Input['PlanRuleCopyActionArgs']]]] = pulumi.input_property("copyActions")
    """
    Configuration block(s) with copy operation settings. Detailed below.
    """
    lifecycle: Optional[pulumi.Input['PlanRuleLifecycleArgs']] = pulumi.input_property("lifecycle")
    """
    The lifecycle defines when a protected resource is copied over to a backup vault and when it expires.  Fields documented above.
    """
    recovery_point_tags: Optional[pulumi.Input[Dict[str, pulumi.Input[str]]]] = pulumi.input_property("recoveryPointTags")
    """
    Metadata that you can assign to help organize the resources that you create.
    """
    schedule: Optional[pulumi.Input[str]] = pulumi.input_property("schedule")
    """
    A CRON expression specifying when AWS Backup initiates a backup job.
    """
    start_window: Optional[pulumi.Input[float]] = pulumi.input_property("startWindow")
    """
    The amount of time in minutes before beginning a backup.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, rule_name: pulumi.Input[str], target_vault_name: pulumi.Input[str], completion_window: Optional[pulumi.Input[float]] = None, copy_actions: Optional[pulumi.Input[List[pulumi.Input['PlanRuleCopyActionArgs']]]] = None, lifecycle: Optional[pulumi.Input['PlanRuleLifecycleArgs']] = None, recovery_point_tags: Optional[pulumi.Input[Dict[str, pulumi.Input[str]]]] = None, schedule: Optional[pulumi.Input[str]] = None, start_window: Optional[pulumi.Input[float]] = None) -> None:
        """
        :param pulumi.Input[str] rule_name: An display name for a backup rule.
        :param pulumi.Input[str] target_vault_name: The name of a logical container where backups are stored.
        :param pulumi.Input[float] completion_window: The amount of time AWS Backup attempts a backup before canceling the job and returning an error.
        :param pulumi.Input[List[pulumi.Input['PlanRuleCopyActionArgs']]] copy_actions: Configuration block(s) with copy operation settings. Detailed below.
        :param pulumi.Input['PlanRuleLifecycleArgs'] lifecycle: The lifecycle defines when a protected resource is copied over to a backup vault and when it expires.  Fields documented above.
        :param pulumi.Input[Dict[str, pulumi.Input[str]]] recovery_point_tags: Metadata that you can assign to help organize the resources that you create.
        :param pulumi.Input[str] schedule: A CRON expression specifying when AWS Backup initiates a backup job.
        :param pulumi.Input[float] start_window: The amount of time in minutes before beginning a backup.
        """
        __self__.rule_name = rule_name
        __self__.target_vault_name = target_vault_name
        __self__.completion_window = completion_window
        __self__.copy_actions = copy_actions
        __self__.lifecycle = lifecycle
        __self__.recovery_point_tags = recovery_point_tags
        __self__.schedule = schedule
        __self__.start_window = start_window

@pulumi.input_type
class PlanRuleCopyActionArgs:
    destination_vault_arn: pulumi.Input[str] = pulumi.input_property("destinationVaultArn")
    """
    An Amazon Resource Name (ARN) that uniquely identifies the destination backup vault for the copied backup.
    """
    lifecycle: Optional[pulumi.Input['PlanRuleCopyActionLifecycleArgs']] = pulumi.input_property("lifecycle")
    """
    The lifecycle defines when a protected resource is copied over to a backup vault and when it expires.  Fields documented above.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, destination_vault_arn: pulumi.Input[str], lifecycle: Optional[pulumi.Input['PlanRuleCopyActionLifecycleArgs']] = None) -> None:
        """
        :param pulumi.Input[str] destination_vault_arn: An Amazon Resource Name (ARN) that uniquely identifies the destination backup vault for the copied backup.
        :param pulumi.Input['PlanRuleCopyActionLifecycleArgs'] lifecycle: The lifecycle defines when a protected resource is copied over to a backup vault and when it expires.  Fields documented above.
        """
        __self__.destination_vault_arn = destination_vault_arn
        __self__.lifecycle = lifecycle

@pulumi.input_type
class PlanRuleCopyActionLifecycleArgs:
    cold_storage_after: Optional[pulumi.Input[float]] = pulumi.input_property("coldStorageAfter")
    """
    Specifies the number of days after creation that a recovery point is moved to cold storage.
    """
    delete_after: Optional[pulumi.Input[float]] = pulumi.input_property("deleteAfter")
    """
    Specifies the number of days after creation that a recovery point is deleted. Must be 90 days greater than `cold_storage_after`.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, cold_storage_after: Optional[pulumi.Input[float]] = None, delete_after: Optional[pulumi.Input[float]] = None) -> None:
        """
        :param pulumi.Input[float] cold_storage_after: Specifies the number of days after creation that a recovery point is moved to cold storage.
        :param pulumi.Input[float] delete_after: Specifies the number of days after creation that a recovery point is deleted. Must be 90 days greater than `cold_storage_after`.
        """
        __self__.cold_storage_after = cold_storage_after
        __self__.delete_after = delete_after

@pulumi.input_type
class PlanRuleLifecycleArgs:
    cold_storage_after: Optional[pulumi.Input[float]] = pulumi.input_property("coldStorageAfter")
    """
    Specifies the number of days after creation that a recovery point is moved to cold storage.
    """
    delete_after: Optional[pulumi.Input[float]] = pulumi.input_property("deleteAfter")
    """
    Specifies the number of days after creation that a recovery point is deleted. Must be 90 days greater than `cold_storage_after`.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, cold_storage_after: Optional[pulumi.Input[float]] = None, delete_after: Optional[pulumi.Input[float]] = None) -> None:
        """
        :param pulumi.Input[float] cold_storage_after: Specifies the number of days after creation that a recovery point is moved to cold storage.
        :param pulumi.Input[float] delete_after: Specifies the number of days after creation that a recovery point is deleted. Must be 90 days greater than `cold_storage_after`.
        """
        __self__.cold_storage_after = cold_storage_after
        __self__.delete_after = delete_after

@pulumi.input_type
class SelectionSelectionTagArgs:
    key: pulumi.Input[str] = pulumi.input_property("key")
    """
    The key in a key-value pair.
    """
    type: pulumi.Input[str] = pulumi.input_property("type")
    """
    An operation, such as `StringEquals`, that is applied to a key-value pair used to filter resources in a selection.
    """
    value: pulumi.Input[str] = pulumi.input_property("value")
    """
    The value in a key-value pair.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, key: pulumi.Input[str], type: pulumi.Input[str], value: pulumi.Input[str]) -> None:
        """
        :param pulumi.Input[str] key: The key in a key-value pair.
        :param pulumi.Input[str] type: An operation, such as `StringEquals`, that is applied to a key-value pair used to filter resources in a selection.
        :param pulumi.Input[str] value: The value in a key-value pair.
        """
        __self__.key = key
        __self__.type = type
        __self__.value = value

