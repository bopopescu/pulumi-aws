# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables

@pulumi.input_type
class DirectoryConnectSettingsArgs:
    customer_dns_ips: pulumi.Input[List[pulumi.Input[str]]] = pulumi.input_property("customerDnsIps")
    """
    The DNS IP addresses of the domain to connect to.
    """
    customer_username: pulumi.Input[str] = pulumi.input_property("customerUsername")
    """
    The username corresponding to the password provided.
    """
    subnet_ids: pulumi.Input[List[pulumi.Input[str]]] = pulumi.input_property("subnetIds")
    """
    The identifiers of the subnets for the directory servers (2 subnets in 2 different AZs).
    """
    vpc_id: pulumi.Input[str] = pulumi.input_property("vpcId")
    """
    The identifier of the VPC that the directory is in.
    """
    availability_zones: Optional[pulumi.Input[List[pulumi.Input[str]]]] = pulumi.input_property("availabilityZones")
    connect_ips: Optional[pulumi.Input[List[pulumi.Input[str]]]] = pulumi.input_property("connectIps")
    """
    The IP addresses of the AD Connector servers.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, customer_dns_ips: pulumi.Input[List[pulumi.Input[str]]], customer_username: pulumi.Input[str], subnet_ids: pulumi.Input[List[pulumi.Input[str]]], vpc_id: pulumi.Input[str], availability_zones: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None, connect_ips: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None) -> None:
        """
        :param pulumi.Input[List[pulumi.Input[str]]] customer_dns_ips: The DNS IP addresses of the domain to connect to.
        :param pulumi.Input[str] customer_username: The username corresponding to the password provided.
        :param pulumi.Input[List[pulumi.Input[str]]] subnet_ids: The identifiers of the subnets for the directory servers (2 subnets in 2 different AZs).
        :param pulumi.Input[str] vpc_id: The identifier of the VPC that the directory is in.
        :param pulumi.Input[List[pulumi.Input[str]]] connect_ips: The IP addresses of the AD Connector servers.
        """
        __self__.customer_dns_ips = customer_dns_ips
        __self__.customer_username = customer_username
        __self__.subnet_ids = subnet_ids
        __self__.vpc_id = vpc_id
        __self__.availability_zones = availability_zones
        __self__.connect_ips = connect_ips

@pulumi.input_type
class DirectoryVpcSettingsArgs:
    subnet_ids: pulumi.Input[List[pulumi.Input[str]]] = pulumi.input_property("subnetIds")
    """
    The identifiers of the subnets for the directory servers (2 subnets in 2 different AZs).
    """
    vpc_id: pulumi.Input[str] = pulumi.input_property("vpcId")
    """
    The identifier of the VPC that the directory is in.
    """
    availability_zones: Optional[pulumi.Input[List[pulumi.Input[str]]]] = pulumi.input_property("availabilityZones")

    # pylint: disable=no-self-argument
    def __init__(__self__, *, subnet_ids: pulumi.Input[List[pulumi.Input[str]]], vpc_id: pulumi.Input[str], availability_zones: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None) -> None:
        """
        :param pulumi.Input[List[pulumi.Input[str]]] subnet_ids: The identifiers of the subnets for the directory servers (2 subnets in 2 different AZs).
        :param pulumi.Input[str] vpc_id: The identifier of the VPC that the directory is in.
        """
        __self__.subnet_ids = subnet_ids
        __self__.vpc_id = vpc_id
        __self__.availability_zones = availability_zones

