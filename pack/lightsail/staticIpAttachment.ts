// *** WARNING: this file was generated by the Lumi Terraform Bridge (TFGEN) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as lumi from "@lumi/lumi";
import * as lumirt from "@lumi/lumirt";

export class StaticIpAttachment extends lumi.NamedResource implements StaticIpAttachmentArgs {
    public readonly instanceName: string;
    public readonly staticIpName: string;

    public static get(id: lumi.ID): StaticIpAttachment {
        return <any>undefined; // functionality provided by the runtime
    }

    public static query(q: any): StaticIpAttachment[] {
        return <any>undefined; // functionality provided by the runtime
    }

    constructor(name: string, args: StaticIpAttachmentArgs) {
        super(name);
        if (lumirt.defaultIfComputed(args.instanceName, "") === undefined) {
            throw new Error("Property argument 'instanceName' is required, but was missing");
        }
        this.instanceName = args.instanceName;
        if (lumirt.defaultIfComputed(args.staticIpName, "") === undefined) {
            throw new Error("Property argument 'staticIpName' is required, but was missing");
        }
        this.staticIpName = args.staticIpName;
    }
}

export interface StaticIpAttachmentArgs {
    readonly instanceName: string;
    readonly staticIpName: string;
}
