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


class DataSource(pulumi.CustomResource):
    api_id: pulumi.Output[str] = pulumi.output_property("apiId")
    """
    The API ID for the GraphQL API for the DataSource.
    """
    arn: pulumi.Output[str] = pulumi.output_property("arn")
    """
    The ARN
    """
    description: pulumi.Output[Optional[str]] = pulumi.output_property("description")
    """
    A description of the DataSource.
    """
    dynamodb_config: pulumi.Output[Optional['outputs.DataSourceDynamodbConfig']] = pulumi.output_property("dynamodbConfig")
    """
    DynamoDB settings. See below
    """
    elasticsearch_config: pulumi.Output[Optional['outputs.DataSourceElasticsearchConfig']] = pulumi.output_property("elasticsearchConfig")
    """
    Amazon Elasticsearch settings. See below
    """
    http_config: pulumi.Output[Optional['outputs.DataSourceHttpConfig']] = pulumi.output_property("httpConfig")
    """
    HTTP settings. See below
    """
    lambda_config: pulumi.Output[Optional['outputs.DataSourceLambdaConfig']] = pulumi.output_property("lambdaConfig")
    """
    AWS Lambda settings. See below
    """
    name: pulumi.Output[str] = pulumi.output_property("name")
    """
    A user-supplied name for the DataSource.
    """
    service_role_arn: pulumi.Output[Optional[str]] = pulumi.output_property("serviceRoleArn")
    """
    The IAM service role ARN for the data source.
    """
    type: pulumi.Output[str] = pulumi.output_property("type")
    """
    The type of the DataSource. Valid values: `AWS_LAMBDA`, `AMAZON_DYNAMODB`, `AMAZON_ELASTICSEARCH`, `HTTP`, `NONE`.
    """
    # pylint: disable=no-self-argument
    def __init__(__self__, resource_name, opts: Optional[pulumi.ResourceOptions] = None, api_id=None, description=None, dynamodb_config=None, elasticsearch_config=None, http_config=None, lambda_config=None, name=None, service_role_arn=None, type=None, __props__=None, __name__=None, __opts__=None) -> None:
        """
        Provides an AppSync DataSource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example_table = aws.dynamodb.Table("exampleTable",
            attributes=[{
                "name": "UserId",
                "type": "S",
            }],
            hash_key="UserId",
            read_capacity=1,
            write_capacity=1)
        example_role = aws.iam.Role("exampleRole", assume_role_policy=\"\"\"{
          "Version": "2012-10-17",
          "Statement": [
            {
              "Action": "sts:AssumeRole",
              "Principal": {
                "Service": "appsync.amazonaws.com"
              },
              "Effect": "Allow"
            }
          ]
        }

        \"\"\")
        example_role_policy = aws.iam.RolePolicy("exampleRolePolicy",
            policy=example_table.arn.apply(lambda arn: f\"\"\"{{
          "Version": "2012-10-17",
          "Statement": [
            {{
              "Action": [
                "dynamodb:*"
              ],
              "Effect": "Allow",
              "Resource": [
                "{arn}"
              ]
            }}
          ]
        }}

        \"\"\"),
            role=example_role.id)
        example_graph_ql_api = aws.appsync.GraphQLApi("exampleGraphQLApi", authentication_type="API_KEY")
        example_data_source = aws.appsync.DataSource("exampleDataSource",
            api_id=example_graph_ql_api.id,
            dynamodb_config={
                "table_name": example_table.name,
            },
            service_role_arn=example_role.arn,
            type="AMAZON_DYNAMODB")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_id: The API ID for the GraphQL API for the DataSource.
        :param pulumi.Input[str] description: A description of the DataSource.
        :param pulumi.Input['DataSourceDynamodbConfigArgs'] dynamodb_config: DynamoDB settings. See below
        :param pulumi.Input['DataSourceElasticsearchConfigArgs'] elasticsearch_config: Amazon Elasticsearch settings. See below
        :param pulumi.Input['DataSourceHttpConfigArgs'] http_config: HTTP settings. See below
        :param pulumi.Input['DataSourceLambdaConfigArgs'] lambda_config: AWS Lambda settings. See below
        :param pulumi.Input[str] name: A user-supplied name for the DataSource.
        :param pulumi.Input[str] service_role_arn: The IAM service role ARN for the data source.
        :param pulumi.Input[str] type: The type of the DataSource. Valid values: `AWS_LAMBDA`, `AMAZON_DYNAMODB`, `AMAZON_ELASTICSEARCH`, `HTTP`, `NONE`.
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

            if api_id is None:
                raise TypeError("Missing required property 'api_id'")
            __props__['api_id'] = api_id
            __props__['description'] = description
            __props__['dynamodb_config'] = dynamodb_config
            __props__['elasticsearch_config'] = elasticsearch_config
            __props__['http_config'] = http_config
            __props__['lambda_config'] = lambda_config
            __props__['name'] = name
            __props__['service_role_arn'] = service_role_arn
            if type is None:
                raise TypeError("Missing required property 'type'")
            __props__['type'] = type
            __props__['arn'] = None
        super(DataSource, __self__).__init__(
            'aws:appsync/dataSource:DataSource',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, api_id=None, arn=None, description=None, dynamodb_config=None, elasticsearch_config=None, http_config=None, lambda_config=None, name=None, service_role_arn=None, type=None):
        """
        Get an existing DataSource resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_id: The API ID for the GraphQL API for the DataSource.
        :param pulumi.Input[str] arn: The ARN
        :param pulumi.Input[str] description: A description of the DataSource.
        :param pulumi.Input['DataSourceDynamodbConfigArgs'] dynamodb_config: DynamoDB settings. See below
        :param pulumi.Input['DataSourceElasticsearchConfigArgs'] elasticsearch_config: Amazon Elasticsearch settings. See below
        :param pulumi.Input['DataSourceHttpConfigArgs'] http_config: HTTP settings. See below
        :param pulumi.Input['DataSourceLambdaConfigArgs'] lambda_config: AWS Lambda settings. See below
        :param pulumi.Input[str] name: A user-supplied name for the DataSource.
        :param pulumi.Input[str] service_role_arn: The IAM service role ARN for the data source.
        :param pulumi.Input[str] type: The type of the DataSource. Valid values: `AWS_LAMBDA`, `AMAZON_DYNAMODB`, `AMAZON_ELASTICSEARCH`, `HTTP`, `NONE`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["api_id"] = api_id
        __props__["arn"] = arn
        __props__["description"] = description
        __props__["dynamodb_config"] = dynamodb_config
        __props__["elasticsearch_config"] = elasticsearch_config
        __props__["http_config"] = http_config
        __props__["lambda_config"] = lambda_config
        __props__["name"] = name
        __props__["service_role_arn"] = service_role_arn
        __props__["type"] = type
        return DataSource(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

