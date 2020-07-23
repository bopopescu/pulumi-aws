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


class Route(pulumi.CustomResource):
    arn: pulumi.Output[str] = pulumi.output_property("arn")
    """
    The ARN of the route.
    """
    created_date: pulumi.Output[str] = pulumi.output_property("createdDate")
    """
    The creation date of the route.
    """
    last_updated_date: pulumi.Output[str] = pulumi.output_property("lastUpdatedDate")
    """
    The last update date of the route.
    """
    mesh_name: pulumi.Output[str] = pulumi.output_property("meshName")
    """
    The name of the service mesh in which to create the route.
    """
    name: pulumi.Output[str] = pulumi.output_property("name")
    """
    The name to use for the route.
    """
    spec: pulumi.Output['outputs.RouteSpec'] = pulumi.output_property("spec")
    """
    The route specification to apply.
    """
    tags: pulumi.Output[Optional[Dict[str, str]]] = pulumi.output_property("tags")
    """
    A map of tags to assign to the resource.
    """
    virtual_router_name: pulumi.Output[str] = pulumi.output_property("virtualRouterName")
    """
    The name of the virtual router in which to create the route.
    """
    # pylint: disable=no-self-argument
    def __init__(__self__, resource_name, opts: Optional[pulumi.ResourceOptions] = None, mesh_name=None, name=None, spec=None, tags=None, virtual_router_name=None, __props__=None, __name__=None, __opts__=None) -> None:
        """
        Provides an AWS App Mesh route resource.

        ## Example Usage
        ### HTTP Routing

        ```python
        import pulumi
        import pulumi_aws as aws

        serviceb = aws.appmesh.Route("serviceb",
            mesh_name=aws_appmesh_mesh["simple"]["id"],
            spec={
                "httpRoute": {
                    "action": {
                        "weightedTarget": [
                            {
                                "virtualNode": aws_appmesh_virtual_node["serviceb1"]["name"],
                                "weight": 90,
                            },
                            {
                                "virtualNode": aws_appmesh_virtual_node["serviceb2"]["name"],
                                "weight": 10,
                            },
                        ],
                    },
                    "match": {
                        "prefix": "/",
                    },
                },
            },
            virtual_router_name=aws_appmesh_virtual_router["serviceb"]["name"])
        ```
        ### HTTP Header Routing

        ```python
        import pulumi
        import pulumi_aws as aws

        serviceb = aws.appmesh.Route("serviceb",
            mesh_name=aws_appmesh_mesh["simple"]["id"],
            spec={
                "httpRoute": {
                    "action": {
                        "weightedTarget": [{
                            "virtualNode": aws_appmesh_virtual_node["serviceb"]["name"],
                            "weight": 100,
                        }],
                    },
                    "match": {
                        "header": [{
                            "match": {
                                "prefix": "123",
                            },
                            "name": "clientRequestId",
                        }],
                        "method": "POST",
                        "prefix": "/",
                        "scheme": "https",
                    },
                },
            },
            virtual_router_name=aws_appmesh_virtual_router["serviceb"]["name"])
        ```
        ### TCP Routing

        ```python
        import pulumi
        import pulumi_aws as aws

        serviceb = aws.appmesh.Route("serviceb",
            mesh_name=aws_appmesh_mesh["simple"]["id"],
            spec={
                "tcpRoute": {
                    "action": {
                        "weightedTarget": [{
                            "virtualNode": aws_appmesh_virtual_node["serviceb1"]["name"],
                            "weight": 100,
                        }],
                    },
                },
            },
            virtual_router_name=aws_appmesh_virtual_router["serviceb"]["name"])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] mesh_name: The name of the service mesh in which to create the route.
        :param pulumi.Input[str] name: The name to use for the route.
        :param pulumi.Input['RouteSpecArgs'] spec: The route specification to apply.
        :param pulumi.Input[Dict[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
        :param pulumi.Input[str] virtual_router_name: The name of the virtual router in which to create the route.
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

            if mesh_name is None:
                raise TypeError("Missing required property 'mesh_name'")
            __props__['mesh_name'] = mesh_name
            __props__['name'] = name
            if spec is None:
                raise TypeError("Missing required property 'spec'")
            __props__['spec'] = spec
            __props__['tags'] = tags
            if virtual_router_name is None:
                raise TypeError("Missing required property 'virtual_router_name'")
            __props__['virtual_router_name'] = virtual_router_name
            __props__['arn'] = None
            __props__['created_date'] = None
            __props__['last_updated_date'] = None
        super(Route, __self__).__init__(
            'aws:appmesh/route:Route',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, arn=None, created_date=None, last_updated_date=None, mesh_name=None, name=None, spec=None, tags=None, virtual_router_name=None):
        """
        Get an existing Route resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The ARN of the route.
        :param pulumi.Input[str] created_date: The creation date of the route.
        :param pulumi.Input[str] last_updated_date: The last update date of the route.
        :param pulumi.Input[str] mesh_name: The name of the service mesh in which to create the route.
        :param pulumi.Input[str] name: The name to use for the route.
        :param pulumi.Input['RouteSpecArgs'] spec: The route specification to apply.
        :param pulumi.Input[Dict[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
        :param pulumi.Input[str] virtual_router_name: The name of the virtual router in which to create the route.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["created_date"] = created_date
        __props__["last_updated_date"] = last_updated_date
        __props__["mesh_name"] = mesh_name
        __props__["name"] = name
        __props__["spec"] = spec
        __props__["tags"] = tags
        __props__["virtual_router_name"] = virtual_router_name
        return Route(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

