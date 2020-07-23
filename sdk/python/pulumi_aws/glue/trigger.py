# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *


class Trigger(pulumi.CustomResource):
    actions: pulumi.Output[List['outputs.TriggerAction']] = pulumi.output_property("actions")
    """
    List of actions initiated by this trigger when it fires. Defined below.
    """
    arn: pulumi.Output[str] = pulumi.output_property("arn")
    """
    Amazon Resource Name (ARN) of Glue Trigger
    """
    description: pulumi.Output[Optional[str]] = pulumi.output_property("description")
    """
    A description of the new trigger.
    """
    enabled: pulumi.Output[Optional[bool]] = pulumi.output_property("enabled")
    """
    Start the trigger. Defaults to `true`. Not valid to disable for `ON_DEMAND` type.
    """
    name: pulumi.Output[str] = pulumi.output_property("name")
    """
    The name of the trigger.
    """
    predicate: pulumi.Output[Optional['outputs.TriggerPredicate']] = pulumi.output_property("predicate")
    """
    A predicate to specify when the new trigger should fire. Required when trigger type is `CONDITIONAL`. Defined below.
    """
    schedule: pulumi.Output[Optional[str]] = pulumi.output_property("schedule")
    """
    A cron expression used to specify the schedule. [Time-Based Schedules for Jobs and Crawlers](https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html)
    """
    tags: pulumi.Output[Optional[Dict[str, str]]] = pulumi.output_property("tags")
    """
    Key-value map of resource tags
    """
    type: pulumi.Output[str] = pulumi.output_property("type")
    """
    The type of trigger. Valid values are `CONDITIONAL`, `ON_DEMAND`, and `SCHEDULED`.
    """
    workflow_name: pulumi.Output[Optional[str]] = pulumi.output_property("workflowName")
    """
    A workflow to which the trigger should be associated to. Every workflow graph (DAG) needs a starting trigger (`ON_DEMAND` or `SCHEDULED` type) and can contain multiple additional `CONDITIONAL` triggers.
    """
    # pylint: disable=no-self-argument
    def __init__(__self__, resource_name, opts: Optional[pulumi.ResourceOptions] = None, actions=None, description=None, enabled=None, name=None, predicate=None, schedule=None, tags=None, type=None, workflow_name=None, __props__=None, __name__=None, __opts__=None) -> None:
        """
        Manages a Glue Trigger resource.

        ## Example Usage
        ### Conditional Trigger

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.glue.Trigger("example",
            actions=[{
                "jobName": aws_glue_job["example1"]["name"],
            }],
            predicate={
                "conditions": [{
                    "jobName": aws_glue_job["example2"]["name"],
                    "state": "SUCCEEDED",
                }],
            },
            type="CONDITIONAL")
        ```
        ### On-Demand Trigger

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.glue.Trigger("example",
            actions=[{
                "jobName": aws_glue_job["example"]["name"],
            }],
            type="ON_DEMAND")
        ```
        ### Scheduled Trigger

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.glue.Trigger("example",
            actions=[{
                "jobName": aws_glue_job["example"]["name"],
            }],
            schedule="cron(15 12 * * ? *)",
            type="SCHEDULED")
        ```
        ### Conditional Trigger with Crawler Action

        **Note:** Triggers can have both a crawler action and a crawler condition, just no example provided.

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.glue.Trigger("example",
            actions=[{
                "crawlerName": aws_glue_crawler["example1"]["name"],
            }],
            predicate={
                "conditions": [{
                    "jobName": aws_glue_job["example2"]["name"],
                    "state": "SUCCEEDED",
                }],
            },
            type="CONDITIONAL")
        ```
        ### Conditional Trigger with Crawler Condition

        **Note:** Triggers can have both a crawler action and a crawler condition, just no example provided.

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.glue.Trigger("example",
            actions=[{
                "jobName": aws_glue_job["example1"]["name"],
            }],
            predicate={
                "conditions": [{
                    "crawlState": "SUCCEEDED",
                    "crawlerName": aws_glue_crawler["example2"]["name"],
                }],
            },
            type="CONDITIONAL")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[List[pulumi.Input['TriggerActionArgs']]] actions: List of actions initiated by this trigger when it fires. Defined below.
        :param pulumi.Input[str] description: A description of the new trigger.
        :param pulumi.Input[bool] enabled: Start the trigger. Defaults to `true`. Not valid to disable for `ON_DEMAND` type.
        :param pulumi.Input[str] name: The name of the trigger.
        :param pulumi.Input['TriggerPredicateArgs'] predicate: A predicate to specify when the new trigger should fire. Required when trigger type is `CONDITIONAL`. Defined below.
        :param pulumi.Input[str] schedule: A cron expression used to specify the schedule. [Time-Based Schedules for Jobs and Crawlers](https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html)
        :param pulumi.Input[Dict[str, pulumi.Input[str]]] tags: Key-value map of resource tags
        :param pulumi.Input[str] type: The type of trigger. Valid values are `CONDITIONAL`, `ON_DEMAND`, and `SCHEDULED`.
        :param pulumi.Input[str] workflow_name: A workflow to which the trigger should be associated to. Every workflow graph (DAG) needs a starting trigger (`ON_DEMAND` or `SCHEDULED` type) and can contain multiple additional `CONDITIONAL` triggers.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if actions is None:
                raise TypeError("Missing required property 'actions'")
            __props__['actions'] = actions
            __props__['description'] = description
            __props__['enabled'] = enabled
            __props__['name'] = name
            __props__['predicate'] = predicate
            __props__['schedule'] = schedule
            __props__['tags'] = tags
            if type is None:
                raise TypeError("Missing required property 'type'")
            __props__['type'] = type
            __props__['workflow_name'] = workflow_name
            __props__['arn'] = None
        super(Trigger, __self__).__init__(
            'aws:glue/trigger:Trigger',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, actions=None, arn=None, description=None, enabled=None, name=None, predicate=None, schedule=None, tags=None, type=None, workflow_name=None):
        """
        Get an existing Trigger resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[List[pulumi.Input['TriggerActionArgs']]] actions: List of actions initiated by this trigger when it fires. Defined below.
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN) of Glue Trigger
        :param pulumi.Input[str] description: A description of the new trigger.
        :param pulumi.Input[bool] enabled: Start the trigger. Defaults to `true`. Not valid to disable for `ON_DEMAND` type.
        :param pulumi.Input[str] name: The name of the trigger.
        :param pulumi.Input['TriggerPredicateArgs'] predicate: A predicate to specify when the new trigger should fire. Required when trigger type is `CONDITIONAL`. Defined below.
        :param pulumi.Input[str] schedule: A cron expression used to specify the schedule. [Time-Based Schedules for Jobs and Crawlers](https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html)
        :param pulumi.Input[Dict[str, pulumi.Input[str]]] tags: Key-value map of resource tags
        :param pulumi.Input[str] type: The type of trigger. Valid values are `CONDITIONAL`, `ON_DEMAND`, and `SCHEDULED`.
        :param pulumi.Input[str] workflow_name: A workflow to which the trigger should be associated to. Every workflow graph (DAG) needs a starting trigger (`ON_DEMAND` or `SCHEDULED` type) and can contain multiple additional `CONDITIONAL` triggers.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["actions"] = actions
        __props__["arn"] = arn
        __props__["description"] = description
        __props__["enabled"] = enabled
        __props__["name"] = name
        __props__["predicate"] = predicate
        __props__["schedule"] = schedule
        __props__["tags"] = tags
        __props__["type"] = type
        __props__["workflow_name"] = workflow_name
        return Trigger(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

