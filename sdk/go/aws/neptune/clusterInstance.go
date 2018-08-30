// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package neptune

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// A Cluster Instance Resource defines attributes that are specific to a single instance in a Neptune Cluster.
// 
// You can simply add neptune instances and Neptune manages the replication. You can use the [count][1]
// meta-parameter to make multiple instances and join them all to the same Neptune Cluster, or you may specify different Cluster Instance resources with various `instance_class` sizes.
// 
type ClusterInstance struct {
	s *pulumi.ResourceState
}

// NewClusterInstance registers a new resource with the given unique name, arguments, and options.
func NewClusterInstance(ctx *pulumi.Context,
	name string, args *ClusterInstanceArgs, opts ...pulumi.ResourceOpt) (*ClusterInstance, error) {
	if args == nil || args.ClusterIdentifier == nil {
		return nil, errors.New("missing required argument 'ClusterIdentifier'")
	}
	if args == nil || args.InstanceClass == nil {
		return nil, errors.New("missing required argument 'InstanceClass'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["applyImmediately"] = nil
		inputs["autoMinorVersionUpgrade"] = nil
		inputs["availabilityZone"] = nil
		inputs["clusterIdentifier"] = nil
		inputs["engine"] = nil
		inputs["engineVersion"] = nil
		inputs["identifier"] = nil
		inputs["identifierPrefix"] = nil
		inputs["instanceClass"] = nil
		inputs["neptuneParameterGroupName"] = nil
		inputs["neptuneSubnetGroupName"] = nil
		inputs["port"] = nil
		inputs["preferredBackupWindow"] = nil
		inputs["preferredMaintenanceWindow"] = nil
		inputs["promotionTier"] = nil
		inputs["publiclyAccessible"] = nil
		inputs["tags"] = nil
	} else {
		inputs["applyImmediately"] = args.ApplyImmediately
		inputs["autoMinorVersionUpgrade"] = args.AutoMinorVersionUpgrade
		inputs["availabilityZone"] = args.AvailabilityZone
		inputs["clusterIdentifier"] = args.ClusterIdentifier
		inputs["engine"] = args.Engine
		inputs["engineVersion"] = args.EngineVersion
		inputs["identifier"] = args.Identifier
		inputs["identifierPrefix"] = args.IdentifierPrefix
		inputs["instanceClass"] = args.InstanceClass
		inputs["neptuneParameterGroupName"] = args.NeptuneParameterGroupName
		inputs["neptuneSubnetGroupName"] = args.NeptuneSubnetGroupName
		inputs["port"] = args.Port
		inputs["preferredBackupWindow"] = args.PreferredBackupWindow
		inputs["preferredMaintenanceWindow"] = args.PreferredMaintenanceWindow
		inputs["promotionTier"] = args.PromotionTier
		inputs["publiclyAccessible"] = args.PubliclyAccessible
		inputs["tags"] = args.Tags
	}
	inputs["address"] = nil
	inputs["arn"] = nil
	inputs["dbiResourceId"] = nil
	inputs["endpoint"] = nil
	inputs["kmsKeyArn"] = nil
	inputs["storageEncrypted"] = nil
	inputs["writer"] = nil
	s, err := ctx.RegisterResource("aws:neptune/clusterInstance:ClusterInstance", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &ClusterInstance{s: s}, nil
}

// GetClusterInstance gets an existing ClusterInstance resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetClusterInstance(ctx *pulumi.Context,
	name string, id pulumi.ID, state *ClusterInstanceState, opts ...pulumi.ResourceOpt) (*ClusterInstance, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["address"] = state.Address
		inputs["applyImmediately"] = state.ApplyImmediately
		inputs["arn"] = state.Arn
		inputs["autoMinorVersionUpgrade"] = state.AutoMinorVersionUpgrade
		inputs["availabilityZone"] = state.AvailabilityZone
		inputs["clusterIdentifier"] = state.ClusterIdentifier
		inputs["dbiResourceId"] = state.DbiResourceId
		inputs["endpoint"] = state.Endpoint
		inputs["engine"] = state.Engine
		inputs["engineVersion"] = state.EngineVersion
		inputs["identifier"] = state.Identifier
		inputs["identifierPrefix"] = state.IdentifierPrefix
		inputs["instanceClass"] = state.InstanceClass
		inputs["kmsKeyArn"] = state.KmsKeyArn
		inputs["neptuneParameterGroupName"] = state.NeptuneParameterGroupName
		inputs["neptuneSubnetGroupName"] = state.NeptuneSubnetGroupName
		inputs["port"] = state.Port
		inputs["preferredBackupWindow"] = state.PreferredBackupWindow
		inputs["preferredMaintenanceWindow"] = state.PreferredMaintenanceWindow
		inputs["promotionTier"] = state.PromotionTier
		inputs["publiclyAccessible"] = state.PubliclyAccessible
		inputs["storageEncrypted"] = state.StorageEncrypted
		inputs["tags"] = state.Tags
		inputs["writer"] = state.Writer
	}
	s, err := ctx.ReadResource("aws:neptune/clusterInstance:ClusterInstance", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &ClusterInstance{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *ClusterInstance) URN() *pulumi.URNOutput {
	return r.s.URN
}

// ID is this resource's unique identifier assigned by its provider.
func (r *ClusterInstance) ID() *pulumi.IDOutput {
	return r.s.ID
}

// The hostname of the instance. See also `endpoint` and `port`.
func (r *ClusterInstance) Address() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["address"])
}

// Specifies whether any instance modifications
// are applied immediately, or during the next maintenance window. Default is`false`.
func (r *ClusterInstance) ApplyImmediately() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["applyImmediately"])
}

// Amazon Resource Name (ARN) of neptune instance
func (r *ClusterInstance) Arn() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["arn"])
}

// Indicates that minor engine upgrades will be applied automatically to the instance during the maintenance window. Default is `true`.
func (r *ClusterInstance) AutoMinorVersionUpgrade() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["autoMinorVersionUpgrade"])
}

// The EC2 Availability Zone that the neptune instance is created in.
func (r *ClusterInstance) AvailabilityZone() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["availabilityZone"])
}

// The identifier of the [`aws_neptune_cluster`](https://www.terraform.io/docs/providers/aws/r/neptune_cluster.html) in which to launch this instance.
func (r *ClusterInstance) ClusterIdentifier() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["clusterIdentifier"])
}

// The region-unique, immutable identifier for the neptune instance.
func (r *ClusterInstance) DbiResourceId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["dbiResourceId"])
}

// The connection endpoint in `address:port` format.
func (r *ClusterInstance) Endpoint() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["endpoint"])
}

// The name of the database engine to be used for the neptune instance. Defaults to `neptune`. Valid Values: `neptune`.
func (r *ClusterInstance) Engine() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["engine"])
}

// The neptune engine version.
func (r *ClusterInstance) EngineVersion() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["engineVersion"])
}

// The indentifier for the neptune instance, if omitted, Terraform will assign a random, unique identifier.
func (r *ClusterInstance) Identifier() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["identifier"])
}

// Creates a unique identifier beginning with the specified prefix. Conflicts with `identifer`.
func (r *ClusterInstance) IdentifierPrefix() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["identifierPrefix"])
}

// The instance class to use.
func (r *ClusterInstance) InstanceClass() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["instanceClass"])
}

// The ARN for the KMS encryption key if one is set to the neptune cluster.
func (r *ClusterInstance) KmsKeyArn() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["kmsKeyArn"])
}

// The name of the neptune parameter group to associate with this instance.
func (r *ClusterInstance) NeptuneParameterGroupName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["neptuneParameterGroupName"])
}

// A subnet group to associate with this neptune instance. **NOTE:** This must match the `neptune_subnet_group_name` of the attached [`aws_neptune_cluster`](https://www.terraform.io/docs/providers/aws/r/neptune_cluster.html).
func (r *ClusterInstance) NeptuneSubnetGroupName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["neptuneSubnetGroupName"])
}

// The port on which the DB accepts connections. Defaults to `8182`.
func (r *ClusterInstance) Port() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["port"])
}

// The daily time range during which automated backups are created if automated backups are enabled. Eg: "04:00-09:00"
func (r *ClusterInstance) PreferredBackupWindow() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["preferredBackupWindow"])
}

// The window to perform maintenance in.
// Syntax: "ddd:hh24:mi-ddd:hh24:mi". Eg: "Mon:00:00-Mon:03:00".
func (r *ClusterInstance) PreferredMaintenanceWindow() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["preferredMaintenanceWindow"])
}

// Default 0. Failover Priority setting on instance level. The reader who has lower tier has higher priority to get promoter to writer.
func (r *ClusterInstance) PromotionTier() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["promotionTier"])
}

// Bool to control if instance is publicly accessible. Default is `false`.
func (r *ClusterInstance) PubliclyAccessible() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["publiclyAccessible"])
}

// Specifies whether the neptune cluster is encrypted.
func (r *ClusterInstance) StorageEncrypted() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["storageEncrypted"])
}

// A mapping of tags to assign to the instance.
func (r *ClusterInstance) Tags() *pulumi.MapOutput {
	return (*pulumi.MapOutput)(r.s.State["tags"])
}

// Boolean indicating if this instance is writable. `False` indicates this instance is a read replica.
func (r *ClusterInstance) Writer() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["writer"])
}

// Input properties used for looking up and filtering ClusterInstance resources.
type ClusterInstanceState struct {
	// The hostname of the instance. See also `endpoint` and `port`.
	Address interface{}
	// Specifies whether any instance modifications
	// are applied immediately, or during the next maintenance window. Default is`false`.
	ApplyImmediately interface{}
	// Amazon Resource Name (ARN) of neptune instance
	Arn interface{}
	// Indicates that minor engine upgrades will be applied automatically to the instance during the maintenance window. Default is `true`.
	AutoMinorVersionUpgrade interface{}
	// The EC2 Availability Zone that the neptune instance is created in.
	AvailabilityZone interface{}
	// The identifier of the [`aws_neptune_cluster`](https://www.terraform.io/docs/providers/aws/r/neptune_cluster.html) in which to launch this instance.
	ClusterIdentifier interface{}
	// The region-unique, immutable identifier for the neptune instance.
	DbiResourceId interface{}
	// The connection endpoint in `address:port` format.
	Endpoint interface{}
	// The name of the database engine to be used for the neptune instance. Defaults to `neptune`. Valid Values: `neptune`.
	Engine interface{}
	// The neptune engine version.
	EngineVersion interface{}
	// The indentifier for the neptune instance, if omitted, Terraform will assign a random, unique identifier.
	Identifier interface{}
	// Creates a unique identifier beginning with the specified prefix. Conflicts with `identifer`.
	IdentifierPrefix interface{}
	// The instance class to use.
	InstanceClass interface{}
	// The ARN for the KMS encryption key if one is set to the neptune cluster.
	KmsKeyArn interface{}
	// The name of the neptune parameter group to associate with this instance.
	NeptuneParameterGroupName interface{}
	// A subnet group to associate with this neptune instance. **NOTE:** This must match the `neptune_subnet_group_name` of the attached [`aws_neptune_cluster`](https://www.terraform.io/docs/providers/aws/r/neptune_cluster.html).
	NeptuneSubnetGroupName interface{}
	// The port on which the DB accepts connections. Defaults to `8182`.
	Port interface{}
	// The daily time range during which automated backups are created if automated backups are enabled. Eg: "04:00-09:00"
	PreferredBackupWindow interface{}
	// The window to perform maintenance in.
	// Syntax: "ddd:hh24:mi-ddd:hh24:mi". Eg: "Mon:00:00-Mon:03:00".
	PreferredMaintenanceWindow interface{}
	// Default 0. Failover Priority setting on instance level. The reader who has lower tier has higher priority to get promoter to writer.
	PromotionTier interface{}
	// Bool to control if instance is publicly accessible. Default is `false`.
	PubliclyAccessible interface{}
	// Specifies whether the neptune cluster is encrypted.
	StorageEncrypted interface{}
	// A mapping of tags to assign to the instance.
	Tags interface{}
	// Boolean indicating if this instance is writable. `False` indicates this instance is a read replica.
	Writer interface{}
}

// The set of arguments for constructing a ClusterInstance resource.
type ClusterInstanceArgs struct {
	// Specifies whether any instance modifications
	// are applied immediately, or during the next maintenance window. Default is`false`.
	ApplyImmediately interface{}
	// Indicates that minor engine upgrades will be applied automatically to the instance during the maintenance window. Default is `true`.
	AutoMinorVersionUpgrade interface{}
	// The EC2 Availability Zone that the neptune instance is created in.
	AvailabilityZone interface{}
	// The identifier of the [`aws_neptune_cluster`](https://www.terraform.io/docs/providers/aws/r/neptune_cluster.html) in which to launch this instance.
	ClusterIdentifier interface{}
	// The name of the database engine to be used for the neptune instance. Defaults to `neptune`. Valid Values: `neptune`.
	Engine interface{}
	// The neptune engine version.
	EngineVersion interface{}
	// The indentifier for the neptune instance, if omitted, Terraform will assign a random, unique identifier.
	Identifier interface{}
	// Creates a unique identifier beginning with the specified prefix. Conflicts with `identifer`.
	IdentifierPrefix interface{}
	// The instance class to use.
	InstanceClass interface{}
	// The name of the neptune parameter group to associate with this instance.
	NeptuneParameterGroupName interface{}
	// A subnet group to associate with this neptune instance. **NOTE:** This must match the `neptune_subnet_group_name` of the attached [`aws_neptune_cluster`](https://www.terraform.io/docs/providers/aws/r/neptune_cluster.html).
	NeptuneSubnetGroupName interface{}
	// The port on which the DB accepts connections. Defaults to `8182`.
	Port interface{}
	// The daily time range during which automated backups are created if automated backups are enabled. Eg: "04:00-09:00"
	PreferredBackupWindow interface{}
	// The window to perform maintenance in.
	// Syntax: "ddd:hh24:mi-ddd:hh24:mi". Eg: "Mon:00:00-Mon:03:00".
	PreferredMaintenanceWindow interface{}
	// Default 0. Failover Priority setting on instance level. The reader who has lower tier has higher priority to get promoter to writer.
	PromotionTier interface{}
	// Bool to control if instance is publicly accessible. Default is `false`.
	PubliclyAccessible interface{}
	// A mapping of tags to assign to the instance.
	Tags interface{}
}