# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables

@pulumi.input_type
class ServiceDnsConfigArgs:
    dns_records: pulumi.Input[List[pulumi.Input['ServiceDnsConfigDnsRecordArgs']]] = pulumi.input_property("dnsRecords")
    """
    An array that contains one DnsRecord object for each resource record set.
    """
    namespace_id: pulumi.Input[str] = pulumi.input_property("namespaceId")
    """
    The ID of the namespace to use for DNS configuration.
    """
    routing_policy: Optional[pulumi.Input[str]] = pulumi.input_property("routingPolicy")
    """
    The routing policy that you want to apply to all records that Route 53 creates when you register an instance and specify the service. Valid Values: MULTIVALUE, WEIGHTED
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, dns_records: pulumi.Input[List[pulumi.Input['ServiceDnsConfigDnsRecordArgs']]], namespace_id: pulumi.Input[str], routing_policy: Optional[pulumi.Input[str]] = None) -> None:
        """
        :param pulumi.Input[List[pulumi.Input['ServiceDnsConfigDnsRecordArgs']]] dns_records: An array that contains one DnsRecord object for each resource record set.
        :param pulumi.Input[str] namespace_id: The ID of the namespace to use for DNS configuration.
        :param pulumi.Input[str] routing_policy: The routing policy that you want to apply to all records that Route 53 creates when you register an instance and specify the service. Valid Values: MULTIVALUE, WEIGHTED
        """
        __self__.dns_records = dns_records
        __self__.namespace_id = namespace_id
        __self__.routing_policy = routing_policy

@pulumi.input_type
class ServiceDnsConfigDnsRecordArgs:
    ttl: pulumi.Input[float] = pulumi.input_property("ttl")
    """
    The amount of time, in seconds, that you want DNS resolvers to cache the settings for this resource record set.
    """
    type: pulumi.Input[str] = pulumi.input_property("type")
    """
    The type of health check that you want to create, which indicates how Route 53 determines whether an endpoint is healthy. Valid Values: HTTP, HTTPS, TCP
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, ttl: pulumi.Input[float], type: pulumi.Input[str]) -> None:
        """
        :param pulumi.Input[float] ttl: The amount of time, in seconds, that you want DNS resolvers to cache the settings for this resource record set.
        :param pulumi.Input[str] type: The type of health check that you want to create, which indicates how Route 53 determines whether an endpoint is healthy. Valid Values: HTTP, HTTPS, TCP
        """
        __self__.ttl = ttl
        __self__.type = type

@pulumi.input_type
class ServiceHealthCheckConfigArgs:
    failure_threshold: Optional[pulumi.Input[float]] = pulumi.input_property("failureThreshold")
    """
    The number of 30-second intervals that you want service discovery to wait before it changes the health status of a service instance.  Maximum value of 10.
    """
    resource_path: Optional[pulumi.Input[str]] = pulumi.input_property("resourcePath")
    """
    The path that you want Route 53 to request when performing health checks. Route 53 automatically adds the DNS name for the service. If you don't specify a value, the default value is /.
    """
    type: Optional[pulumi.Input[str]] = pulumi.input_property("type")
    """
    The type of health check that you want to create, which indicates how Route 53 determines whether an endpoint is healthy. Valid Values: HTTP, HTTPS, TCP
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, failure_threshold: Optional[pulumi.Input[float]] = None, resource_path: Optional[pulumi.Input[str]] = None, type: Optional[pulumi.Input[str]] = None) -> None:
        """
        :param pulumi.Input[float] failure_threshold: The number of 30-second intervals that you want service discovery to wait before it changes the health status of a service instance.  Maximum value of 10.
        :param pulumi.Input[str] resource_path: The path that you want Route 53 to request when performing health checks. Route 53 automatically adds the DNS name for the service. If you don't specify a value, the default value is /.
        :param pulumi.Input[str] type: The type of health check that you want to create, which indicates how Route 53 determines whether an endpoint is healthy. Valid Values: HTTP, HTTPS, TCP
        """
        __self__.failure_threshold = failure_threshold
        __self__.resource_path = resource_path
        __self__.type = type

@pulumi.input_type
class ServiceHealthCheckCustomConfigArgs:
    failure_threshold: Optional[pulumi.Input[float]] = pulumi.input_property("failureThreshold")
    """
    The number of 30-second intervals that you want service discovery to wait before it changes the health status of a service instance.  Maximum value of 10.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, failure_threshold: Optional[pulumi.Input[float]] = None) -> None:
        """
        :param pulumi.Input[float] failure_threshold: The number of 30-second intervals that you want service discovery to wait before it changes the health status of a service instance.  Maximum value of 10.
        """
        __self__.failure_threshold = failure_threshold

