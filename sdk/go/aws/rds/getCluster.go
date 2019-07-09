// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package rds

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides information about a RDS cluster.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/rds_cluster.html.markdown.
func LookupCluster(ctx *pulumi.Context, args *GetClusterArgs) (*GetClusterResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["clusterIdentifier"] = args.ClusterIdentifier
		inputs["tags"] = args.Tags
	}
	outputs, err := ctx.Invoke("aws:rds/getCluster:getCluster", inputs)
	if err != nil {
		return nil, err
	}
	return &GetClusterResult{
		Arn: outputs["arn"],
		AvailabilityZones: outputs["availabilityZones"],
		BackupRetentionPeriod: outputs["backupRetentionPeriod"],
		ClusterIdentifier: outputs["clusterIdentifier"],
		ClusterMembers: outputs["clusterMembers"],
		ClusterResourceId: outputs["clusterResourceId"],
		DatabaseName: outputs["databaseName"],
		DbClusterParameterGroupName: outputs["dbClusterParameterGroupName"],
		DbSubnetGroupName: outputs["dbSubnetGroupName"],
		EnabledCloudwatchLogsExports: outputs["enabledCloudwatchLogsExports"],
		Endpoint: outputs["endpoint"],
		Engine: outputs["engine"],
		EngineVersion: outputs["engineVersion"],
		FinalSnapshotIdentifier: outputs["finalSnapshotIdentifier"],
		HostedZoneId: outputs["hostedZoneId"],
		IamDatabaseAuthenticationEnabled: outputs["iamDatabaseAuthenticationEnabled"],
		IamRoles: outputs["iamRoles"],
		KmsKeyId: outputs["kmsKeyId"],
		MasterUsername: outputs["masterUsername"],
		Port: outputs["port"],
		PreferredBackupWindow: outputs["preferredBackupWindow"],
		PreferredMaintenanceWindow: outputs["preferredMaintenanceWindow"],
		ReaderEndpoint: outputs["readerEndpoint"],
		ReplicationSourceIdentifier: outputs["replicationSourceIdentifier"],
		StorageEncrypted: outputs["storageEncrypted"],
		Tags: outputs["tags"],
		VpcSecurityGroupIds: outputs["vpcSecurityGroupIds"],
		Id: outputs["id"],
	}, nil
}

// A collection of arguments for invoking getCluster.
type GetClusterArgs struct {
	// The cluster identifier of the RDS cluster.
	ClusterIdentifier interface{}
	Tags interface{}
}

// A collection of values returned by getCluster.
type GetClusterResult struct {
	Arn interface{}
	AvailabilityZones interface{}
	BackupRetentionPeriod interface{}
	ClusterIdentifier interface{}
	ClusterMembers interface{}
	ClusterResourceId interface{}
	DatabaseName interface{}
	DbClusterParameterGroupName interface{}
	DbSubnetGroupName interface{}
	EnabledCloudwatchLogsExports interface{}
	Endpoint interface{}
	Engine interface{}
	EngineVersion interface{}
	FinalSnapshotIdentifier interface{}
	HostedZoneId interface{}
	IamDatabaseAuthenticationEnabled interface{}
	IamRoles interface{}
	KmsKeyId interface{}
	MasterUsername interface{}
	Port interface{}
	PreferredBackupWindow interface{}
	PreferredMaintenanceWindow interface{}
	ReaderEndpoint interface{}
	ReplicationSourceIdentifier interface{}
	StorageEncrypted interface{}
	Tags interface{}
	VpcSecurityGroupIds interface{}
	// id is the provider-assigned unique ID for this managed resource.
	Id interface{}
}
