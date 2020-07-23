# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables

@pulumi.input_type
class ClusterClusterCertificateArgs:
    aws_hardware_certificate: Optional[pulumi.Input[str]] = pulumi.input_property("awsHardwareCertificate")
    cluster_certificate: Optional[pulumi.Input[str]] = pulumi.input_property("clusterCertificate")
    cluster_csr: Optional[pulumi.Input[str]] = pulumi.input_property("clusterCsr")
    hsm_certificate: Optional[pulumi.Input[str]] = pulumi.input_property("hsmCertificate")
    manufacturer_hardware_certificate: Optional[pulumi.Input[str]] = pulumi.input_property("manufacturerHardwareCertificate")

    # pylint: disable=no-self-argument
    def __init__(__self__, *, aws_hardware_certificate: Optional[pulumi.Input[str]] = None, cluster_certificate: Optional[pulumi.Input[str]] = None, cluster_csr: Optional[pulumi.Input[str]] = None, hsm_certificate: Optional[pulumi.Input[str]] = None, manufacturer_hardware_certificate: Optional[pulumi.Input[str]] = None) -> None:
        __self__.aws_hardware_certificate = aws_hardware_certificate
        __self__.cluster_certificate = cluster_certificate
        __self__.cluster_csr = cluster_csr
        __self__.hsm_certificate = hsm_certificate
        __self__.manufacturer_hardware_certificate = manufacturer_hardware_certificate

