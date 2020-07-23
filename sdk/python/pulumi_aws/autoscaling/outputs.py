# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables

@pulumi.output_type
class GroupInitialLifecycleHook(dict):
    default_result: Optional[str] = pulumi.output_property("defaultResult")
    heartbeat_timeout: Optional[float] = pulumi.output_property("heartbeatTimeout")
    lifecycle_transition: str = pulumi.output_property("lifecycleTransition")
    name: str = pulumi.output_property("name")
    """
    The name of the auto scaling group. By default generated by this provider.
    """
    notification_metadata: Optional[str] = pulumi.output_property("notificationMetadata")
    notification_target_arn: Optional[str] = pulumi.output_property("notificationTargetArn")
    role_arn: Optional[str] = pulumi.output_property("roleArn")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GroupLaunchTemplate(dict):
    id: Optional[str] = pulumi.output_property("id")
    """
    The ID of the launch template. Conflicts with `name`.
    """
    name: Optional[str] = pulumi.output_property("name")
    """
    The name of the auto scaling group. By default generated by this provider.
    """
    version: Optional[str] = pulumi.output_property("version")
    """
    Template version. Can be version number, `$Latest`, or `$Default`. (Default: `$Default`).
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GroupMixedInstancesPolicy(dict):
    instances_distribution: Optional['outputs.GroupMixedInstancesPolicyInstancesDistribution'] = pulumi.output_property("instancesDistribution")
    """
    Nested argument containing settings on how to mix on-demand and Spot instances in the Auto Scaling group. Defined below.
    """
    launch_template: 'outputs.GroupMixedInstancesPolicyLaunchTemplate' = pulumi.output_property("launchTemplate")
    """
    Nested argument containing launch template settings along with the overrides to specify multiple instance types and weights. Defined below.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GroupMixedInstancesPolicyInstancesDistribution(dict):
    on_demand_allocation_strategy: Optional[str] = pulumi.output_property("onDemandAllocationStrategy")
    """
    Strategy to use when launching on-demand instances. Valid values: `prioritized`. Default: `prioritized`.
    """
    on_demand_base_capacity: Optional[float] = pulumi.output_property("onDemandBaseCapacity")
    """
    Absolute minimum amount of desired capacity that must be fulfilled by on-demand instances. Default: `0`.
    """
    on_demand_percentage_above_base_capacity: Optional[float] = pulumi.output_property("onDemandPercentageAboveBaseCapacity")
    """
    Percentage split between on-demand and Spot instances above the base on-demand capacity. Default: `100`.
    """
    spot_allocation_strategy: Optional[str] = pulumi.output_property("spotAllocationStrategy")
    """
    How to allocate capacity across the Spot pools. Valid values: `lowest-price`, `capacity-optimized`. Default: `lowest-price`.
    """
    spot_instance_pools: Optional[float] = pulumi.output_property("spotInstancePools")
    """
    Number of Spot pools per availability zone to allocate capacity. EC2 Auto Scaling selects the cheapest Spot pools and evenly allocates Spot capacity across the number of Spot pools that you specify. Default: `2`.
    """
    spot_max_price: Optional[str] = pulumi.output_property("spotMaxPrice")
    """
    Maximum price per unit hour that the user is willing to pay for the Spot instances. Default: an empty string which means the on-demand price.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GroupMixedInstancesPolicyLaunchTemplate(dict):
    launch_template_specification: 'outputs.GroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification' = pulumi.output_property("launchTemplateSpecification")
    """
    Nested argument defines the Launch Template. Defined below.
    """
    overrides: Optional[List['outputs.GroupMixedInstancesPolicyLaunchTemplateOverride']] = pulumi.output_property("overrides")
    """
    List of nested arguments provides the ability to specify multiple instance types. This will override the same parameter in the launch template. For on-demand instances, Auto Scaling considers the order of preference of instance types to launch based on the order specified in the overrides list. Defined below.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification(dict):
    launch_template_id: Optional[str] = pulumi.output_property("launchTemplateId")
    """
    The ID of the launch template. Conflicts with `launch_template_name`.
    """
    launch_template_name: Optional[str] = pulumi.output_property("launchTemplateName")
    """
    The name of the launch template. Conflicts with `launch_template_id`.
    """
    version: Optional[str] = pulumi.output_property("version")
    """
    Template version. Can be version number, `$Latest`, or `$Default`. (Default: `$Default`).
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GroupMixedInstancesPolicyLaunchTemplateOverride(dict):
    instance_type: Optional[str] = pulumi.output_property("instanceType")
    """
    Override the instance type in the Launch Template.
    """
    weighted_capacity: Optional[str] = pulumi.output_property("weightedCapacity")
    """
    The number of capacity units, which gives the instance type a proportional weight to other instance types.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GroupTag(dict):
    key: str = pulumi.output_property("key")
    """
    Key
    """
    propagate_at_launch: bool = pulumi.output_property("propagateAtLaunch")
    """
    Enables propagation of the tag to
    Amazon EC2 instances launched via this ASG
    """
    value: str = pulumi.output_property("value")
    """
    Value
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class PolicyStepAdjustment(dict):
    metric_interval_lower_bound: Optional[str] = pulumi.output_property("metricIntervalLowerBound")
    """
    The lower bound for the
    difference between the alarm threshold and the CloudWatch metric.
    Without a value, AWS will treat this bound as infinity.
    """
    metric_interval_upper_bound: Optional[str] = pulumi.output_property("metricIntervalUpperBound")
    """
    The upper bound for the
    difference between the alarm threshold and the CloudWatch metric.
    Without a value, AWS will treat this bound as infinity. The upper bound
    must be greater than the lower bound.
    """
    scaling_adjustment: float = pulumi.output_property("scalingAdjustment")
    """
    The number of members by which to
    scale, when the adjustment bounds are breached. A positive value scales
    up. A negative value scales down.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class PolicyTargetTrackingConfiguration(dict):
    customized_metric_specification: Optional['outputs.PolicyTargetTrackingConfigurationCustomizedMetricSpecification'] = pulumi.output_property("customizedMetricSpecification")
    """
    A customized metric. Conflicts with `predefined_metric_specification`.
    """
    disable_scale_in: Optional[bool] = pulumi.output_property("disableScaleIn")
    """
    Indicates whether scale in by the target tracking policy is disabled.
    """
    predefined_metric_specification: Optional['outputs.PolicyTargetTrackingConfigurationPredefinedMetricSpecification'] = pulumi.output_property("predefinedMetricSpecification")
    """
    A predefined metric. Conflicts with `customized_metric_specification`.
    """
    target_value: float = pulumi.output_property("targetValue")
    """
    The target value for the metric.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class PolicyTargetTrackingConfigurationCustomizedMetricSpecification(dict):
    metric_dimensions: Optional[List['outputs.PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimension']] = pulumi.output_property("metricDimensions")
    """
    The dimensions of the metric.
    """
    metric_name: str = pulumi.output_property("metricName")
    """
    The name of the metric.
    """
    namespace: str = pulumi.output_property("namespace")
    """
    The namespace of the metric.
    """
    statistic: str = pulumi.output_property("statistic")
    """
    The statistic of the metric.
    """
    unit: Optional[str] = pulumi.output_property("unit")
    """
    The unit of the metric.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimension(dict):
    name: str = pulumi.output_property("name")
    """
    The name of the dimension.
    """
    value: str = pulumi.output_property("value")
    """
    The value of the dimension.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class PolicyTargetTrackingConfigurationPredefinedMetricSpecification(dict):
    predefined_metric_type: str = pulumi.output_property("predefinedMetricType")
    """
    The metric type.
    """
    resource_label: Optional[str] = pulumi.output_property("resourceLabel")
    """
    Identifies the resource associated with the metric type.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


