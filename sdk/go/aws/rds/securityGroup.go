// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package rds

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides an RDS security group resource. This is only for DB instances in the
// EC2-Classic Platform. For instances inside a VPC, use the
// [`aws_db_instance.vpc_security_group_ids`](https://www.terraform.io/docs/providers/aws/r/db_instance.html#vpc_security_group_ids)
// attribute instead.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/db_security_group.html.markdown.
type SecurityGroup struct {
	s *pulumi.ResourceState
}

// NewSecurityGroup registers a new resource with the given unique name, arguments, and options.
func NewSecurityGroup(ctx *pulumi.Context,
	name string, args *SecurityGroupArgs, opts ...pulumi.ResourceOpt) (*SecurityGroup, error) {
	if args == nil || args.Ingress == nil {
		return nil, errors.New("missing required argument 'Ingress'")
	}
	inputs := make(map[string]interface{})
	inputs["description"] = "Managed by Pulumi"
	if args == nil {
		inputs["ingress"] = nil
		inputs["name"] = nil
		inputs["tags"] = nil
	} else {
		inputs["description"] = args.Description
		inputs["ingress"] = args.Ingress
		inputs["name"] = args.Name
		inputs["tags"] = args.Tags
	}
	inputs["arn"] = nil
	s, err := ctx.RegisterResource("aws:rds/securityGroup:SecurityGroup", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &SecurityGroup{s: s}, nil
}

// GetSecurityGroup gets an existing SecurityGroup resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSecurityGroup(ctx *pulumi.Context,
	name string, id pulumi.ID, state *SecurityGroupState, opts ...pulumi.ResourceOpt) (*SecurityGroup, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["arn"] = state.Arn
		inputs["description"] = state.Description
		inputs["ingress"] = state.Ingress
		inputs["name"] = state.Name
		inputs["tags"] = state.Tags
	}
	s, err := ctx.ReadResource("aws:rds/securityGroup:SecurityGroup", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &SecurityGroup{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *SecurityGroup) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *SecurityGroup) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The arn of the DB security group.
func (r *SecurityGroup) Arn() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["arn"])
}

func (r *SecurityGroup) Description() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["description"])
}

// A list of ingress rules.
func (r *SecurityGroup) Ingress() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["ingress"])
}

// The name of the DB security group.
func (r *SecurityGroup) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// A mapping of tags to assign to the resource.
func (r *SecurityGroup) Tags() *pulumi.MapOutput {
	return (*pulumi.MapOutput)(r.s.State["tags"])
}

// Input properties used for looking up and filtering SecurityGroup resources.
type SecurityGroupState struct {
	// The arn of the DB security group.
	Arn interface{}
	Description interface{}
	// A list of ingress rules.
	Ingress interface{}
	// The name of the DB security group.
	Name interface{}
	// A mapping of tags to assign to the resource.
	Tags interface{}
}

// The set of arguments for constructing a SecurityGroup resource.
type SecurityGroupArgs struct {
	Description interface{}
	// A list of ingress rules.
	Ingress interface{}
	// The name of the DB security group.
	Name interface{}
	// A mapping of tags to assign to the resource.
	Tags interface{}
}
