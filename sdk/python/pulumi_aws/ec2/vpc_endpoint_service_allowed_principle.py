# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class VpcEndpointServiceAllowedPrinciple(pulumi.CustomResource):
    principal_arn: pulumi.Output[str]
    """
    The ARN of the principal to allow permissions.
    """
    vpc_endpoint_service_id: pulumi.Output[str]
    """
    The ID of the VPC endpoint service to allow permission.
    """
    def __init__(__self__, resource_name, opts=None, principal_arn=None, vpc_endpoint_service_id=None, __name__=None, __opts__=None):
        """
        Create a VpcEndpointServiceAllowedPrinciple resource with the given unique name, props, and options.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] principal_arn: The ARN of the principal to allow permissions.
        :param pulumi.Input[str] vpc_endpoint_service_id: The ID of the VPC endpoint service to allow permission.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/vpc_endpoint_service_allowed_principal.html.markdown.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if not resource_name:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(resource_name, str):
            raise TypeError('Expected resource name to be a string')
        if opts and not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if principal_arn is None:
            raise TypeError("Missing required property 'principal_arn'")
        __props__['principal_arn'] = principal_arn

        if vpc_endpoint_service_id is None:
            raise TypeError("Missing required property 'vpc_endpoint_service_id'")
        __props__['vpc_endpoint_service_id'] = vpc_endpoint_service_id

        super(VpcEndpointServiceAllowedPrinciple, __self__).__init__(
            'aws:ec2/vpcEndpointServiceAllowedPrinciple:VpcEndpointServiceAllowedPrinciple',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

