# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables

@pulumi.input_type
class BudgetCostTypesArgs:
    include_credit: Optional[pulumi.Input[bool]] = pulumi.input_property("includeCredit")
    """
    A boolean value whether to include credits in the cost budget. Defaults to `true`
    """
    include_discount: Optional[pulumi.Input[bool]] = pulumi.input_property("includeDiscount")
    """
    Specifies whether a budget includes discounts. Defaults to `true`
    """
    include_other_subscription: Optional[pulumi.Input[bool]] = pulumi.input_property("includeOtherSubscription")
    """
    A boolean value whether to include other subscription costs in the cost budget. Defaults to `true`
    """
    include_recurring: Optional[pulumi.Input[bool]] = pulumi.input_property("includeRecurring")
    """
    A boolean value whether to include recurring costs in the cost budget. Defaults to `true`
    """
    include_refund: Optional[pulumi.Input[bool]] = pulumi.input_property("includeRefund")
    """
    A boolean value whether to include refunds in the cost budget. Defaults to `true`
    """
    include_subscription: Optional[pulumi.Input[bool]] = pulumi.input_property("includeSubscription")
    """
    A boolean value whether to include subscriptions in the cost budget. Defaults to `true`
    """
    include_support: Optional[pulumi.Input[bool]] = pulumi.input_property("includeSupport")
    """
    A boolean value whether to include support costs in the cost budget. Defaults to `true`
    """
    include_tax: Optional[pulumi.Input[bool]] = pulumi.input_property("includeTax")
    """
    A boolean value whether to include tax in the cost budget. Defaults to `true`
    """
    include_upfront: Optional[pulumi.Input[bool]] = pulumi.input_property("includeUpfront")
    """
    A boolean value whether to include upfront costs in the cost budget. Defaults to `true`
    """
    use_amortized: Optional[pulumi.Input[bool]] = pulumi.input_property("useAmortized")
    """
    Specifies whether a budget uses the amortized rate. Defaults to `false`
    """
    use_blended: Optional[pulumi.Input[bool]] = pulumi.input_property("useBlended")
    """
    A boolean value whether to use blended costs in the cost budget. Defaults to `false`
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, include_credit: Optional[pulumi.Input[bool]] = None, include_discount: Optional[pulumi.Input[bool]] = None, include_other_subscription: Optional[pulumi.Input[bool]] = None, include_recurring: Optional[pulumi.Input[bool]] = None, include_refund: Optional[pulumi.Input[bool]] = None, include_subscription: Optional[pulumi.Input[bool]] = None, include_support: Optional[pulumi.Input[bool]] = None, include_tax: Optional[pulumi.Input[bool]] = None, include_upfront: Optional[pulumi.Input[bool]] = None, use_amortized: Optional[pulumi.Input[bool]] = None, use_blended: Optional[pulumi.Input[bool]] = None) -> None:
        """
        :param pulumi.Input[bool] include_credit: A boolean value whether to include credits in the cost budget. Defaults to `true`
        :param pulumi.Input[bool] include_discount: Specifies whether a budget includes discounts. Defaults to `true`
        :param pulumi.Input[bool] include_other_subscription: A boolean value whether to include other subscription costs in the cost budget. Defaults to `true`
        :param pulumi.Input[bool] include_recurring: A boolean value whether to include recurring costs in the cost budget. Defaults to `true`
        :param pulumi.Input[bool] include_refund: A boolean value whether to include refunds in the cost budget. Defaults to `true`
        :param pulumi.Input[bool] include_subscription: A boolean value whether to include subscriptions in the cost budget. Defaults to `true`
        :param pulumi.Input[bool] include_support: A boolean value whether to include support costs in the cost budget. Defaults to `true`
        :param pulumi.Input[bool] include_tax: A boolean value whether to include tax in the cost budget. Defaults to `true`
        :param pulumi.Input[bool] include_upfront: A boolean value whether to include upfront costs in the cost budget. Defaults to `true`
        :param pulumi.Input[bool] use_amortized: Specifies whether a budget uses the amortized rate. Defaults to `false`
        :param pulumi.Input[bool] use_blended: A boolean value whether to use blended costs in the cost budget. Defaults to `false`
        """
        __self__.include_credit = include_credit
        __self__.include_discount = include_discount
        __self__.include_other_subscription = include_other_subscription
        __self__.include_recurring = include_recurring
        __self__.include_refund = include_refund
        __self__.include_subscription = include_subscription
        __self__.include_support = include_support
        __self__.include_tax = include_tax
        __self__.include_upfront = include_upfront
        __self__.use_amortized = use_amortized
        __self__.use_blended = use_blended

@pulumi.input_type
class BudgetNotificationArgs:
    comparison_operator: pulumi.Input[str] = pulumi.input_property("comparisonOperator")
    """
    (Required) Comparison operator to use to evaluate the condition. Can be `LESS_THAN`, `EQUAL_TO` or `GREATER_THAN`.
    """
    notification_type: pulumi.Input[str] = pulumi.input_property("notificationType")
    """
    (Required) What kind of budget value to notify on. Can be `ACTUAL` or `FORECASTED`
    """
    threshold: pulumi.Input[float] = pulumi.input_property("threshold")
    """
    (Required) Threshold when the notification should be sent.
    """
    threshold_type: pulumi.Input[str] = pulumi.input_property("thresholdType")
    """
    (Required) What kind of threshold is defined. Can be `PERCENTAGE` OR `ABSOLUTE_VALUE`.
    """
    subscriber_email_addresses: Optional[pulumi.Input[List[pulumi.Input[str]]]] = pulumi.input_property("subscriberEmailAddresses")
    """
    (Optional) E-Mail addresses to notify. Either this or `subscriber_sns_topic_arns` is required.
    """
    subscriber_sns_topic_arns: Optional[pulumi.Input[List[pulumi.Input[str]]]] = pulumi.input_property("subscriberSnsTopicArns")
    """
    (Optional) SNS topics to notify. Either this or `subscriber_email_addresses` is required.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, comparison_operator: pulumi.Input[str], notification_type: pulumi.Input[str], threshold: pulumi.Input[float], threshold_type: pulumi.Input[str], subscriber_email_addresses: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None, subscriber_sns_topic_arns: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None) -> None:
        """
        :param pulumi.Input[str] comparison_operator: (Required) Comparison operator to use to evaluate the condition. Can be `LESS_THAN`, `EQUAL_TO` or `GREATER_THAN`.
        :param pulumi.Input[str] notification_type: (Required) What kind of budget value to notify on. Can be `ACTUAL` or `FORECASTED`
        :param pulumi.Input[float] threshold: (Required) Threshold when the notification should be sent.
        :param pulumi.Input[str] threshold_type: (Required) What kind of threshold is defined. Can be `PERCENTAGE` OR `ABSOLUTE_VALUE`.
        :param pulumi.Input[List[pulumi.Input[str]]] subscriber_email_addresses: (Optional) E-Mail addresses to notify. Either this or `subscriber_sns_topic_arns` is required.
        :param pulumi.Input[List[pulumi.Input[str]]] subscriber_sns_topic_arns: (Optional) SNS topics to notify. Either this or `subscriber_email_addresses` is required.
        """
        __self__.comparison_operator = comparison_operator
        __self__.notification_type = notification_type
        __self__.threshold = threshold
        __self__.threshold_type = threshold_type
        __self__.subscriber_email_addresses = subscriber_email_addresses
        __self__.subscriber_sns_topic_arns = subscriber_sns_topic_arns

