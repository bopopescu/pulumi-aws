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


class EndpointConfiguration(pulumi.CustomResource):
    arn: pulumi.Output[str] = pulumi.output_property("arn")
    """
    The Amazon Resource Name (ARN) assigned by AWS to this endpoint configuration.
    """
    kms_key_arn: pulumi.Output[Optional[str]] = pulumi.output_property("kmsKeyArn")
    """
    Amazon Resource Name (ARN) of a AWS Key Management Service key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance that hosts the endpoint.
    """
    name: pulumi.Output[str] = pulumi.output_property("name")
    """
    The name of the endpoint configuration. If omitted, this provider will assign a random, unique name.
    """
    production_variants: pulumi.Output[List['outputs.EndpointConfigurationProductionVariant']] = pulumi.output_property("productionVariants")
    """
    Fields are documented below.
    """
    tags: pulumi.Output[Optional[Dict[str, str]]] = pulumi.output_property("tags")
    """
    A mapping of tags to assign to the resource.
    """
    # pylint: disable=no-self-argument
    def __init__(__self__, resource_name, opts: Optional[pulumi.ResourceOptions] = None, kms_key_arn=None, name=None, production_variants=None, tags=None, __props__=None, __name__=None, __opts__=None) -> None:
        """
        Provides a SageMaker endpoint configuration resource.

        ## Example Usage

        Basic usage:

        ```python
        import pulumi
        import pulumi_aws as aws

        ec = aws.sagemaker.EndpointConfiguration("ec",
            production_variants=[{
                "initialInstanceCount": 1,
                "instance_type": "ml.t2.medium",
                "modelName": aws_sagemaker_model["m"]["name"],
                "variantName": "variant-1",
            }],
            tags={
                "Name": "foo",
            })
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] kms_key_arn: Amazon Resource Name (ARN) of a AWS Key Management Service key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance that hosts the endpoint.
        :param pulumi.Input[str] name: The name of the endpoint configuration. If omitted, this provider will assign a random, unique name.
        :param pulumi.Input[List[pulumi.Input['EndpointConfigurationProductionVariantArgs']]] production_variants: Fields are documented below.
        :param pulumi.Input[Dict[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
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

    @staticmethod
    def get(resource_name, id, opts=None, arn=None, kms_key_arn=None, name=None, production_variants=None, tags=None):
        """
        Get an existing EndpointConfiguration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The Amazon Resource Name (ARN) assigned by AWS to this endpoint configuration.
        :param pulumi.Input[str] kms_key_arn: Amazon Resource Name (ARN) of a AWS Key Management Service key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance that hosts the endpoint.
        :param pulumi.Input[str] name: The name of the endpoint configuration. If omitted, this provider will assign a random, unique name.
        :param pulumi.Input[List[pulumi.Input['EndpointConfigurationProductionVariantArgs']]] production_variants: Fields are documented below.
        :param pulumi.Input[Dict[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["kms_key_arn"] = kms_key_arn
        __props__["name"] = name
        __props__["production_variants"] = production_variants
        __props__["tags"] = tags
        return EndpointConfiguration(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

