# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class EndpointConfiguration(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    The Amazon Resource Name (ARN) assigned by AWS to this endpoint configuration.
    """
    kms_key_arn: pulumi.Output[str]
    """
    Amazon Resource Name (ARN) of a AWS Key Management Service key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance that hosts the endpoint.
    """
    name: pulumi.Output[str]
    """
    The name of the endpoint configuration.
    """
    production_variants: pulumi.Output[list]
    """
    Fields are documented below.
    """
    tags: pulumi.Output[dict]
    """
    A mapping of tags to assign to the resource.
    """
    def __init__(__self__, resource_name, opts=None, kms_key_arn=None, name=None, production_variants=None, tags=None, __name__=None, __opts__=None):
        """
        Provides a SageMaker endpoint configuration resource.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] kms_key_arn: Amazon Resource Name (ARN) of a AWS Key Management Service key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance that hosts the endpoint.
        :param pulumi.Input[str] name: The name of the endpoint configuration.
        :param pulumi.Input[list] production_variants: Fields are documented below.
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/sagemaker_endpoint_configuration.html.markdown.
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

        __props__['kms_key_arn'] = kms_key_arn

        __props__['name'] = name

        if production_variants is None:
            raise TypeError("Missing required property 'production_variants'")
        __props__['production_variants'] = production_variants

        __props__['tags'] = tags

        __props__['arn'] = None

        super(EndpointConfiguration, __self__).__init__(
            'aws:sagemaker/endpointConfiguration:EndpointConfiguration',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

