// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package cognito

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides an AWS Cognito Identity Pool.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_identity_pool.html.markdown.
type IdentityPool struct {
	s *pulumi.ResourceState
}

// NewIdentityPool registers a new resource with the given unique name, arguments, and options.
func NewIdentityPool(ctx *pulumi.Context,
	name string, args *IdentityPoolArgs, opts ...pulumi.ResourceOpt) (*IdentityPool, error) {
	if args == nil || args.IdentityPoolName == nil {
		return nil, errors.New("missing required argument 'IdentityPoolName'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["allowUnauthenticatedIdentities"] = nil
		inputs["cognitoIdentityProviders"] = nil
		inputs["developerProviderName"] = nil
		inputs["identityPoolName"] = nil
		inputs["openidConnectProviderArns"] = nil
		inputs["samlProviderArns"] = nil
		inputs["supportedLoginProviders"] = nil
	} else {
		inputs["allowUnauthenticatedIdentities"] = args.AllowUnauthenticatedIdentities
		inputs["cognitoIdentityProviders"] = args.CognitoIdentityProviders
		inputs["developerProviderName"] = args.DeveloperProviderName
		inputs["identityPoolName"] = args.IdentityPoolName
		inputs["openidConnectProviderArns"] = args.OpenidConnectProviderArns
		inputs["samlProviderArns"] = args.SamlProviderArns
		inputs["supportedLoginProviders"] = args.SupportedLoginProviders
	}
	inputs["arn"] = nil
	s, err := ctx.RegisterResource("aws:cognito/identityPool:IdentityPool", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &IdentityPool{s: s}, nil
}

// GetIdentityPool gets an existing IdentityPool resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetIdentityPool(ctx *pulumi.Context,
	name string, id pulumi.ID, state *IdentityPoolState, opts ...pulumi.ResourceOpt) (*IdentityPool, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["allowUnauthenticatedIdentities"] = state.AllowUnauthenticatedIdentities
		inputs["arn"] = state.Arn
		inputs["cognitoIdentityProviders"] = state.CognitoIdentityProviders
		inputs["developerProviderName"] = state.DeveloperProviderName
		inputs["identityPoolName"] = state.IdentityPoolName
		inputs["openidConnectProviderArns"] = state.OpenidConnectProviderArns
		inputs["samlProviderArns"] = state.SamlProviderArns
		inputs["supportedLoginProviders"] = state.SupportedLoginProviders
	}
	s, err := ctx.ReadResource("aws:cognito/identityPool:IdentityPool", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &IdentityPool{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *IdentityPool) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *IdentityPool) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// Whether the identity pool supports unauthenticated logins or not.
func (r *IdentityPool) AllowUnauthenticatedIdentities() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["allowUnauthenticatedIdentities"])
}

// The ARN of the identity pool.
func (r *IdentityPool) Arn() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["arn"])
}

// An array of Amazon Cognito Identity user pools and their client IDs.
func (r *IdentityPool) CognitoIdentityProviders() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["cognitoIdentityProviders"])
}

// The "domain" by which Cognito will refer to your users. This name acts as a placeholder that allows your
// backend and the Cognito service to communicate about the developer provider.
func (r *IdentityPool) DeveloperProviderName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["developerProviderName"])
}

// The Cognito Identity Pool name.
func (r *IdentityPool) IdentityPoolName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["identityPoolName"])
}

// A list of OpendID Connect provider ARNs.
func (r *IdentityPool) OpenidConnectProviderArns() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["openidConnectProviderArns"])
}

// An array of Amazon Resource Names (ARNs) of the SAML provider for your identity.
func (r *IdentityPool) SamlProviderArns() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["samlProviderArns"])
}

// Key-Value pairs mapping provider names to provider app IDs.
func (r *IdentityPool) SupportedLoginProviders() *pulumi.MapOutput {
	return (*pulumi.MapOutput)(r.s.State["supportedLoginProviders"])
}

// Input properties used for looking up and filtering IdentityPool resources.
type IdentityPoolState struct {
	// Whether the identity pool supports unauthenticated logins or not.
	AllowUnauthenticatedIdentities interface{}
	// The ARN of the identity pool.
	Arn interface{}
	// An array of Amazon Cognito Identity user pools and their client IDs.
	CognitoIdentityProviders interface{}
	// The "domain" by which Cognito will refer to your users. This name acts as a placeholder that allows your
	// backend and the Cognito service to communicate about the developer provider.
	DeveloperProviderName interface{}
	// The Cognito Identity Pool name.
	IdentityPoolName interface{}
	// A list of OpendID Connect provider ARNs.
	OpenidConnectProviderArns interface{}
	// An array of Amazon Resource Names (ARNs) of the SAML provider for your identity.
	SamlProviderArns interface{}
	// Key-Value pairs mapping provider names to provider app IDs.
	SupportedLoginProviders interface{}
}

// The set of arguments for constructing a IdentityPool resource.
type IdentityPoolArgs struct {
	// Whether the identity pool supports unauthenticated logins or not.
	AllowUnauthenticatedIdentities interface{}
	// An array of Amazon Cognito Identity user pools and their client IDs.
	CognitoIdentityProviders interface{}
	// The "domain" by which Cognito will refer to your users. This name acts as a placeholder that allows your
	// backend and the Cognito service to communicate about the developer provider.
	DeveloperProviderName interface{}
	// The Cognito Identity Pool name.
	IdentityPoolName interface{}
	// A list of OpendID Connect provider ARNs.
	OpenidConnectProviderArns interface{}
	// An array of Amazon Resource Names (ARNs) of the SAML provider for your identity.
	SamlProviderArns interface{}
	// Key-Value pairs mapping provider names to provider app IDs.
	SupportedLoginProviders interface{}
}
