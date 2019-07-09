// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package pinpoint

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides a Pinpoint GCM Channel resource.
// 
// > **Note:** Api Key argument will be stored in the raw state as plain-text.
// [Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/pinpoint_gcm_channel.html.markdown.
type GcmChannel struct {
	s *pulumi.ResourceState
}

// NewGcmChannel registers a new resource with the given unique name, arguments, and options.
func NewGcmChannel(ctx *pulumi.Context,
	name string, args *GcmChannelArgs, opts ...pulumi.ResourceOpt) (*GcmChannel, error) {
	if args == nil || args.ApiKey == nil {
		return nil, errors.New("missing required argument 'ApiKey'")
	}
	if args == nil || args.ApplicationId == nil {
		return nil, errors.New("missing required argument 'ApplicationId'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["apiKey"] = nil
		inputs["applicationId"] = nil
		inputs["enabled"] = nil
	} else {
		inputs["apiKey"] = args.ApiKey
		inputs["applicationId"] = args.ApplicationId
		inputs["enabled"] = args.Enabled
	}
	s, err := ctx.RegisterResource("aws:pinpoint/gcmChannel:GcmChannel", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &GcmChannel{s: s}, nil
}

// GetGcmChannel gets an existing GcmChannel resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetGcmChannel(ctx *pulumi.Context,
	name string, id pulumi.ID, state *GcmChannelState, opts ...pulumi.ResourceOpt) (*GcmChannel, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["apiKey"] = state.ApiKey
		inputs["applicationId"] = state.ApplicationId
		inputs["enabled"] = state.Enabled
	}
	s, err := ctx.ReadResource("aws:pinpoint/gcmChannel:GcmChannel", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &GcmChannel{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *GcmChannel) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *GcmChannel) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// Platform credential API key from Google.
func (r *GcmChannel) ApiKey() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["apiKey"])
}

// The application ID.
func (r *GcmChannel) ApplicationId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["applicationId"])
}

// Whether the channel is enabled or disabled. Defaults to `true`.
func (r *GcmChannel) Enabled() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["enabled"])
}

// Input properties used for looking up and filtering GcmChannel resources.
type GcmChannelState struct {
	// Platform credential API key from Google.
	ApiKey interface{}
	// The application ID.
	ApplicationId interface{}
	// Whether the channel is enabled or disabled. Defaults to `true`.
	Enabled interface{}
}

// The set of arguments for constructing a GcmChannel resource.
type GcmChannelArgs struct {
	// Platform credential API key from Google.
	ApiKey interface{}
	// The application ID.
	ApplicationId interface{}
	// Whether the channel is enabled or disabled. Defaults to `true`.
	Enabled interface{}
}
