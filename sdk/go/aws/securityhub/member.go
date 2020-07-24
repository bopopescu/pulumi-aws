// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package securityhub

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides a Security Hub member resource.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v2/go/aws/securityhub"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := securityhub.NewAccount(ctx, "exampleAccount", nil)
// 		if err != nil {
// 			return err
// 		}
// 		_, err = securityhub.NewMember(ctx, "exampleMember", &securityhub.MemberArgs{
// 			AccountId: pulumi.String("123456789012"),
// 			Email:     pulumi.String("example@example.com"),
// 			Invite:    pulumi.Bool(true),
// 		}, pulumi.DependsOn([]pulumi.Resource{
// 			"aws_securityhub_account.example",
// 		}))
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type Member struct {
	pulumi.CustomResourceState

	// The ID of the member AWS account.
	AccountId pulumi.StringOutput `pulumi:"accountId"`
	// The email of the member AWS account.
	Email pulumi.StringOutput `pulumi:"email"`
	// Boolean whether to invite the account to Security Hub as a member. Defaults to `false`.
	Invite pulumi.BoolPtrOutput `pulumi:"invite"`
	// The ID of the main Security Hub AWS account.
	MainId pulumi.StringOutput `pulumi:"mainId"`
	// The status of the member account relationship.
	MemberStatus pulumi.StringOutput `pulumi:"memberStatus"`
}

// NewMember registers a new resource with the given unique name, arguments, and options.
func NewMember(ctx *pulumi.Context,
	name string, args *MemberArgs, opts ...pulumi.ResourceOption) (*Member, error) {
	if args == nil || args.AccountId == nil {
		return nil, errors.New("missing required argument 'AccountId'")
	}
	if args == nil || args.Email == nil {
		return nil, errors.New("missing required argument 'Email'")
	}
	if args == nil {
		args = &MemberArgs{}
	}
	var resource Member
	err := ctx.RegisterResource("aws:securityhub/member:Member", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetMember gets an existing Member resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetMember(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *MemberState, opts ...pulumi.ResourceOption) (*Member, error) {
	var resource Member
	err := ctx.ReadResource("aws:securityhub/member:Member", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Member resources.
type memberState struct {
	// The ID of the member AWS account.
	AccountId *string `pulumi:"accountId"`
	// The email of the member AWS account.
	Email *string `pulumi:"email"`
	// Boolean whether to invite the account to Security Hub as a member. Defaults to `false`.
	Invite *bool `pulumi:"invite"`
	// The ID of the main Security Hub AWS account.
	MainId *string `pulumi:"mainId"`
	// The status of the member account relationship.
	MemberStatus *string `pulumi:"memberStatus"`
}

type MemberState struct {
	// The ID of the member AWS account.
	AccountId pulumi.StringPtrInput
	// The email of the member AWS account.
	Email pulumi.StringPtrInput
	// Boolean whether to invite the account to Security Hub as a member. Defaults to `false`.
	Invite pulumi.BoolPtrInput
	// The ID of the main Security Hub AWS account.
	MainId pulumi.StringPtrInput
	// The status of the member account relationship.
	MemberStatus pulumi.StringPtrInput
}

func (MemberState) ElementType() reflect.Type {
	return reflect.TypeOf((*memberState)(nil)).Elem()
}

type memberArgs struct {
	// The ID of the member AWS account.
	AccountId string `pulumi:"accountId"`
	// The email of the member AWS account.
	Email string `pulumi:"email"`
	// Boolean whether to invite the account to Security Hub as a member. Defaults to `false`.
	Invite *bool `pulumi:"invite"`
}

// The set of arguments for constructing a Member resource.
type MemberArgs struct {
	// The ID of the member AWS account.
	AccountId pulumi.StringInput
	// The email of the member AWS account.
	Email pulumi.StringInput
	// Boolean whether to invite the account to Security Hub as a member. Defaults to `false`.
	Invite pulumi.BoolPtrInput
}

func (MemberArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*memberArgs)(nil)).Elem()
}
