// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ssm

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Registers an on-premises server or virtual machine with Amazon EC2 so that it can be managed using Run Command.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ssm_activation.html.markdown.
type Activation struct {
	s *pulumi.ResourceState
}

// NewActivation registers a new resource with the given unique name, arguments, and options.
func NewActivation(ctx *pulumi.Context,
	name string, args *ActivationArgs, opts ...pulumi.ResourceOpt) (*Activation, error) {
	if args == nil || args.IamRole == nil {
		return nil, errors.New("missing required argument 'IamRole'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["description"] = nil
		inputs["expirationDate"] = nil
		inputs["iamRole"] = nil
		inputs["name"] = nil
		inputs["registrationLimit"] = nil
		inputs["tags"] = nil
	} else {
		inputs["description"] = args.Description
		inputs["expirationDate"] = args.ExpirationDate
		inputs["iamRole"] = args.IamRole
		inputs["name"] = args.Name
		inputs["registrationLimit"] = args.RegistrationLimit
		inputs["tags"] = args.Tags
	}
	inputs["activationCode"] = nil
	inputs["expired"] = nil
	inputs["registrationCount"] = nil
	s, err := ctx.RegisterResource("aws:ssm/activation:Activation", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Activation{s: s}, nil
}

// GetActivation gets an existing Activation resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetActivation(ctx *pulumi.Context,
	name string, id pulumi.ID, state *ActivationState, opts ...pulumi.ResourceOpt) (*Activation, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["activationCode"] = state.ActivationCode
		inputs["description"] = state.Description
		inputs["expirationDate"] = state.ExpirationDate
		inputs["expired"] = state.Expired
		inputs["iamRole"] = state.IamRole
		inputs["name"] = state.Name
		inputs["registrationCount"] = state.RegistrationCount
		inputs["registrationLimit"] = state.RegistrationLimit
		inputs["tags"] = state.Tags
	}
	s, err := ctx.ReadResource("aws:ssm/activation:Activation", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Activation{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *Activation) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *Activation) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The code the system generates when it processes the activation.
func (r *Activation) ActivationCode() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["activationCode"])
}

// The description of the resource that you want to register.
func (r *Activation) Description() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["description"])
}

// A timestamp in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8) by which this activation request should expire. The default value is 24 hours from resource creation time.
func (r *Activation) ExpirationDate() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["expirationDate"])
}

// If the current activation has expired.
func (r *Activation) Expired() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["expired"])
}

// The IAM Role to attach to the managed instance.
func (r *Activation) IamRole() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["iamRole"])
}

// The default name of the registered managed instance.
func (r *Activation) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// The number of managed instances that are currently registered using this activation.
func (r *Activation) RegistrationCount() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["registrationCount"])
}

// The maximum number of managed instances you want to register. The default value is 1 instance.
func (r *Activation) RegistrationLimit() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["registrationLimit"])
}

// A mapping of tags to assign to the object.
func (r *Activation) Tags() *pulumi.MapOutput {
	return (*pulumi.MapOutput)(r.s.State["tags"])
}

// Input properties used for looking up and filtering Activation resources.
type ActivationState struct {
	// The code the system generates when it processes the activation.
	ActivationCode interface{}
	// The description of the resource that you want to register.
	Description interface{}
	// A timestamp in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8) by which this activation request should expire. The default value is 24 hours from resource creation time.
	ExpirationDate interface{}
	// If the current activation has expired.
	Expired interface{}
	// The IAM Role to attach to the managed instance.
	IamRole interface{}
	// The default name of the registered managed instance.
	Name interface{}
	// The number of managed instances that are currently registered using this activation.
	RegistrationCount interface{}
	// The maximum number of managed instances you want to register. The default value is 1 instance.
	RegistrationLimit interface{}
	// A mapping of tags to assign to the object.
	Tags interface{}
}

// The set of arguments for constructing a Activation resource.
type ActivationArgs struct {
	// The description of the resource that you want to register.
	Description interface{}
	// A timestamp in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8) by which this activation request should expire. The default value is 24 hours from resource creation time.
	ExpirationDate interface{}
	// The IAM Role to attach to the managed instance.
	IamRole interface{}
	// The default name of the registered managed instance.
	Name interface{}
	// The maximum number of managed instances you want to register. The default value is 1 instance.
	RegistrationLimit interface{}
	// A mapping of tags to assign to the object.
	Tags interface{}
}
