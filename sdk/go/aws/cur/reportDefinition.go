// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package cur

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Manages Cost and Usage Report Definitions.
// 
// > *NOTE:* The AWS Cost and Usage Report service is only available in `us-east-1` currently.
// 
// > *NOTE:* If AWS Organizations is enabled, only the master account can use this resource.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cur_report_definition.html.markdown.
type ReportDefinition struct {
	s *pulumi.ResourceState
}

// NewReportDefinition registers a new resource with the given unique name, arguments, and options.
func NewReportDefinition(ctx *pulumi.Context,
	name string, args *ReportDefinitionArgs, opts ...pulumi.ResourceOpt) (*ReportDefinition, error) {
	if args == nil || args.AdditionalSchemaElements == nil {
		return nil, errors.New("missing required argument 'AdditionalSchemaElements'")
	}
	if args == nil || args.Compression == nil {
		return nil, errors.New("missing required argument 'Compression'")
	}
	if args == nil || args.Format == nil {
		return nil, errors.New("missing required argument 'Format'")
	}
	if args == nil || args.ReportName == nil {
		return nil, errors.New("missing required argument 'ReportName'")
	}
	if args == nil || args.S3Bucket == nil {
		return nil, errors.New("missing required argument 'S3Bucket'")
	}
	if args == nil || args.S3Region == nil {
		return nil, errors.New("missing required argument 'S3Region'")
	}
	if args == nil || args.TimeUnit == nil {
		return nil, errors.New("missing required argument 'TimeUnit'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["additionalArtifacts"] = nil
		inputs["additionalSchemaElements"] = nil
		inputs["compression"] = nil
		inputs["format"] = nil
		inputs["reportName"] = nil
		inputs["s3Bucket"] = nil
		inputs["s3Prefix"] = nil
		inputs["s3Region"] = nil
		inputs["timeUnit"] = nil
	} else {
		inputs["additionalArtifacts"] = args.AdditionalArtifacts
		inputs["additionalSchemaElements"] = args.AdditionalSchemaElements
		inputs["compression"] = args.Compression
		inputs["format"] = args.Format
		inputs["reportName"] = args.ReportName
		inputs["s3Bucket"] = args.S3Bucket
		inputs["s3Prefix"] = args.S3Prefix
		inputs["s3Region"] = args.S3Region
		inputs["timeUnit"] = args.TimeUnit
	}
	s, err := ctx.RegisterResource("aws:cur/reportDefinition:ReportDefinition", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &ReportDefinition{s: s}, nil
}

// GetReportDefinition gets an existing ReportDefinition resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetReportDefinition(ctx *pulumi.Context,
	name string, id pulumi.ID, state *ReportDefinitionState, opts ...pulumi.ResourceOpt) (*ReportDefinition, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["additionalArtifacts"] = state.AdditionalArtifacts
		inputs["additionalSchemaElements"] = state.AdditionalSchemaElements
		inputs["compression"] = state.Compression
		inputs["format"] = state.Format
		inputs["reportName"] = state.ReportName
		inputs["s3Bucket"] = state.S3Bucket
		inputs["s3Prefix"] = state.S3Prefix
		inputs["s3Region"] = state.S3Region
		inputs["timeUnit"] = state.TimeUnit
	}
	s, err := ctx.ReadResource("aws:cur/reportDefinition:ReportDefinition", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &ReportDefinition{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *ReportDefinition) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *ReportDefinition) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// A list of additional artifacts. Valid values are: REDSHIFT, QUICKSIGHT.
func (r *ReportDefinition) AdditionalArtifacts() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["additionalArtifacts"])
}

// A list of schema elements. Valid values are: RESOURCES.
func (r *ReportDefinition) AdditionalSchemaElements() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["additionalSchemaElements"])
}

// Compression format for report. Valid values are: GZIP, ZIP.
func (r *ReportDefinition) Compression() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["compression"])
}

// Format for report. Valid values are: textORcsv.
func (r *ReportDefinition) Format() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["format"])
}

// Unique name for the report. Must start with a number/letter and is case sensitive. Limited to 256 characters.
func (r *ReportDefinition) ReportName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["reportName"])
}

// Name of the existing S3 bucket to hold generated reports.
func (r *ReportDefinition) S3Bucket() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["s3Bucket"])
}

// Report path prefix. Limited to 256 characters.
func (r *ReportDefinition) S3Prefix() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["s3Prefix"])
}

// Region of the existing S3 bucket to hold generated reports.
func (r *ReportDefinition) S3Region() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["s3Region"])
}

// The frequency on which report data are measured and displayed.  Valid values are: HOURLY, DAILY.
func (r *ReportDefinition) TimeUnit() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["timeUnit"])
}

// Input properties used for looking up and filtering ReportDefinition resources.
type ReportDefinitionState struct {
	// A list of additional artifacts. Valid values are: REDSHIFT, QUICKSIGHT.
	AdditionalArtifacts interface{}
	// A list of schema elements. Valid values are: RESOURCES.
	AdditionalSchemaElements interface{}
	// Compression format for report. Valid values are: GZIP, ZIP.
	Compression interface{}
	// Format for report. Valid values are: textORcsv.
	Format interface{}
	// Unique name for the report. Must start with a number/letter and is case sensitive. Limited to 256 characters.
	ReportName interface{}
	// Name of the existing S3 bucket to hold generated reports.
	S3Bucket interface{}
	// Report path prefix. Limited to 256 characters.
	S3Prefix interface{}
	// Region of the existing S3 bucket to hold generated reports.
	S3Region interface{}
	// The frequency on which report data are measured and displayed.  Valid values are: HOURLY, DAILY.
	TimeUnit interface{}
}

// The set of arguments for constructing a ReportDefinition resource.
type ReportDefinitionArgs struct {
	// A list of additional artifacts. Valid values are: REDSHIFT, QUICKSIGHT.
	AdditionalArtifacts interface{}
	// A list of schema elements. Valid values are: RESOURCES.
	AdditionalSchemaElements interface{}
	// Compression format for report. Valid values are: GZIP, ZIP.
	Compression interface{}
	// Format for report. Valid values are: textORcsv.
	Format interface{}
	// Unique name for the report. Must start with a number/letter and is case sensitive. Limited to 256 characters.
	ReportName interface{}
	// Name of the existing S3 bucket to hold generated reports.
	S3Bucket interface{}
	// Report path prefix. Limited to 256 characters.
	S3Prefix interface{}
	// Region of the existing S3 bucket to hold generated reports.
	S3Region interface{}
	// The frequency on which report data are measured and displayed.  Valid values are: HOURLY, DAILY.
	TimeUnit interface{}
}
