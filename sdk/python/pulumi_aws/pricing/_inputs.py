# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables

@pulumi.input_type
class GetProductFilterArgs:
    field: str = pulumi.input_property("field")
    """
    The product attribute name that you want to filter on.
    """
    value: str = pulumi.input_property("value")
    """
    The product attribute value that you want to filter on.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, field: str, value: str) -> None:
        """
        :param str field: The product attribute name that you want to filter on.
        :param str value: The product attribute value that you want to filter on.
        """
        __self__.field = field
        __self__.value = value

