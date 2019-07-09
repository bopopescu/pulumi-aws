// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

export class SecurityGroupRule extends pulumi.CustomResource {
    /**
     * Get an existing SecurityGroupRule resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SecurityGroupRuleState, opts?: pulumi.CustomResourceOptions): SecurityGroupRule {
        return new SecurityGroupRule(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:ec2/securityGroupRule:SecurityGroupRule';

    /**
     * Returns true if the given object is an instance of SecurityGroupRule.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is SecurityGroupRule {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === SecurityGroupRule.__pulumiType;
    }

    /**
     * List of CIDR blocks. Cannot be specified with `source_security_group_id`.
     */
    public readonly cidrBlocks!: pulumi.Output<string[] | undefined>;
    /**
     * Description of the rule.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The start port (or ICMP type number if protocol is "icmp").
     */
    public readonly fromPort!: pulumi.Output<number>;
    /**
     * List of IPv6 CIDR blocks.
     */
    public readonly ipv6CidrBlocks!: pulumi.Output<string[] | undefined>;
    /**
     * List of prefix list IDs (for allowing access to VPC endpoints).
     * Only valid with `egress`.
     */
    public readonly prefixListIds!: pulumi.Output<string[] | undefined>;
    /**
     * The protocol. If not icmp, tcp, udp, or all use the [protocol number](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml)
     */
    public readonly protocol!: pulumi.Output<string>;
    /**
     * The security group to apply this rule to.
     */
    public readonly securityGroupId!: pulumi.Output<string>;
    /**
     * If true, the security group itself will be added as
     * a source to this ingress rule.
     */
    public readonly self!: pulumi.Output<boolean | undefined>;
    /**
     * The security group id to allow access to/from,
     * depending on the `type`. Cannot be specified with `cidr_blocks`.
     */
    public readonly sourceSecurityGroupId!: pulumi.Output<string>;
    /**
     * The end port (or ICMP code if protocol is "icmp").
     */
    public readonly toPort!: pulumi.Output<number>;
    /**
     * The type of rule being created. Valid options are `ingress` (inbound)
     * or `egress` (outbound).
     */
    public readonly type!: pulumi.Output<string>;

    /**
     * Create a SecurityGroupRule resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: SecurityGroupRuleArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: SecurityGroupRuleArgs | SecurityGroupRuleState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as SecurityGroupRuleState | undefined;
            inputs["cidrBlocks"] = state ? state.cidrBlocks : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["fromPort"] = state ? state.fromPort : undefined;
            inputs["ipv6CidrBlocks"] = state ? state.ipv6CidrBlocks : undefined;
            inputs["prefixListIds"] = state ? state.prefixListIds : undefined;
            inputs["protocol"] = state ? state.protocol : undefined;
            inputs["securityGroupId"] = state ? state.securityGroupId : undefined;
            inputs["self"] = state ? state.self : undefined;
            inputs["sourceSecurityGroupId"] = state ? state.sourceSecurityGroupId : undefined;
            inputs["toPort"] = state ? state.toPort : undefined;
            inputs["type"] = state ? state.type : undefined;
        } else {
            const args = argsOrState as SecurityGroupRuleArgs | undefined;
            if (!args || args.fromPort === undefined) {
                throw new Error("Missing required property 'fromPort'");
            }
            if (!args || args.protocol === undefined) {
                throw new Error("Missing required property 'protocol'");
            }
            if (!args || args.securityGroupId === undefined) {
                throw new Error("Missing required property 'securityGroupId'");
            }
            if (!args || args.toPort === undefined) {
                throw new Error("Missing required property 'toPort'");
            }
            if (!args || args.type === undefined) {
                throw new Error("Missing required property 'type'");
            }
            inputs["cidrBlocks"] = args ? args.cidrBlocks : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["fromPort"] = args ? args.fromPort : undefined;
            inputs["ipv6CidrBlocks"] = args ? args.ipv6CidrBlocks : undefined;
            inputs["prefixListIds"] = args ? args.prefixListIds : undefined;
            inputs["protocol"] = args ? args.protocol : undefined;
            inputs["securityGroupId"] = args ? args.securityGroupId : undefined;
            inputs["self"] = args ? args.self : undefined;
            inputs["sourceSecurityGroupId"] = args ? args.sourceSecurityGroupId : undefined;
            inputs["toPort"] = args ? args.toPort : undefined;
            inputs["type"] = args ? args.type : undefined;
        }
        super(SecurityGroupRule.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering SecurityGroupRule resources.
 */
export interface SecurityGroupRuleState {
    /**
     * List of CIDR blocks. Cannot be specified with `source_security_group_id`.
     */
    readonly cidrBlocks?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Description of the rule.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The start port (or ICMP type number if protocol is "icmp").
     */
    readonly fromPort?: pulumi.Input<number>;
    /**
     * List of IPv6 CIDR blocks.
     */
    readonly ipv6CidrBlocks?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * List of prefix list IDs (for allowing access to VPC endpoints).
     * Only valid with `egress`.
     */
    readonly prefixListIds?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The protocol. If not icmp, tcp, udp, or all use the [protocol number](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml)
     */
    readonly protocol?: pulumi.Input<string>;
    /**
     * The security group to apply this rule to.
     */
    readonly securityGroupId?: pulumi.Input<string>;
    /**
     * If true, the security group itself will be added as
     * a source to this ingress rule.
     */
    readonly self?: pulumi.Input<boolean>;
    /**
     * The security group id to allow access to/from,
     * depending on the `type`. Cannot be specified with `cidr_blocks`.
     */
    readonly sourceSecurityGroupId?: pulumi.Input<string>;
    /**
     * The end port (or ICMP code if protocol is "icmp").
     */
    readonly toPort?: pulumi.Input<number>;
    /**
     * The type of rule being created. Valid options are `ingress` (inbound)
     * or `egress` (outbound).
     */
    readonly type?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a SecurityGroupRule resource.
 */
export interface SecurityGroupRuleArgs {
    /**
     * List of CIDR blocks. Cannot be specified with `source_security_group_id`.
     */
    readonly cidrBlocks?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Description of the rule.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The start port (or ICMP type number if protocol is "icmp").
     */
    readonly fromPort: pulumi.Input<number>;
    /**
     * List of IPv6 CIDR blocks.
     */
    readonly ipv6CidrBlocks?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * List of prefix list IDs (for allowing access to VPC endpoints).
     * Only valid with `egress`.
     */
    readonly prefixListIds?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The protocol. If not icmp, tcp, udp, or all use the [protocol number](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml)
     */
    readonly protocol: pulumi.Input<string>;
    /**
     * The security group to apply this rule to.
     */
    readonly securityGroupId: pulumi.Input<string>;
    /**
     * If true, the security group itself will be added as
     * a source to this ingress rule.
     */
    readonly self?: pulumi.Input<boolean>;
    /**
     * The security group id to allow access to/from,
     * depending on the `type`. Cannot be specified with `cidr_blocks`.
     */
    readonly sourceSecurityGroupId?: pulumi.Input<string>;
    /**
     * The end port (or ICMP code if protocol is "icmp").
     */
    readonly toPort: pulumi.Input<number>;
    /**
     * The type of rule being created. Valid options are `ingress` (inbound)
     * or `egress` (outbound).
     */
    readonly type: pulumi.Input<string>;
}
