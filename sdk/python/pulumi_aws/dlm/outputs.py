# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables

@pulumi.output_type
class LifecyclePolicyPolicyDetails(dict):
    resource_types: List[str] = pulumi.output_property("resourceTypes")
    """
    A list of resource types that should be targeted by the lifecycle policy. `VOLUME` is currently the only allowed value.
    """
    schedules: List['outputs.LifecyclePolicyPolicyDetailsSchedule'] = pulumi.output_property("schedules")
    """
    See the `schedule` configuration block.
    """
    target_tags: Dict[str, str] = pulumi.output_property("targetTags")
    """
    A map of tag keys and their values. Any resources that match the `resource_types` and are tagged with _any_ of these tags will be targeted.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class LifecyclePolicyPolicyDetailsSchedule(dict):
    copy_tags: Optional[bool] = pulumi.output_property("copyTags")
    """
    Copy all user-defined tags on a source volume to snapshots of the volume created by this policy.
    """
    create_rule: 'outputs.LifecyclePolicyPolicyDetailsScheduleCreateRule' = pulumi.output_property("createRule")
    """
    See the `create_rule` block. Max of 1 per schedule.
    """
    name: str = pulumi.output_property("name")
    """
    A name for the schedule.
    """
    retain_rule: 'outputs.LifecyclePolicyPolicyDetailsScheduleRetainRule' = pulumi.output_property("retainRule")
    """
    See the `retain_rule` block. Max of 1 per schedule.
    """
    tags_to_add: Optional[Dict[str, str]] = pulumi.output_property("tagsToAdd")
    """
    A map of tag keys and their values. DLM lifecycle policies will already tag the snapshot with the tags on the volume. This configuration adds extra tags on top of these.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class LifecyclePolicyPolicyDetailsScheduleCreateRule(dict):
    interval: float = pulumi.output_property("interval")
    """
    How often this lifecycle policy should be evaluated. `1`, `2`,`3`,`4`,`6`,`8`,`12` or `24` are valid values.
    """
    interval_unit: Optional[str] = pulumi.output_property("intervalUnit")
    """
    The unit for how often the lifecycle policy should be evaluated. `HOURS` is currently the only allowed value and also the default value.
    """
    times: Optional[str] = pulumi.output_property("times")
    """
    A list of times in 24 hour clock format that sets when the lifecycle policy should be evaluated. Max of 1.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class LifecyclePolicyPolicyDetailsScheduleRetainRule(dict):
    count: float = pulumi.output_property("count")
    """
    How many snapshots to keep. Must be an integer between 1 and 1000.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


