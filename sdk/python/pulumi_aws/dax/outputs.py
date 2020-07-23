# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables

@pulumi.output_type
class ClusterNode(dict):
    address: Optional[str] = pulumi.output_property("address")
    availability_zone: Optional[str] = pulumi.output_property("availabilityZone")
    id: Optional[str] = pulumi.output_property("id")
    port: Optional[float] = pulumi.output_property("port")
    """
    The port used by the configuration endpoint
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ClusterServerSideEncryption(dict):
    enabled: Optional[bool] = pulumi.output_property("enabled")
    """
    Whether to enable encryption at rest. Defaults to `false`.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ParameterGroupParameter(dict):
    name: str = pulumi.output_property("name")
    """
    The name of the parameter.
    """
    value: str = pulumi.output_property("value")
    """
    The value for the parameter.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


