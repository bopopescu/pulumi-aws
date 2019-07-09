// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package msk

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

type Configuration struct {
	s *pulumi.ResourceState
}

// NewConfiguration registers a new resource with the given unique name, arguments, and options.
func NewConfiguration(ctx *pulumi.Context,
	name string, args *ConfigurationArgs, opts ...pulumi.ResourceOpt) (*Configuration, error) {
	if args == nil || args.KafkaVersions == nil {
		return nil, errors.New("missing required argument 'KafkaVersions'")
	}
	if args == nil || args.ServerProperties == nil {
		return nil, errors.New("missing required argument 'ServerProperties'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["description"] = nil
		inputs["kafkaVersions"] = nil
		inputs["name"] = nil
		inputs["serverProperties"] = nil
	} else {
		inputs["description"] = args.Description
		inputs["kafkaVersions"] = args.KafkaVersions
		inputs["name"] = args.Name
		inputs["serverProperties"] = args.ServerProperties
	}
	inputs["arn"] = nil
	inputs["latestRevision"] = nil
	s, err := ctx.RegisterResource("aws:msk/configuration:Configuration", name, true, inputs, opts...)
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
		inputs["description"] = state.Description
		inputs["kafkaVersions"] = state.KafkaVersions
		inputs["latestRevision"] = state.LatestRevision
		inputs["name"] = state.Name
		inputs["serverProperties"] = state.ServerProperties
	}
	s, err := ctx.ReadResource("aws:msk/configuration:Configuration", name, id, inputs, opts...)
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

// Amazon Resource Name (ARN) of the configuration.
func (r *Configuration) Arn() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["arn"])
}

// Description of the configuration.
func (r *Configuration) Description() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["description"])
}

// List of Apache Kafka versions which can use this configuration.
func (r *Configuration) KafkaVersions() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["kafkaVersions"])
}

// Latest revision of the configuration.
func (r *Configuration) LatestRevision() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["latestRevision"])
}

// Name of the configuration.
func (r *Configuration) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// Contents of the server.properties file. Supported properties are documented in the [MSK Developer Guide](https://docs.aws.amazon.com/msk/latest/developerguide/msk-configuration-properties.html).
func (r *Configuration) ServerProperties() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["serverProperties"])
}

// Input properties used for looking up and filtering Configuration resources.
type ConfigurationState struct {
	// Amazon Resource Name (ARN) of the configuration.
	Arn interface{}
	// Description of the configuration.
	Description interface{}
	// List of Apache Kafka versions which can use this configuration.
	KafkaVersions interface{}
	// Latest revision of the configuration.
	LatestRevision interface{}
	// Name of the configuration.
	Name interface{}
	// Contents of the server.properties file. Supported properties are documented in the [MSK Developer Guide](https://docs.aws.amazon.com/msk/latest/developerguide/msk-configuration-properties.html).
	ServerProperties interface{}
}

// The set of arguments for constructing a Configuration resource.
type ConfigurationArgs struct {
	// Description of the configuration.
	Description interface{}
	// List of Apache Kafka versions which can use this configuration.
	KafkaVersions interface{}
	// Name of the configuration.
	Name interface{}
	// Contents of the server.properties file. Supported properties are documented in the [MSK Developer Guide](https://docs.aws.amazon.com/msk/latest/developerguide/msk-configuration-properties.html).
	ServerProperties interface{}
}
