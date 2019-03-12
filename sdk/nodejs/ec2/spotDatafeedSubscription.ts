// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * > **Note:** There is only a single subscription allowed per account.
 * 
 * To help you understand the charges for your Spot instances, Amazon EC2 provides a data feed that describes your Spot instance usage and pricing.
 * This data feed is sent to an Amazon S3 bucket that you specify when you subscribe to the data feed.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const defaultBucket = new aws.s3.Bucket("default", {});
 * const defaultSpotDatafeedSubscription = new aws.ec2.SpotDatafeedSubscription("default", {
 *     bucket: defaultBucket.bucket,
 *     prefix: "my_subdirectory",
 * });
 * ```
 */
export class SpotDatafeedSubscription extends pulumi.CustomResource {
    /**
     * Get an existing SpotDatafeedSubscription resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SpotDatafeedSubscriptionState, opts?: pulumi.CustomResourceOptions): SpotDatafeedSubscription {
        return new SpotDatafeedSubscription(name, <any>state, { ...opts, id: id });
    }

    /**
     * The Amazon S3 bucket in which to store the Spot instance data feed.
     */
    public readonly bucket: pulumi.Output<string>;
    /**
     * Path of folder inside bucket to place spot pricing data.
     */
    public readonly prefix: pulumi.Output<string | undefined>;

    /**
     * Create a SpotDatafeedSubscription resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: SpotDatafeedSubscriptionArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: SpotDatafeedSubscriptionArgs | SpotDatafeedSubscriptionState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: SpotDatafeedSubscriptionState = argsOrState as SpotDatafeedSubscriptionState | undefined;
            inputs["bucket"] = state ? state.bucket : undefined;
            inputs["prefix"] = state ? state.prefix : undefined;
        } else {
            const args = argsOrState as SpotDatafeedSubscriptionArgs | undefined;
            if (!args || args.bucket === undefined) {
                throw new Error("Missing required property 'bucket'");
            }
            inputs["bucket"] = args ? args.bucket : undefined;
            inputs["prefix"] = args ? args.prefix : undefined;
        }
        super("aws:ec2/spotDatafeedSubscription:SpotDatafeedSubscription", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering SpotDatafeedSubscription resources.
 */
export interface SpotDatafeedSubscriptionState {
    /**
     * The Amazon S3 bucket in which to store the Spot instance data feed.
     */
    readonly bucket?: pulumi.Input<string>;
    /**
     * Path of folder inside bucket to place spot pricing data.
     */
    readonly prefix?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a SpotDatafeedSubscription resource.
 */
export interface SpotDatafeedSubscriptionArgs {
    /**
     * The Amazon S3 bucket in which to store the Spot instance data feed.
     */
    readonly bucket: pulumi.Input<string>;
    /**
     * Path of folder inside bucket to place spot pricing data.
     */
    readonly prefix?: pulumi.Input<string>;
}
