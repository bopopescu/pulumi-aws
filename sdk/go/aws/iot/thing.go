// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package iot

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Creates and manages an AWS IoT Thing.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iot_thing.html.markdown.
type Thing struct {
	s *pulumi.ResourceState
}

// NewThing registers a new resource with the given unique name, arguments, and options.
func NewThing(ctx *pulumi.Context,
	name string, args *ThingArgs, opts ...pulumi.ResourceOpt) (*Thing, error) {
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["attributes"] = nil
		inputs["name"] = nil
		inputs["thingTypeName"] = nil
	} else {
		inputs["attributes"] = args.Attributes
		inputs["name"] = args.Name
		inputs["thingTypeName"] = args.ThingTypeName
	}
	inputs["arn"] = nil
	inputs["defaultClientId"] = nil
	inputs["version"] = nil
	s, err := ctx.RegisterResource("aws:iot/thing:Thing", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Thing{s: s}, nil
}

// GetThing gets an existing Thing resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetThing(ctx *pulumi.Context,
	name string, id pulumi.ID, state *ThingState, opts ...pulumi.ResourceOpt) (*Thing, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["arn"] = state.Arn
		inputs["attributes"] = state.Attributes
		inputs["defaultClientId"] = state.DefaultClientId
		inputs["name"] = state.Name
		inputs["thingTypeName"] = state.ThingTypeName
		inputs["version"] = state.Version
	}
	s, err := ctx.ReadResource("aws:iot/thing:Thing", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Thing{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *Thing) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *Thing) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The ARN of the thing.
func (r *Thing) Arn() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["arn"])
}

// Map of attributes of the thing.
func (r *Thing) Attributes() *pulumi.MapOutput {
	return (*pulumi.MapOutput)(r.s.State["attributes"])
}

// The default client ID.
func (r *Thing) DefaultClientId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["defaultClientId"])
}

// The name of the thing.
func (r *Thing) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// The thing type name.
func (r *Thing) ThingTypeName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["thingTypeName"])
}

// The current version of the thing record in the registry.
func (r *Thing) Version() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["version"])
}

// Input properties used for looking up and filtering Thing resources.
type ThingState struct {
	// The ARN of the thing.
	Arn interface{}
	// Map of attributes of the thing.
	Attributes interface{}
	// The default client ID.
	DefaultClientId interface{}
	// The name of the thing.
	Name interface{}
	// The thing type name.
	ThingTypeName interface{}
	// The current version of the thing record in the registry.
	Version interface{}
}

// The set of arguments for constructing a Thing resource.
type ThingArgs struct {
	// Map of attributes of the thing.
	Attributes interface{}
	// The name of the thing.
	Name interface{}
	// The thing type name.
	ThingTypeName interface{}
}
