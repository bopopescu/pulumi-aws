# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables


class Protection(pulumi.CustomResource):
    name: pulumi.Output[str] = pulumi.output_property("name")
    """
    A friendly name for the Protection you are creating.
    """
    resource_arn: pulumi.Output[str] = pulumi.output_property("resourceArn")
    """
    The ARN (Amazon Resource Name) of the resource to be protected.
    """
    # pylint: disable=no-self-argument
    def __init__(__self__, resource_name, opts: Optional[pulumi.ResourceOptions] = None, name=None, resource_arn=None, __props__=None, __name__=None, __opts__=None) -> None:
        """
        Enables AWS Shield Advanced for a specific AWS resource.
        The resource can be an Amazon CloudFront distribution, Elastic Load Balancing load balancer, AWS Global Accelerator accelerator, Elastic IP Address, or an Amazon Route 53 hosted zone.

        ## Example Usage
        ### Create protection

        ```python
        import pulumi
        import pulumi_aws as aws

        available = aws.get_availability_zones()
        current_region = aws.get_region()
        current_caller_identity = aws.get_caller_identity()
        foo_eip = aws.ec2.Eip("fooEip", vpc=True)
        foo_protection = aws.shield.Protection("fooProtection", resource_arn=foo_eip.id.apply(lambda id: f"arn:aws:ec2:{current_region.name}:{current_caller_identity.account_id}:eip-allocation/{id}"))
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: A friendly name for the Protection you are creating.
        :param pulumi.Input[str] resource_arn: The ARN (Amazon Resource Name) of the resource to be protected.
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

            __props__['name'] = name
            if resource_arn is None:
                raise TypeError("Missing required property 'resource_arn'")
            __props__['resource_arn'] = resource_arn
        super(Protection, __self__).__init__(
            'aws:shield/protection:Protection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, name=None, resource_arn=None):
        """
        Get an existing Protection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: A friendly name for the Protection you are creating.
        :param pulumi.Input[str] resource_arn: The ARN (Amazon Resource Name) of the resource to be protected.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["name"] = name
        __props__["resource_arn"] = resource_arn
        return Protection(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

