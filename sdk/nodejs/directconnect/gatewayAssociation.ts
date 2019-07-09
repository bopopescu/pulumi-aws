// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

export class GatewayAssociation extends pulumi.CustomResource {
    /**
     * Get an existing GatewayAssociation resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GatewayAssociationState, opts?: pulumi.CustomResourceOptions): GatewayAssociation {
        return new GatewayAssociation(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:directconnect/gatewayAssociation:GatewayAssociation';

    /**
     * Returns true if the given object is an instance of GatewayAssociation.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is GatewayAssociation {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === GatewayAssociation.__pulumiType;
    }

    /**
     * VPC prefixes (CIDRs) to advertise to the Direct Connect gateway. Defaults to the CIDR block of the VPC associated with the Virtual Gateway. To enable drift detection, must be configured.
     */
    public readonly allowedPrefixes!: pulumi.Output<string[]>;
    /**
     * The ID of the VGW or transit gateway with which to associate the Direct Connect gateway.
     * Used for single account Direct Connect gateway associations.
     */
    public readonly associatedGatewayId!: pulumi.Output<string>;
    /**
     * The ID of the AWS account that owns the VGW or transit gateway with which to associate the Direct Connect gateway.
     * Used for cross-account Direct Connect gateway associations.
     */
    public readonly associatedGatewayOwnerAccountId!: pulumi.Output<string>;
    /**
     * The type of the associated gateway, `transitGateway` or `virtualPrivateGateway`.
     */
    public /*out*/ readonly associatedGatewayType!: pulumi.Output<string>;
    /**
     * The ID of the Direct Connect gateway association.
     */
    public /*out*/ readonly dxGatewayAssociationId!: pulumi.Output<string>;
    /**
     * The ID of the Direct Connect gateway.
     */
    public readonly dxGatewayId!: pulumi.Output<string>;
    /**
     * The ID of the AWS account that owns the Direct Connect gateway.
     */
    public /*out*/ readonly dxGatewayOwnerAccountId!: pulumi.Output<string>;
    /**
     * The ID of the Direct Connect gateway association proposal.
     * Used for cross-account Direct Connect gateway associations.
     */
    public readonly proposalId!: pulumi.Output<string | undefined>;
    /**
     * *Deprecated:* Use `associated_gateway_id` instead. The ID of the VGW with which to associate the gateway.
     * Used for single account Direct Connect gateway associations.
     */
    public readonly vpnGatewayId!: pulumi.Output<string | undefined>;

    /**
     * Create a GatewayAssociation resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: GatewayAssociationArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: GatewayAssociationArgs | GatewayAssociationState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as GatewayAssociationState | undefined;
            inputs["allowedPrefixes"] = state ? state.allowedPrefixes : undefined;
            inputs["associatedGatewayId"] = state ? state.associatedGatewayId : undefined;
            inputs["associatedGatewayOwnerAccountId"] = state ? state.associatedGatewayOwnerAccountId : undefined;
            inputs["associatedGatewayType"] = state ? state.associatedGatewayType : undefined;
            inputs["dxGatewayAssociationId"] = state ? state.dxGatewayAssociationId : undefined;
            inputs["dxGatewayId"] = state ? state.dxGatewayId : undefined;
            inputs["dxGatewayOwnerAccountId"] = state ? state.dxGatewayOwnerAccountId : undefined;
            inputs["proposalId"] = state ? state.proposalId : undefined;
            inputs["vpnGatewayId"] = state ? state.vpnGatewayId : undefined;
        } else {
            const args = argsOrState as GatewayAssociationArgs | undefined;
            if (!args || args.dxGatewayId === undefined) {
                throw new Error("Missing required property 'dxGatewayId'");
            }
            inputs["allowedPrefixes"] = args ? args.allowedPrefixes : undefined;
            inputs["associatedGatewayId"] = args ? args.associatedGatewayId : undefined;
            inputs["associatedGatewayOwnerAccountId"] = args ? args.associatedGatewayOwnerAccountId : undefined;
            inputs["dxGatewayId"] = args ? args.dxGatewayId : undefined;
            inputs["proposalId"] = args ? args.proposalId : undefined;
            inputs["vpnGatewayId"] = args ? args.vpnGatewayId : undefined;
            inputs["associatedGatewayType"] = undefined /*out*/;
            inputs["dxGatewayAssociationId"] = undefined /*out*/;
            inputs["dxGatewayOwnerAccountId"] = undefined /*out*/;
        }
        super(GatewayAssociation.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering GatewayAssociation resources.
 */
export interface GatewayAssociationState {
    /**
     * VPC prefixes (CIDRs) to advertise to the Direct Connect gateway. Defaults to the CIDR block of the VPC associated with the Virtual Gateway. To enable drift detection, must be configured.
     */
    readonly allowedPrefixes?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The ID of the VGW or transit gateway with which to associate the Direct Connect gateway.
     * Used for single account Direct Connect gateway associations.
     */
    readonly associatedGatewayId?: pulumi.Input<string>;
    /**
     * The ID of the AWS account that owns the VGW or transit gateway with which to associate the Direct Connect gateway.
     * Used for cross-account Direct Connect gateway associations.
     */
    readonly associatedGatewayOwnerAccountId?: pulumi.Input<string>;
    /**
     * The type of the associated gateway, `transitGateway` or `virtualPrivateGateway`.
     */
    readonly associatedGatewayType?: pulumi.Input<string>;
    /**
     * The ID of the Direct Connect gateway association.
     */
    readonly dxGatewayAssociationId?: pulumi.Input<string>;
    /**
     * The ID of the Direct Connect gateway.
     */
    readonly dxGatewayId?: pulumi.Input<string>;
    /**
     * The ID of the AWS account that owns the Direct Connect gateway.
     */
    readonly dxGatewayOwnerAccountId?: pulumi.Input<string>;
    /**
     * The ID of the Direct Connect gateway association proposal.
     * Used for cross-account Direct Connect gateway associations.
     */
    readonly proposalId?: pulumi.Input<string>;
    /**
     * *Deprecated:* Use `associated_gateway_id` instead. The ID of the VGW with which to associate the gateway.
     * Used for single account Direct Connect gateway associations.
     */
    readonly vpnGatewayId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a GatewayAssociation resource.
 */
export interface GatewayAssociationArgs {
    /**
     * VPC prefixes (CIDRs) to advertise to the Direct Connect gateway. Defaults to the CIDR block of the VPC associated with the Virtual Gateway. To enable drift detection, must be configured.
     */
    readonly allowedPrefixes?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The ID of the VGW or transit gateway with which to associate the Direct Connect gateway.
     * Used for single account Direct Connect gateway associations.
     */
    readonly associatedGatewayId?: pulumi.Input<string>;
    /**
     * The ID of the AWS account that owns the VGW or transit gateway with which to associate the Direct Connect gateway.
     * Used for cross-account Direct Connect gateway associations.
     */
    readonly associatedGatewayOwnerAccountId?: pulumi.Input<string>;
    /**
     * The ID of the Direct Connect gateway.
     */
    readonly dxGatewayId: pulumi.Input<string>;
    /**
     * The ID of the Direct Connect gateway association proposal.
     * Used for cross-account Direct Connect gateway associations.
     */
    readonly proposalId?: pulumi.Input<string>;
    /**
     * *Deprecated:* Use `associated_gateway_id` instead. The ID of the VGW with which to associate the gateway.
     * Used for single account Direct Connect gateway associations.
     */
    readonly vpnGatewayId?: pulumi.Input<string>;
}
