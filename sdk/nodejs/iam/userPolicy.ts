// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

import {PolicyDocument} from "./documents";

/**
 * Provides an IAM policy attached to a user.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const lbUser = new aws.iam.User("lb", {
 *     path: "/system/",
 * });
 * const lbAccessKey = new aws.iam.AccessKey("lb", {
 *     user: lbUser.name,
 * });
 * const lbRo = new aws.iam.UserPolicy("lb_ro", {
 *     policy: `{
 *   "Version": "2012-10-17",
 *   "Statement": [
 *     {
 *       "Action": [
 *         "ec2:Describe*"
 *       ],
 *       "Effect": "Allow",
 *       "Resource": "*"
 *     }
 *   ]
 * }
 * `,
 *     user: lbUser.name,
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_user_policy.html.markdown.
 */
export class UserPolicy extends pulumi.CustomResource {
    /**
     * Get an existing UserPolicy resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: UserPolicyState, opts?: pulumi.CustomResourceOptions): UserPolicy {
        return new UserPolicy(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:iam/userPolicy:UserPolicy';

    /**
     * Returns true if the given object is an instance of UserPolicy.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is UserPolicy {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === UserPolicy.__pulumiType;
    }

    /**
     * The name of the policy (always set).
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Creates a unique name beginning with the specified prefix. Conflicts with `name`.
     */
    public readonly namePrefix!: pulumi.Output<string | undefined>;
    public readonly policy!: pulumi.Output<string>;
    /**
     * IAM user to which to attach this policy.
     */
    public readonly user!: pulumi.Output<string>;

    /**
     * Create a UserPolicy resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: UserPolicyArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: UserPolicyArgs | UserPolicyState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as UserPolicyState | undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["namePrefix"] = state ? state.namePrefix : undefined;
            inputs["policy"] = state ? state.policy : undefined;
            inputs["user"] = state ? state.user : undefined;
        } else {
            const args = argsOrState as UserPolicyArgs | undefined;
            if (!args || args.policy === undefined) {
                throw new Error("Missing required property 'policy'");
            }
            if (!args || args.user === undefined) {
                throw new Error("Missing required property 'user'");
            }
            inputs["name"] = args ? args.name : undefined;
            inputs["namePrefix"] = args ? args.namePrefix : undefined;
            inputs["policy"] = args ? args.policy : undefined;
            inputs["user"] = args ? args.user : undefined;
        }
        super(UserPolicy.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering UserPolicy resources.
 */
export interface UserPolicyState {
    /**
     * The name of the policy (always set).
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Creates a unique name beginning with the specified prefix. Conflicts with `name`.
     */
    readonly namePrefix?: pulumi.Input<string>;
    readonly policy?: pulumi.Input<string | PolicyDocument>;
    /**
     * IAM user to which to attach this policy.
     */
    readonly user?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a UserPolicy resource.
 */
export interface UserPolicyArgs {
    /**
     * The name of the policy (always set).
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Creates a unique name beginning with the specified prefix. Conflicts with `name`.
     */
    readonly namePrefix?: pulumi.Input<string>;
    readonly policy: pulumi.Input<string | PolicyDocument>;
    /**
     * IAM user to which to attach this policy.
     */
    readonly user: pulumi.Input<string>;
}
