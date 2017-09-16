// *** WARNING: this file was generated by the Pulumi Terraform Bridge (TFGEN) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as fabric from "@pulumi/pulumi-fabric";

export class TargetGroup extends fabric.Resource {
    public /*out*/ readonly arn: fabric.Computed<string>;
    public /*out*/ readonly arnSuffix: fabric.Computed<string>;
    public readonly deregistrationDelay?: fabric.Computed<number>;
    public readonly healthChecks: fabric.Computed<{ healthyThreshold?: number, interval?: number, matcher?: string, path?: string, port?: string, protocol?: string, timeout?: number, unhealthyThreshold?: number }[]>;
    public readonly name: fabric.Computed<string>;
    public readonly namePrefix?: fabric.Computed<string>;
    public readonly port: fabric.Computed<number>;
    public readonly protocol: fabric.Computed<string>;
    public readonly stickiness: fabric.Computed<{ cookieDuration?: number, enabled?: boolean, type: string }[]>;
    public readonly tags?: fabric.Computed<{[key: string]: any}>;
    public readonly vpcId: fabric.Computed<string>;

    constructor(urnName: string, args: TargetGroupArgs, dependsOn?: fabric.Resource[]) {
        if (args.port === undefined) {
            throw new Error("Missing required property 'port'");
        }
        if (args.protocol === undefined) {
            throw new Error("Missing required property 'protocol'");
        }
        if (args.vpcId === undefined) {
            throw new Error("Missing required property 'vpcId'");
        }
        super("aws:elasticloadbalancingv2/targetGroup:TargetGroup", urnName, {
            "deregistrationDelay": args.deregistrationDelay,
            "healthChecks": args.healthChecks,
            "name": args.name,
            "namePrefix": args.namePrefix,
            "port": args.port,
            "protocol": args.protocol,
            "stickiness": args.stickiness,
            "tags": args.tags,
            "vpcId": args.vpcId,
            "arn": undefined,
            "arnSuffix": undefined,
        }, dependsOn);
    }
}

export interface TargetGroupArgs {
    readonly deregistrationDelay?: fabric.MaybeComputed<number>;
    readonly healthChecks?: fabric.MaybeComputed<{ healthyThreshold?: fabric.MaybeComputed<number>, interval?: fabric.MaybeComputed<number>, matcher?: fabric.MaybeComputed<string>, path?: fabric.MaybeComputed<string>, port?: fabric.MaybeComputed<string>, protocol?: fabric.MaybeComputed<string>, timeout?: fabric.MaybeComputed<number>, unhealthyThreshold?: fabric.MaybeComputed<number> }>[];
    readonly name?: fabric.MaybeComputed<string>;
    readonly namePrefix?: fabric.MaybeComputed<string>;
    readonly port: fabric.MaybeComputed<number>;
    readonly protocol: fabric.MaybeComputed<string>;
    readonly stickiness?: fabric.MaybeComputed<{ cookieDuration?: fabric.MaybeComputed<number>, enabled?: fabric.MaybeComputed<boolean>, type: fabric.MaybeComputed<string> }>[];
    readonly tags?: fabric.MaybeComputed<{[key: string]: any}>;
    readonly vpcId: fabric.MaybeComputed<string>;
}

