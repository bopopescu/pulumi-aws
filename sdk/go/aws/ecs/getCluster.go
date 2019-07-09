// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ecs

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// The ECS Cluster data source allows access to details of a specific
// cluster within an AWS ECS service.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/ecs_cluster.html.markdown.
func LookupCluster(ctx *pulumi.Context, args *GetClusterArgs) (*GetClusterResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["clusterName"] = args.ClusterName
	}
	outputs, err := ctx.Invoke("aws:ecs/getCluster:getCluster", inputs)
	if err != nil {
		return nil, err
	}
	return &GetClusterResult{
		Arn: outputs["arn"],
		ClusterName: outputs["clusterName"],
		PendingTasksCount: outputs["pendingTasksCount"],
		RegisteredContainerInstancesCount: outputs["registeredContainerInstancesCount"],
		RunningTasksCount: outputs["runningTasksCount"],
		Status: outputs["status"],
		Id: outputs["id"],
	}, nil
}

// A collection of arguments for invoking getCluster.
type GetClusterArgs struct {
	// The name of the ECS Cluster
	ClusterName interface{}
}

// A collection of values returned by getCluster.
type GetClusterResult struct {
	// The ARN of the ECS Cluster
	Arn interface{}
	ClusterName interface{}
	// The number of pending tasks for the ECS Cluster
	PendingTasksCount interface{}
	// The number of registered container instances for the ECS Cluster
	RegisteredContainerInstancesCount interface{}
	// The number of running tasks for the ECS Cluster
	RunningTasksCount interface{}
	// The status of the ECS Cluster
	Status interface{}
	// id is the provider-assigned unique ID for this managed resource.
	Id interface{}
}
