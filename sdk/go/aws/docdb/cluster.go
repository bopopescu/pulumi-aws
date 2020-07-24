// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package docdb

import (
	"reflect"

	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages a DocDB Cluster.
//
// Changes to a DocDB Cluster can occur when you manually change a
// parameter, such as `port`, and are reflected in the next maintenance
// window. Because of this, this provider may report a difference in its planning
// phase because a modification has not yet taken place. You can use the
// `applyImmediately` flag to instruct the service to apply the change immediately
// (see documentation below).
//
// > **Note:** using `applyImmediately` can result in a brief downtime as the server reboots.
// **Note:** All arguments including the username and password will be stored in the raw state as plain-text.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v2/go/aws/docdb"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := docdb.NewCluster(ctx, "docdb", &docdb.ClusterArgs{
// 			BackupRetentionPeriod: pulumi.Int(5),
// 			ClusterIdentifier:     pulumi.String("my-docdb-cluster"),
// 			Engine:                pulumi.String("docdb"),
// 			MainPassword:        pulumi.String("mustbeeightchars"),
// 			MainUsername:        pulumi.String("foo"),
// 			PreferredBackupWindow: pulumi.String("07:00-09:00"),
// 			SkipFinalSnapshot:     pulumi.Bool(true),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type Cluster struct {
	pulumi.CustomResourceState

	// Specifies whether any cluster modifications
	// are applied immediately, or during the next maintenance window. Default is
	// `false`.
	ApplyImmediately pulumi.BoolOutput `pulumi:"applyImmediately"`
	// Amazon Resource Name (ARN) of cluster
	Arn pulumi.StringOutput `pulumi:"arn"`
	// A list of EC2 Availability Zones that
	// instances in the DB cluster can be created in.
	AvailabilityZones pulumi.StringArrayOutput `pulumi:"availabilityZones"`
	// The days to retain backups for. Default `1`
	BackupRetentionPeriod pulumi.IntPtrOutput `pulumi:"backupRetentionPeriod"`
	// The cluster identifier. If omitted, this provider will assign a random, unique identifier.
	ClusterIdentifier pulumi.StringOutput `pulumi:"clusterIdentifier"`
	// Creates a unique cluster identifier beginning with the specified prefix. Conflicts with `clusterIdentifer`.
	ClusterIdentifierPrefix pulumi.StringOutput `pulumi:"clusterIdentifierPrefix"`
	// List of DocDB Instances that are a part of this cluster
	ClusterMembers pulumi.StringArrayOutput `pulumi:"clusterMembers"`
	// The DocDB Cluster Resource ID
	ClusterResourceId pulumi.StringOutput `pulumi:"clusterResourceId"`
	// A cluster parameter group to associate with the cluster.
	DbClusterParameterGroupName pulumi.StringOutput `pulumi:"dbClusterParameterGroupName"`
	// A DB subnet group to associate with this DB instance.
	DbSubnetGroupName pulumi.StringOutput `pulumi:"dbSubnetGroupName"`
	// A value that indicates whether the DB cluster has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection is disabled.
	DeletionProtection pulumi.BoolPtrOutput `pulumi:"deletionProtection"`
	// List of log types to export to cloudwatch. If omitted, no logs will be exported.
	// The following log types are supported: `audit`, `profiler`.
	EnabledCloudwatchLogsExports pulumi.StringArrayOutput `pulumi:"enabledCloudwatchLogsExports"`
	// The DNS address of the DocDB instance
	Endpoint pulumi.StringOutput `pulumi:"endpoint"`
	// The name of the database engine to be used for this DB cluster. Defaults to `docdb`. Valid Values: `docdb`
	Engine pulumi.StringPtrOutput `pulumi:"engine"`
	// The database engine version. Updating this argument results in an outage.
	EngineVersion pulumi.StringOutput `pulumi:"engineVersion"`
	// The name of your final DB snapshot
	// when this DB cluster is deleted. If omitted, no final snapshot will be
	// made.
	FinalSnapshotIdentifier pulumi.StringPtrOutput `pulumi:"finalSnapshotIdentifier"`
	// The Route53 Hosted Zone ID of the endpoint
	HostedZoneId pulumi.StringOutput `pulumi:"hostedZoneId"`
	// The ARN for the KMS encryption key. When specifying `kmsKeyId`, `storageEncrypted` needs to be set to true.
	KmsKeyId pulumi.StringOutput `pulumi:"kmsKeyId"`
	// Password for the main DB user. Note that this may
	// show up in logs, and it will be stored in the state file. Please refer to the DocDB Naming Constraints.
	MainPassword pulumi.StringPtrOutput `pulumi:"mainPassword"`
	// Username for the main DB user.
	MainUsername pulumi.StringOutput `pulumi:"mainUsername"`
	// The port on which the DB accepts connections
	Port pulumi.IntPtrOutput `pulumi:"port"`
	// The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter.Time in UTC
	// Default: A 30-minute window selected at random from an 8-hour block of time per region. e.g. 04:00-09:00
	PreferredBackupWindow      pulumi.StringOutput `pulumi:"preferredBackupWindow"`
	PreferredMaintenanceWindow pulumi.StringOutput `pulumi:"preferredMaintenanceWindow"`
	// A read-only endpoint for the DocDB cluster, automatically load-balanced across replicas
	ReaderEndpoint pulumi.StringOutput `pulumi:"readerEndpoint"`
	// Determines whether a final DB snapshot is created before the DB cluster is deleted. If true is specified, no DB snapshot is created. If false is specified, a DB snapshot is created before the DB cluster is deleted, using the value from `finalSnapshotIdentifier`. Default is `false`.
	SkipFinalSnapshot pulumi.BoolPtrOutput `pulumi:"skipFinalSnapshot"`
	// Specifies whether or not to create this cluster from a snapshot. You can use either the name or ARN when specifying a DB cluster snapshot, or the ARN when specifying a DB snapshot.
	SnapshotIdentifier pulumi.StringPtrOutput `pulumi:"snapshotIdentifier"`
	// Specifies whether the DB cluster is encrypted. The default is `false`.
	StorageEncrypted pulumi.BoolPtrOutput `pulumi:"storageEncrypted"`
	// A map of tags to assign to the DB cluster.
	Tags pulumi.StringMapOutput `pulumi:"tags"`
	// List of VPC security groups to associate
	// with the Cluster
	VpcSecurityGroupIds pulumi.StringArrayOutput `pulumi:"vpcSecurityGroupIds"`
}

// NewCluster registers a new resource with the given unique name, arguments, and options.
func NewCluster(ctx *pulumi.Context,
	name string, args *ClusterArgs, opts ...pulumi.ResourceOption) (*Cluster, error) {
	if args == nil {
		args = &ClusterArgs{}
	}
	var resource Cluster
	err := ctx.RegisterResource("aws:docdb/cluster:Cluster", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetCluster gets an existing Cluster resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCluster(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ClusterState, opts ...pulumi.ResourceOption) (*Cluster, error) {
	var resource Cluster
	err := ctx.ReadResource("aws:docdb/cluster:Cluster", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Cluster resources.
type clusterState struct {
	// Specifies whether any cluster modifications
	// are applied immediately, or during the next maintenance window. Default is
	// `false`.
	ApplyImmediately *bool `pulumi:"applyImmediately"`
	// Amazon Resource Name (ARN) of cluster
	Arn *string `pulumi:"arn"`
	// A list of EC2 Availability Zones that
	// instances in the DB cluster can be created in.
	AvailabilityZones []string `pulumi:"availabilityZones"`
	// The days to retain backups for. Default `1`
	BackupRetentionPeriod *int `pulumi:"backupRetentionPeriod"`
	// The cluster identifier. If omitted, this provider will assign a random, unique identifier.
	ClusterIdentifier *string `pulumi:"clusterIdentifier"`
	// Creates a unique cluster identifier beginning with the specified prefix. Conflicts with `clusterIdentifer`.
	ClusterIdentifierPrefix *string `pulumi:"clusterIdentifierPrefix"`
	// List of DocDB Instances that are a part of this cluster
	ClusterMembers []string `pulumi:"clusterMembers"`
	// The DocDB Cluster Resource ID
	ClusterResourceId *string `pulumi:"clusterResourceId"`
	// A cluster parameter group to associate with the cluster.
	DbClusterParameterGroupName *string `pulumi:"dbClusterParameterGroupName"`
	// A DB subnet group to associate with this DB instance.
	DbSubnetGroupName *string `pulumi:"dbSubnetGroupName"`
	// A value that indicates whether the DB cluster has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection is disabled.
	DeletionProtection *bool `pulumi:"deletionProtection"`
	// List of log types to export to cloudwatch. If omitted, no logs will be exported.
	// The following log types are supported: `audit`, `profiler`.
	EnabledCloudwatchLogsExports []string `pulumi:"enabledCloudwatchLogsExports"`
	// The DNS address of the DocDB instance
	Endpoint *string `pulumi:"endpoint"`
	// The name of the database engine to be used for this DB cluster. Defaults to `docdb`. Valid Values: `docdb`
	Engine *string `pulumi:"engine"`
	// The database engine version. Updating this argument results in an outage.
	EngineVersion *string `pulumi:"engineVersion"`
	// The name of your final DB snapshot
	// when this DB cluster is deleted. If omitted, no final snapshot will be
	// made.
	FinalSnapshotIdentifier *string `pulumi:"finalSnapshotIdentifier"`
	// The Route53 Hosted Zone ID of the endpoint
	HostedZoneId *string `pulumi:"hostedZoneId"`
	// The ARN for the KMS encryption key. When specifying `kmsKeyId`, `storageEncrypted` needs to be set to true.
	KmsKeyId *string `pulumi:"kmsKeyId"`
	// Password for the main DB user. Note that this may
	// show up in logs, and it will be stored in the state file. Please refer to the DocDB Naming Constraints.
	MainPassword *string `pulumi:"mainPassword"`
	// Username for the main DB user.
	MainUsername *string `pulumi:"mainUsername"`
	// The port on which the DB accepts connections
	Port *int `pulumi:"port"`
	// The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter.Time in UTC
	// Default: A 30-minute window selected at random from an 8-hour block of time per region. e.g. 04:00-09:00
	PreferredBackupWindow      *string `pulumi:"preferredBackupWindow"`
	PreferredMaintenanceWindow *string `pulumi:"preferredMaintenanceWindow"`
	// A read-only endpoint for the DocDB cluster, automatically load-balanced across replicas
	ReaderEndpoint *string `pulumi:"readerEndpoint"`
	// Determines whether a final DB snapshot is created before the DB cluster is deleted. If true is specified, no DB snapshot is created. If false is specified, a DB snapshot is created before the DB cluster is deleted, using the value from `finalSnapshotIdentifier`. Default is `false`.
	SkipFinalSnapshot *bool `pulumi:"skipFinalSnapshot"`
	// Specifies whether or not to create this cluster from a snapshot. You can use either the name or ARN when specifying a DB cluster snapshot, or the ARN when specifying a DB snapshot.
	SnapshotIdentifier *string `pulumi:"snapshotIdentifier"`
	// Specifies whether the DB cluster is encrypted. The default is `false`.
	StorageEncrypted *bool `pulumi:"storageEncrypted"`
	// A map of tags to assign to the DB cluster.
	Tags map[string]string `pulumi:"tags"`
	// List of VPC security groups to associate
	// with the Cluster
	VpcSecurityGroupIds []string `pulumi:"vpcSecurityGroupIds"`
}

type ClusterState struct {
	// Specifies whether any cluster modifications
	// are applied immediately, or during the next maintenance window. Default is
	// `false`.
	ApplyImmediately pulumi.BoolPtrInput
	// Amazon Resource Name (ARN) of cluster
	Arn pulumi.StringPtrInput
	// A list of EC2 Availability Zones that
	// instances in the DB cluster can be created in.
	AvailabilityZones pulumi.StringArrayInput
	// The days to retain backups for. Default `1`
	BackupRetentionPeriod pulumi.IntPtrInput
	// The cluster identifier. If omitted, this provider will assign a random, unique identifier.
	ClusterIdentifier pulumi.StringPtrInput
	// Creates a unique cluster identifier beginning with the specified prefix. Conflicts with `clusterIdentifer`.
	ClusterIdentifierPrefix pulumi.StringPtrInput
	// List of DocDB Instances that are a part of this cluster
	ClusterMembers pulumi.StringArrayInput
	// The DocDB Cluster Resource ID
	ClusterResourceId pulumi.StringPtrInput
	// A cluster parameter group to associate with the cluster.
	DbClusterParameterGroupName pulumi.StringPtrInput
	// A DB subnet group to associate with this DB instance.
	DbSubnetGroupName pulumi.StringPtrInput
	// A value that indicates whether the DB cluster has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection is disabled.
	DeletionProtection pulumi.BoolPtrInput
	// List of log types to export to cloudwatch. If omitted, no logs will be exported.
	// The following log types are supported: `audit`, `profiler`.
	EnabledCloudwatchLogsExports pulumi.StringArrayInput
	// The DNS address of the DocDB instance
	Endpoint pulumi.StringPtrInput
	// The name of the database engine to be used for this DB cluster. Defaults to `docdb`. Valid Values: `docdb`
	Engine pulumi.StringPtrInput
	// The database engine version. Updating this argument results in an outage.
	EngineVersion pulumi.StringPtrInput
	// The name of your final DB snapshot
	// when this DB cluster is deleted. If omitted, no final snapshot will be
	// made.
	FinalSnapshotIdentifier pulumi.StringPtrInput
	// The Route53 Hosted Zone ID of the endpoint
	HostedZoneId pulumi.StringPtrInput
	// The ARN for the KMS encryption key. When specifying `kmsKeyId`, `storageEncrypted` needs to be set to true.
	KmsKeyId pulumi.StringPtrInput
	// Password for the main DB user. Note that this may
	// show up in logs, and it will be stored in the state file. Please refer to the DocDB Naming Constraints.
	MainPassword pulumi.StringPtrInput
	// Username for the main DB user.
	MainUsername pulumi.StringPtrInput
	// The port on which the DB accepts connections
	Port pulumi.IntPtrInput
	// The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter.Time in UTC
	// Default: A 30-minute window selected at random from an 8-hour block of time per region. e.g. 04:00-09:00
	PreferredBackupWindow      pulumi.StringPtrInput
	PreferredMaintenanceWindow pulumi.StringPtrInput
	// A read-only endpoint for the DocDB cluster, automatically load-balanced across replicas
	ReaderEndpoint pulumi.StringPtrInput
	// Determines whether a final DB snapshot is created before the DB cluster is deleted. If true is specified, no DB snapshot is created. If false is specified, a DB snapshot is created before the DB cluster is deleted, using the value from `finalSnapshotIdentifier`. Default is `false`.
	SkipFinalSnapshot pulumi.BoolPtrInput
	// Specifies whether or not to create this cluster from a snapshot. You can use either the name or ARN when specifying a DB cluster snapshot, or the ARN when specifying a DB snapshot.
	SnapshotIdentifier pulumi.StringPtrInput
	// Specifies whether the DB cluster is encrypted. The default is `false`.
	StorageEncrypted pulumi.BoolPtrInput
	// A map of tags to assign to the DB cluster.
	Tags pulumi.StringMapInput
	// List of VPC security groups to associate
	// with the Cluster
	VpcSecurityGroupIds pulumi.StringArrayInput
}

func (ClusterState) ElementType() reflect.Type {
	return reflect.TypeOf((*clusterState)(nil)).Elem()
}

type clusterArgs struct {
	// Specifies whether any cluster modifications
	// are applied immediately, or during the next maintenance window. Default is
	// `false`.
	ApplyImmediately *bool `pulumi:"applyImmediately"`
	// A list of EC2 Availability Zones that
	// instances in the DB cluster can be created in.
	AvailabilityZones []string `pulumi:"availabilityZones"`
	// The days to retain backups for. Default `1`
	BackupRetentionPeriod *int `pulumi:"backupRetentionPeriod"`
	// The cluster identifier. If omitted, this provider will assign a random, unique identifier.
	ClusterIdentifier *string `pulumi:"clusterIdentifier"`
	// Creates a unique cluster identifier beginning with the specified prefix. Conflicts with `clusterIdentifer`.
	ClusterIdentifierPrefix *string `pulumi:"clusterIdentifierPrefix"`
	// List of DocDB Instances that are a part of this cluster
	ClusterMembers []string `pulumi:"clusterMembers"`
	// A cluster parameter group to associate with the cluster.
	DbClusterParameterGroupName *string `pulumi:"dbClusterParameterGroupName"`
	// A DB subnet group to associate with this DB instance.
	DbSubnetGroupName *string `pulumi:"dbSubnetGroupName"`
	// A value that indicates whether the DB cluster has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection is disabled.
	DeletionProtection *bool `pulumi:"deletionProtection"`
	// List of log types to export to cloudwatch. If omitted, no logs will be exported.
	// The following log types are supported: `audit`, `profiler`.
	EnabledCloudwatchLogsExports []string `pulumi:"enabledCloudwatchLogsExports"`
	// The name of the database engine to be used for this DB cluster. Defaults to `docdb`. Valid Values: `docdb`
	Engine *string `pulumi:"engine"`
	// The database engine version. Updating this argument results in an outage.
	EngineVersion *string `pulumi:"engineVersion"`
	// The name of your final DB snapshot
	// when this DB cluster is deleted. If omitted, no final snapshot will be
	// made.
	FinalSnapshotIdentifier *string `pulumi:"finalSnapshotIdentifier"`
	// The ARN for the KMS encryption key. When specifying `kmsKeyId`, `storageEncrypted` needs to be set to true.
	KmsKeyId *string `pulumi:"kmsKeyId"`
	// Password for the main DB user. Note that this may
	// show up in logs, and it will be stored in the state file. Please refer to the DocDB Naming Constraints.
	MainPassword *string `pulumi:"mainPassword"`
	// Username for the main DB user.
	MainUsername *string `pulumi:"mainUsername"`
	// The port on which the DB accepts connections
	Port *int `pulumi:"port"`
	// The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter.Time in UTC
	// Default: A 30-minute window selected at random from an 8-hour block of time per region. e.g. 04:00-09:00
	PreferredBackupWindow      *string `pulumi:"preferredBackupWindow"`
	PreferredMaintenanceWindow *string `pulumi:"preferredMaintenanceWindow"`
	// Determines whether a final DB snapshot is created before the DB cluster is deleted. If true is specified, no DB snapshot is created. If false is specified, a DB snapshot is created before the DB cluster is deleted, using the value from `finalSnapshotIdentifier`. Default is `false`.
	SkipFinalSnapshot *bool `pulumi:"skipFinalSnapshot"`
	// Specifies whether or not to create this cluster from a snapshot. You can use either the name or ARN when specifying a DB cluster snapshot, or the ARN when specifying a DB snapshot.
	SnapshotIdentifier *string `pulumi:"snapshotIdentifier"`
	// Specifies whether the DB cluster is encrypted. The default is `false`.
	StorageEncrypted *bool `pulumi:"storageEncrypted"`
	// A map of tags to assign to the DB cluster.
	Tags map[string]string `pulumi:"tags"`
	// List of VPC security groups to associate
	// with the Cluster
	VpcSecurityGroupIds []string `pulumi:"vpcSecurityGroupIds"`
}

// The set of arguments for constructing a Cluster resource.
type ClusterArgs struct {
	// Specifies whether any cluster modifications
	// are applied immediately, or during the next maintenance window. Default is
	// `false`.
	ApplyImmediately pulumi.BoolPtrInput
	// A list of EC2 Availability Zones that
	// instances in the DB cluster can be created in.
	AvailabilityZones pulumi.StringArrayInput
	// The days to retain backups for. Default `1`
	BackupRetentionPeriod pulumi.IntPtrInput
	// The cluster identifier. If omitted, this provider will assign a random, unique identifier.
	ClusterIdentifier pulumi.StringPtrInput
	// Creates a unique cluster identifier beginning with the specified prefix. Conflicts with `clusterIdentifer`.
	ClusterIdentifierPrefix pulumi.StringPtrInput
	// List of DocDB Instances that are a part of this cluster
	ClusterMembers pulumi.StringArrayInput
	// A cluster parameter group to associate with the cluster.
	DbClusterParameterGroupName pulumi.StringPtrInput
	// A DB subnet group to associate with this DB instance.
	DbSubnetGroupName pulumi.StringPtrInput
	// A value that indicates whether the DB cluster has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection is disabled.
	DeletionProtection pulumi.BoolPtrInput
	// List of log types to export to cloudwatch. If omitted, no logs will be exported.
	// The following log types are supported: `audit`, `profiler`.
	EnabledCloudwatchLogsExports pulumi.StringArrayInput
	// The name of the database engine to be used for this DB cluster. Defaults to `docdb`. Valid Values: `docdb`
	Engine pulumi.StringPtrInput
	// The database engine version. Updating this argument results in an outage.
	EngineVersion pulumi.StringPtrInput
	// The name of your final DB snapshot
	// when this DB cluster is deleted. If omitted, no final snapshot will be
	// made.
	FinalSnapshotIdentifier pulumi.StringPtrInput
	// The ARN for the KMS encryption key. When specifying `kmsKeyId`, `storageEncrypted` needs to be set to true.
	KmsKeyId pulumi.StringPtrInput
	// Password for the main DB user. Note that this may
	// show up in logs, and it will be stored in the state file. Please refer to the DocDB Naming Constraints.
	MainPassword pulumi.StringPtrInput
	// Username for the main DB user.
	MainUsername pulumi.StringPtrInput
	// The port on which the DB accepts connections
	Port pulumi.IntPtrInput
	// The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter.Time in UTC
	// Default: A 30-minute window selected at random from an 8-hour block of time per region. e.g. 04:00-09:00
	PreferredBackupWindow      pulumi.StringPtrInput
	PreferredMaintenanceWindow pulumi.StringPtrInput
	// Determines whether a final DB snapshot is created before the DB cluster is deleted. If true is specified, no DB snapshot is created. If false is specified, a DB snapshot is created before the DB cluster is deleted, using the value from `finalSnapshotIdentifier`. Default is `false`.
	SkipFinalSnapshot pulumi.BoolPtrInput
	// Specifies whether or not to create this cluster from a snapshot. You can use either the name or ARN when specifying a DB cluster snapshot, or the ARN when specifying a DB snapshot.
	SnapshotIdentifier pulumi.StringPtrInput
	// Specifies whether the DB cluster is encrypted. The default is `false`.
	StorageEncrypted pulumi.BoolPtrInput
	// A map of tags to assign to the DB cluster.
	Tags pulumi.StringMapInput
	// List of VPC security groups to associate
	// with the Cluster
	VpcSecurityGroupIds pulumi.StringArrayInput
}

func (ClusterArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*clusterArgs)(nil)).Elem()
}
