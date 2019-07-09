// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package mq

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides an MQ Configuration Resource. 
// 
// For more information on Amazon MQ, see [Amazon MQ documentation](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/welcome.html).
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/mq_configuration.html.markdown.
type Configuration struct {
	s *pulumi.ResourceState
}

// NewConfiguration registers a new resource with the given unique name, arguments, and options.
func NewConfiguration(ctx *pulumi.Context,
	name string, args *ConfigurationArgs, opts ...pulumi.ResourceOpt) (*Configuration, error) {
	if args == nil || args.Data == nil {
		return nil, errors.New("missing required argument 'Data'")
	}
	if args == nil || args.EngineType == nil {
		return nil, errors.New("missing required argument 'EngineType'")
	}
	if args == nil || args.EngineVersion == nil {
		return nil, errors.New("missing required argument 'EngineVersion'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["data"] = nil
		inputs["description"] = nil
		inputs["engineType"] = nil
		inputs["engineVersion"] = nil
		inputs["name"] = nil
		inputs["tags"] = nil
	} else {
		inputs["data"] = args.Data
		inputs["description"] = args.Description
		inputs["engineType"] = args.EngineType
		inputs["engineVersion"] = args.EngineVersion
		inputs["name"] = args.Name
		inputs["tags"] = args.Tags
	}
	inputs["arn"] = nil
	inputs["latestRevision"] = nil
	s, err := ctx.RegisterResource("aws:mq/configuration:Configuration", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Configuration{s: s}, nil
}

// GetConfiguration gets an existing Configuration resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetConfiguration(ctx *pulumi.Context,
	name string, id pulumi.ID, state *ConfigurationState, opts ...pulumi.ResourceOpt) (*Configuration, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["arn"] = state.Arn
		inputs["data"] = state.Data
		inputs["description"] = state.Description
		inputs["engineType"] = state.EngineType
		inputs["engineVersion"] = state.EngineVersion
		inputs["latestRevision"] = state.LatestRevision
		inputs["name"] = state.Name
		inputs["tags"] = state.Tags
	}
	s, err := ctx.ReadResource("aws:mq/configuration:Configuration", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Configuration{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *Configuration) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *Configuration) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The ARN of the configuration.
func (r *Configuration) Arn() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["arn"])
}

// The broker configuration in XML format.
// See [official docs](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-broker-configuration-parameters.html)
// for supported parameters and format of the XML.
func (r *Configuration) Data() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["data"])
}

// The description of the configuration.
func (r *Configuration) Description() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["description"])
}

// The type of broker engine.
func (r *Configuration) EngineType() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["engineType"])
}

// The version of the broker engine.
func (r *Configuration) EngineVersion() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["engineVersion"])
}

// The latest revision of the configuration.
func (r *Configuration) LatestRevision() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["latestRevision"])
}

// The name of the configuration
func (r *Configuration) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// A mapping of tags to assign to the resource.
func (r *Configuration) Tags() *pulumi.MapOutput {
	return (*pulumi.MapOutput)(r.s.State["tags"])
}

// Input properties used for looking up and filtering Configuration resources.
type ConfigurationState struct {
	// The ARN of the configuration.
	Arn interface{}
	// The broker configuration in XML format.
	// See [official docs](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-broker-configuration-parameters.html)
	// for supported parameters and format of the XML.
	Data interface{}
	// The description of the configuration.
	Description interface{}
	// The type of broker engine.
	EngineType interface{}
	// The version of the broker engine.
	EngineVersion interface{}
	// The latest revision of the configuration.
	LatestRevision interface{}
	// The name of the configuration
	Name interface{}
	// A mapping of tags to assign to the resource.
	Tags interface{}
}

// The set of arguments for constructing a Configuration resource.
type ConfigurationArgs struct {
	// The broker configuration in XML format.
	// See [official docs](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-broker-configuration-parameters.html)
	// for supported parameters and format of the XML.
	Data interface{}
	// The description of the configuration.
	Description interface{}
	// The type of broker engine.
	EngineType interface{}
	// The version of the broker engine.
	EngineVersion interface{}
	// The name of the configuration
	Name interface{}
	// A mapping of tags to assign to the resource.
	Tags interface{}
}
