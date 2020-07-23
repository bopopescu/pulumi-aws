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


class Domain(pulumi.CustomResource):
    access_policies: pulumi.Output[str] = pulumi.output_property("accessPolicies")
    """
    IAM policy document specifying the access policies for the domain
    """
    advanced_options: pulumi.Output[Dict[str, str]] = pulumi.output_property("advancedOptions")
    """
    Key-value string pairs to specify advanced configuration options.
    Note that the values for these configuration options must be strings (wrapped in quotes) or they
    may be wrong and cause a perpetual diff, causing this provider to want to recreate your Elasticsearch
    domain on every apply.
    """
    advanced_security_options: pulumi.Output['outputs.DomainAdvancedSecurityOptions'] = pulumi.output_property("advancedSecurityOptions")
    """
    Options for [fine-grained access control](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/fgac.html). See below for more details.
    """
    arn: pulumi.Output[str] = pulumi.output_property("arn")
    """
    Amazon Resource Name (ARN) of the domain.
    """
    cluster_config: pulumi.Output['outputs.DomainClusterConfig'] = pulumi.output_property("clusterConfig")
    """
    Cluster configuration of the domain, see below.
    """
    cognito_options: pulumi.Output[Optional['outputs.DomainCognitoOptions']] = pulumi.output_property("cognitoOptions")
    domain_endpoint_options: pulumi.Output['outputs.DomainDomainEndpointOptions'] = pulumi.output_property("domainEndpointOptions")
    """
    Domain endpoint HTTP(S) related options. See below.
    """
    domain_id: pulumi.Output[str] = pulumi.output_property("domainId")
    """
    Unique identifier for the domain.
    """
    domain_name: pulumi.Output[str] = pulumi.output_property("domainName")
    """
    Name of the domain.
    """
    ebs_options: pulumi.Output['outputs.DomainEbsOptions'] = pulumi.output_property("ebsOptions")
    """
    EBS related options, may be required based on chosen [instance size](https://aws.amazon.com/elasticsearch-service/pricing/). See below.
    """
    elasticsearch_version: pulumi.Output[Optional[str]] = pulumi.output_property("elasticsearchVersion")
    """
    The version of Elasticsearch to deploy. Defaults to `1.5`
    """
    encrypt_at_rest: pulumi.Output['outputs.DomainEncryptAtRest'] = pulumi.output_property("encryptAtRest")
    """
    Encrypt at rest options. Only available for [certain instance types](http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/aes-supported-instance-types.html). See below.
    """
    endpoint: pulumi.Output[str] = pulumi.output_property("endpoint")
    """
    Domain-specific endpoint used to submit index, search, and data upload requests.
    """
    kibana_endpoint: pulumi.Output[str] = pulumi.output_property("kibanaEndpoint")
    """
    Domain-specific endpoint for kibana without https scheme.
    * `vpc_options.0.availability_zones` - If the domain was created inside a VPC, the names of the availability zones the configured `subnet_ids` were created inside.
    * `vpc_options.0.vpc_id` - If the domain was created inside a VPC, the ID of the VPC.
    """
    log_publishing_options: pulumi.Output[Optional[List['outputs.DomainLogPublishingOption']]] = pulumi.output_property("logPublishingOptions")
    """
    Options for publishing slow logs to CloudWatch Logs.
    """
    node_to_node_encryption: pulumi.Output['outputs.DomainNodeToNodeEncryption'] = pulumi.output_property("nodeToNodeEncryption")
    """
    Node-to-node encryption options. See below.
    """
    snapshot_options: pulumi.Output[Optional['outputs.DomainSnapshotOptions']] = pulumi.output_property("snapshotOptions")
    """
    Snapshot related options, see below.
    """
    tags: pulumi.Output[Optional[Dict[str, str]]] = pulumi.output_property("tags")
    """
    A map of tags to assign to the resource
    """
    vpc_options: pulumi.Output[Optional['outputs.DomainVpcOptions']] = pulumi.output_property("vpcOptions")
    """
    VPC related options, see below. Adding or removing this configuration forces a new resource ([documentation](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html#es-vpc-limitations)).
    """
    # pylint: disable=no-self-argument
    def __init__(__self__, resource_name, opts: Optional[pulumi.ResourceOptions] = None, access_policies=None, advanced_options=None, advanced_security_options=None, cluster_config=None, cognito_options=None, domain_endpoint_options=None, domain_name=None, ebs_options=None, elasticsearch_version=None, encrypt_at_rest=None, log_publishing_options=None, node_to_node_encryption=None, snapshot_options=None, tags=None, vpc_options=None, __props__=None, __name__=None, __opts__=None) -> None:
        """
        Manages an AWS Elasticsearch Domain.

        ## Example Usage
        ### Basic Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.elasticsearch.Domain("example",
            cluster_config={
                "instance_type": "r4.large.elasticsearch",
            },
            elasticsearch_version="1.5",
            snapshot_options={
                "automatedSnapshotStartHour": 23,
            },
            tags={
                "Domain": "TestDomain",
            })
        ```
        ### Access Policy

        > See also: `elasticsearch.DomainPolicy` resource

        ```python
        import pulumi
        import pulumi_aws as aws

        config = pulumi.Config()
        domain = config.get("domain")
        if domain is None:
            domain = "tf-test"
        current_region = aws.get_region()
        current_caller_identity = aws.get_caller_identity()
        example = aws.elasticsearch.Domain("example", access_policies=f\"\"\"{{
          "Version": "2012-10-17",
          "Statement": [
            {{
              "Action": "es:*",
              "Principal": "*",
              "Effect": "Allow",
              "Resource": "arn:aws:es:{current_region.name}:{current_caller_identity.account_id}:domain/{domain}/*",
              "Condition": {{
                "IpAddress": {{"aws:SourceIp": ["66.193.100.22/32"]}}
              }}
            }}
          ]
        }}

        \"\"\")
        ```
        ### Log Publishing to CloudWatch Logs

        ```python
        import pulumi
        import pulumi_aws as aws

        example_log_group = aws.cloudwatch.LogGroup("exampleLogGroup")
        example_log_resource_policy = aws.cloudwatch.LogResourcePolicy("exampleLogResourcePolicy",
            policy_document=\"\"\"{
          "Version": "2012-10-17",
          "Statement": [
            {
              "Effect": "Allow",
              "Principal": {
                "Service": "es.amazonaws.com"
              },
              "Action": [
                "logs:PutLogEvents",
                "logs:PutLogEventsBatch",
                "logs:CreateLogStream"
              ],
              "Resource": "arn:aws:logs:*"
            }
          ]
        }

        \"\"\",
            policy_name="example")
        example_domain = aws.elasticsearch.Domain("exampleDomain", log_publishing_options=[{
            "cloudwatch_log_group_arn": example_log_group.arn,
            "logType": "INDEX_SLOW_LOGS",
        }])
        ```
        ### VPC based ES

        ```python
        import pulumi
        import pulumi_aws as aws

        config = pulumi.Config()
        vpc = config.require_object("vpc")
        domain = config.get("domain")
        if domain is None:
            domain = "tf-test"
        selected_vpc = aws.ec2.get_vpc(tags={
            "Name": vpc,
        })
        selected_subnet_ids = aws.ec2.get_subnet_ids(tags={
                "Tier": "private",
            },
            vpc_id=selected_vpc.id)
        current_region = aws.get_region()
        current_caller_identity = aws.get_caller_identity()
        es_security_group = aws.ec2.SecurityGroup("esSecurityGroup",
            description="Managed by Pulumi",
            ingress=[{
                "cidr_blocks": [selected_vpc.cidr_block],
                "from_port": 443,
                "protocol": "tcp",
                "to_port": 443,
            }],
            vpc_id=selected_vpc.id)
        es_service_linked_role = aws.iam.ServiceLinkedRole("esServiceLinkedRole", aws_service_name="es.amazonaws.com")
        es_domain = aws.elasticsearch.Domain("esDomain",
            access_policies=f\"\"\"{{
        	"Version": "2012-10-17",
        	"Statement": [
        		{{
        			"Action": "es:*",
        			"Principal": "*",
        			"Effect": "Allow",
        			"Resource": "arn:aws:es:{current_region.name}:{current_caller_identity.account_id}:domain/{domain}/*"
        		}}
        	]
        }}

        \"\"\",
            advanced_options={
                "rest.action.multi.allow_explicit_index": "true",
            },
            cluster_config={
                "instance_type": "m4.large.elasticsearch",
            },
            elasticsearch_version="6.3",
            snapshot_options={
                "automatedSnapshotStartHour": 23,
            },
            tags={
                "Domain": "TestDomain",
            },
            vpc_options={
                "security_group_ids": [es_security_group.id],
                "subnet_ids": [
                    selected_subnet_ids.ids[0],
                    selected_subnet_ids.ids[1],
                ],
            },
            opts=ResourceOptions(depends_on=["aws_iam_service_linked_role.es"]))
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_policies: IAM policy document specifying the access policies for the domain
        :param pulumi.Input[Dict[str, pulumi.Input[str]]] advanced_options: Key-value string pairs to specify advanced configuration options.
               Note that the values for these configuration options must be strings (wrapped in quotes) or they
               may be wrong and cause a perpetual diff, causing this provider to want to recreate your Elasticsearch
               domain on every apply.
        :param pulumi.Input['DomainAdvancedSecurityOptionsArgs'] advanced_security_options: Options for [fine-grained access control](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/fgac.html). See below for more details.
        :param pulumi.Input['DomainClusterConfigArgs'] cluster_config: Cluster configuration of the domain, see below.
        :param pulumi.Input['DomainDomainEndpointOptionsArgs'] domain_endpoint_options: Domain endpoint HTTP(S) related options. See below.
        :param pulumi.Input[str] domain_name: Name of the domain.
        :param pulumi.Input['DomainEbsOptionsArgs'] ebs_options: EBS related options, may be required based on chosen [instance size](https://aws.amazon.com/elasticsearch-service/pricing/). See below.
        :param pulumi.Input[str] elasticsearch_version: The version of Elasticsearch to deploy. Defaults to `1.5`
        :param pulumi.Input['DomainEncryptAtRestArgs'] encrypt_at_rest: Encrypt at rest options. Only available for [certain instance types](http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/aes-supported-instance-types.html). See below.
        :param pulumi.Input[List[pulumi.Input['DomainLogPublishingOptionArgs']]] log_publishing_options: Options for publishing slow logs to CloudWatch Logs.
        :param pulumi.Input['DomainNodeToNodeEncryptionArgs'] node_to_node_encryption: Node-to-node encryption options. See below.
        :param pulumi.Input['DomainSnapshotOptionsArgs'] snapshot_options: Snapshot related options, see below.
        :param pulumi.Input[Dict[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource
        :param pulumi.Input['DomainVpcOptionsArgs'] vpc_options: VPC related options, see below. Adding or removing this configuration forces a new resource ([documentation](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html#es-vpc-limitations)).
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

            __props__['access_policies'] = access_policies
            __props__['advanced_options'] = advanced_options
            __props__['advanced_security_options'] = advanced_security_options
            __props__['cluster_config'] = cluster_config
            __props__['cognito_options'] = cognito_options
            __props__['domain_endpoint_options'] = domain_endpoint_options
            __props__['domain_name'] = domain_name
            __props__['ebs_options'] = ebs_options
            __props__['elasticsearch_version'] = elasticsearch_version
            __props__['encrypt_at_rest'] = encrypt_at_rest
            __props__['log_publishing_options'] = log_publishing_options
            __props__['node_to_node_encryption'] = node_to_node_encryption
            __props__['snapshot_options'] = snapshot_options
            __props__['tags'] = tags
            __props__['vpc_options'] = vpc_options
            __props__['arn'] = None
            __props__['domain_id'] = None
            __props__['endpoint'] = None
            __props__['kibana_endpoint'] = None
        super(Domain, __self__).__init__(
            'aws:elasticsearch/domain:Domain',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, access_policies=None, advanced_options=None, advanced_security_options=None, arn=None, cluster_config=None, cognito_options=None, domain_endpoint_options=None, domain_id=None, domain_name=None, ebs_options=None, elasticsearch_version=None, encrypt_at_rest=None, endpoint=None, kibana_endpoint=None, log_publishing_options=None, node_to_node_encryption=None, snapshot_options=None, tags=None, vpc_options=None):
        """
        Get an existing Domain resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_policies: IAM policy document specifying the access policies for the domain
        :param pulumi.Input[Dict[str, pulumi.Input[str]]] advanced_options: Key-value string pairs to specify advanced configuration options.
               Note that the values for these configuration options must be strings (wrapped in quotes) or they
               may be wrong and cause a perpetual diff, causing this provider to want to recreate your Elasticsearch
               domain on every apply.
        :param pulumi.Input['DomainAdvancedSecurityOptionsArgs'] advanced_security_options: Options for [fine-grained access control](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/fgac.html). See below for more details.
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN) of the domain.
        :param pulumi.Input['DomainClusterConfigArgs'] cluster_config: Cluster configuration of the domain, see below.
        :param pulumi.Input['DomainDomainEndpointOptionsArgs'] domain_endpoint_options: Domain endpoint HTTP(S) related options. See below.
        :param pulumi.Input[str] domain_id: Unique identifier for the domain.
        :param pulumi.Input[str] domain_name: Name of the domain.
        :param pulumi.Input['DomainEbsOptionsArgs'] ebs_options: EBS related options, may be required based on chosen [instance size](https://aws.amazon.com/elasticsearch-service/pricing/). See below.
        :param pulumi.Input[str] elasticsearch_version: The version of Elasticsearch to deploy. Defaults to `1.5`
        :param pulumi.Input['DomainEncryptAtRestArgs'] encrypt_at_rest: Encrypt at rest options. Only available for [certain instance types](http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/aes-supported-instance-types.html). See below.
        :param pulumi.Input[str] endpoint: Domain-specific endpoint used to submit index, search, and data upload requests.
        :param pulumi.Input[str] kibana_endpoint: Domain-specific endpoint for kibana without https scheme.
               * `vpc_options.0.availability_zones` - If the domain was created inside a VPC, the names of the availability zones the configured `subnet_ids` were created inside.
               * `vpc_options.0.vpc_id` - If the domain was created inside a VPC, the ID of the VPC.
        :param pulumi.Input[List[pulumi.Input['DomainLogPublishingOptionArgs']]] log_publishing_options: Options for publishing slow logs to CloudWatch Logs.
        :param pulumi.Input['DomainNodeToNodeEncryptionArgs'] node_to_node_encryption: Node-to-node encryption options. See below.
        :param pulumi.Input['DomainSnapshotOptionsArgs'] snapshot_options: Snapshot related options, see below.
        :param pulumi.Input[Dict[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource
        :param pulumi.Input['DomainVpcOptionsArgs'] vpc_options: VPC related options, see below. Adding or removing this configuration forces a new resource ([documentation](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html#es-vpc-limitations)).
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["access_policies"] = access_policies
        __props__["advanced_options"] = advanced_options
        __props__["advanced_security_options"] = advanced_security_options
        __props__["arn"] = arn
        __props__["cluster_config"] = cluster_config
        __props__["cognito_options"] = cognito_options
        __props__["domain_endpoint_options"] = domain_endpoint_options
        __props__["domain_id"] = domain_id
        __props__["domain_name"] = domain_name
        __props__["ebs_options"] = ebs_options
        __props__["elasticsearch_version"] = elasticsearch_version
        __props__["encrypt_at_rest"] = encrypt_at_rest
        __props__["endpoint"] = endpoint
        __props__["kibana_endpoint"] = kibana_endpoint
        __props__["log_publishing_options"] = log_publishing_options
        __props__["node_to_node_encryption"] = node_to_node_encryption
        __props__["snapshot_options"] = snapshot_options
        __props__["tags"] = tags
        __props__["vpc_options"] = vpc_options
        return Domain(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

