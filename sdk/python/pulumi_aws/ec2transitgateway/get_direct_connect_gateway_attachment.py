# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class GetDirectConnectGatewayAttachmentResult:
    """
    A collection of values returned by getDirectConnectGatewayAttachment.
    """
    def __init__(__self__, dx_gateway_id=None, tags=None, transit_gateway_id=None, id=None):
        if dx_gateway_id and not isinstance(dx_gateway_id, str):
            raise TypeError("Expected argument 'dx_gateway_id' to be a str")
        __self__.dx_gateway_id = dx_gateway_id
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        __self__.tags = tags
        """
        Key-value tags for the EC2 Transit Gateway Attachment
        """
        if transit_gateway_id and not isinstance(transit_gateway_id, str):
            raise TypeError("Expected argument 'transit_gateway_id' to be a str")
        __self__.transit_gateway_id = transit_gateway_id
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

async def get_direct_connect_gateway_attachment(dx_gateway_id=None,tags=None,transit_gateway_id=None,opts=None):
    """
    Get information on an EC2 Transit Gateway's attachment to a Direct Connect Gateway.

    > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/ec2_transit_gateway_dx_gateway_attachment.html.markdown.
    """
    __args__ = dict()

    __args__['dxGatewayId'] = dx_gateway_id
    __args__['tags'] = tags
    __args__['transitGatewayId'] = transit_gateway_id
    __ret__ = await pulumi.runtime.invoke('aws:ec2transitgateway/getDirectConnectGatewayAttachment:getDirectConnectGatewayAttachment', __args__, opts=opts)

    return GetDirectConnectGatewayAttachmentResult(
        dx_gateway_id=__ret__.get('dxGatewayId'),
        tags=__ret__.get('tags'),
        transit_gateway_id=__ret__.get('transitGatewayId'),
        id=__ret__.get('id'))
