# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class Cluster(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    The Amazon Resource Name (ARN) that identifies the cluster
    """
    capacity_providers: pulumi.Output[list]
    """
    List of short names of one or more capacity providers to associate with the cluster. Valid values also include `FARGATE` and `FARGATE_SPOT`.
    """
    default_capacity_provider_strategies: pulumi.Output[list]
    """
    The capacity provider strategy to use by default for the cluster. Can be one or more.  Defined below.

      * `base` (`float`) - The number of tasks, at a minimum, to run on the specified capacity provider. Only one capacity provider in a capacity provider strategy can have a base defined.
      * `capacityProvider` (`str`) - The short name of the capacity provider.
      * `weight` (`float`) - The relative percentage of the total number of launched tasks that should use the specified capacity provider.
    """
    name: pulumi.Output[str]
    """
    The name of the cluster (up to 255 letters, numbers, hyphens, and underscores)
    """
    settings: pulumi.Output[list]
    """
    Configuration block(s) with cluster settings. For example, this can be used to enable CloudWatch Container Insights for a cluster. Defined below.

      * `name` (`str`) - Name of the setting to manage. Valid values: `containerInsights`.
      * `value` (`str`) - The value to assign to the setting. Value values are `enabled` and `disabled`.
    """
    tags: pulumi.Output[dict]
    """
    Key-value map of resource tags
    """
    def __init__(__self__, resource_name, opts=None, capacity_providers=None, default_capacity_provider_strategies=None, name=None, settings=None, tags=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides an ECS cluster.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        foo = aws.ecs.Cluster("foo")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] capacity_providers: List of short names of one or more capacity providers to associate with the cluster. Valid values also include `FARGATE` and `FARGATE_SPOT`.
        :param pulumi.Input[list] default_capacity_provider_strategies: The capacity provider strategy to use by default for the cluster. Can be one or more.  Defined below.
        :param pulumi.Input[str] name: The name of the cluster (up to 255 letters, numbers, hyphens, and underscores)
        :param pulumi.Input[list] settings: Configuration block(s) with cluster settings. For example, this can be used to enable CloudWatch Container Insights for a cluster. Defined below.
        :param pulumi.Input[dict] tags: Key-value map of resource tags

        The **default_capacity_provider_strategies** object supports the following:

          * `base` (`pulumi.Input[float]`) - The number of tasks, at a minimum, to run on the specified capacity provider. Only one capacity provider in a capacity provider strategy can have a base defined.
          * `capacityProvider` (`pulumi.Input[str]`) - The short name of the capacity provider.
          * `weight` (`pulumi.Input[float]`) - The relative percentage of the total number of launched tasks that should use the specified capacity provider.

        The **settings** object supports the following:

          * `name` (`pulumi.Input[str]`) - Name of the setting to manage. Valid values: `containerInsights`.
          * `value` (`pulumi.Input[str]`) - The value to assign to the setting. Value values are `enabled` and `disabled`.
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
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['capacity_providers'] = capacity_providers
            __props__['default_capacity_provider_strategies'] = default_capacity_provider_strategies
            __props__['name'] = name
            __props__['settings'] = settings
            __props__['tags'] = tags
            __props__['arn'] = None
        super(Cluster, __self__).__init__(
            'aws:ecs/cluster:Cluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, arn=None, capacity_providers=None, default_capacity_provider_strategies=None, name=None, settings=None, tags=None):
        """
        Get an existing Cluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The Amazon Resource Name (ARN) that identifies the cluster
        :param pulumi.Input[list] capacity_providers: List of short names of one or more capacity providers to associate with the cluster. Valid values also include `FARGATE` and `FARGATE_SPOT`.
        :param pulumi.Input[list] default_capacity_provider_strategies: The capacity provider strategy to use by default for the cluster. Can be one or more.  Defined below.
        :param pulumi.Input[str] name: The name of the cluster (up to 255 letters, numbers, hyphens, and underscores)
        :param pulumi.Input[list] settings: Configuration block(s) with cluster settings. For example, this can be used to enable CloudWatch Container Insights for a cluster. Defined below.
        :param pulumi.Input[dict] tags: Key-value map of resource tags

        The **default_capacity_provider_strategies** object supports the following:

          * `base` (`pulumi.Input[float]`) - The number of tasks, at a minimum, to run on the specified capacity provider. Only one capacity provider in a capacity provider strategy can have a base defined.
          * `capacityProvider` (`pulumi.Input[str]`) - The short name of the capacity provider.
          * `weight` (`pulumi.Input[float]`) - The relative percentage of the total number of launched tasks that should use the specified capacity provider.

        The **settings** object supports the following:

          * `name` (`pulumi.Input[str]`) - Name of the setting to manage. Valid values: `containerInsights`.
          * `value` (`pulumi.Input[str]`) - The value to assign to the setting. Value values are `enabled` and `disabled`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["capacity_providers"] = capacity_providers
        __props__["default_capacity_provider_strategies"] = default_capacity_provider_strategies
        __props__["name"] = name
        __props__["settings"] = settings
        __props__["tags"] = tags
        return Cluster(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
