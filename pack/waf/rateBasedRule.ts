// *** WARNING: this file was generated by the Pulumi Terraform Bridge (TFGEN) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as fabric from "@pulumi/pulumi-fabric";

/**
 * Provides a WAF Rate Based Rule Resource
 */
export class RateBasedRule extends fabric.Resource {
    /**
     * The name or description for the Amazon CloudWatch metric of this rule.
     */
    public readonly metricName: fabric.Computed<string>;
    /**
     * The name or description of the rule.
     */
    public readonly name: fabric.Computed<string>;
    /**
     * One of ByteMatchSet, IPSet, SizeConstraintSet, SqlInjectionMatchSet, or XssMatchSet objects to include in a rule.
     */
    public readonly predicates?: fabric.Computed<{ dataId: string, negated: boolean, type: string }[]>;
    /**
     * Valid value is IP.
     */
    public readonly rateKey: fabric.Computed<string>;
    /**
     * The maximum number of requests, which have an identical value in the field specified by the RateKey, allowed in a five-minute period. Minimum value is 2000.
     */
    public readonly rateLimit: fabric.Computed<number>;

    /**
     * Create a RateBasedRule resource with the given unique name, arguments and optional additional
     * resource dependencies.
     *
     * @param urnName A _unique_ name for this RateBasedRule instance
     * @param args A collection of arguments for creating this RateBasedRule intance
     * @param dependsOn A optional array of additional resources this intance depends on
     */
    constructor(urnName: string, args: RateBasedRuleArgs, dependsOn?: fabric.Resource[]) {
        if (args.metricName === undefined) {
            throw new Error("Missing required property 'metricName'");
        }
        if (args.rateKey === undefined) {
            throw new Error("Missing required property 'rateKey'");
        }
        if (args.rateLimit === undefined) {
            throw new Error("Missing required property 'rateLimit'");
        }
        super("aws:waf/rateBasedRule:RateBasedRule", urnName, {
            "metricName": args.metricName,
            "name": args.name,
            "predicates": args.predicates,
            "rateKey": args.rateKey,
            "rateLimit": args.rateLimit,
        }, dependsOn);
    }
}

/**
 * The set of arguments for constructing a RateBasedRule resource.
 */
export interface RateBasedRuleArgs {
    /**
     * The name or description for the Amazon CloudWatch metric of this rule.
     */
    readonly metricName: fabric.ComputedValue<string>;
    /**
     * The name or description of the rule.
     */
    readonly name?: fabric.ComputedValue<string>;
    /**
     * One of ByteMatchSet, IPSet, SizeConstraintSet, SqlInjectionMatchSet, or XssMatchSet objects to include in a rule.
     */
    readonly predicates?: fabric.ComputedValue<{ dataId: fabric.ComputedValue<string>, negated: fabric.ComputedValue<boolean>, type: fabric.ComputedValue<string> }>[];
    /**
     * Valid value is IP.
     */
    readonly rateKey: fabric.ComputedValue<string>;
    /**
     * The maximum number of requests, which have an identical value in the field specified by the RateKey, allowed in a five-minute period. Minimum value is 2000.
     */
    readonly rateLimit: fabric.ComputedValue<number>;
}
