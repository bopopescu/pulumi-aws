// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package glue

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages a Glue Trigger resource.
//
// ## Example Usage
// ### Conditional Trigger
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v2/go/aws/glue"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := glue.NewTrigger(ctx, "example", &glue.TriggerArgs{
// 			Actions: glue.TriggerActionArray{
// 				&glue.TriggerActionArgs{
// 					JobName: pulumi.String(aws_glue_job.Example1.Name),
// 				},
// 			},
// 			Predicate: &glue.TriggerPredicateArgs{
// 				Conditions: glue.TriggerPredicateConditionArray{
// 					&glue.TriggerPredicateConditionArgs{
// 						JobName: pulumi.String(aws_glue_job.Example2.Name),
// 						State:   pulumi.String("SUCCEEDED"),
// 					},
// 				},
// 			},
// 			Type: pulumi.String("CONDITIONAL"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
// ### On-Demand Trigger
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v2/go/aws/glue"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := glue.NewTrigger(ctx, "example", &glue.TriggerArgs{
// 			Actions: glue.TriggerActionArray{
// 				&glue.TriggerActionArgs{
// 					JobName: pulumi.String(aws_glue_job.Example.Name),
// 				},
// 			},
// 			Type: pulumi.String("ON_DEMAND"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
// ### Scheduled Trigger
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v2/go/aws/glue"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := glue.NewTrigger(ctx, "example", &glue.TriggerArgs{
// 			Actions: glue.TriggerActionArray{
// 				&glue.TriggerActionArgs{
// 					JobName: pulumi.String(aws_glue_job.Example.Name),
// 				},
// 			},
// 			Schedule: pulumi.String("cron(15 12 * * ? *)"),
// 			Type:     pulumi.String("SCHEDULED"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
// ### Conditional Trigger with Crawler Action
//
// **Note:** Triggers can have both a crawler action and a crawler condition, just no example provided.
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v2/go/aws/glue"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := glue.NewTrigger(ctx, "example", &glue.TriggerArgs{
// 			Actions: glue.TriggerActionArray{
// 				&glue.TriggerActionArgs{
// 					CrawlerName: pulumi.String(aws_glue_crawler.Example1.Name),
// 				},
// 			},
// 			Predicate: &glue.TriggerPredicateArgs{
// 				Conditions: glue.TriggerPredicateConditionArray{
// 					&glue.TriggerPredicateConditionArgs{
// 						JobName: pulumi.String(aws_glue_job.Example2.Name),
// 						State:   pulumi.String("SUCCEEDED"),
// 					},
// 				},
// 			},
// 			Type: pulumi.String("CONDITIONAL"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
// ### Conditional Trigger with Crawler Condition
//
// **Note:** Triggers can have both a crawler action and a crawler condition, just no example provided.
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v2/go/aws/glue"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := glue.NewTrigger(ctx, "example", &glue.TriggerArgs{
// 			Actions: glue.TriggerActionArray{
// 				&glue.TriggerActionArgs{
// 					JobName: pulumi.String(aws_glue_job.Example1.Name),
// 				},
// 			},
// 			Predicate: &glue.TriggerPredicateArgs{
// 				Conditions: glue.TriggerPredicateConditionArray{
// 					&glue.TriggerPredicateConditionArgs{
// 						CrawlState:  pulumi.String("SUCCEEDED"),
// 						CrawlerName: pulumi.String(aws_glue_crawler.Example2.Name),
// 					},
// 				},
// 			},
// 			Type: pulumi.String("CONDITIONAL"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type Trigger struct {
	pulumi.CustomResourceState

	// List of actions initiated by this trigger when it fires. Defined below.
	Actions TriggerActionArrayOutput `pulumi:"actions"`
	// Amazon Resource Name (ARN) of Glue Trigger
	Arn pulumi.StringOutput `pulumi:"arn"`
	// A description of the new trigger.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// Start the trigger. Defaults to `true`. Not valid to disable for `ON_DEMAND` type.
	Enabled pulumi.BoolPtrOutput `pulumi:"enabled"`
	// The name of the trigger.
	Name pulumi.StringOutput `pulumi:"name"`
	// A predicate to specify when the new trigger should fire. Required when trigger type is `CONDITIONAL`. Defined below.
	Predicate TriggerPredicatePtrOutput `pulumi:"predicate"`
	// A cron expression used to specify the schedule. [Time-Based Schedules for Jobs and Crawlers](https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html)
	Schedule pulumi.StringPtrOutput `pulumi:"schedule"`
	// Key-value map of resource tags
	Tags pulumi.StringMapOutput `pulumi:"tags"`
	// The type of trigger. Valid values are `CONDITIONAL`, `ON_DEMAND`, and `SCHEDULED`.
	Type pulumi.StringOutput `pulumi:"type"`
	// A workflow to which the trigger should be associated to. Every workflow graph (DAG) needs a starting trigger (`ON_DEMAND` or `SCHEDULED` type) and can contain multiple additional `CONDITIONAL` triggers.
	WorkflowName pulumi.StringPtrOutput `pulumi:"workflowName"`
}

// NewTrigger registers a new resource with the given unique name, arguments, and options.
func NewTrigger(ctx *pulumi.Context,
	name string, args *TriggerArgs, opts ...pulumi.ResourceOption) (*Trigger, error) {
	if args == nil || args.Actions == nil {
		return nil, errors.New("missing required argument 'Actions'")
	}
	if args == nil || args.Type == nil {
		return nil, errors.New("missing required argument 'Type'")
	}
	if args == nil {
		args = &TriggerArgs{}
	}
	var resource Trigger
	err := ctx.RegisterResource("aws:glue/trigger:Trigger", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetTrigger gets an existing Trigger resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetTrigger(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *TriggerState, opts ...pulumi.ResourceOption) (*Trigger, error) {
	var resource Trigger
	err := ctx.ReadResource("aws:glue/trigger:Trigger", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Trigger resources.
type triggerState struct {
	// List of actions initiated by this trigger when it fires. Defined below.
	Actions []TriggerAction `pulumi:"actions"`
	// Amazon Resource Name (ARN) of Glue Trigger
	Arn *string `pulumi:"arn"`
	// A description of the new trigger.
	Description *string `pulumi:"description"`
	// Start the trigger. Defaults to `true`. Not valid to disable for `ON_DEMAND` type.
	Enabled *bool `pulumi:"enabled"`
	// The name of the trigger.
	Name *string `pulumi:"name"`
	// A predicate to specify when the new trigger should fire. Required when trigger type is `CONDITIONAL`. Defined below.
	Predicate *TriggerPredicate `pulumi:"predicate"`
	// A cron expression used to specify the schedule. [Time-Based Schedules for Jobs and Crawlers](https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html)
	Schedule *string `pulumi:"schedule"`
	// Key-value map of resource tags
	Tags map[string]string `pulumi:"tags"`
	// The type of trigger. Valid values are `CONDITIONAL`, `ON_DEMAND`, and `SCHEDULED`.
	Type *string `pulumi:"type"`
	// A workflow to which the trigger should be associated to. Every workflow graph (DAG) needs a starting trigger (`ON_DEMAND` or `SCHEDULED` type) and can contain multiple additional `CONDITIONAL` triggers.
	WorkflowName *string `pulumi:"workflowName"`
}

type TriggerState struct {
	// List of actions initiated by this trigger when it fires. Defined below.
	Actions TriggerActionArrayInput
	// Amazon Resource Name (ARN) of Glue Trigger
	Arn pulumi.StringPtrInput
	// A description of the new trigger.
	Description pulumi.StringPtrInput
	// Start the trigger. Defaults to `true`. Not valid to disable for `ON_DEMAND` type.
	Enabled pulumi.BoolPtrInput
	// The name of the trigger.
	Name pulumi.StringPtrInput
	// A predicate to specify when the new trigger should fire. Required when trigger type is `CONDITIONAL`. Defined below.
	Predicate TriggerPredicatePtrInput
	// A cron expression used to specify the schedule. [Time-Based Schedules for Jobs and Crawlers](https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html)
	Schedule pulumi.StringPtrInput
	// Key-value map of resource tags
	Tags pulumi.StringMapInput
	// The type of trigger. Valid values are `CONDITIONAL`, `ON_DEMAND`, and `SCHEDULED`.
	Type pulumi.StringPtrInput
	// A workflow to which the trigger should be associated to. Every workflow graph (DAG) needs a starting trigger (`ON_DEMAND` or `SCHEDULED` type) and can contain multiple additional `CONDITIONAL` triggers.
	WorkflowName pulumi.StringPtrInput
}

func (TriggerState) ElementType() reflect.Type {
	return reflect.TypeOf((*triggerState)(nil)).Elem()
}

type triggerArgs struct {
	// List of actions initiated by this trigger when it fires. Defined below.
	Actions []TriggerAction `pulumi:"actions"`
	// A description of the new trigger.
	Description *string `pulumi:"description"`
	// Start the trigger. Defaults to `true`. Not valid to disable for `ON_DEMAND` type.
	Enabled *bool `pulumi:"enabled"`
	// The name of the trigger.
	Name *string `pulumi:"name"`
	// A predicate to specify when the new trigger should fire. Required when trigger type is `CONDITIONAL`. Defined below.
	Predicate *TriggerPredicate `pulumi:"predicate"`
	// A cron expression used to specify the schedule. [Time-Based Schedules for Jobs and Crawlers](https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html)
	Schedule *string `pulumi:"schedule"`
	// Key-value map of resource tags
	Tags map[string]string `pulumi:"tags"`
	// The type of trigger. Valid values are `CONDITIONAL`, `ON_DEMAND`, and `SCHEDULED`.
	Type string `pulumi:"type"`
	// A workflow to which the trigger should be associated to. Every workflow graph (DAG) needs a starting trigger (`ON_DEMAND` or `SCHEDULED` type) and can contain multiple additional `CONDITIONAL` triggers.
	WorkflowName *string `pulumi:"workflowName"`
}

// The set of arguments for constructing a Trigger resource.
type TriggerArgs struct {
	// List of actions initiated by this trigger when it fires. Defined below.
	Actions TriggerActionArrayInput
	// A description of the new trigger.
	Description pulumi.StringPtrInput
	// Start the trigger. Defaults to `true`. Not valid to disable for `ON_DEMAND` type.
	Enabled pulumi.BoolPtrInput
	// The name of the trigger.
	Name pulumi.StringPtrInput
	// A predicate to specify when the new trigger should fire. Required when trigger type is `CONDITIONAL`. Defined below.
	Predicate TriggerPredicatePtrInput
	// A cron expression used to specify the schedule. [Time-Based Schedules for Jobs and Crawlers](https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html)
	Schedule pulumi.StringPtrInput
	// Key-value map of resource tags
	Tags pulumi.StringMapInput
	// The type of trigger. Valid values are `CONDITIONAL`, `ON_DEMAND`, and `SCHEDULED`.
	Type pulumi.StringInput
	// A workflow to which the trigger should be associated to. Every workflow graph (DAG) needs a starting trigger (`ON_DEMAND` or `SCHEDULED` type) and can contain multiple additional `CONDITIONAL` triggers.
	WorkflowName pulumi.StringPtrInput
}

func (TriggerArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*triggerArgs)(nil)).Elem()
}
