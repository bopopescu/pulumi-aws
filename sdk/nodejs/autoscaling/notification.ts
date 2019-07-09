// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

import {NotificationType} from "./notificationType";

/**
 * Provides an AutoScaling Group with Notification support, via SNS Topics. Each of
 * the `notifications` map to a [Notification Configuration][2] inside Amazon Web
 * Services, and are applied to each AutoScaling Group you supply.
 * 
 * ## Example Usage
 * 
 * Basic usage:
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const bar = new aws.autoscaling.Group("bar", {});
 * const foo = new aws.autoscaling.Group("foo", {});
 * const example = new aws.sns.Topic("example", {});
 * const exampleNotifications = new aws.autoscaling.Notification("example_notifications", {
 *     groupNames: [
 *         bar.name,
 *         foo.name,
 *     ],
 *     notifications: [
 *         "autoscaling:EC2_INSTANCE_LAUNCH",
 *         "autoscaling:EC2_INSTANCE_TERMINATE",
 *         "autoscaling:EC2_INSTANCE_LAUNCH_ERROR",
 *         "autoscaling:EC2_INSTANCE_TERMINATE_ERROR",
 *     ],
 *     topicArn: example.arn,
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/autoscaling_notification.html.markdown.
 */
export class Notification extends pulumi.CustomResource {
    /**
     * Get an existing Notification resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NotificationState, opts?: pulumi.CustomResourceOptions): Notification {
        return new Notification(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:autoscaling/notification:Notification';

    /**
     * Returns true if the given object is an instance of Notification.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Notification {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Notification.__pulumiType;
    }

    /**
     * A list of AutoScaling Group Names
     */
    public readonly groupNames!: pulumi.Output<string[]>;
    /**
     * A list of Notification Types that trigger
     * notifications. Acceptable values are documented [in the AWS documentation here][1]
     */
    public readonly notifications!: pulumi.Output<NotificationType[]>;
    /**
     * The Topic ARN for notifications to be sent through
     */
    public readonly topicArn!: pulumi.Output<string>;

    /**
     * Create a Notification resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: NotificationArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: NotificationArgs | NotificationState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as NotificationState | undefined;
            inputs["groupNames"] = state ? state.groupNames : undefined;
            inputs["notifications"] = state ? state.notifications : undefined;
            inputs["topicArn"] = state ? state.topicArn : undefined;
        } else {
            const args = argsOrState as NotificationArgs | undefined;
            if (!args || args.groupNames === undefined) {
                throw new Error("Missing required property 'groupNames'");
            }
            if (!args || args.notifications === undefined) {
                throw new Error("Missing required property 'notifications'");
            }
            if (!args || args.topicArn === undefined) {
                throw new Error("Missing required property 'topicArn'");
            }
            inputs["groupNames"] = args ? args.groupNames : undefined;
            inputs["notifications"] = args ? args.notifications : undefined;
            inputs["topicArn"] = args ? args.topicArn : undefined;
        }
        super(Notification.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Notification resources.
 */
export interface NotificationState {
    /**
     * A list of AutoScaling Group Names
     */
    readonly groupNames?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * A list of Notification Types that trigger
     * notifications. Acceptable values are documented [in the AWS documentation here][1]
     */
    readonly notifications?: pulumi.Input<pulumi.Input<NotificationType>[]>;
    /**
     * The Topic ARN for notifications to be sent through
     */
    readonly topicArn?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Notification resource.
 */
export interface NotificationArgs {
    /**
     * A list of AutoScaling Group Names
     */
    readonly groupNames: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * A list of Notification Types that trigger
     * notifications. Acceptable values are documented [in the AWS documentation here][1]
     */
    readonly notifications: pulumi.Input<pulumi.Input<NotificationType>[]>;
    /**
     * The Topic ARN for notifications to be sent through
     */
    readonly topicArn: pulumi.Input<string>;
}
