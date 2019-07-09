// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package efs

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides an Elastic File System (EFS) resource.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/efs_file_system.html.markdown.
type FileSystem struct {
	s *pulumi.ResourceState
}

// NewFileSystem registers a new resource with the given unique name, arguments, and options.
func NewFileSystem(ctx *pulumi.Context,
	name string, args *FileSystemArgs, opts ...pulumi.ResourceOpt) (*FileSystem, error) {
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["creationToken"] = nil
		inputs["encrypted"] = nil
		inputs["kmsKeyId"] = nil
		inputs["performanceMode"] = nil
		inputs["provisionedThroughputInMibps"] = nil
		inputs["tags"] = nil
		inputs["throughputMode"] = nil
	} else {
		inputs["creationToken"] = args.CreationToken
		inputs["encrypted"] = args.Encrypted
		inputs["kmsKeyId"] = args.KmsKeyId
		inputs["performanceMode"] = args.PerformanceMode
		inputs["provisionedThroughputInMibps"] = args.ProvisionedThroughputInMibps
		inputs["tags"] = args.Tags
		inputs["throughputMode"] = args.ThroughputMode
	}
	inputs["arn"] = nil
	inputs["dnsName"] = nil
	s, err := ctx.RegisterResource("aws:efs/fileSystem:FileSystem", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &FileSystem{s: s}, nil
}

// GetFileSystem gets an existing FileSystem resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetFileSystem(ctx *pulumi.Context,
	name string, id pulumi.ID, state *FileSystemState, opts ...pulumi.ResourceOpt) (*FileSystem, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["arn"] = state.Arn
		inputs["creationToken"] = state.CreationToken
		inputs["dnsName"] = state.DnsName
		inputs["encrypted"] = state.Encrypted
		inputs["kmsKeyId"] = state.KmsKeyId
		inputs["performanceMode"] = state.PerformanceMode
		inputs["provisionedThroughputInMibps"] = state.ProvisionedThroughputInMibps
		inputs["tags"] = state.Tags
		inputs["throughputMode"] = state.ThroughputMode
	}
	s, err := ctx.ReadResource("aws:efs/fileSystem:FileSystem", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &FileSystem{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *FileSystem) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *FileSystem) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// Amazon Resource Name of the file system.
func (r *FileSystem) Arn() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["arn"])
}

func (r *FileSystem) CreationToken() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["creationToken"])
}

// The DNS name for the filesystem per [documented convention](http://docs.aws.amazon.com/efs/latest/ug/mounting-fs-mount-cmd-dns-name.html).
func (r *FileSystem) DnsName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["dnsName"])
}

// If true, the disk will be encrypted.
func (r *FileSystem) Encrypted() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["encrypted"])
}

// The ARN for the KMS encryption key. When specifying kms_key_id, encrypted needs to be set to true.
func (r *FileSystem) KmsKeyId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["kmsKeyId"])
}

// The file system performance mode. Can be either `"generalPurpose"` or `"maxIO"` (Default: `"generalPurpose"`).
func (r *FileSystem) PerformanceMode() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["performanceMode"])
}

// The throughput, measured in MiB/s, that you want to provision for the file system. Only applicable with `throughput_mode` set to `provisioned`.
func (r *FileSystem) ProvisionedThroughputInMibps() *pulumi.Float64Output {
	return (*pulumi.Float64Output)(r.s.State["provisionedThroughputInMibps"])
}

// A mapping of tags to assign to the file system.
func (r *FileSystem) Tags() *pulumi.MapOutput {
	return (*pulumi.MapOutput)(r.s.State["tags"])
}

// Throughput mode for the file system. Defaults to `bursting`. Valid values: `bursting`, `provisioned`. When using `provisioned`, also set `provisioned_throughput_in_mibps`.
func (r *FileSystem) ThroughputMode() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["throughputMode"])
}

// Input properties used for looking up and filtering FileSystem resources.
type FileSystemState struct {
	// Amazon Resource Name of the file system.
	Arn interface{}
	CreationToken interface{}
	// The DNS name for the filesystem per [documented convention](http://docs.aws.amazon.com/efs/latest/ug/mounting-fs-mount-cmd-dns-name.html).
	DnsName interface{}
	// If true, the disk will be encrypted.
	Encrypted interface{}
	// The ARN for the KMS encryption key. When specifying kms_key_id, encrypted needs to be set to true.
	KmsKeyId interface{}
	// The file system performance mode. Can be either `"generalPurpose"` or `"maxIO"` (Default: `"generalPurpose"`).
	PerformanceMode interface{}
	// The throughput, measured in MiB/s, that you want to provision for the file system. Only applicable with `throughput_mode` set to `provisioned`.
	ProvisionedThroughputInMibps interface{}
	// A mapping of tags to assign to the file system.
	Tags interface{}
	// Throughput mode for the file system. Defaults to `bursting`. Valid values: `bursting`, `provisioned`. When using `provisioned`, also set `provisioned_throughput_in_mibps`.
	ThroughputMode interface{}
}

// The set of arguments for constructing a FileSystem resource.
type FileSystemArgs struct {
	CreationToken interface{}
	// If true, the disk will be encrypted.
	Encrypted interface{}
	// The ARN for the KMS encryption key. When specifying kms_key_id, encrypted needs to be set to true.
	KmsKeyId interface{}
	// The file system performance mode. Can be either `"generalPurpose"` or `"maxIO"` (Default: `"generalPurpose"`).
	PerformanceMode interface{}
	// The throughput, measured in MiB/s, that you want to provision for the file system. Only applicable with `throughput_mode` set to `provisioned`.
	ProvisionedThroughputInMibps interface{}
	// A mapping of tags to assign to the file system.
	Tags interface{}
	// Throughput mode for the file system. Defaults to `bursting`. Valid values: `bursting`, `provisioned`. When using `provisioned`, also set `provisioned_throughput_in_mibps`.
	ThroughputMode interface{}
}
