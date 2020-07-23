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


class EventSourceMapping(pulumi.CustomResource):
    batch_size: pulumi.Output[Optional[float]] = pulumi.output_property("batchSize")
    """
    The largest number of records that Lambda will retrieve from your event source at the time of invocation. Defaults to `100` for DynamoDB and Kinesis, `10` for SQS.
    """
    bisect_batch_on_function_error: pulumi.Output[Optional[bool]] = pulumi.output_property("bisectBatchOnFunctionError")
    destination_config: pulumi.Output[Optional['outputs.EventSourceMappingDestinationConfig']] = pulumi.output_property("destinationConfig")
    enabled: pulumi.Output[Optional[bool]] = pulumi.output_property("enabled")
    """
    Determines if the mapping will be enabled on creation. Defaults to `true`.
    """
    event_source_arn: pulumi.Output[str] = pulumi.output_property("eventSourceArn")
    """
    The event source ARN - can be a Kinesis stream, DynamoDB stream, or SQS queue.
    """
    function_arn: pulumi.Output[str] = pulumi.output_property("functionArn")
    """
    The the ARN of the Lambda function the event source mapping is sending events to. (Note: this is a computed value that differs from `function_name` above.)
    """
    function_name: pulumi.Output[str] = pulumi.output_property("functionName")
    """
    The name or the ARN of the Lambda function that will be subscribing to events.
    """
    last_modified: pulumi.Output[str] = pulumi.output_property("lastModified")
    """
    The date this resource was last modified.
    """
    last_processing_result: pulumi.Output[str] = pulumi.output_property("lastProcessingResult")
    """
    The result of the last AWS Lambda invocation of your Lambda function.
    """
    maximum_batching_window_in_seconds: pulumi.Output[Optional[float]] = pulumi.output_property("maximumBatchingWindowInSeconds")
    """
    The maximum amount of time to gather records before invoking the function, in seconds.  Records will continue to buffer until either `maximum_batching_window_in_seconds` expires or `batch_size` has been met. Defaults to as soon as records are available in the stream. If the batch it reads from the stream only has one record in it, Lambda only sends one record to the function.
    """
    maximum_record_age_in_seconds: pulumi.Output[float] = pulumi.output_property("maximumRecordAgeInSeconds")
    maximum_retry_attempts: pulumi.Output[float] = pulumi.output_property("maximumRetryAttempts")
    parallelization_factor: pulumi.Output[float] = pulumi.output_property("parallelizationFactor")
    starting_position: pulumi.Output[Optional[str]] = pulumi.output_property("startingPosition")
    """
    The position in the stream where AWS Lambda should start reading. Must be one of `AT_TIMESTAMP` (Kinesis only), `LATEST` or `TRIM_HORIZON` if getting events from Kinesis or DynamoDB. Must not be provided if getting events from SQS. More information about these positions can be found in the [AWS DynamoDB Streams API Reference](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_GetShardIterator.html) and [AWS Kinesis API Reference](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetShardIterator.html#Kinesis-GetShardIterator-request-ShardIteratorType).
    """
    starting_position_timestamp: pulumi.Output[Optional[str]] = pulumi.output_property("startingPositionTimestamp")
    """
    A timestamp in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8) of the data record which to start reading when using `starting_position` set to `AT_TIMESTAMP`. If a record with this exact timestamp does not exist, the next later record is chosen. If the timestamp is older than the current trim horizon, the oldest available record is chosen.
    * `parallelization_factor`: - (Optional) The number of batches to process from each shard concurrently. Only available for stream sources (DynamoDB and Kinesis). Minimum and default of 1, maximum of 10.
    * `maximum_retry_attempts`: - (Optional) The maximum number of times to retry when the function returns an error. Only available for stream sources (DynamoDB and Kinesis). Minimum of 0, maximum and default of 10000.
    * `maximum_record_age_in_seconds`: - (Optional) The maximum age of a record that Lambda sends to a function for processing. Only available for stream sources (DynamoDB and Kinesis). Minimum of 60, maximum and default of 604800.
    * `bisect_batch_on_function_error`: - (Optional) If the function returns an error, split the batch in two and retry. Only available for stream sources (DynamoDB and Kinesis). Defaults to `false`.
    * `destination_config`: - (Optional) An Amazon SQS queue or Amazon SNS topic destination for failed records. Only available for stream sources (DynamoDB and Kinesis). Detailed below.
    """
    state: pulumi.Output[str] = pulumi.output_property("state")
    """
    The state of the event source mapping.
    """
    state_transition_reason: pulumi.Output[str] = pulumi.output_property("stateTransitionReason")
    """
    The reason the event source mapping is in its current state.
    """
    uuid: pulumi.Output[str] = pulumi.output_property("uuid")
    """
    The UUID of the created event source mapping.
    """
    # pylint: disable=no-self-argument
    def __init__(__self__, resource_name, opts: Optional[pulumi.ResourceOptions] = None, batch_size=None, bisect_batch_on_function_error=None, destination_config=None, enabled=None, event_source_arn=None, function_name=None, maximum_batching_window_in_seconds=None, maximum_record_age_in_seconds=None, maximum_retry_attempts=None, parallelization_factor=None, starting_position=None, starting_position_timestamp=None, __props__=None, __name__=None, __opts__=None) -> None:
        """
        Provides a Lambda event source mapping. This allows Lambda functions to get events from Kinesis, DynamoDB and SQS.

        For information about Lambda and how to use it, see [What is AWS Lambda?](http://docs.aws.amazon.com/lambda/latest/dg/welcome.html).
        For information about event source mappings, see [CreateEventSourceMapping](http://docs.aws.amazon.com/lambda/latest/dg/API_CreateEventSourceMapping.html) in the API docs.

        ## Example Usage
        ### DynamoDB

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.lambda_.EventSourceMapping("example",
            event_source_arn=aws_dynamodb_table["example"]["stream_arn"],
            function_name=aws_lambda_function["example"]["arn"],
            starting_position="LATEST")
        ```
        ### Kinesis

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.lambda_.EventSourceMapping("example",
            event_source_arn=aws_kinesis_stream["example"]["arn"],
            function_name=aws_lambda_function["example"]["arn"],
            starting_position="LATEST")
        ```
        ### SQS

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.lambda_.EventSourceMapping("example",
            event_source_arn=aws_sqs_queue["sqs_queue_test"]["arn"],
            function_name=aws_lambda_function["example"]["arn"])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[float] batch_size: The largest number of records that Lambda will retrieve from your event source at the time of invocation. Defaults to `100` for DynamoDB and Kinesis, `10` for SQS.
        :param pulumi.Input[bool] enabled: Determines if the mapping will be enabled on creation. Defaults to `true`.
        :param pulumi.Input[str] event_source_arn: The event source ARN - can be a Kinesis stream, DynamoDB stream, or SQS queue.
        :param pulumi.Input[str] function_name: The name or the ARN of the Lambda function that will be subscribing to events.
        :param pulumi.Input[float] maximum_batching_window_in_seconds: The maximum amount of time to gather records before invoking the function, in seconds.  Records will continue to buffer until either `maximum_batching_window_in_seconds` expires or `batch_size` has been met. Defaults to as soon as records are available in the stream. If the batch it reads from the stream only has one record in it, Lambda only sends one record to the function.
        :param pulumi.Input[str] starting_position: The position in the stream where AWS Lambda should start reading. Must be one of `AT_TIMESTAMP` (Kinesis only), `LATEST` or `TRIM_HORIZON` if getting events from Kinesis or DynamoDB. Must not be provided if getting events from SQS. More information about these positions can be found in the [AWS DynamoDB Streams API Reference](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_GetShardIterator.html) and [AWS Kinesis API Reference](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetShardIterator.html#Kinesis-GetShardIterator-request-ShardIteratorType).
        :param pulumi.Input[str] starting_position_timestamp: A timestamp in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8) of the data record which to start reading when using `starting_position` set to `AT_TIMESTAMP`. If a record with this exact timestamp does not exist, the next later record is chosen. If the timestamp is older than the current trim horizon, the oldest available record is chosen.
               * `parallelization_factor`: - (Optional) The number of batches to process from each shard concurrently. Only available for stream sources (DynamoDB and Kinesis). Minimum and default of 1, maximum of 10.
               * `maximum_retry_attempts`: - (Optional) The maximum number of times to retry when the function returns an error. Only available for stream sources (DynamoDB and Kinesis). Minimum of 0, maximum and default of 10000.
               * `maximum_record_age_in_seconds`: - (Optional) The maximum age of a record that Lambda sends to a function for processing. Only available for stream sources (DynamoDB and Kinesis). Minimum of 60, maximum and default of 604800.
               * `bisect_batch_on_function_error`: - (Optional) If the function returns an error, split the batch in two and retry. Only available for stream sources (DynamoDB and Kinesis). Defaults to `false`.
               * `destination_config`: - (Optional) An Amazon SQS queue or Amazon SNS topic destination for failed records. Only available for stream sources (DynamoDB and Kinesis). Detailed below.
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

            __props__['batch_size'] = batch_size
            __props__['bisect_batch_on_function_error'] = bisect_batch_on_function_error
            __props__['destination_config'] = destination_config
            __props__['enabled'] = enabled
            if event_source_arn is None:
                raise TypeError("Missing required property 'event_source_arn'")
            __props__['event_source_arn'] = event_source_arn
            if function_name is None:
                raise TypeError("Missing required property 'function_name'")
            __props__['function_name'] = function_name
            __props__['maximum_batching_window_in_seconds'] = maximum_batching_window_in_seconds
            __props__['maximum_record_age_in_seconds'] = maximum_record_age_in_seconds
            __props__['maximum_retry_attempts'] = maximum_retry_attempts
            __props__['parallelization_factor'] = parallelization_factor
            __props__['starting_position'] = starting_position
            __props__['starting_position_timestamp'] = starting_position_timestamp
            __props__['function_arn'] = None
            __props__['last_modified'] = None
            __props__['last_processing_result'] = None
            __props__['state'] = None
            __props__['state_transition_reason'] = None
            __props__['uuid'] = None
        super(EventSourceMapping, __self__).__init__(
            'aws:lambda/eventSourceMapping:EventSourceMapping',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, batch_size=None, bisect_batch_on_function_error=None, destination_config=None, enabled=None, event_source_arn=None, function_arn=None, function_name=None, last_modified=None, last_processing_result=None, maximum_batching_window_in_seconds=None, maximum_record_age_in_seconds=None, maximum_retry_attempts=None, parallelization_factor=None, starting_position=None, starting_position_timestamp=None, state=None, state_transition_reason=None, uuid=None):
        """
        Get an existing EventSourceMapping resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[float] batch_size: The largest number of records that Lambda will retrieve from your event source at the time of invocation. Defaults to `100` for DynamoDB and Kinesis, `10` for SQS.
        :param pulumi.Input[bool] enabled: Determines if the mapping will be enabled on creation. Defaults to `true`.
        :param pulumi.Input[str] event_source_arn: The event source ARN - can be a Kinesis stream, DynamoDB stream, or SQS queue.
        :param pulumi.Input[str] function_arn: The the ARN of the Lambda function the event source mapping is sending events to. (Note: this is a computed value that differs from `function_name` above.)
        :param pulumi.Input[str] function_name: The name or the ARN of the Lambda function that will be subscribing to events.
        :param pulumi.Input[str] last_modified: The date this resource was last modified.
        :param pulumi.Input[str] last_processing_result: The result of the last AWS Lambda invocation of your Lambda function.
        :param pulumi.Input[float] maximum_batching_window_in_seconds: The maximum amount of time to gather records before invoking the function, in seconds.  Records will continue to buffer until either `maximum_batching_window_in_seconds` expires or `batch_size` has been met. Defaults to as soon as records are available in the stream. If the batch it reads from the stream only has one record in it, Lambda only sends one record to the function.
        :param pulumi.Input[str] starting_position: The position in the stream where AWS Lambda should start reading. Must be one of `AT_TIMESTAMP` (Kinesis only), `LATEST` or `TRIM_HORIZON` if getting events from Kinesis or DynamoDB. Must not be provided if getting events from SQS. More information about these positions can be found in the [AWS DynamoDB Streams API Reference](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_GetShardIterator.html) and [AWS Kinesis API Reference](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetShardIterator.html#Kinesis-GetShardIterator-request-ShardIteratorType).
        :param pulumi.Input[str] starting_position_timestamp: A timestamp in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8) of the data record which to start reading when using `starting_position` set to `AT_TIMESTAMP`. If a record with this exact timestamp does not exist, the next later record is chosen. If the timestamp is older than the current trim horizon, the oldest available record is chosen.
               * `parallelization_factor`: - (Optional) The number of batches to process from each shard concurrently. Only available for stream sources (DynamoDB and Kinesis). Minimum and default of 1, maximum of 10.
               * `maximum_retry_attempts`: - (Optional) The maximum number of times to retry when the function returns an error. Only available for stream sources (DynamoDB and Kinesis). Minimum of 0, maximum and default of 10000.
               * `maximum_record_age_in_seconds`: - (Optional) The maximum age of a record that Lambda sends to a function for processing. Only available for stream sources (DynamoDB and Kinesis). Minimum of 60, maximum and default of 604800.
               * `bisect_batch_on_function_error`: - (Optional) If the function returns an error, split the batch in two and retry. Only available for stream sources (DynamoDB and Kinesis). Defaults to `false`.
               * `destination_config`: - (Optional) An Amazon SQS queue or Amazon SNS topic destination for failed records. Only available for stream sources (DynamoDB and Kinesis). Detailed below.
        :param pulumi.Input[str] state: The state of the event source mapping.
        :param pulumi.Input[str] state_transition_reason: The reason the event source mapping is in its current state.
        :param pulumi.Input[str] uuid: The UUID of the created event source mapping.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["batch_size"] = batch_size
        __props__["bisect_batch_on_function_error"] = bisect_batch_on_function_error
        __props__["destination_config"] = destination_config
        __props__["enabled"] = enabled
        __props__["event_source_arn"] = event_source_arn
        __props__["function_arn"] = function_arn
        __props__["function_name"] = function_name
        __props__["last_modified"] = last_modified
        __props__["last_processing_result"] = last_processing_result
        __props__["maximum_batching_window_in_seconds"] = maximum_batching_window_in_seconds
        __props__["maximum_record_age_in_seconds"] = maximum_record_age_in_seconds
        __props__["maximum_retry_attempts"] = maximum_retry_attempts
        __props__["parallelization_factor"] = parallelization_factor
        __props__["starting_position"] = starting_position
        __props__["starting_position_timestamp"] = starting_position_timestamp
        __props__["state"] = state
        __props__["state_transition_reason"] = state_transition_reason
        __props__["uuid"] = uuid
        return EventSourceMapping(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

