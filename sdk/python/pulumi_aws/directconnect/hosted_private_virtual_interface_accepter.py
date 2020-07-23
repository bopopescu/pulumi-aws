# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables


class HostedPrivateVirtualInterfaceAccepter(pulumi.CustomResource):
    arn: pulumi.Output[str] = pulumi.output_property("arn")
    """
    The ARN of the virtual interface.
    """
    dx_gateway_id: pulumi.Output[Optional[str]] = pulumi.output_property("dxGatewayId")
    """
    The ID of the Direct Connect gateway to which to connect the virtual interface.
    """
    tags: pulumi.Output[Optional[Dict[str, str]]] = pulumi.output_property("tags")
    """
    A map of tags to assign to the resource.
    """
    virtual_interface_id: pulumi.Output[str] = pulumi.output_property("virtualInterfaceId")
    """
    The ID of the Direct Connect virtual interface to accept.
    """
    vpn_gateway_id: pulumi.Output[Optional[str]] = pulumi.output_property("vpnGatewayId")
    """
    The ID of the virtual private gateway to which to connect the virtual interface.
    """
    # pylint: disable=no-self-argument
    def __init__(__self__, resource_name, opts: Optional[pulumi.ResourceOptions] = None, dx_gateway_id=None, tags=None, virtual_interface_id=None, vpn_gateway_id=None, __props__=None, __name__=None, __opts__=None) -> None:
        """
        Provides a resource to manage the accepter's side of a Direct Connect hosted private virtual interface.
        This resource accepts ownership of a private virtual interface created by another AWS account.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws
        import pulumi_pulumi as pulumi

        accepter = pulumi.providers.Aws("accepter")
        accepter_caller_identity = aws.get_caller_identity()
        # Creator's side of the VIF
        creator = aws.directconnect.HostedPrivateVirtualInterface("creator",
            address_family="ipv4",
            bgp_asn=65352,
            connection_id="dxcon-zzzzzzzz",
            owner_account_id=accepter_caller_identity.account_id,
            vlan=4094,
            opts=ResourceOptions(depends_on=["aws_vpn_gateway.vpn_gw"]))
        # Accepter's side of the VIF.
        vpn_gw = aws.ec2.VpnGateway("vpnGw", opts=ResourceOptions(provider="aws.accepter"))
        accepter_hosted_private_virtual_interface_accepter = aws.directconnect.HostedPrivateVirtualInterfaceAccepter("accepterHostedPrivateVirtualInterfaceAccepter",
            tags={
                "Side": "Accepter",
            },
            virtual_interface_id=creator.id,
            vpn_gateway_id=vpn_gw.id,
            opts=ResourceOptions(provider="aws.accepter"))
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] dx_gateway_id: The ID of the Direct Connect gateway to which to connect the virtual interface.
        :param pulumi.Input[Dict[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
        :param pulumi.Input[str] virtual_interface_id: The ID of the Direct Connect virtual interface to accept.
        :param pulumi.Input[str] vpn_gateway_id: The ID of the virtual private gateway to which to connect the virtual interface.
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

            __props__['dx_gateway_id'] = dx_gateway_id
            __props__['tags'] = tags
            if virtual_interface_id is None:
                raise TypeError("Missing required property 'virtual_interface_id'")
            __props__['virtual_interface_id'] = virtual_interface_id
            __props__['vpn_gateway_id'] = vpn_gateway_id
            __props__['arn'] = None
        super(HostedPrivateVirtualInterfaceAccepter, __self__).__init__(
            'aws:directconnect/hostedPrivateVirtualInterfaceAccepter:HostedPrivateVirtualInterfaceAccepter',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, arn=None, dx_gateway_id=None, tags=None, virtual_interface_id=None, vpn_gateway_id=None):
        """
        Get an existing HostedPrivateVirtualInterfaceAccepter resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The ARN of the virtual interface.
        :param pulumi.Input[str] dx_gateway_id: The ID of the Direct Connect gateway to which to connect the virtual interface.
        :param pulumi.Input[Dict[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
        :param pulumi.Input[str] virtual_interface_id: The ID of the Direct Connect virtual interface to accept.
        :param pulumi.Input[str] vpn_gateway_id: The ID of the virtual private gateway to which to connect the virtual interface.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["dx_gateway_id"] = dx_gateway_id
        __props__["tags"] = tags
        __props__["virtual_interface_id"] = virtual_interface_id
        __props__["vpn_gateway_id"] = vpn_gateway_id
        return HostedPrivateVirtualInterfaceAccepter(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

