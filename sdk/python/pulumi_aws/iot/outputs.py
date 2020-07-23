# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables

@pulumi.output_type
class ThingTypeProperties(dict):
    description: Optional[str] = pulumi.output_property("description")
    """
    The description of the thing type.
    """
    searchable_attributes: Optional[List[str]] = pulumi.output_property("searchableAttributes")
    """
    A list of searchable thing attribute names.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class TopicRuleCloudwatchAlarm(dict):
    alarm_name: str = pulumi.output_property("alarmName")
    """
    The CloudWatch alarm name.
    """
    role_arn: str = pulumi.output_property("roleArn")
    """
    The IAM role ARN that allows access to the CloudWatch alarm.
    """
    state_reason: str = pulumi.output_property("stateReason")
    """
    The reason for the alarm change.
    """
    state_value: str = pulumi.output_property("stateValue")
    """
    The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class TopicRuleCloudwatchMetric(dict):
    metric_name: str = pulumi.output_property("metricName")
    """
    The CloudWatch metric name.
    """
    metric_namespace: str = pulumi.output_property("metricNamespace")
    """
    The CloudWatch metric namespace name.
    """
    metric_timestamp: Optional[str] = pulumi.output_property("metricTimestamp")
    """
    An optional Unix timestamp (http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#about_timestamp).
    """
    metric_unit: str = pulumi.output_property("metricUnit")
    """
    The metric unit (supported units can be found here: http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#Unit)
    """
    metric_value: str = pulumi.output_property("metricValue")
    """
    The CloudWatch metric value.
    """
    role_arn: str = pulumi.output_property("roleArn")
    """
    The IAM role ARN that allows access to the CloudWatch metric.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class TopicRuleDynamodb(dict):
    hash_key_field: str = pulumi.output_property("hashKeyField")
    """
    The hash key name.
    """
    hash_key_type: Optional[str] = pulumi.output_property("hashKeyType")
    """
    The hash key type. Valid values are "STRING" or "NUMBER".
    """
    hash_key_value: str = pulumi.output_property("hashKeyValue")
    """
    The hash key value.
    """
    operation: Optional[str] = pulumi.output_property("operation")
    """
    The operation. Valid values are "INSERT", "UPDATE", or "DELETE".
    """
    payload_field: Optional[str] = pulumi.output_property("payloadField")
    """
    The action payload.
    """
    range_key_field: Optional[str] = pulumi.output_property("rangeKeyField")
    """
    The range key name.
    """
    range_key_type: Optional[str] = pulumi.output_property("rangeKeyType")
    """
    The range key type. Valid values are "STRING" or "NUMBER".
    """
    range_key_value: Optional[str] = pulumi.output_property("rangeKeyValue")
    """
    The range key value.
    """
    role_arn: str = pulumi.output_property("roleArn")
    """
    The ARN of the IAM role that grants access to the DynamoDB table.
    """
    table_name: str = pulumi.output_property("tableName")
    """
    The name of the DynamoDB table.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class TopicRuleDynamodbv2(dict):
    put_item: Optional['outputs.TopicRuleDynamodbv2PutItem'] = pulumi.output_property("putItem")
    """
    Configuration block with DynamoDB Table to which the message will be written. Nested arguments below.
    """
    role_arn: str = pulumi.output_property("roleArn")
    """
    The IAM role ARN that allows access to the CloudWatch alarm.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class TopicRuleDynamodbv2PutItem(dict):
    table_name: str = pulumi.output_property("tableName")
    """
    The name of the DynamoDB table.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class TopicRuleElasticsearch(dict):
    endpoint: str = pulumi.output_property("endpoint")
    """
    The endpoint of your Elasticsearch domain.
    """
    id: str = pulumi.output_property("id")
    """
    The unique identifier for the document you are storing.
    """
    index: str = pulumi.output_property("index")
    """
    The Elasticsearch index where you want to store your data.
    """
    role_arn: str = pulumi.output_property("roleArn")
    """
    The IAM role ARN that has access to Elasticsearch.
    """
    type: str = pulumi.output_property("type")
    """
    The type of document you are storing.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class TopicRuleErrorAction(dict):
    cloudwatch_alarm: Optional['outputs.TopicRuleErrorActionCloudwatchAlarm'] = pulumi.output_property("cloudwatchAlarm")
    cloudwatch_metric: Optional['outputs.TopicRuleErrorActionCloudwatchMetric'] = pulumi.output_property("cloudwatchMetric")
    dynamodb: Optional['outputs.TopicRuleErrorActionDynamodb'] = pulumi.output_property("dynamodb")
    dynamodbv2: Optional['outputs.TopicRuleErrorActionDynamodbv2'] = pulumi.output_property("dynamodbv2")
    elasticsearch: Optional['outputs.TopicRuleErrorActionElasticsearch'] = pulumi.output_property("elasticsearch")
    firehose: Optional['outputs.TopicRuleErrorActionFirehose'] = pulumi.output_property("firehose")
    iot_analytics: Optional['outputs.TopicRuleErrorActionIotAnalytics'] = pulumi.output_property("iotAnalytics")
    iot_events: Optional['outputs.TopicRuleErrorActionIotEvents'] = pulumi.output_property("iotEvents")
    kinesis: Optional['outputs.TopicRuleErrorActionKinesis'] = pulumi.output_property("kinesis")
    lambda_: Optional['outputs.TopicRuleErrorActionLambda'] = pulumi.output_property("lambda")
    republish: Optional['outputs.TopicRuleErrorActionRepublish'] = pulumi.output_property("republish")
    s3: Optional['outputs.TopicRuleErrorActionS3'] = pulumi.output_property("s3")
    sns: Optional['outputs.TopicRuleErrorActionSns'] = pulumi.output_property("sns")
    sqs: Optional['outputs.TopicRuleErrorActionSqs'] = pulumi.output_property("sqs")
    step_functions: Optional['outputs.TopicRuleErrorActionStepFunctions'] = pulumi.output_property("stepFunctions")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class TopicRuleErrorActionCloudwatchAlarm(dict):
    alarm_name: str = pulumi.output_property("alarmName")
    """
    The CloudWatch alarm name.
    """
    role_arn: str = pulumi.output_property("roleArn")
    """
    The IAM role ARN that allows access to the CloudWatch alarm.
    """
    state_reason: str = pulumi.output_property("stateReason")
    """
    The reason for the alarm change.
    """
    state_value: str = pulumi.output_property("stateValue")
    """
    The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class TopicRuleErrorActionCloudwatchMetric(dict):
    metric_name: str = pulumi.output_property("metricName")
    """
    The CloudWatch metric name.
    """
    metric_namespace: str = pulumi.output_property("metricNamespace")
    """
    The CloudWatch metric namespace name.
    """
    metric_timestamp: Optional[str] = pulumi.output_property("metricTimestamp")
    """
    An optional Unix timestamp (http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#about_timestamp).
    """
    metric_unit: str = pulumi.output_property("metricUnit")
    """
    The metric unit (supported units can be found here: http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#Unit)
    """
    metric_value: str = pulumi.output_property("metricValue")
    """
    The CloudWatch metric value.
    """
    role_arn: str = pulumi.output_property("roleArn")
    """
    The IAM role ARN that allows access to the CloudWatch metric.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class TopicRuleErrorActionDynamodb(dict):
    hash_key_field: str = pulumi.output_property("hashKeyField")
    """
    The hash key name.
    """
    hash_key_type: Optional[str] = pulumi.output_property("hashKeyType")
    """
    The hash key type. Valid values are "STRING" or "NUMBER".
    """
    hash_key_value: str = pulumi.output_property("hashKeyValue")
    """
    The hash key value.
    """
    operation: Optional[str] = pulumi.output_property("operation")
    """
    The operation. Valid values are "INSERT", "UPDATE", or "DELETE".
    """
    payload_field: Optional[str] = pulumi.output_property("payloadField")
    """
    The action payload.
    """
    range_key_field: Optional[str] = pulumi.output_property("rangeKeyField")
    """
    The range key name.
    """
    range_key_type: Optional[str] = pulumi.output_property("rangeKeyType")
    """
    The range key type. Valid values are "STRING" or "NUMBER".
    """
    range_key_value: Optional[str] = pulumi.output_property("rangeKeyValue")
    """
    The range key value.
    """
    role_arn: str = pulumi.output_property("roleArn")
    """
    The ARN of the IAM role that grants access to the DynamoDB table.
    """
    table_name: str = pulumi.output_property("tableName")
    """
    The name of the DynamoDB table.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class TopicRuleErrorActionDynamodbv2(dict):
    put_item: Optional['outputs.TopicRuleErrorActionDynamodbv2PutItem'] = pulumi.output_property("putItem")
    """
    Configuration block with DynamoDB Table to which the message will be written. Nested arguments below.
    """
    role_arn: str = pulumi.output_property("roleArn")
    """
    The IAM role ARN that allows access to the CloudWatch alarm.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class TopicRuleErrorActionDynamodbv2PutItem(dict):
    table_name: str = pulumi.output_property("tableName")
    """
    The name of the DynamoDB table.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class TopicRuleErrorActionElasticsearch(dict):
    endpoint: str = pulumi.output_property("endpoint")
    """
    The endpoint of your Elasticsearch domain.
    """
    id: str = pulumi.output_property("id")
    """
    The unique identifier for the document you are storing.
    """
    index: str = pulumi.output_property("index")
    """
    The Elasticsearch index where you want to store your data.
    """
    role_arn: str = pulumi.output_property("roleArn")
    """
    The IAM role ARN that has access to Elasticsearch.
    """
    type: str = pulumi.output_property("type")
    """
    The type of document you are storing.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class TopicRuleErrorActionFirehose(dict):
    delivery_stream_name: str = pulumi.output_property("deliveryStreamName")
    """
    The delivery stream name.
    """
    role_arn: str = pulumi.output_property("roleArn")
    """
    The IAM role ARN that grants access to the Amazon Kinesis Firehose stream.
    """
    separator: Optional[str] = pulumi.output_property("separator")
    """
    A character separator that is used to separate records written to the Firehose stream. Valid values are: '\n' (newline), '\t' (tab), '\r\n' (Windows newline), ',' (comma).
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class TopicRuleErrorActionIotAnalytics(dict):
    channel_name: str = pulumi.output_property("channelName")
    """
    Name of AWS IOT Analytics channel.
    """
    role_arn: str = pulumi.output_property("roleArn")
    """
    The ARN of the IAM role that grants access.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class TopicRuleErrorActionIotEvents(dict):
    input_name: str = pulumi.output_property("inputName")
    """
    The name of the AWS IoT Events input.
    """
    message_id: Optional[str] = pulumi.output_property("messageId")
    """
    Use this to ensure that only one input (message) with a given messageId is processed by an AWS IoT Events detector.
    """
    role_arn: str = pulumi.output_property("roleArn")
    """
    The ARN of the IAM role that grants access.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class TopicRuleErrorActionKinesis(dict):
    partition_key: Optional[str] = pulumi.output_property("partitionKey")
    """
    The partition key.
    """
    role_arn: str = pulumi.output_property("roleArn")
    """
    The ARN of the IAM role that grants access to the Amazon Kinesis stream.
    """
    stream_name: str = pulumi.output_property("streamName")
    """
    The name of the Amazon Kinesis stream.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class TopicRuleErrorActionLambda(dict):
    function_arn: str = pulumi.output_property("functionArn")
    """
    The ARN of the Lambda function.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class TopicRuleErrorActionRepublish(dict):
    qos: Optional[float] = pulumi.output_property("qos")
    """
    The Quality of Service (QoS) level to use when republishing messages. Valid values are 0 or 1. The default value is 0.
    """
    role_arn: str = pulumi.output_property("roleArn")
    """
    The ARN of the IAM role that grants access.
    """
    topic: str = pulumi.output_property("topic")
    """
    The name of the MQTT topic the message should be republished to.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class TopicRuleErrorActionS3(dict):
    bucket_name: str = pulumi.output_property("bucketName")
    """
    The Amazon S3 bucket name.
    """
    key: str = pulumi.output_property("key")
    """
    The object key.
    """
    role_arn: str = pulumi.output_property("roleArn")
    """
    The IAM role ARN that allows access to the CloudWatch alarm.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class TopicRuleErrorActionSns(dict):
    message_format: Optional[str] = pulumi.output_property("messageFormat")
    """
    The message format of the message to publish. Accepted values are "JSON" and "RAW".
    """
    role_arn: str = pulumi.output_property("roleArn")
    """
    The ARN of the IAM role that grants access.
    """
    target_arn: str = pulumi.output_property("targetArn")
    """
    The ARN of the SNS topic.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class TopicRuleErrorActionSqs(dict):
    queue_url: str = pulumi.output_property("queueUrl")
    """
    The URL of the Amazon SQS queue.
    """
    role_arn: str = pulumi.output_property("roleArn")
    """
    The ARN of the IAM role that grants access.
    """
    use_base64: bool = pulumi.output_property("useBase64")
    """
    Specifies whether to use Base64 encoding.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class TopicRuleErrorActionStepFunctions(dict):
    execution_name_prefix: Optional[str] = pulumi.output_property("executionNamePrefix")
    """
    The prefix used to generate, along with a UUID, the unique state machine execution name.
    """
    role_arn: str = pulumi.output_property("roleArn")
    """
    The ARN of the IAM role that grants access to start execution of the state machine.
    """
    state_machine_name: str = pulumi.output_property("stateMachineName")
    """
    The name of the Step Functions state machine whose execution will be started.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class TopicRuleFirehose(dict):
    delivery_stream_name: str = pulumi.output_property("deliveryStreamName")
    """
    The delivery stream name.
    """
    role_arn: str = pulumi.output_property("roleArn")
    """
    The IAM role ARN that grants access to the Amazon Kinesis Firehose stream.
    """
    separator: Optional[str] = pulumi.output_property("separator")
    """
    A character separator that is used to separate records written to the Firehose stream. Valid values are: '\n' (newline), '\t' (tab), '\r\n' (Windows newline), ',' (comma).
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class TopicRuleIotAnalytic(dict):
    channel_name: str = pulumi.output_property("channelName")
    """
    Name of AWS IOT Analytics channel.
    """
    role_arn: str = pulumi.output_property("roleArn")
    """
    The ARN of the IAM role that grants access.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class TopicRuleIotEvent(dict):
    input_name: str = pulumi.output_property("inputName")
    """
    The name of the AWS IoT Events input.
    """
    message_id: Optional[str] = pulumi.output_property("messageId")
    """
    Use this to ensure that only one input (message) with a given messageId is processed by an AWS IoT Events detector.
    """
    role_arn: str = pulumi.output_property("roleArn")
    """
    The ARN of the IAM role that grants access.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class TopicRuleKinesis(dict):
    partition_key: Optional[str] = pulumi.output_property("partitionKey")
    """
    The partition key.
    """
    role_arn: str = pulumi.output_property("roleArn")
    """
    The ARN of the IAM role that grants access to the Amazon Kinesis stream.
    """
    stream_name: str = pulumi.output_property("streamName")
    """
    The name of the Amazon Kinesis stream.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class TopicRuleLambda(dict):
    function_arn: str = pulumi.output_property("functionArn")
    """
    The ARN of the Lambda function.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class TopicRuleRepublish(dict):
    qos: Optional[float] = pulumi.output_property("qos")
    """
    The Quality of Service (QoS) level to use when republishing messages. Valid values are 0 or 1. The default value is 0.
    """
    role_arn: str = pulumi.output_property("roleArn")
    """
    The ARN of the IAM role that grants access.
    """
    topic: str = pulumi.output_property("topic")
    """
    The name of the MQTT topic the message should be republished to.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class TopicRuleS3(dict):
    bucket_name: str = pulumi.output_property("bucketName")
    """
    The Amazon S3 bucket name.
    """
    key: str = pulumi.output_property("key")
    """
    The object key.
    """
    role_arn: str = pulumi.output_property("roleArn")
    """
    The IAM role ARN that allows access to the CloudWatch alarm.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class TopicRuleSns(dict):
    message_format: Optional[str] = pulumi.output_property("messageFormat")
    """
    The message format of the message to publish. Accepted values are "JSON" and "RAW".
    """
    role_arn: str = pulumi.output_property("roleArn")
    """
    The ARN of the IAM role that grants access.
    """
    target_arn: str = pulumi.output_property("targetArn")
    """
    The ARN of the SNS topic.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class TopicRuleSqs(dict):
    queue_url: str = pulumi.output_property("queueUrl")
    """
    The URL of the Amazon SQS queue.
    """
    role_arn: str = pulumi.output_property("roleArn")
    """
    The ARN of the IAM role that grants access.
    """
    use_base64: bool = pulumi.output_property("useBase64")
    """
    Specifies whether to use Base64 encoding.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class TopicRuleStepFunction(dict):
    execution_name_prefix: Optional[str] = pulumi.output_property("executionNamePrefix")
    """
    The prefix used to generate, along with a UUID, the unique state machine execution name.
    """
    role_arn: str = pulumi.output_property("roleArn")
    """
    The ARN of the IAM role that grants access to start execution of the state machine.
    """
    state_machine_name: str = pulumi.output_property("stateMachineName")
    """
    The name of the Step Functions state machine whose execution will be started.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


