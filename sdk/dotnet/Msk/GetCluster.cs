// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Msk
{
    public static class GetCluster
    {
        /// <summary>
        /// Get information on an Amazon MSK Cluster.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Aws = Pulumi.Aws;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var example = Output.Create(Aws.Msk.GetCluster.InvokeAsync(new Aws.Msk.GetClusterArgs
        ///         {
        ///             ClusterName = "example",
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetClusterResult> InvokeAsync(GetClusterArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetClusterResult>("aws:msk/getCluster:getCluster", args ?? new GetClusterArgs(), options.WithVersion());
    }


    public sealed class GetClusterArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Name of the cluster.
        /// </summary>
        [Input("clusterName", required: true)]
        public string ClusterName { get; set; } = null!;

        [Input("tags")]
        private Dictionary<string, string>? _tags;

        /// <summary>
        /// Map of key-value pairs assigned to the cluster.
        /// </summary>
        public Dictionary<string, string> Tags
        {
            get => _tags ?? (_tags = new Dictionary<string, string>());
            set => _tags = value;
        }

        public GetClusterArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetClusterResult
    {
        /// <summary>
        /// Amazon Resource Name (ARN) of the MSK cluster.
        /// </summary>
        public readonly string Arn;
        /// <summary>
        /// A comma separated list of one or more hostname:port pairs of Kafka brokers suitable to boostrap connectivity to the Kafka cluster.
        /// </summary>
        public readonly string BootstrapBrokers;
        /// <summary>
        /// A comma separated list of one or more DNS names (or IPs) and TLS port pairs kafka brokers suitable to boostrap connectivity to the kafka cluster.
        /// </summary>
        public readonly string BootstrapBrokersTls;
        public readonly string ClusterName;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Apache Kafka version.
        /// </summary>
        public readonly string KafkaVersion;
        /// <summary>
        /// Number of broker nodes in the cluster.
        /// </summary>
        public readonly int NumberOfBrokerNodes;
        /// <summary>
        /// Map of key-value pairs assigned to the cluster.
        /// </summary>
        public readonly ImmutableDictionary<string, string> Tags;
        /// <summary>
        /// A comma separated list of one or more hostname:port pairs to use to connect to the Apache Zookeeper cluster.
        /// </summary>
        public readonly string ZookeeperConnectString;

        [OutputConstructor]
        private GetClusterResult(
            string arn,

            string bootstrapBrokers,

            string bootstrapBrokersTls,

            string clusterName,

            string id,

            string kafkaVersion,

            int numberOfBrokerNodes,

            ImmutableDictionary<string, string> tags,

            string zookeeperConnectString)
        {
            Arn = arn;
            BootstrapBrokers = bootstrapBrokers;
            BootstrapBrokersTls = bootstrapBrokersTls;
            ClusterName = clusterName;
            Id = id;
            KafkaVersion = kafkaVersion;
            NumberOfBrokerNodes = numberOfBrokerNodes;
            Tags = tags;
            ZookeeperConnectString = zookeeperConnectString;
        }
    }
}
