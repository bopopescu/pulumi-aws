// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ec2

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides an Elastic IP resource.
// 
// > **Note:** EIP may require IGW to exist prior to association. Use `depends_on` to set an explicit dependency on the IGW.
// 
// > **Note:** Do not use `network_interface` to associate the EIP to `aws_lb` or `aws_nat_gateway` resources. Instead use the `allocation_id` available in those resources to allow AWS to manage the association, otherwise you will see `AuthFailure` errors.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/eip.html.markdown.
type Eip struct {
	s *pulumi.ResourceState
}

// NewEip registers a new resource with the given unique name, arguments, and options.
func NewEip(ctx *pulumi.Context,
	name string, args *EipArgs, opts ...pulumi.ResourceOpt) (*Eip, error) {
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["associateWithPrivateIp"] = nil
		inputs["instance"] = nil
		inputs["networkInterface"] = nil
		inputs["publicIpv4Pool"] = nil
		inputs["tags"] = nil
		inputs["vpc"] = nil
	} else {
		inputs["associateWithPrivateIp"] = args.AssociateWithPrivateIp
		inputs["instance"] = args.Instance
		inputs["networkInterface"] = args.NetworkInterface
		inputs["publicIpv4Pool"] = args.PublicIpv4Pool
		inputs["tags"] = args.Tags
		inputs["vpc"] = args.Vpc
	}
	inputs["allocationId"] = nil
	inputs["associationId"] = nil
	inputs["domain"] = nil
	inputs["privateDns"] = nil
	inputs["privateIp"] = nil
	inputs["publicDns"] = nil
	inputs["publicIp"] = nil
	s, err := ctx.RegisterResource("aws:ec2/eip:Eip", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Eip{s: s}, nil
}

// GetEip gets an existing Eip resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetEip(ctx *pulumi.Context,
	name string, id pulumi.ID, state *EipState, opts ...pulumi.ResourceOpt) (*Eip, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["allocationId"] = state.AllocationId
		inputs["associateWithPrivateIp"] = state.AssociateWithPrivateIp
		inputs["associationId"] = state.AssociationId
		inputs["domain"] = state.Domain
		inputs["instance"] = state.Instance
		inputs["networkInterface"] = state.NetworkInterface
		inputs["privateDns"] = state.PrivateDns
		inputs["privateIp"] = state.PrivateIp
		inputs["publicDns"] = state.PublicDns
		inputs["publicIp"] = state.PublicIp
		inputs["publicIpv4Pool"] = state.PublicIpv4Pool
		inputs["tags"] = state.Tags
		inputs["vpc"] = state.Vpc
	}
	s, err := ctx.ReadResource("aws:ec2/eip:Eip", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Eip{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *Eip) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *Eip) ID() *pulumi.IDOutput {
	return r.s.ID()
}

func (r *Eip) AllocationId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["allocationId"])
}

// A user specified primary or secondary private IP address to
// associate with the Elastic IP address. If no private IP address is specified,
// the Elastic IP address is associated with the primary private IP address.
func (r *Eip) AssociateWithPrivateIp() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["associateWithPrivateIp"])
}

func (r *Eip) AssociationId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["associationId"])
}

func (r *Eip) Domain() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["domain"])
}

// EC2 instance ID.
func (r *Eip) Instance() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["instance"])
}

// Network interface ID to associate with.
func (r *Eip) NetworkInterface() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["networkInterface"])
}

// The Private DNS associated with the Elastic IP address (if in VPC).
func (r *Eip) PrivateDns() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["privateDns"])
}

// Contains the private IP address (if in VPC).
func (r *Eip) PrivateIp() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["privateIp"])
}

// Public DNS associated with the Elastic IP address.
func (r *Eip) PublicDns() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["publicDns"])
}

// Contains the public IP address.
func (r *Eip) PublicIp() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["publicIp"])
}

// EC2 IPv4 address pool identifier or `amazon`. This option is only available for VPC EIPs.
func (r *Eip) PublicIpv4Pool() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["publicIpv4Pool"])
}

// A mapping of tags to assign to the resource.
func (r *Eip) Tags() *pulumi.MapOutput {
	return (*pulumi.MapOutput)(r.s.State["tags"])
}

// Boolean if the EIP is in a VPC or not.
func (r *Eip) Vpc() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["vpc"])
}

// Input properties used for looking up and filtering Eip resources.
type EipState struct {
	AllocationId interface{}
	// A user specified primary or secondary private IP address to
	// associate with the Elastic IP address. If no private IP address is specified,
	// the Elastic IP address is associated with the primary private IP address.
	AssociateWithPrivateIp interface{}
	AssociationId interface{}
	Domain interface{}
	// EC2 instance ID.
	Instance interface{}
	// Network interface ID to associate with.
	NetworkInterface interface{}
	// The Private DNS associated with the Elastic IP address (if in VPC).
	PrivateDns interface{}
	// Contains the private IP address (if in VPC).
	PrivateIp interface{}
	// Public DNS associated with the Elastic IP address.
	PublicDns interface{}
	// Contains the public IP address.
	PublicIp interface{}
	// EC2 IPv4 address pool identifier or `amazon`. This option is only available for VPC EIPs.
	PublicIpv4Pool interface{}
	// A mapping of tags to assign to the resource.
	Tags interface{}
	// Boolean if the EIP is in a VPC or not.
	Vpc interface{}
}

// The set of arguments for constructing a Eip resource.
type EipArgs struct {
	// A user specified primary or secondary private IP address to
	// associate with the Elastic IP address. If no private IP address is specified,
	// the Elastic IP address is associated with the primary private IP address.
	AssociateWithPrivateIp interface{}
	// EC2 instance ID.
	Instance interface{}
	// Network interface ID to associate with.
	NetworkInterface interface{}
	// EC2 IPv4 address pool identifier or `amazon`. This option is only available for VPC EIPs.
	PublicIpv4Pool interface{}
	// A mapping of tags to assign to the resource.
	Tags interface{}
	// Boolean if the EIP is in a VPC or not.
	Vpc interface{}
}
