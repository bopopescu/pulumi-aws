// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";

/**
 * Retrieve information about an EKS Cluster.
 */
export function getCluster(args: GetClusterArgs): Promise<GetClusterResult> {
    return pulumi.runtime.invoke("aws:eks/getCluster:getCluster", {
        "name": args.name,
    });
}

/**
 * A collection of arguments for invoking getCluster.
 */
export interface GetClusterArgs {
    /**
     * The name of the cluster
     */
    readonly name: pulumi.Input<string>;
}

/**
 * A collection of values returned by getCluster.
 */
export interface GetClusterResult {
    /**
     * Nested attribute containing `certificate-authority-data` for your cluster.
     */
    readonly certificateAuthority: { data: string };
    /**
     * The Unix epoch time stamp in seconds for when the cluster was created.
     */
    readonly createdAt: string;
    /**
     * The endpoint for your Kubernetes API server.
     */
    readonly endpoint: string;
    /**
     * The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf.
     */
    readonly roleArn: string;
    /**
     * The Kubernetes server version for the cluster.
     */
    readonly version: string;
    /**
     * Nested attribute containing VPC configuration for the cluster.
     */
    readonly vpcConfig: { securityGroupIds: string[], subnetIds: string[], vpcId: string };
}