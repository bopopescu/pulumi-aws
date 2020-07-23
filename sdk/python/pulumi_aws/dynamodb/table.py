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


class Table(pulumi.CustomResource):
    arn: pulumi.Output[str] = pulumi.output_property("arn")
    """
    The arn of the table
    """
    attributes: pulumi.Output[List['outputs.TableAttribute']] = pulumi.output_property("attributes")
    """
    List of nested attribute definitions. Only required for `hash_key` and `range_key` attributes. Each attribute has two properties:
    """
    billing_mode: pulumi.Output[Optional[str]] = pulumi.output_property("billingMode")
    """
    Controls how you are charged for read and write throughput and how you manage capacity. The valid values are `PROVISIONED` and `PAY_PER_REQUEST`. Defaults to `PROVISIONED`.
    """
    global_secondary_indexes: pulumi.Output[Optional[List['outputs.TableGlobalSecondaryIndex']]] = pulumi.output_property("globalSecondaryIndexes")
    """
    Describe a GSI for the table;
    subject to the normal limits on the number of GSIs, projected
    attributes, etc.
    """
    hash_key: pulumi.Output[str] = pulumi.output_property("hashKey")
    """
    The name of the hash key in the index; must be
    defined as an attribute in the resource.
    """
    local_secondary_indexes: pulumi.Output[Optional[List['outputs.TableLocalSecondaryIndex']]] = pulumi.output_property("localSecondaryIndexes")
    """
    Describe an LSI on the table;
    these can only be allocated *at creation* so you cannot change this
    definition after you have created the resource.
    """
    name: pulumi.Output[str] = pulumi.output_property("name")
    """
    The name of the index
    """
    point_in_time_recovery: pulumi.Output['outputs.TablePointInTimeRecovery'] = pulumi.output_property("pointInTimeRecovery")
    """
    Point-in-time recovery options.
    """
    range_key: pulumi.Output[Optional[str]] = pulumi.output_property("rangeKey")
    """
    The name of the range key; must be defined
    """
    read_capacity: pulumi.Output[Optional[float]] = pulumi.output_property("readCapacity")
    """
    The number of read units for this index. Must be set if billing_mode is set to PROVISIONED.
    """
    replicas: pulumi.Output[Optional[List['outputs.TableReplica']]] = pulumi.output_property("replicas")
    """
    Configuration block(s) with [DynamoDB Global Tables V2 (version 2019.11.21)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables.V2.html) replication configurations. Detailed below.
    """
    server_side_encryption: pulumi.Output['outputs.TableServerSideEncryption'] = pulumi.output_property("serverSideEncryption")
    """
    Encryption at rest options. AWS DynamoDB tables are automatically encrypted at rest with an AWS owned Customer Master Key if this argument isn't specified.
    """
    stream_arn: pulumi.Output[str] = pulumi.output_property("streamArn")
    """
    The ARN of the Table Stream. Only available when `stream_enabled = true`
    """
    stream_enabled: pulumi.Output[Optional[bool]] = pulumi.output_property("streamEnabled")
    """
    Indicates whether Streams are to be enabled (true) or disabled (false).
    """
    stream_label: pulumi.Output[str] = pulumi.output_property("streamLabel")
    """
    A timestamp, in ISO 8601 format, for this stream. Note that this timestamp is not
    a unique identifier for the stream on its own. However, the combination of AWS customer ID,
    table name and this field is guaranteed to be unique.
    It can be used for creating CloudWatch Alarms. Only available when `stream_enabled = true`
    """
    stream_view_type: pulumi.Output[str] = pulumi.output_property("streamViewType")
    """
    When an item in the table is modified, StreamViewType determines what information is written to the table's stream. Valid values are `KEYS_ONLY`, `NEW_IMAGE`, `OLD_IMAGE`, `NEW_AND_OLD_IMAGES`.
    """
    tags: pulumi.Output[Optional[Dict[str, str]]] = pulumi.output_property("tags")
    """
    A map of tags to populate on the created table.
    """
    ttl: pulumi.Output[Optional['outputs.TableTtl']] = pulumi.output_property("ttl")
    """
    Defines ttl, has two properties, and can only be specified once:
    """
    write_capacity: pulumi.Output[Optional[float]] = pulumi.output_property("writeCapacity")
    """
    The number of write units for this index. Must be set if billing_mode is set to PROVISIONED.
    """
    # pylint: disable=no-self-argument
    def __init__(__self__, resource_name, opts: Optional[pulumi.ResourceOptions] = None, attributes=None, billing_mode=None, global_secondary_indexes=None, hash_key=None, local_secondary_indexes=None, name=None, point_in_time_recovery=None, range_key=None, read_capacity=None, replicas=None, server_side_encryption=None, stream_enabled=None, stream_view_type=None, tags=None, ttl=None, write_capacity=None, __props__=None, __name__=None, __opts__=None) -> None:
        """
        Provides a DynamoDB table resource

        > **Note:** It is recommended to use [`ignoreChanges`](https://www.pulumi.com/docs/intro/concepts/programming-model/#ignorechanges) for `read_capacity` and/or `write_capacity` if there's `autoscaling policy` attached to the table.

        ## Example Usage

        The following dynamodb table description models the table and GSI shown
        in the [AWS SDK example documentation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GSI.html)

        ```python
        import pulumi
        import pulumi_aws as aws

        basic_dynamodb_table = aws.dynamodb.Table("basic-dynamodb-table",
            attributes=[
                {
                    "name": "UserId",
                    "type": "S",
                },
                {
                    "name": "GameTitle",
                    "type": "S",
                },
                {
                    "name": "TopScore",
                    "type": "N",
                },
            ],
            billing_mode="PROVISIONED",
            global_secondary_indexes=[{
                "hash_key": "GameTitle",
                "name": "GameTitleIndex",
                "nonKeyAttributes": ["UserId"],
                "projectionType": "INCLUDE",
                "range_key": "TopScore",
                "read_capacity": 10,
                "write_capacity": 10,
            }],
            hash_key="UserId",
            range_key="GameTitle",
            read_capacity=20,
            tags={
                "Environment": "production",
                "Name": "dynamodb-table-1",
            },
            ttl={
                "attributeName": "TimeToExist",
                "enabled": False,
            },
            write_capacity=20)
        ```
        ### Global Tables

        This resource implements support for [DynamoDB Global Tables V2 (version 2019.11.21)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables.V2.html) via `replica` configuration blocks. For working with [DynamoDB Global Tables V1 (version 2017.11.29)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables.V1.html), see the `dynamodb.GlobalTable` resource.

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.dynamodb.Table("example",
            attributes=[{
                "name": "TestTableHashKey",
                "type": "S",
            }],
            billing_mode="PAY_PER_REQUEST",
            hash_key="TestTableHashKey",
            replicas=[
                {
                    "regionName": "us-east-2",
                },
                {
                    "regionName": "us-west-2",
                },
            ],
            stream_enabled=True,
            stream_view_type="NEW_AND_OLD_IMAGES")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[List[pulumi.Input['TableAttributeArgs']]] attributes: List of nested attribute definitions. Only required for `hash_key` and `range_key` attributes. Each attribute has two properties:
        :param pulumi.Input[str] billing_mode: Controls how you are charged for read and write throughput and how you manage capacity. The valid values are `PROVISIONED` and `PAY_PER_REQUEST`. Defaults to `PROVISIONED`.
        :param pulumi.Input[List[pulumi.Input['TableGlobalSecondaryIndexArgs']]] global_secondary_indexes: Describe a GSI for the table;
               subject to the normal limits on the number of GSIs, projected
               attributes, etc.
        :param pulumi.Input[str] hash_key: The name of the hash key in the index; must be
               defined as an attribute in the resource.
        :param pulumi.Input[List[pulumi.Input['TableLocalSecondaryIndexArgs']]] local_secondary_indexes: Describe an LSI on the table;
               these can only be allocated *at creation* so you cannot change this
               definition after you have created the resource.
        :param pulumi.Input[str] name: The name of the index
        :param pulumi.Input['TablePointInTimeRecoveryArgs'] point_in_time_recovery: Point-in-time recovery options.
        :param pulumi.Input[str] range_key: The name of the range key; must be defined
        :param pulumi.Input[float] read_capacity: The number of read units for this index. Must be set if billing_mode is set to PROVISIONED.
        :param pulumi.Input[List[pulumi.Input['TableReplicaArgs']]] replicas: Configuration block(s) with [DynamoDB Global Tables V2 (version 2019.11.21)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables.V2.html) replication configurations. Detailed below.
        :param pulumi.Input['TableServerSideEncryptionArgs'] server_side_encryption: Encryption at rest options. AWS DynamoDB tables are automatically encrypted at rest with an AWS owned Customer Master Key if this argument isn't specified.
        :param pulumi.Input[bool] stream_enabled: Indicates whether Streams are to be enabled (true) or disabled (false).
        :param pulumi.Input[str] stream_view_type: When an item in the table is modified, StreamViewType determines what information is written to the table's stream. Valid values are `KEYS_ONLY`, `NEW_IMAGE`, `OLD_IMAGE`, `NEW_AND_OLD_IMAGES`.
        :param pulumi.Input[Dict[str, pulumi.Input[str]]] tags: A map of tags to populate on the created table.
        :param pulumi.Input['TableTtlArgs'] ttl: Defines ttl, has two properties, and can only be specified once:
        :param pulumi.Input[float] write_capacity: The number of write units for this index. Must be set if billing_mode is set to PROVISIONED.
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

            if attributes is None:
                raise TypeError("Missing required property 'attributes'")
            __props__['attributes'] = attributes
            __props__['billing_mode'] = billing_mode
            __props__['global_secondary_indexes'] = global_secondary_indexes
            if hash_key is None:
                raise TypeError("Missing required property 'hash_key'")
            __props__['hash_key'] = hash_key
            __props__['local_secondary_indexes'] = local_secondary_indexes
            __props__['name'] = name
            __props__['point_in_time_recovery'] = point_in_time_recovery
            __props__['range_key'] = range_key
            __props__['read_capacity'] = read_capacity
            __props__['replicas'] = replicas
            __props__['server_side_encryption'] = server_side_encryption
            __props__['stream_enabled'] = stream_enabled
            __props__['stream_view_type'] = stream_view_type
            __props__['tags'] = tags
            __props__['ttl'] = ttl
            __props__['write_capacity'] = write_capacity
            __props__['arn'] = None
            __props__['stream_arn'] = None
            __props__['stream_label'] = None
        super(Table, __self__).__init__(
            'aws:dynamodb/table:Table',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, arn=None, attributes=None, billing_mode=None, global_secondary_indexes=None, hash_key=None, local_secondary_indexes=None, name=None, point_in_time_recovery=None, range_key=None, read_capacity=None, replicas=None, server_side_encryption=None, stream_arn=None, stream_enabled=None, stream_label=None, stream_view_type=None, tags=None, ttl=None, write_capacity=None):
        """
        Get an existing Table resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The arn of the table
        :param pulumi.Input[List[pulumi.Input['TableAttributeArgs']]] attributes: List of nested attribute definitions. Only required for `hash_key` and `range_key` attributes. Each attribute has two properties:
        :param pulumi.Input[str] billing_mode: Controls how you are charged for read and write throughput and how you manage capacity. The valid values are `PROVISIONED` and `PAY_PER_REQUEST`. Defaults to `PROVISIONED`.
        :param pulumi.Input[List[pulumi.Input['TableGlobalSecondaryIndexArgs']]] global_secondary_indexes: Describe a GSI for the table;
               subject to the normal limits on the number of GSIs, projected
               attributes, etc.
        :param pulumi.Input[str] hash_key: The name of the hash key in the index; must be
               defined as an attribute in the resource.
        :param pulumi.Input[List[pulumi.Input['TableLocalSecondaryIndexArgs']]] local_secondary_indexes: Describe an LSI on the table;
               these can only be allocated *at creation* so you cannot change this
               definition after you have created the resource.
        :param pulumi.Input[str] name: The name of the index
        :param pulumi.Input['TablePointInTimeRecoveryArgs'] point_in_time_recovery: Point-in-time recovery options.
        :param pulumi.Input[str] range_key: The name of the range key; must be defined
        :param pulumi.Input[float] read_capacity: The number of read units for this index. Must be set if billing_mode is set to PROVISIONED.
        :param pulumi.Input[List[pulumi.Input['TableReplicaArgs']]] replicas: Configuration block(s) with [DynamoDB Global Tables V2 (version 2019.11.21)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables.V2.html) replication configurations. Detailed below.
        :param pulumi.Input['TableServerSideEncryptionArgs'] server_side_encryption: Encryption at rest options. AWS DynamoDB tables are automatically encrypted at rest with an AWS owned Customer Master Key if this argument isn't specified.
        :param pulumi.Input[str] stream_arn: The ARN of the Table Stream. Only available when `stream_enabled = true`
        :param pulumi.Input[bool] stream_enabled: Indicates whether Streams are to be enabled (true) or disabled (false).
        :param pulumi.Input[str] stream_label: A timestamp, in ISO 8601 format, for this stream. Note that this timestamp is not
               a unique identifier for the stream on its own. However, the combination of AWS customer ID,
               table name and this field is guaranteed to be unique.
               It can be used for creating CloudWatch Alarms. Only available when `stream_enabled = true`
        :param pulumi.Input[str] stream_view_type: When an item in the table is modified, StreamViewType determines what information is written to the table's stream. Valid values are `KEYS_ONLY`, `NEW_IMAGE`, `OLD_IMAGE`, `NEW_AND_OLD_IMAGES`.
        :param pulumi.Input[Dict[str, pulumi.Input[str]]] tags: A map of tags to populate on the created table.
        :param pulumi.Input['TableTtlArgs'] ttl: Defines ttl, has two properties, and can only be specified once:
        :param pulumi.Input[float] write_capacity: The number of write units for this index. Must be set if billing_mode is set to PROVISIONED.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["attributes"] = attributes
        __props__["billing_mode"] = billing_mode
        __props__["global_secondary_indexes"] = global_secondary_indexes
        __props__["hash_key"] = hash_key
        __props__["local_secondary_indexes"] = local_secondary_indexes
        __props__["name"] = name
        __props__["point_in_time_recovery"] = point_in_time_recovery
        __props__["range_key"] = range_key
        __props__["read_capacity"] = read_capacity
        __props__["replicas"] = replicas
        __props__["server_side_encryption"] = server_side_encryption
        __props__["stream_arn"] = stream_arn
        __props__["stream_enabled"] = stream_enabled
        __props__["stream_label"] = stream_label
        __props__["stream_view_type"] = stream_view_type
        __props__["tags"] = tags
        __props__["ttl"] = ttl
        __props__["write_capacity"] = write_capacity
        return Table(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

