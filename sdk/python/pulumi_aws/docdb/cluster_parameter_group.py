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


class ClusterParameterGroup(pulumi.CustomResource):
    arn: pulumi.Output[str] = pulumi.output_property("arn")
    """
    The ARN of the documentDB cluster parameter group.
    """
    description: pulumi.Output[Optional[str]] = pulumi.output_property("description")
    """
    The description of the documentDB cluster parameter group. Defaults to "Managed by Pulumi".
    """
    family: pulumi.Output[str] = pulumi.output_property("family")
    """
    The family of the documentDB cluster parameter group.
    """
    name: pulumi.Output[str] = pulumi.output_property("name")
    """
    The name of the documentDB parameter.
    """
    name_prefix: pulumi.Output[str] = pulumi.output_property("namePrefix")
    """
    Creates a unique name beginning with the specified prefix. Conflicts with `name`.
    """
    parameters: pulumi.Output[Optional[List['outputs.ClusterParameterGroupParameter']]] = pulumi.output_property("parameters")
    """
    A list of documentDB parameters to apply.
    """
    tags: pulumi.Output[Optional[Dict[str, str]]] = pulumi.output_property("tags")
    """
    A map of tags to assign to the resource.
    """
    # pylint: disable=no-self-argument
    def __init__(__self__, resource_name, opts: Optional[pulumi.ResourceOptions] = None, description=None, family=None, name=None, name_prefix=None, parameters=None, tags=None, __props__=None, __name__=None, __opts__=None) -> None:
        """
        Manages a DocumentDB Cluster Parameter Group

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.docdb.ClusterParameterGroup("example",
            description="docdb cluster parameter group",
            family="docdb3.6",
            parameters=[{
                "name": "tls",
                "value": "enabled",
            }])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the documentDB cluster parameter group. Defaults to "Managed by Pulumi".
        :param pulumi.Input[str] family: The family of the documentDB cluster parameter group.
        :param pulumi.Input[str] name: The name of the documentDB parameter.
        :param pulumi.Input[str] name_prefix: Creates a unique name beginning with the specified prefix. Conflicts with `name`.
        :param pulumi.Input[List[pulumi.Input['ClusterParameterGroupParameterArgs']]] parameters: A list of documentDB parameters to apply.
        :param pulumi.Input[Dict[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
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

            __props__['description'] = description
            if family is None:
                raise TypeError("Missing required property 'family'")
            __props__['family'] = family
            __props__['name'] = name
            __props__['name_prefix'] = name_prefix
            __props__['parameters'] = parameters
            __props__['tags'] = tags
            __props__['arn'] = None
        super(ClusterParameterGroup, __self__).__init__(
            'aws:docdb/clusterParameterGroup:ClusterParameterGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, arn=None, description=None, family=None, name=None, name_prefix=None, parameters=None, tags=None):
        """
        Get an existing ClusterParameterGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The ARN of the documentDB cluster parameter group.
        :param pulumi.Input[str] description: The description of the documentDB cluster parameter group. Defaults to "Managed by Pulumi".
        :param pulumi.Input[str] family: The family of the documentDB cluster parameter group.
        :param pulumi.Input[str] name: The name of the documentDB parameter.
        :param pulumi.Input[str] name_prefix: Creates a unique name beginning with the specified prefix. Conflicts with `name`.
        :param pulumi.Input[List[pulumi.Input['ClusterParameterGroupParameterArgs']]] parameters: A list of documentDB parameters to apply.
        :param pulumi.Input[Dict[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["description"] = description
        __props__["family"] = family
        __props__["name"] = name
        __props__["name_prefix"] = name_prefix
        __props__["parameters"] = parameters
        __props__["tags"] = tags
        return ClusterParameterGroup(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

