// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package elasticache

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

type ReplicationGroup struct {
	s *pulumi.ResourceState
}

// NewReplicationGroup registers a new resource with the given unique name, arguments, and options.
func NewReplicationGroup(ctx *pulumi.Context,
	name string, args *ReplicationGroupArgs, opts ...pulumi.ResourceOpt) (*ReplicationGroup, error) {
	if args == nil || args.ReplicationGroupDescription == nil {
		return nil, errors.New("missing required argument 'ReplicationGroupDescription'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["applyImmediately"] = nil
		inputs["atRestEncryptionEnabled"] = nil
		inputs["authToken"] = nil
		inputs["autoMinorVersionUpgrade"] = nil
		inputs["automaticFailoverEnabled"] = nil
		inputs["availabilityZones"] = nil
		inputs["clusterMode"] = nil
		inputs["engine"] = nil
		inputs["engineVersion"] = nil
		inputs["maintenanceWindow"] = nil
		inputs["nodeType"] = nil
		inputs["notificationTopicArn"] = nil
		inputs["numberCacheClusters"] = nil
		inputs["parameterGroupName"] = nil
		inputs["port"] = nil
		inputs["replicationGroupDescription"] = nil
		inputs["replicationGroupId"] = nil
		inputs["securityGroupIds"] = nil
		inputs["securityGroupNames"] = nil
		inputs["snapshotArns"] = nil
		inputs["snapshotName"] = nil
		inputs["snapshotRetentionLimit"] = nil
		inputs["snapshotWindow"] = nil
		inputs["subnetGroupName"] = nil
		inputs["tags"] = nil
		inputs["transitEncryptionEnabled"] = nil
	} else {
		inputs["applyImmediately"] = args.ApplyImmediately
		inputs["atRestEncryptionEnabled"] = args.AtRestEncryptionEnabled
		inputs["authToken"] = args.AuthToken
		inputs["autoMinorVersionUpgrade"] = args.AutoMinorVersionUpgrade
		inputs["automaticFailoverEnabled"] = args.AutomaticFailoverEnabled
		inputs["availabilityZones"] = args.AvailabilityZones
		inputs["clusterMode"] = args.ClusterMode
		inputs["engine"] = args.Engine
		inputs["engineVersion"] = args.EngineVersion
		inputs["maintenanceWindow"] = args.MaintenanceWindow
		inputs["nodeType"] = args.NodeType
		inputs["notificationTopicArn"] = args.NotificationTopicArn
		inputs["numberCacheClusters"] = args.NumberCacheClusters
		inputs["parameterGroupName"] = args.ParameterGroupName
		inputs["port"] = args.Port
		inputs["replicationGroupDescription"] = args.ReplicationGroupDescription
		inputs["replicationGroupId"] = args.ReplicationGroupId
		inputs["securityGroupIds"] = args.SecurityGroupIds
		inputs["securityGroupNames"] = args.SecurityGroupNames
		inputs["snapshotArns"] = args.SnapshotArns
		inputs["snapshotName"] = args.SnapshotName
		inputs["snapshotRetentionLimit"] = args.SnapshotRetentionLimit
		inputs["snapshotWindow"] = args.SnapshotWindow
		inputs["subnetGroupName"] = args.SubnetGroupName
		inputs["tags"] = args.Tags
		inputs["transitEncryptionEnabled"] = args.TransitEncryptionEnabled
	}
	inputs["configurationEndpointAddress"] = nil
	inputs["memberClusters"] = nil
	inputs["primaryEndpointAddress"] = nil
	s, err := ctx.RegisterResource("aws:elasticache/replicationGroup:ReplicationGroup", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &ReplicationGroup{s: s}, nil
}

// GetReplicationGroup gets an existing ReplicationGroup resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetReplicationGroup(ctx *pulumi.Context,
	name string, id pulumi.ID, state *ReplicationGroupState, opts ...pulumi.ResourceOpt) (*ReplicationGroup, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["applyImmediately"] = state.ApplyImmediately
		inputs["atRestEncryptionEnabled"] = state.AtRestEncryptionEnabled
		inputs["authToken"] = state.AuthToken
		inputs["autoMinorVersionUpgrade"] = state.AutoMinorVersionUpgrade
		inputs["automaticFailoverEnabled"] = state.AutomaticFailoverEnabled
		inputs["availabilityZones"] = state.AvailabilityZones
		inputs["clusterMode"] = state.ClusterMode
		inputs["configurationEndpointAddress"] = state.ConfigurationEndpointAddress
		inputs["engine"] = state.Engine
		inputs["engineVersion"] = state.EngineVersion
		inputs["maintenanceWindow"] = state.MaintenanceWindow
		inputs["memberClusters"] = state.MemberClusters
		inputs["nodeType"] = state.NodeType
		inputs["notificationTopicArn"] = state.NotificationTopicArn
		inputs["numberCacheClusters"] = state.NumberCacheClusters
		inputs["parameterGroupName"] = state.ParameterGroupName
		inputs["port"] = state.Port
		inputs["primaryEndpointAddress"] = state.PrimaryEndpointAddress
		inputs["replicationGroupDescription"] = state.ReplicationGroupDescription
		inputs["replicationGroupId"] = state.ReplicationGroupId
		inputs["securityGroupIds"] = state.SecurityGroupIds
		inputs["securityGroupNames"] = state.SecurityGroupNames
		inputs["snapshotArns"] = state.SnapshotArns
		inputs["snapshotName"] = state.SnapshotName
		inputs["snapshotRetentionLimit"] = state.SnapshotRetentionLimit
		inputs["snapshotWindow"] = state.SnapshotWindow
		inputs["subnetGroupName"] = state.SubnetGroupName
		inputs["tags"] = state.Tags
		inputs["transitEncryptionEnabled"] = state.TransitEncryptionEnabled
	}
	s, err := ctx.ReadResource("aws:elasticache/replicationGroup:ReplicationGroup", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &ReplicationGroup{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *ReplicationGroup) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *ReplicationGroup) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// Specifies whether any modifications are applied immediately, or during the next maintenance window. Default is `false`.
func (r *ReplicationGroup) ApplyImmediately() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["applyImmediately"])
}

// Whether to enable encryption at rest.
func (r *ReplicationGroup) AtRestEncryptionEnabled() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["atRestEncryptionEnabled"])
}

// The password used to access a password protected server. Can be specified only if `transit_encryption_enabled = true`.
func (r *ReplicationGroup) AuthToken() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["authToken"])
}

// Specifies whether a minor engine upgrades will be applied automatically to the underlying Cache Cluster instances during the maintenance window. Defaults to `true`.
func (r *ReplicationGroup) AutoMinorVersionUpgrade() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["autoMinorVersionUpgrade"])
}

// Specifies whether a read-only replica will be automatically promoted to read/write primary if the existing primary fails. If true, Multi-AZ is enabled for this replication group. If false, Multi-AZ is disabled for this replication group. Must be enabled for Redis (cluster mode enabled) replication groups. Defaults to `false`.
func (r *ReplicationGroup) AutomaticFailoverEnabled() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["automaticFailoverEnabled"])
}

// A list of EC2 availability zones in which the replication group's cache clusters will be created. The order of the availability zones in the list is not important.
func (r *ReplicationGroup) AvailabilityZones() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["availabilityZones"])
}

// Create a native redis cluster. `automatic_failover_enabled` must be set to true. Cluster Mode documented below. Only 1 `cluster_mode` block is allowed.
func (r *ReplicationGroup) ClusterMode() *pulumi.Output {
	return r.s.State["clusterMode"]
}

// The address of the replication group configuration endpoint when cluster mode is enabled.
func (r *ReplicationGroup) ConfigurationEndpointAddress() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["configurationEndpointAddress"])
}

// The name of the cache engine to be used for the clusters in this replication group. e.g. `redis`
func (r *ReplicationGroup) Engine() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["engine"])
}

// The version number of the cache engine to be used for the cache clusters in this replication group.
func (r *ReplicationGroup) EngineVersion() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["engineVersion"])
}

// Specifies the weekly time range for when maintenance
// on the cache cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi` (24H Clock UTC).
// The minimum maintenance window is a 60 minute period. Example: `sun:05:00-sun:09:00`
func (r *ReplicationGroup) MaintenanceWindow() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["maintenanceWindow"])
}

// The identifiers of all the nodes that are part of this replication group.
func (r *ReplicationGroup) MemberClusters() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["memberClusters"])
}

// The compute and memory capacity of the nodes in the node group.
func (r *ReplicationGroup) NodeType() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["nodeType"])
}

// An Amazon Resource Name (ARN) of an
// SNS topic to send ElastiCache notifications to. Example:
// `arn:aws:sns:us-east-1:012345678999:my_sns_topic`
func (r *ReplicationGroup) NotificationTopicArn() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["notificationTopicArn"])
}

// The number of cache clusters (primary and replicas) this replication group will have. If Multi-AZ is enabled, the value of this parameter must be at least 2. Updates will occur before other modifications.
func (r *ReplicationGroup) NumberCacheClusters() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["numberCacheClusters"])
}

// The name of the parameter group to associate with this replication group. If this argument is omitted, the default cache parameter group for the specified engine is used.
func (r *ReplicationGroup) ParameterGroupName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["parameterGroupName"])
}

// The port number on which each of the cache nodes will accept connections. For Memcache the default is 11211, and for Redis the default port is 6379.
func (r *ReplicationGroup) Port() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["port"])
}

// (Redis only) The address of the endpoint for the primary node in the replication group, if the cluster mode is disabled.
func (r *ReplicationGroup) PrimaryEndpointAddress() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["primaryEndpointAddress"])
}

// A user-created description for the replication group.
func (r *ReplicationGroup) ReplicationGroupDescription() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["replicationGroupDescription"])
}

// The replication group identifier. This parameter is stored as a lowercase string.
func (r *ReplicationGroup) ReplicationGroupId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["replicationGroupId"])
}

// One or more Amazon VPC security groups associated with this replication group. Use this parameter only when you are creating a replication group in an Amazon Virtual Private Cloud
func (r *ReplicationGroup) SecurityGroupIds() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["securityGroupIds"])
}

// A list of cache security group names to associate with this replication group.
func (r *ReplicationGroup) SecurityGroupNames() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["securityGroupNames"])
}

// A single-element string list containing an
// Amazon Resource Name (ARN) of a Redis RDB snapshot file stored in Amazon S3.
// Example: `arn:aws:s3:::my_bucket/snapshot1.rdb`
func (r *ReplicationGroup) SnapshotArns() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["snapshotArns"])
}

// The name of a snapshot from which to restore data into the new node group. Changing the `snapshot_name` forces a new resource.
func (r *ReplicationGroup) SnapshotName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["snapshotName"])
}

// The number of days for which ElastiCache will
// retain automatic cache cluster snapshots before deleting them. For example, if you set
// SnapshotRetentionLimit to 5, then a snapshot that was taken today will be retained for 5 days
// before being deleted. If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
// Please note that setting a `snapshot_retention_limit` is not supported on cache.t1.micro or cache.t2.* cache nodes
func (r *ReplicationGroup) SnapshotRetentionLimit() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["snapshotRetentionLimit"])
}

// The daily time range (in UTC) during which ElastiCache will
// begin taking a daily snapshot of your cache cluster. The minimum snapshot window is a 60 minute period. Example: `05:00-09:00`
func (r *ReplicationGroup) SnapshotWindow() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["snapshotWindow"])
}

// The name of the cache subnet group to be used for the replication group.
func (r *ReplicationGroup) SubnetGroupName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["subnetGroupName"])
}

// A mapping of tags to assign to the resource
func (r *ReplicationGroup) Tags() *pulumi.MapOutput {
	return (*pulumi.MapOutput)(r.s.State["tags"])
}

// Whether to enable encryption in transit.
func (r *ReplicationGroup) TransitEncryptionEnabled() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["transitEncryptionEnabled"])
}

// Input properties used for looking up and filtering ReplicationGroup resources.
type ReplicationGroupState struct {
	// Specifies whether any modifications are applied immediately, or during the next maintenance window. Default is `false`.
	ApplyImmediately interface{}
	// Whether to enable encryption at rest.
	AtRestEncryptionEnabled interface{}
	// The password used to access a password protected server. Can be specified only if `transit_encryption_enabled = true`.
	AuthToken interface{}
	// Specifies whether a minor engine upgrades will be applied automatically to the underlying Cache Cluster instances during the maintenance window. Defaults to `true`.
	AutoMinorVersionUpgrade interface{}
	// Specifies whether a read-only replica will be automatically promoted to read/write primary if the existing primary fails. If true, Multi-AZ is enabled for this replication group. If false, Multi-AZ is disabled for this replication group. Must be enabled for Redis (cluster mode enabled) replication groups. Defaults to `false`.
	AutomaticFailoverEnabled interface{}
	// A list of EC2 availability zones in which the replication group's cache clusters will be created. The order of the availability zones in the list is not important.
	AvailabilityZones interface{}
	// Create a native redis cluster. `automatic_failover_enabled` must be set to true. Cluster Mode documented below. Only 1 `cluster_mode` block is allowed.
	ClusterMode interface{}
	// The address of the replication group configuration endpoint when cluster mode is enabled.
	ConfigurationEndpointAddress interface{}
	// The name of the cache engine to be used for the clusters in this replication group. e.g. `redis`
	Engine interface{}
	// The version number of the cache engine to be used for the cache clusters in this replication group.
	EngineVersion interface{}
	// Specifies the weekly time range for when maintenance
	// on the cache cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi` (24H Clock UTC).
	// The minimum maintenance window is a 60 minute period. Example: `sun:05:00-sun:09:00`
	MaintenanceWindow interface{}
	// The identifiers of all the nodes that are part of this replication group.
	MemberClusters interface{}
	// The compute and memory capacity of the nodes in the node group.
	NodeType interface{}
	// An Amazon Resource Name (ARN) of an
	// SNS topic to send ElastiCache notifications to. Example:
	// `arn:aws:sns:us-east-1:012345678999:my_sns_topic`
	NotificationTopicArn interface{}
	// The number of cache clusters (primary and replicas) this replication group will have. If Multi-AZ is enabled, the value of this parameter must be at least 2. Updates will occur before other modifications.
	NumberCacheClusters interface{}
	// The name of the parameter group to associate with this replication group. If this argument is omitted, the default cache parameter group for the specified engine is used.
	ParameterGroupName interface{}
	// The port number on which each of the cache nodes will accept connections. For Memcache the default is 11211, and for Redis the default port is 6379.
	Port interface{}
	// (Redis only) The address of the endpoint for the primary node in the replication group, if the cluster mode is disabled.
	PrimaryEndpointAddress interface{}
	// A user-created description for the replication group.
	ReplicationGroupDescription interface{}
	// The replication group identifier. This parameter is stored as a lowercase string.
	ReplicationGroupId interface{}
	// One or more Amazon VPC security groups associated with this replication group. Use this parameter only when you are creating a replication group in an Amazon Virtual Private Cloud
	SecurityGroupIds interface{}
	// A list of cache security group names to associate with this replication group.
	SecurityGroupNames interface{}
	// A single-element string list containing an
	// Amazon Resource Name (ARN) of a Redis RDB snapshot file stored in Amazon S3.
	// Example: `arn:aws:s3:::my_bucket/snapshot1.rdb`
	SnapshotArns interface{}
	// The name of a snapshot from which to restore data into the new node group. Changing the `snapshot_name` forces a new resource.
	SnapshotName interface{}
	// The number of days for which ElastiCache will
	// retain automatic cache cluster snapshots before deleting them. For example, if you set
	// SnapshotRetentionLimit to 5, then a snapshot that was taken today will be retained for 5 days
	// before being deleted. If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
	// Please note that setting a `snapshot_retention_limit` is not supported on cache.t1.micro or cache.t2.* cache nodes
	SnapshotRetentionLimit interface{}
	// The daily time range (in UTC) during which ElastiCache will
	// begin taking a daily snapshot of your cache cluster. The minimum snapshot window is a 60 minute period. Example: `05:00-09:00`
	SnapshotWindow interface{}
	// The name of the cache subnet group to be used for the replication group.
	SubnetGroupName interface{}
	// A mapping of tags to assign to the resource
	Tags interface{}
	// Whether to enable encryption in transit.
	TransitEncryptionEnabled interface{}
}

// The set of arguments for constructing a ReplicationGroup resource.
type ReplicationGroupArgs struct {
	// Specifies whether any modifications are applied immediately, or during the next maintenance window. Default is `false`.
	ApplyImmediately interface{}
	// Whether to enable encryption at rest.
	AtRestEncryptionEnabled interface{}
	// The password used to access a password protected server. Can be specified only if `transit_encryption_enabled = true`.
	AuthToken interface{}
	// Specifies whether a minor engine upgrades will be applied automatically to the underlying Cache Cluster instances during the maintenance window. Defaults to `true`.
	AutoMinorVersionUpgrade interface{}
	// Specifies whether a read-only replica will be automatically promoted to read/write primary if the existing primary fails. If true, Multi-AZ is enabled for this replication group. If false, Multi-AZ is disabled for this replication group. Must be enabled for Redis (cluster mode enabled) replication groups. Defaults to `false`.
	AutomaticFailoverEnabled interface{}
	// A list of EC2 availability zones in which the replication group's cache clusters will be created. The order of the availability zones in the list is not important.
	AvailabilityZones interface{}
	// Create a native redis cluster. `automatic_failover_enabled` must be set to true. Cluster Mode documented below. Only 1 `cluster_mode` block is allowed.
	ClusterMode interface{}
	// The name of the cache engine to be used for the clusters in this replication group. e.g. `redis`
	Engine interface{}
	// The version number of the cache engine to be used for the cache clusters in this replication group.
	EngineVersion interface{}
	// Specifies the weekly time range for when maintenance
	// on the cache cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi` (24H Clock UTC).
	// The minimum maintenance window is a 60 minute period. Example: `sun:05:00-sun:09:00`
	MaintenanceWindow interface{}
	// The compute and memory capacity of the nodes in the node group.
	NodeType interface{}
	// An Amazon Resource Name (ARN) of an
	// SNS topic to send ElastiCache notifications to. Example:
	// `arn:aws:sns:us-east-1:012345678999:my_sns_topic`
	NotificationTopicArn interface{}
	// The number of cache clusters (primary and replicas) this replication group will have. If Multi-AZ is enabled, the value of this parameter must be at least 2. Updates will occur before other modifications.
	NumberCacheClusters interface{}
	// The name of the parameter group to associate with this replication group. If this argument is omitted, the default cache parameter group for the specified engine is used.
	ParameterGroupName interface{}
	// The port number on which each of the cache nodes will accept connections. For Memcache the default is 11211, and for Redis the default port is 6379.
	Port interface{}
	// A user-created description for the replication group.
	ReplicationGroupDescription interface{}
	// The replication group identifier. This parameter is stored as a lowercase string.
	ReplicationGroupId interface{}
	// One or more Amazon VPC security groups associated with this replication group. Use this parameter only when you are creating a replication group in an Amazon Virtual Private Cloud
	SecurityGroupIds interface{}
	// A list of cache security group names to associate with this replication group.
	SecurityGroupNames interface{}
	// A single-element string list containing an
	// Amazon Resource Name (ARN) of a Redis RDB snapshot file stored in Amazon S3.
	// Example: `arn:aws:s3:::my_bucket/snapshot1.rdb`
	SnapshotArns interface{}
	// The name of a snapshot from which to restore data into the new node group. Changing the `snapshot_name` forces a new resource.
	SnapshotName interface{}
	// The number of days for which ElastiCache will
	// retain automatic cache cluster snapshots before deleting them. For example, if you set
	// SnapshotRetentionLimit to 5, then a snapshot that was taken today will be retained for 5 days
	// before being deleted. If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
	// Please note that setting a `snapshot_retention_limit` is not supported on cache.t1.micro or cache.t2.* cache nodes
	SnapshotRetentionLimit interface{}
	// The daily time range (in UTC) during which ElastiCache will
	// begin taking a daily snapshot of your cache cluster. The minimum snapshot window is a 60 minute period. Example: `05:00-09:00`
	SnapshotWindow interface{}
	// The name of the cache subnet group to be used for the replication group.
	SubnetGroupName interface{}
	// A mapping of tags to assign to the resource
	Tags interface{}
	// Whether to enable encryption in transit.
	TransitEncryptionEnabled interface{}
}
