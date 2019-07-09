// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package iam

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// This data source can be used to fetch information about a specific
// IAM group. By using this data source, you can reference IAM group
// properties without having to hard code ARNs as input.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/iam_group.html.markdown.
func LookupGroup(ctx *pulumi.Context, args *GetGroupArgs) (*GetGroupResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["groupName"] = args.GroupName
	}
	outputs, err := ctx.Invoke("aws:iam/getGroup:getGroup", inputs)
	if err != nil {
		return nil, err
	}
	return &GetGroupResult{
		Arn: outputs["arn"],
		GroupId: outputs["groupId"],
		GroupName: outputs["groupName"],
		Path: outputs["path"],
		Id: outputs["id"],
	}, nil
}

// A collection of arguments for invoking getGroup.
type GetGroupArgs struct {
	// The friendly IAM group name to match.
	GroupName interface{}
}

// A collection of values returned by getGroup.
type GetGroupResult struct {
	// The Amazon Resource Name (ARN) specifying the group.
	Arn interface{}
	// The stable and unique string identifying the group.
	GroupId interface{}
	GroupName interface{}
	// The path to the group.
	Path interface{}
	// id is the provider-assigned unique ID for this managed resource.
	Id interface{}
}
