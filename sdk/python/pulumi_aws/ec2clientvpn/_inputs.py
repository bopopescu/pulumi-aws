# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables

@pulumi.input_type
class EndpointAuthenticationOptionArgs:
    type: pulumi.Input[str] = pulumi.input_property("type")
    """
    The type of client authentication to be used. Specify `certificate-authentication` to use certificate-based authentication, or `directory-service-authentication` to use Active Directory authentication.
    """
    active_directory_id: Optional[pulumi.Input[str]] = pulumi.input_property("activeDirectoryId")
    """
    The ID of the Active Directory to be used for authentication if type is `directory-service-authentication`.
    """
    root_certificate_chain_arn: Optional[pulumi.Input[str]] = pulumi.input_property("rootCertificateChainArn")
    """
    The ARN of the client certificate. The certificate must be signed by a certificate authority (CA) and it must be provisioned in AWS Certificate Manager (ACM). Only necessary when type is set to `certificate-authentication`.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, type: pulumi.Input[str], active_directory_id: Optional[pulumi.Input[str]] = None, root_certificate_chain_arn: Optional[pulumi.Input[str]] = None) -> None:
        """
        :param pulumi.Input[str] type: The type of client authentication to be used. Specify `certificate-authentication` to use certificate-based authentication, or `directory-service-authentication` to use Active Directory authentication.
        :param pulumi.Input[str] active_directory_id: The ID of the Active Directory to be used for authentication if type is `directory-service-authentication`.
        :param pulumi.Input[str] root_certificate_chain_arn: The ARN of the client certificate. The certificate must be signed by a certificate authority (CA) and it must be provisioned in AWS Certificate Manager (ACM). Only necessary when type is set to `certificate-authentication`.
        """
        __self__.type = type
        __self__.active_directory_id = active_directory_id
        __self__.root_certificate_chain_arn = root_certificate_chain_arn

@pulumi.input_type
class EndpointConnectionLogOptionsArgs:
    enabled: pulumi.Input[bool] = pulumi.input_property("enabled")
    """
    Indicates whether connection logging is enabled.
    """
    cloudwatch_log_group: Optional[pulumi.Input[str]] = pulumi.input_property("cloudwatchLogGroup")
    """
    The name of the CloudWatch Logs log group.
    """
    cloudwatch_log_stream: Optional[pulumi.Input[str]] = pulumi.input_property("cloudwatchLogStream")
    """
    The name of the CloudWatch Logs log stream to which the connection data is published.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, enabled: pulumi.Input[bool], cloudwatch_log_group: Optional[pulumi.Input[str]] = None, cloudwatch_log_stream: Optional[pulumi.Input[str]] = None) -> None:
        """
        :param pulumi.Input[bool] enabled: Indicates whether connection logging is enabled.
        :param pulumi.Input[str] cloudwatch_log_group: The name of the CloudWatch Logs log group.
        :param pulumi.Input[str] cloudwatch_log_stream: The name of the CloudWatch Logs log stream to which the connection data is published.
        """
        __self__.enabled = enabled
        __self__.cloudwatch_log_group = cloudwatch_log_group
        __self__.cloudwatch_log_stream = cloudwatch_log_stream

