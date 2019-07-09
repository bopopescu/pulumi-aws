// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ec2

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides an EC2 launch template resource. Can be used to create instances or auto scaling groups.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/launch_template.html.markdown.
type LaunchTemplate struct {
	s *pulumi.ResourceState
}

// NewLaunchTemplate registers a new resource with the given unique name, arguments, and options.
func NewLaunchTemplate(ctx *pulumi.Context,
	name string, args *LaunchTemplateArgs, opts ...pulumi.ResourceOpt) (*LaunchTemplate, error) {
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["blockDeviceMappings"] = nil
		inputs["capacityReservationSpecification"] = nil
		inputs["creditSpecification"] = nil
		inputs["description"] = nil
		inputs["disableApiTermination"] = nil
		inputs["ebsOptimized"] = nil
		inputs["elasticGpuSpecifications"] = nil
		inputs["elasticInferenceAccelerator"] = nil
		inputs["iamInstanceProfile"] = nil
		inputs["imageId"] = nil
		inputs["instanceInitiatedShutdownBehavior"] = nil
		inputs["instanceMarketOptions"] = nil
		inputs["instanceType"] = nil
		inputs["kernelId"] = nil
		inputs["keyName"] = nil
		inputs["licenseSpecifications"] = nil
		inputs["monitoring"] = nil
		inputs["name"] = nil
		inputs["namePrefix"] = nil
		inputs["networkInterfaces"] = nil
		inputs["placement"] = nil
		inputs["ramDiskId"] = nil
		inputs["securityGroupNames"] = nil
		inputs["tagSpecifications"] = nil
		inputs["tags"] = nil
		inputs["userData"] = nil
		inputs["vpcSecurityGroupIds"] = nil
	} else {
		inputs["blockDeviceMappings"] = args.BlockDeviceMappings
		inputs["capacityReservationSpecification"] = args.CapacityReservationSpecification
		inputs["creditSpecification"] = args.CreditSpecification
		inputs["description"] = args.Description
		inputs["disableApiTermination"] = args.DisableApiTermination
		inputs["ebsOptimized"] = args.EbsOptimized
		inputs["elasticGpuSpecifications"] = args.ElasticGpuSpecifications
		inputs["elasticInferenceAccelerator"] = args.ElasticInferenceAccelerator
		inputs["iamInstanceProfile"] = args.IamInstanceProfile
		inputs["imageId"] = args.ImageId
		inputs["instanceInitiatedShutdownBehavior"] = args.InstanceInitiatedShutdownBehavior
		inputs["instanceMarketOptions"] = args.InstanceMarketOptions
		inputs["instanceType"] = args.InstanceType
		inputs["kernelId"] = args.KernelId
		inputs["keyName"] = args.KeyName
		inputs["licenseSpecifications"] = args.LicenseSpecifications
		inputs["monitoring"] = args.Monitoring
		inputs["name"] = args.Name
		inputs["namePrefix"] = args.NamePrefix
		inputs["networkInterfaces"] = args.NetworkInterfaces
		inputs["placement"] = args.Placement
		inputs["ramDiskId"] = args.RamDiskId
		inputs["securityGroupNames"] = args.SecurityGroupNames
		inputs["tagSpecifications"] = args.TagSpecifications
		inputs["tags"] = args.Tags
		inputs["userData"] = args.UserData
		inputs["vpcSecurityGroupIds"] = args.VpcSecurityGroupIds
	}
	inputs["arn"] = nil
	inputs["defaultVersion"] = nil
	inputs["latestVersion"] = nil
	s, err := ctx.RegisterResource("aws:ec2/launchTemplate:LaunchTemplate", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &LaunchTemplate{s: s}, nil
}

// GetLaunchTemplate gets an existing LaunchTemplate resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetLaunchTemplate(ctx *pulumi.Context,
	name string, id pulumi.ID, state *LaunchTemplateState, opts ...pulumi.ResourceOpt) (*LaunchTemplate, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["arn"] = state.Arn
		inputs["blockDeviceMappings"] = state.BlockDeviceMappings
		inputs["capacityReservationSpecification"] = state.CapacityReservationSpecification
		inputs["creditSpecification"] = state.CreditSpecification
		inputs["defaultVersion"] = state.DefaultVersion
		inputs["description"] = state.Description
		inputs["disableApiTermination"] = state.DisableApiTermination
		inputs["ebsOptimized"] = state.EbsOptimized
		inputs["elasticGpuSpecifications"] = state.ElasticGpuSpecifications
		inputs["elasticInferenceAccelerator"] = state.ElasticInferenceAccelerator
		inputs["iamInstanceProfile"] = state.IamInstanceProfile
		inputs["imageId"] = state.ImageId
		inputs["instanceInitiatedShutdownBehavior"] = state.InstanceInitiatedShutdownBehavior
		inputs["instanceMarketOptions"] = state.InstanceMarketOptions
		inputs["instanceType"] = state.InstanceType
		inputs["kernelId"] = state.KernelId
		inputs["keyName"] = state.KeyName
		inputs["latestVersion"] = state.LatestVersion
		inputs["licenseSpecifications"] = state.LicenseSpecifications
		inputs["monitoring"] = state.Monitoring
		inputs["name"] = state.Name
		inputs["namePrefix"] = state.NamePrefix
		inputs["networkInterfaces"] = state.NetworkInterfaces
		inputs["placement"] = state.Placement
		inputs["ramDiskId"] = state.RamDiskId
		inputs["securityGroupNames"] = state.SecurityGroupNames
		inputs["tagSpecifications"] = state.TagSpecifications
		inputs["tags"] = state.Tags
		inputs["userData"] = state.UserData
		inputs["vpcSecurityGroupIds"] = state.VpcSecurityGroupIds
	}
	s, err := ctx.ReadResource("aws:ec2/launchTemplate:LaunchTemplate", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &LaunchTemplate{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *LaunchTemplate) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *LaunchTemplate) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// Amazon Resource Name (ARN) of the launch template.
func (r *LaunchTemplate) Arn() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["arn"])
}

// Specify volumes to attach to the instance besides the volumes specified by the AMI.
// See Block Devices below for details.
func (r *LaunchTemplate) BlockDeviceMappings() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["blockDeviceMappings"])
}

// Targeting for EC2 capacity reservations. See Capacity Reservation Specification below for more details.
func (r *LaunchTemplate) CapacityReservationSpecification() *pulumi.Output {
	return r.s.State["capacityReservationSpecification"]
}

// Customize the credit specification of the instance. See Credit
// Specification below for more details.
func (r *LaunchTemplate) CreditSpecification() *pulumi.Output {
	return r.s.State["creditSpecification"]
}

// The default version of the launch template.
func (r *LaunchTemplate) DefaultVersion() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["defaultVersion"])
}

// Description of the launch template.
func (r *LaunchTemplate) Description() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["description"])
}

// If `true`, enables [EC2 Instance
// Termination Protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingDisableAPITermination)
func (r *LaunchTemplate) DisableApiTermination() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["disableApiTermination"])
}

// If `true`, the launched EC2 instance will be EBS-optimized.
func (r *LaunchTemplate) EbsOptimized() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["ebsOptimized"])
}

// The elastic GPU to attach to the instance. See Elastic GPU
// below for more details.
func (r *LaunchTemplate) ElasticGpuSpecifications() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["elasticGpuSpecifications"])
}

// Configuration block containing an Elastic Inference Accelerator to attach to the instance. See Elastic Inference Accelerator below for more details.
func (r *LaunchTemplate) ElasticInferenceAccelerator() *pulumi.Output {
	return r.s.State["elasticInferenceAccelerator"]
}

// The IAM Instance Profile to launch the instance with. See Instance Profile
// below for more details.
func (r *LaunchTemplate) IamInstanceProfile() *pulumi.Output {
	return r.s.State["iamInstanceProfile"]
}

// The AMI from which to launch the instance.
func (r *LaunchTemplate) ImageId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["imageId"])
}

// Shutdown behavior for the instance. Can be `stop` or `terminate`.
// (Default: `stop`).
func (r *LaunchTemplate) InstanceInitiatedShutdownBehavior() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["instanceInitiatedShutdownBehavior"])
}

// The market (purchasing) option for the instance. See Market Options
// below for details.
func (r *LaunchTemplate) InstanceMarketOptions() *pulumi.Output {
	return r.s.State["instanceMarketOptions"]
}

// The type of the instance.
func (r *LaunchTemplate) InstanceType() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["instanceType"])
}

// The kernel ID.
func (r *LaunchTemplate) KernelId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["kernelId"])
}

// The key name to use for the instance.
func (r *LaunchTemplate) KeyName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["keyName"])
}

// The latest version of the launch template.
func (r *LaunchTemplate) LatestVersion() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["latestVersion"])
}

// A list of license specifications to associate with. See License Specification below for more details.
func (r *LaunchTemplate) LicenseSpecifications() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["licenseSpecifications"])
}

// The monitoring option for the instance. See Monitoring below for more details.
func (r *LaunchTemplate) Monitoring() *pulumi.Output {
	return r.s.State["monitoring"]
}

func (r *LaunchTemplate) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// Creates a unique name beginning with the specified prefix. Conflicts with `name`.
func (r *LaunchTemplate) NamePrefix() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["namePrefix"])
}

// Customize network interfaces to be attached at instance boot time. See Network
// Interfaces below for more details.
func (r *LaunchTemplate) NetworkInterfaces() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["networkInterfaces"])
}

// The placement of the instance. See Placement below for more details.
func (r *LaunchTemplate) Placement() *pulumi.Output {
	return r.s.State["placement"]
}

// The ID of the RAM disk.
func (r *LaunchTemplate) RamDiskId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["ramDiskId"])
}

// A list of security group names to associate with. If you are creating Instances in a VPC, use
// `vpc_security_group_ids` instead.
func (r *LaunchTemplate) SecurityGroupNames() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["securityGroupNames"])
}

// The tags to apply to the resources during launch. See Tag Specifications below for more details.
func (r *LaunchTemplate) TagSpecifications() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["tagSpecifications"])
}

// A mapping of tags to assign to the launch template.
func (r *LaunchTemplate) Tags() *pulumi.MapOutput {
	return (*pulumi.MapOutput)(r.s.State["tags"])
}

// The Base64-encoded user data to provide when launching the instance.
func (r *LaunchTemplate) UserData() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["userData"])
}

// A list of security group IDs to associate with.
func (r *LaunchTemplate) VpcSecurityGroupIds() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["vpcSecurityGroupIds"])
}

// Input properties used for looking up and filtering LaunchTemplate resources.
type LaunchTemplateState struct {
	// Amazon Resource Name (ARN) of the launch template.
	Arn interface{}
	// Specify volumes to attach to the instance besides the volumes specified by the AMI.
	// See Block Devices below for details.
	BlockDeviceMappings interface{}
	// Targeting for EC2 capacity reservations. See Capacity Reservation Specification below for more details.
	CapacityReservationSpecification interface{}
	// Customize the credit specification of the instance. See Credit
	// Specification below for more details.
	CreditSpecification interface{}
	// The default version of the launch template.
	DefaultVersion interface{}
	// Description of the launch template.
	Description interface{}
	// If `true`, enables [EC2 Instance
	// Termination Protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingDisableAPITermination)
	DisableApiTermination interface{}
	// If `true`, the launched EC2 instance will be EBS-optimized.
	EbsOptimized interface{}
	// The elastic GPU to attach to the instance. See Elastic GPU
	// below for more details.
	ElasticGpuSpecifications interface{}
	// Configuration block containing an Elastic Inference Accelerator to attach to the instance. See Elastic Inference Accelerator below for more details.
	ElasticInferenceAccelerator interface{}
	// The IAM Instance Profile to launch the instance with. See Instance Profile
	// below for more details.
	IamInstanceProfile interface{}
	// The AMI from which to launch the instance.
	ImageId interface{}
	// Shutdown behavior for the instance. Can be `stop` or `terminate`.
	// (Default: `stop`).
	InstanceInitiatedShutdownBehavior interface{}
	// The market (purchasing) option for the instance. See Market Options
	// below for details.
	InstanceMarketOptions interface{}
	// The type of the instance.
	InstanceType interface{}
	// The kernel ID.
	KernelId interface{}
	// The key name to use for the instance.
	KeyName interface{}
	// The latest version of the launch template.
	LatestVersion interface{}
	// A list of license specifications to associate with. See License Specification below for more details.
	LicenseSpecifications interface{}
	// The monitoring option for the instance. See Monitoring below for more details.
	Monitoring interface{}
	Name interface{}
	// Creates a unique name beginning with the specified prefix. Conflicts with `name`.
	NamePrefix interface{}
	// Customize network interfaces to be attached at instance boot time. See Network
	// Interfaces below for more details.
	NetworkInterfaces interface{}
	// The placement of the instance. See Placement below for more details.
	Placement interface{}
	// The ID of the RAM disk.
	RamDiskId interface{}
	// A list of security group names to associate with. If you are creating Instances in a VPC, use
	// `vpc_security_group_ids` instead.
	SecurityGroupNames interface{}
	// The tags to apply to the resources during launch. See Tag Specifications below for more details.
	TagSpecifications interface{}
	// A mapping of tags to assign to the launch template.
	Tags interface{}
	// The Base64-encoded user data to provide when launching the instance.
	UserData interface{}
	// A list of security group IDs to associate with.
	VpcSecurityGroupIds interface{}
}

// The set of arguments for constructing a LaunchTemplate resource.
type LaunchTemplateArgs struct {
	// Specify volumes to attach to the instance besides the volumes specified by the AMI.
	// See Block Devices below for details.
	BlockDeviceMappings interface{}
	// Targeting for EC2 capacity reservations. See Capacity Reservation Specification below for more details.
	CapacityReservationSpecification interface{}
	// Customize the credit specification of the instance. See Credit
	// Specification below for more details.
	CreditSpecification interface{}
	// Description of the launch template.
	Description interface{}
	// If `true`, enables [EC2 Instance
	// Termination Protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingDisableAPITermination)
	DisableApiTermination interface{}
	// If `true`, the launched EC2 instance will be EBS-optimized.
	EbsOptimized interface{}
	// The elastic GPU to attach to the instance. See Elastic GPU
	// below for more details.
	ElasticGpuSpecifications interface{}
	// Configuration block containing an Elastic Inference Accelerator to attach to the instance. See Elastic Inference Accelerator below for more details.
	ElasticInferenceAccelerator interface{}
	// The IAM Instance Profile to launch the instance with. See Instance Profile
	// below for more details.
	IamInstanceProfile interface{}
	// The AMI from which to launch the instance.
	ImageId interface{}
	// Shutdown behavior for the instance. Can be `stop` or `terminate`.
	// (Default: `stop`).
	InstanceInitiatedShutdownBehavior interface{}
	// The market (purchasing) option for the instance. See Market Options
	// below for details.
	InstanceMarketOptions interface{}
	// The type of the instance.
	InstanceType interface{}
	// The kernel ID.
	KernelId interface{}
	// The key name to use for the instance.
	KeyName interface{}
	// A list of license specifications to associate with. See License Specification below for more details.
	LicenseSpecifications interface{}
	// The monitoring option for the instance. See Monitoring below for more details.
	Monitoring interface{}
	Name interface{}
	// Creates a unique name beginning with the specified prefix. Conflicts with `name`.
	NamePrefix interface{}
	// Customize network interfaces to be attached at instance boot time. See Network
	// Interfaces below for more details.
	NetworkInterfaces interface{}
	// The placement of the instance. See Placement below for more details.
	Placement interface{}
	// The ID of the RAM disk.
	RamDiskId interface{}
	// A list of security group names to associate with. If you are creating Instances in a VPC, use
	// `vpc_security_group_ids` instead.
	SecurityGroupNames interface{}
	// The tags to apply to the resources during launch. See Tag Specifications below for more details.
	TagSpecifications interface{}
	// A mapping of tags to assign to the launch template.
	Tags interface{}
	// The Base64-encoded user data to provide when launching the instance.
	UserData interface{}
	// A list of security group IDs to associate with.
	VpcSecurityGroupIds interface{}
}
