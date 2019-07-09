// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package eks

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Get an authentication token to communicate with an EKS cluster.
// 
// Uses IAM credentials from the AWS provider to generate a temporary token that is compatible with
// [AWS IAM Authenticator](https://github.com/kubernetes-sigs/aws-iam-authenticator) authentication.
// This can be used to authenticate to an EKS cluster or to a cluster that has the AWS IAM Authenticator
// server configured.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/eks_cluster_auth.html.markdown.
func LookupClusterAuth(ctx *pulumi.Context, args *GetClusterAuthArgs) (*GetClusterAuthResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["name"] = args.Name
	}
	outputs, err := ctx.Invoke("aws:eks/getClusterAuth:getClusterAuth", inputs)
	if err != nil {
		return nil, err
	}
	return &GetClusterAuthResult{
		Name: outputs["name"],
		Token: outputs["token"],
		Id: outputs["id"],
	}, nil
}

// A collection of arguments for invoking getClusterAuth.
type GetClusterAuthArgs struct {
	// The name of the cluster
	Name interface{}
}

// A collection of values returned by getClusterAuth.
type GetClusterAuthResult struct {
	Name interface{}
	// The token to use to authenticate with the cluster.
	Token interface{}
	// id is the provider-assigned unique ID for this managed resource.
	Id interface{}
}
