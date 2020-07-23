# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables


class GetClusterResult:
    """
    A collection of values returned by getCluster.
    """
    # pylint: disable=no-self-argument
    def __init__(__self__, arn=None, bootstrap_brokers=None, bootstrap_brokers_tls=None, cluster_name=None, id=None, kafka_version=None, number_of_broker_nodes=None, tags=None, zookeeper_connect_string=None) -> None:
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        __self__.arn = arn
        """
        Amazon Resource Name (ARN) of the MSK cluster.
        """
        if bootstrap_brokers and not isinstance(bootstrap_brokers, str):
            raise TypeError("Expected argument 'bootstrap_brokers' to be a str")
        __self__.bootstrap_brokers = bootstrap_brokers
        """
        A comma separated list of one or more hostname:port pairs of Kafka brokers suitable to boostrap connectivity to the Kafka cluster.
        """
        if bootstrap_brokers_tls and not isinstance(bootstrap_brokers_tls, str):
            raise TypeError("Expected argument 'bootstrap_brokers_tls' to be a str")
        __self__.bootstrap_brokers_tls = bootstrap_brokers_tls
        """
        A comma separated list of one or more DNS names (or IPs) and TLS port pairs kafka brokers suitable to boostrap connectivity to the kafka cluster.
        """
        if cluster_name and not isinstance(cluster_name, str):
            raise TypeError("Expected argument 'cluster_name' to be a str")
        __self__.cluster_name = cluster_name
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if kafka_version and not isinstance(kafka_version, str):
            raise TypeError("Expected argument 'kafka_version' to be a str")
        __self__.kafka_version = kafka_version
        """
        Apache Kafka version.
        """
        if number_of_broker_nodes and not isinstance(number_of_broker_nodes, float):
            raise TypeError("Expected argument 'number_of_broker_nodes' to be a float")
        __self__.number_of_broker_nodes = number_of_broker_nodes
        """
        Number of broker nodes in the cluster.
        """
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        __self__.tags = tags
        """
        Map of key-value pairs assigned to the cluster.
        """
        if zookeeper_connect_string and not isinstance(zookeeper_connect_string, str):
            raise TypeError("Expected argument 'zookeeper_connect_string' to be a str")
        __self__.zookeeper_connect_string = zookeeper_connect_string
        """
        A comma separated list of one or more hostname:port pairs to use to connect to the Apache Zookeeper cluster.
        """


class AwaitableGetClusterResult(GetClusterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetClusterResult(
            arn=self.arn,
            bootstrap_brokers=self.bootstrap_brokers,
            bootstrap_brokers_tls=self.bootstrap_brokers_tls,
            cluster_name=self.cluster_name,
            id=self.id,
            kafka_version=self.kafka_version,
            number_of_broker_nodes=self.number_of_broker_nodes,
            tags=self.tags,
            zookeeper_connect_string=self.zookeeper_connect_string)


def get_cluster(cluster_name=None, tags=None, opts=None):
    """
    Get information on an Amazon MSK Cluster.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.msk.get_cluster(cluster_name="example")
    ```


    :param str cluster_name: Name of the cluster.
    :param Dict[str, str] tags: Map of key-value pairs assigned to the cluster.
    """
    __args__ = dict()
    __args__['clusterName'] = cluster_name
    __args__['tags'] = tags
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:msk/getCluster:getCluster', __args__, opts=opts).value

    return AwaitableGetClusterResult(
        arn=__ret__.get('arn'),
        bootstrap_brokers=__ret__.get('bootstrapBrokers'),
        bootstrap_brokers_tls=__ret__.get('bootstrapBrokersTls'),
        cluster_name=__ret__.get('clusterName'),
        id=__ret__.get('id'),
        kafka_version=__ret__.get('kafkaVersion'),
        number_of_broker_nodes=__ret__.get('numberOfBrokerNodes'),
        tags=__ret__.get('tags'),
        zookeeper_connect_string=__ret__.get('zookeeperConnectString'))
