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


class Association(pulumi.CustomResource):
    association_id: pulumi.Output[str] = pulumi.output_property("associationId")
    """
    The ID of the SSM association.
    """
    association_name: pulumi.Output[Optional[str]] = pulumi.output_property("associationName")
    """
    The descriptive name for the association.
    """
    automation_target_parameter_name: pulumi.Output[Optional[str]] = pulumi.output_property("automationTargetParameterName")
    """
    Specify the target for the association. This target is required for associations that use an `Automation` document and target resources by using rate controls.
    """
    compliance_severity: pulumi.Output[Optional[str]] = pulumi.output_property("complianceSeverity")
    """
    The compliance severity for the association. Can be one of the following: `UNSPECIFIED`, `LOW`, `MEDIUM`, `HIGH` or `CRITICAL`
    """
    document_version: pulumi.Output[str] = pulumi.output_property("documentVersion")
    """
    The document version you want to associate with the target(s). Can be a specific version or the default version.
    """
    instance_id: pulumi.Output[Optional[str]] = pulumi.output_property("instanceId")
    """
    The instance ID to apply an SSM document to. Use `targets` with key `InstanceIds` for document schema versions 2.0 and above.
    """
    max_concurrency: pulumi.Output[Optional[str]] = pulumi.output_property("maxConcurrency")
    """
    The maximum number of targets allowed to run the association at the same time. You can specify a number, for example 10, or a percentage of the target set, for example 10%.
    """
    max_errors: pulumi.Output[Optional[str]] = pulumi.output_property("maxErrors")
    """
    The number of errors that are allowed before the system stops sending requests to run the association on additional targets. You can specify a number, for example 10, or a percentage of the target set, for example 10%.
    """
    name: pulumi.Output[str] = pulumi.output_property("name")
    """
    The name of the SSM document to apply.
    """
    output_location: pulumi.Output[Optional['outputs.AssociationOutputLocation']] = pulumi.output_property("outputLocation")
    """
    An output location block. Output Location is documented below.
    """
    parameters: pulumi.Output[Dict[str, str]] = pulumi.output_property("parameters")
    """
    A block of arbitrary string parameters to pass to the SSM document.
    """
    schedule_expression: pulumi.Output[Optional[str]] = pulumi.output_property("scheduleExpression")
    """
    A cron expression when the association will be applied to the target(s).
    """
    targets: pulumi.Output[List['outputs.AssociationTarget']] = pulumi.output_property("targets")
    """
    A block containing the targets of the SSM association. Targets are documented below. AWS currently supports a maximum of 5 targets.
    """
    # pylint: disable=no-self-argument
    def __init__(__self__, resource_name, opts: Optional[pulumi.ResourceOptions] = None, association_name=None, automation_target_parameter_name=None, compliance_severity=None, document_version=None, instance_id=None, max_concurrency=None, max_errors=None, name=None, output_location=None, parameters=None, schedule_expression=None, targets=None, __props__=None, __name__=None, __opts__=None) -> None:
        """
        Associates an SSM Document to an instance or EC2 tag.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.ssm.Association("example", targets=[{
            "key": "InstanceIds",
            "values": [aws_instance["example"]["id"]],
        }])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] association_name: The descriptive name for the association.
        :param pulumi.Input[str] automation_target_parameter_name: Specify the target for the association. This target is required for associations that use an `Automation` document and target resources by using rate controls.
        :param pulumi.Input[str] compliance_severity: The compliance severity for the association. Can be one of the following: `UNSPECIFIED`, `LOW`, `MEDIUM`, `HIGH` or `CRITICAL`
        :param pulumi.Input[str] document_version: The document version you want to associate with the target(s). Can be a specific version or the default version.
        :param pulumi.Input[str] instance_id: The instance ID to apply an SSM document to. Use `targets` with key `InstanceIds` for document schema versions 2.0 and above.
        :param pulumi.Input[str] max_concurrency: The maximum number of targets allowed to run the association at the same time. You can specify a number, for example 10, or a percentage of the target set, for example 10%.
        :param pulumi.Input[str] max_errors: The number of errors that are allowed before the system stops sending requests to run the association on additional targets. You can specify a number, for example 10, or a percentage of the target set, for example 10%.
        :param pulumi.Input[str] name: The name of the SSM document to apply.
        :param pulumi.Input['AssociationOutputLocationArgs'] output_location: An output location block. Output Location is documented below.
        :param pulumi.Input[Dict[str, pulumi.Input[str]]] parameters: A block of arbitrary string parameters to pass to the SSM document.
        :param pulumi.Input[str] schedule_expression: A cron expression when the association will be applied to the target(s).
        :param pulumi.Input[List[pulumi.Input['AssociationTargetArgs']]] targets: A block containing the targets of the SSM association. Targets are documented below. AWS currently supports a maximum of 5 targets.
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

            __props__['association_name'] = association_name
            __props__['automation_target_parameter_name'] = automation_target_parameter_name
            __props__['compliance_severity'] = compliance_severity
            __props__['document_version'] = document_version
            __props__['instance_id'] = instance_id
            __props__['max_concurrency'] = max_concurrency
            __props__['max_errors'] = max_errors
            __props__['name'] = name
            __props__['output_location'] = output_location
            __props__['parameters'] = parameters
            __props__['schedule_expression'] = schedule_expression
            __props__['targets'] = targets
            __props__['association_id'] = None
        super(Association, __self__).__init__(
            'aws:ssm/association:Association',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, association_id=None, association_name=None, automation_target_parameter_name=None, compliance_severity=None, document_version=None, instance_id=None, max_concurrency=None, max_errors=None, name=None, output_location=None, parameters=None, schedule_expression=None, targets=None):
        """
        Get an existing Association resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] association_id: The ID of the SSM association.
        :param pulumi.Input[str] association_name: The descriptive name for the association.
        :param pulumi.Input[str] automation_target_parameter_name: Specify the target for the association. This target is required for associations that use an `Automation` document and target resources by using rate controls.
        :param pulumi.Input[str] compliance_severity: The compliance severity for the association. Can be one of the following: `UNSPECIFIED`, `LOW`, `MEDIUM`, `HIGH` or `CRITICAL`
        :param pulumi.Input[str] document_version: The document version you want to associate with the target(s). Can be a specific version or the default version.
        :param pulumi.Input[str] instance_id: The instance ID to apply an SSM document to. Use `targets` with key `InstanceIds` for document schema versions 2.0 and above.
        :param pulumi.Input[str] max_concurrency: The maximum number of targets allowed to run the association at the same time. You can specify a number, for example 10, or a percentage of the target set, for example 10%.
        :param pulumi.Input[str] max_errors: The number of errors that are allowed before the system stops sending requests to run the association on additional targets. You can specify a number, for example 10, or a percentage of the target set, for example 10%.
        :param pulumi.Input[str] name: The name of the SSM document to apply.
        :param pulumi.Input['AssociationOutputLocationArgs'] output_location: An output location block. Output Location is documented below.
        :param pulumi.Input[Dict[str, pulumi.Input[str]]] parameters: A block of arbitrary string parameters to pass to the SSM document.
        :param pulumi.Input[str] schedule_expression: A cron expression when the association will be applied to the target(s).
        :param pulumi.Input[List[pulumi.Input['AssociationTargetArgs']]] targets: A block containing the targets of the SSM association. Targets are documented below. AWS currently supports a maximum of 5 targets.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["association_id"] = association_id
        __props__["association_name"] = association_name
        __props__["automation_target_parameter_name"] = automation_target_parameter_name
        __props__["compliance_severity"] = compliance_severity
        __props__["document_version"] = document_version
        __props__["instance_id"] = instance_id
        __props__["max_concurrency"] = max_concurrency
        __props__["max_errors"] = max_errors
        __props__["name"] = name
        __props__["output_location"] = output_location
        __props__["parameters"] = parameters
        __props__["schedule_expression"] = schedule_expression
        __props__["targets"] = targets
        return Association(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

