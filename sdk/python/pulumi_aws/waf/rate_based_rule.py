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


class RateBasedRule(pulumi.CustomResource):
    arn: pulumi.Output[str] = pulumi.output_property("arn")
    """
    Amazon Resource Name (ARN)
    """
    metric_name: pulumi.Output[str] = pulumi.output_property("metricName")
    """
    The name or description for the Amazon CloudWatch metric of this rule.
    """
    name: pulumi.Output[str] = pulumi.output_property("name")
    """
    The name or description of the rule.
    """
    predicates: pulumi.Output[Optional[List['outputs.RateBasedRulePredicate']]] = pulumi.output_property("predicates")
    """
    The objects to include in a rule (documented below).
    """
    rate_key: pulumi.Output[str] = pulumi.output_property("rateKey")
    """
    Valid value is IP.
    """
    rate_limit: pulumi.Output[float] = pulumi.output_property("rateLimit")
    """
    The maximum number of requests, which have an identical value in the field specified by the RateKey, allowed in a five-minute period. Minimum value is 100.
    """
    tags: pulumi.Output[Optional[Dict[str, str]]] = pulumi.output_property("tags")
    """
    Key-value map of resource tags
    """
    # pylint: disable=no-self-argument
    def __init__(__self__, resource_name, opts: Optional[pulumi.ResourceOptions] = None, metric_name=None, name=None, predicates=None, rate_key=None, rate_limit=None, tags=None, __props__=None, __name__=None, __opts__=None) -> None:
        """
        Provides a WAF Rate Based Rule Resource

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        ipset = aws.waf.IpSet("ipset", ip_set_descriptors=[{
            "type": "IPV4",
            "value": "192.0.7.0/24",
        }])
        wafrule = aws.waf.RateBasedRule("wafrule",
            metric_name="tfWAFRule",
            predicates=[{
                "dataId": ipset.id,
                "negated": False,
                "type": "IPMatch",
            }],
            rate_key="IP",
            rate_limit=100,
            opts=ResourceOptions(depends_on=["aws_waf_ipset.ipset"]))
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] metric_name: The name or description for the Amazon CloudWatch metric of this rule.
        :param pulumi.Input[str] name: The name or description of the rule.
        :param pulumi.Input[List[pulumi.Input['RateBasedRulePredicateArgs']]] predicates: The objects to include in a rule (documented below).
        :param pulumi.Input[str] rate_key: Valid value is IP.
        :param pulumi.Input[float] rate_limit: The maximum number of requests, which have an identical value in the field specified by the RateKey, allowed in a five-minute period. Minimum value is 100.
        :param pulumi.Input[Dict[str, pulumi.Input[str]]] tags: Key-value map of resource tags
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

            if metric_name is None:
                raise TypeError("Missing required property 'metric_name'")
            __props__['metric_name'] = metric_name
            __props__['name'] = name
            __props__['predicates'] = predicates
            if rate_key is None:
                raise TypeError("Missing required property 'rate_key'")
            __props__['rate_key'] = rate_key
            if rate_limit is None:
                raise TypeError("Missing required property 'rate_limit'")
            __props__['rate_limit'] = rate_limit
            __props__['tags'] = tags
            __props__['arn'] = None
        super(RateBasedRule, __self__).__init__(
            'aws:waf/rateBasedRule:RateBasedRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, arn=None, metric_name=None, name=None, predicates=None, rate_key=None, rate_limit=None, tags=None):
        """
        Get an existing RateBasedRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN)
        :param pulumi.Input[str] metric_name: The name or description for the Amazon CloudWatch metric of this rule.
        :param pulumi.Input[str] name: The name or description of the rule.
        :param pulumi.Input[List[pulumi.Input['RateBasedRulePredicateArgs']]] predicates: The objects to include in a rule (documented below).
        :param pulumi.Input[str] rate_key: Valid value is IP.
        :param pulumi.Input[float] rate_limit: The maximum number of requests, which have an identical value in the field specified by the RateKey, allowed in a five-minute period. Minimum value is 100.
        :param pulumi.Input[Dict[str, pulumi.Input[str]]] tags: Key-value map of resource tags
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["metric_name"] = metric_name
        __props__["name"] = name
        __props__["predicates"] = predicates
        __props__["rate_key"] = rate_key
        __props__["rate_limit"] = rate_limit
        __props__["tags"] = tags
        return RateBasedRule(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

