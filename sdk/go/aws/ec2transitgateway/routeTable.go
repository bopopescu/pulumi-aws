// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ec2transitgateway

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Manages an EC2 Transit Gateway Route Table.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ec2_transit_gateway_route_table.html.markdown.
type RouteTable struct {
	s *pulumi.ResourceState
}

// NewRouteTable registers a new resource with the given unique name, arguments, and options.
func NewRouteTable(ctx *pulumi.Context,
	name string, args *RouteTableArgs, opts ...pulumi.ResourceOpt) (*RouteTable, error) {
	if args == nil || args.TransitGatewayId == nil {
		return nil, errors.New("missing required argument 'TransitGatewayId'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["tags"] = nil
		inputs["transitGatewayId"] = nil
	} else {
		inputs["tags"] = args.Tags
		inputs["transitGatewayId"] = args.TransitGatewayId
	}
	inputs["defaultAssociationRouteTable"] = nil
	inputs["defaultPropagationRouteTable"] = nil
	s, err := ctx.RegisterResource("aws:ec2transitgateway/routeTable:RouteTable", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &RouteTable{s: s}, nil
}

// GetRouteTable gets an existing RouteTable resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRouteTable(ctx *pulumi.Context,
	name string, id pulumi.ID, state *RouteTableState, opts ...pulumi.ResourceOpt) (*RouteTable, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["defaultAssociationRouteTable"] = state.DefaultAssociationRouteTable
		inputs["defaultPropagationRouteTable"] = state.DefaultPropagationRouteTable
		inputs["tags"] = state.Tags
		inputs["transitGatewayId"] = state.TransitGatewayId
	}
	s, err := ctx.ReadResource("aws:ec2transitgateway/routeTable:RouteTable", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &RouteTable{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *RouteTable) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *RouteTable) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// Boolean whether this is the default association route table for the EC2 Transit Gateway.
func (r *RouteTable) DefaultAssociationRouteTable() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["defaultAssociationRouteTable"])
}

// Boolean whether this is the default propagation route table for the EC2 Transit Gateway.
func (r *RouteTable) DefaultPropagationRouteTable() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["defaultPropagationRouteTable"])
}

// Key-value tags for the EC2 Transit Gateway Route Table.
func (r *RouteTable) Tags() *pulumi.MapOutput {
	return (*pulumi.MapOutput)(r.s.State["tags"])
}

// Identifier of EC2 Transit Gateway.
func (r *RouteTable) TransitGatewayId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["transitGatewayId"])
}

// Input properties used for looking up and filtering RouteTable resources.
type RouteTableState struct {
	// Boolean whether this is the default association route table for the EC2 Transit Gateway.
	DefaultAssociationRouteTable interface{}
	// Boolean whether this is the default propagation route table for the EC2 Transit Gateway.
	DefaultPropagationRouteTable interface{}
	// Key-value tags for the EC2 Transit Gateway Route Table.
	Tags interface{}
	// Identifier of EC2 Transit Gateway.
	TransitGatewayId interface{}
}

// The set of arguments for constructing a RouteTable resource.
type RouteTableArgs struct {
	// Key-value tags for the EC2 Transit Gateway Route Table.
	Tags interface{}
	// Identifier of EC2 Transit Gateway.
	TransitGatewayId interface{}
}
