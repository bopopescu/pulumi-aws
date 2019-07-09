// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package pinpoint

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides a Pinpoint ADM (Amazon Device Messaging) Channel resource.
// 
// > **Note:** All arguments including the Client ID and Client Secret will be stored in the raw state as plain-text.
// [Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/pinpoint_adm_channel.html.markdown.
type AdmChannel struct {
	s *pulumi.ResourceState
}

// NewAdmChannel registers a new resource with the given unique name, arguments, and options.
func NewAdmChannel(ctx *pulumi.Context,
	name string, args *AdmChannelArgs, opts ...pulumi.ResourceOpt) (*AdmChannel, error) {
	if args == nil || args.ApplicationId == nil {
		return nil, errors.New("missing required argument 'ApplicationId'")
	}
	if args == nil || args.ClientId == nil {
		return nil, errors.New("missing required argument 'ClientId'")
	}
	if args == nil || args.ClientSecret == nil {
		return nil, errors.New("missing required argument 'ClientSecret'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["applicationId"] = nil
		inputs["clientId"] = nil
		inputs["clientSecret"] = nil
		inputs["enabled"] = nil
	} else {
		inputs["applicationId"] = args.ApplicationId
		inputs["clientId"] = args.ClientId
		inputs["clientSecret"] = args.ClientSecret
		inputs["enabled"] = args.Enabled
	}
	s, err := ctx.RegisterResource("aws:pinpoint/admChannel:AdmChannel", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &AdmChannel{s: s}, nil
}

// GetAdmChannel gets an existing AdmChannel resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetAdmChannel(ctx *pulumi.Context,
	name string, id pulumi.ID, state *AdmChannelState, opts ...pulumi.ResourceOpt) (*AdmChannel, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["applicationId"] = state.ApplicationId
		inputs["clientId"] = state.ClientId
		inputs["clientSecret"] = state.ClientSecret
		inputs["enabled"] = state.Enabled
	}
	s, err := ctx.ReadResource("aws:pinpoint/admChannel:AdmChannel", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &AdmChannel{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *AdmChannel) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *AdmChannel) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The application ID.
func (r *AdmChannel) ApplicationId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["applicationId"])
}

// Client ID (part of OAuth Credentials) obtained via Amazon Developer Account.
func (r *AdmChannel) ClientId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["clientId"])
}

// Client Secret (part of OAuth Credentials) obtained via Amazon Developer Account.
func (r *AdmChannel) ClientSecret() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["clientSecret"])
}

// Specifies whether to enable the channel. Defaults to `true`.
func (r *AdmChannel) Enabled() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["enabled"])
}

// Input properties used for looking up and filtering AdmChannel resources.
type AdmChannelState struct {
	// The application ID.
	ApplicationId interface{}
	// Client ID (part of OAuth Credentials) obtained via Amazon Developer Account.
	ClientId interface{}
	// Client Secret (part of OAuth Credentials) obtained via Amazon Developer Account.
	ClientSecret interface{}
	// Specifies whether to enable the channel. Defaults to `true`.
	Enabled interface{}
}

// The set of arguments for constructing a AdmChannel resource.
type AdmChannelArgs struct {
	// The application ID.
	ApplicationId interface{}
	// Client ID (part of OAuth Credentials) obtained via Amazon Developer Account.
	ClientId interface{}
	// Client Secret (part of OAuth Credentials) obtained via Amazon Developer Account.
	ClientSecret interface{}
	// Specifies whether to enable the channel. Defaults to `true`.
	Enabled interface{}
}
