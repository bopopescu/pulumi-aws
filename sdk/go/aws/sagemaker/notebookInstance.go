// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sagemaker

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides a Sagemaker Notebook Instance resource.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/sagemaker_notebook_instance.html.markdown.
type NotebookInstance struct {
	s *pulumi.ResourceState
}

// NewNotebookInstance registers a new resource with the given unique name, arguments, and options.
func NewNotebookInstance(ctx *pulumi.Context,
	name string, args *NotebookInstanceArgs, opts ...pulumi.ResourceOpt) (*NotebookInstance, error) {
	if args == nil || args.InstanceType == nil {
		return nil, errors.New("missing required argument 'InstanceType'")
	}
	if args == nil || args.RoleArn == nil {
		return nil, errors.New("missing required argument 'RoleArn'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["instanceType"] = nil
		inputs["kmsKeyId"] = nil
		inputs["lifecycleConfigName"] = nil
		inputs["name"] = nil
		inputs["roleArn"] = nil
		inputs["securityGroups"] = nil
		inputs["subnetId"] = nil
		inputs["tags"] = nil
	} else {
		inputs["instanceType"] = args.InstanceType
		inputs["kmsKeyId"] = args.KmsKeyId
		inputs["lifecycleConfigName"] = args.LifecycleConfigName
		inputs["name"] = args.Name
		inputs["roleArn"] = args.RoleArn
		inputs["securityGroups"] = args.SecurityGroups
		inputs["subnetId"] = args.SubnetId
		inputs["tags"] = args.Tags
	}
	inputs["arn"] = nil
	s, err := ctx.RegisterResource("aws:sagemaker/notebookInstance:NotebookInstance", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &NotebookInstance{s: s}, nil
}

// GetNotebookInstance gets an existing NotebookInstance resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetNotebookInstance(ctx *pulumi.Context,
	name string, id pulumi.ID, state *NotebookInstanceState, opts ...pulumi.ResourceOpt) (*NotebookInstance, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["arn"] = state.Arn
		inputs["instanceType"] = state.InstanceType
		inputs["kmsKeyId"] = state.KmsKeyId
		inputs["lifecycleConfigName"] = state.LifecycleConfigName
		inputs["name"] = state.Name
		inputs["roleArn"] = state.RoleArn
		inputs["securityGroups"] = state.SecurityGroups
		inputs["subnetId"] = state.SubnetId
		inputs["tags"] = state.Tags
	}
	s, err := ctx.ReadResource("aws:sagemaker/notebookInstance:NotebookInstance", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &NotebookInstance{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *NotebookInstance) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *NotebookInstance) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The Amazon Resource Name (ARN) assigned by AWS to this notebook instance.
func (r *NotebookInstance) Arn() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["arn"])
}

// The name of ML compute instance type.
func (r *NotebookInstance) InstanceType() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["instanceType"])
}

// The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption.
func (r *NotebookInstance) KmsKeyId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["kmsKeyId"])
}

// The name of a lifecycle configuration to associate with the notebook instance.
func (r *NotebookInstance) LifecycleConfigName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["lifecycleConfigName"])
}

// The name of the notebook instance (must be unique).
func (r *NotebookInstance) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// The ARN of the IAM role to be used by the notebook instance which allows SageMaker to call other services on your behalf.
func (r *NotebookInstance) RoleArn() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["roleArn"])
}

// The associated security groups.
func (r *NotebookInstance) SecurityGroups() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["securityGroups"])
}

// The VPC subnet ID.
func (r *NotebookInstance) SubnetId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["subnetId"])
}

// A mapping of tags to assign to the resource.
func (r *NotebookInstance) Tags() *pulumi.MapOutput {
	return (*pulumi.MapOutput)(r.s.State["tags"])
}

// Input properties used for looking up and filtering NotebookInstance resources.
type NotebookInstanceState struct {
	// The Amazon Resource Name (ARN) assigned by AWS to this notebook instance.
	Arn interface{}
	// The name of ML compute instance type.
	InstanceType interface{}
	// The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption.
	KmsKeyId interface{}
	// The name of a lifecycle configuration to associate with the notebook instance.
	LifecycleConfigName interface{}
	// The name of the notebook instance (must be unique).
	Name interface{}
	// The ARN of the IAM role to be used by the notebook instance which allows SageMaker to call other services on your behalf.
	RoleArn interface{}
	// The associated security groups.
	SecurityGroups interface{}
	// The VPC subnet ID.
	SubnetId interface{}
	// A mapping of tags to assign to the resource.
	Tags interface{}
}

// The set of arguments for constructing a NotebookInstance resource.
type NotebookInstanceArgs struct {
	// The name of ML compute instance type.
	InstanceType interface{}
	// The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption.
	KmsKeyId interface{}
	// The name of a lifecycle configuration to associate with the notebook instance.
	LifecycleConfigName interface{}
	// The name of the notebook instance (must be unique).
	Name interface{}
	// The ARN of the IAM role to be used by the notebook instance which allows SageMaker to call other services on your behalf.
	RoleArn interface{}
	// The associated security groups.
	SecurityGroups interface{}
	// The VPC subnet ID.
	SubnetId interface{}
	// A mapping of tags to assign to the resource.
	Tags interface{}
}
