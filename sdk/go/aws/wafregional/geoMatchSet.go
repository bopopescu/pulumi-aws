// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package wafregional

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides a WAF Regional Geo Match Set Resource
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/wafregional_geo_match_set.html.markdown.
type GeoMatchSet struct {
	s *pulumi.ResourceState
}

// NewGeoMatchSet registers a new resource with the given unique name, arguments, and options.
func NewGeoMatchSet(ctx *pulumi.Context,
	name string, args *GeoMatchSetArgs, opts ...pulumi.ResourceOpt) (*GeoMatchSet, error) {
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["geoMatchConstraints"] = nil
		inputs["name"] = nil
	} else {
		inputs["geoMatchConstraints"] = args.GeoMatchConstraints
		inputs["name"] = args.Name
	}
	s, err := ctx.RegisterResource("aws:wafregional/geoMatchSet:GeoMatchSet", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &GeoMatchSet{s: s}, nil
}

// GetGeoMatchSet gets an existing GeoMatchSet resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetGeoMatchSet(ctx *pulumi.Context,
	name string, id pulumi.ID, state *GeoMatchSetState, opts ...pulumi.ResourceOpt) (*GeoMatchSet, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["geoMatchConstraints"] = state.GeoMatchConstraints
		inputs["name"] = state.Name
	}
	s, err := ctx.ReadResource("aws:wafregional/geoMatchSet:GeoMatchSet", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &GeoMatchSet{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *GeoMatchSet) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *GeoMatchSet) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The Geo Match Constraint objects which contain the country that you want AWS WAF to search for.
func (r *GeoMatchSet) GeoMatchConstraints() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["geoMatchConstraints"])
}

// The name or description of the Geo Match Set.
func (r *GeoMatchSet) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// Input properties used for looking up and filtering GeoMatchSet resources.
type GeoMatchSetState struct {
	// The Geo Match Constraint objects which contain the country that you want AWS WAF to search for.
	GeoMatchConstraints interface{}
	// The name or description of the Geo Match Set.
	Name interface{}
}

// The set of arguments for constructing a GeoMatchSet resource.
type GeoMatchSetArgs struct {
	// The Geo Match Constraint objects which contain the country that you want AWS WAF to search for.
	GeoMatchConstraints interface{}
	// The name or description of the Geo Match Set.
	Name interface{}
}
