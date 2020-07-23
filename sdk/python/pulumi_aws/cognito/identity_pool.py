# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *


class IdentityPool(pulumi.CustomResource):
    allow_unauthenticated_identities: pulumi.Output[Optional[bool]] = pulumi.output_property("allowUnauthenticatedIdentities")
    """
    Whether the identity pool supports unauthenticated logins or not.
    """
    arn: pulumi.Output[str] = pulumi.output_property("arn")
    """
    The ARN of the identity pool.
    """
    cognito_identity_providers: pulumi.Output[Optional[List['outputs.IdentityPoolCognitoIdentityProvider']]] = pulumi.output_property("cognitoIdentityProviders")
    """
    An array of Amazon Cognito Identity user pools and their client IDs.
    """
    developer_provider_name: pulumi.Output[Optional[str]] = pulumi.output_property("developerProviderName")
    """
    The "domain" by which Cognito will refer to your users. This name acts as a placeholder that allows your
    backend and the Cognito service to communicate about the developer provider.
    """
    identity_pool_name: pulumi.Output[str] = pulumi.output_property("identityPoolName")
    """
    The Cognito Identity Pool name.
    """
    openid_connect_provider_arns: pulumi.Output[Optional[List[str]]] = pulumi.output_property("openidConnectProviderArns")
    """
    A list of OpendID Connect provider ARNs.
    """
    saml_provider_arns: pulumi.Output[Optional[List[str]]] = pulumi.output_property("samlProviderArns")
    """
    An array of Amazon Resource Names (ARNs) of the SAML provider for your identity.
    """
    supported_login_providers: pulumi.Output[Optional[Dict[str, str]]] = pulumi.output_property("supportedLoginProviders")
    """
    Key-Value pairs mapping provider names to provider app IDs.
    """
    tags: pulumi.Output[Optional[Dict[str, str]]] = pulumi.output_property("tags")
    """
    A map of tags to assign to the Identity Pool.
    """
    # pylint: disable=no-self-argument
    def __init__(__self__, resource_name, opts: Optional[pulumi.ResourceOptions] = None, allow_unauthenticated_identities=None, cognito_identity_providers=None, developer_provider_name=None, identity_pool_name=None, openid_connect_provider_arns=None, saml_provider_arns=None, supported_login_providers=None, tags=None, __props__=None, __name__=None, __opts__=None) -> None:
        """
        Provides an AWS Cognito Identity Pool.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        default = aws.iam.SamlProvider("default", saml_metadata_document=(lambda path: open(path).read())("saml-metadata.xml"))
        main = aws.cognito.IdentityPool("main",
            allow_unauthenticated_identities=False,
            cognito_identity_providers=[
                {
                    "client_id": "6lhlkkfbfb4q5kpp90urffae",
                    "provider_name": "cognito-idp.us-east-1.amazonaws.com/us-east-1_Tv0493apJ",
                    "serverSideTokenCheck": False,
                },
                {
                    "client_id": "7kodkvfqfb4qfkp39eurffae",
                    "provider_name": "cognito-idp.us-east-1.amazonaws.com/eu-west-1_Zr231apJu",
                    "serverSideTokenCheck": False,
                },
            ],
            identity_pool_name="identity pool",
            openid_connect_provider_arns=["arn:aws:iam::123456789012:oidc-provider/foo.example.com"],
            saml_provider_arns=[default.arn],
            supported_login_providers={
                "accounts.google.com": "123456789012.apps.googleusercontent.com",
                "graph.facebook.com": "7346241598935552",
            })
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] allow_unauthenticated_identities: Whether the identity pool supports unauthenticated logins or not.
        :param pulumi.Input[List[pulumi.Input['IdentityPoolCognitoIdentityProviderArgs']]] cognito_identity_providers: An array of Amazon Cognito Identity user pools and their client IDs.
        :param pulumi.Input[str] developer_provider_name: The "domain" by which Cognito will refer to your users. This name acts as a placeholder that allows your
               backend and the Cognito service to communicate about the developer provider.
        :param pulumi.Input[str] identity_pool_name: The Cognito Identity Pool name.
        :param pulumi.Input[List[pulumi.Input[str]]] openid_connect_provider_arns: A list of OpendID Connect provider ARNs.
        :param pulumi.Input[List[pulumi.Input[str]]] saml_provider_arns: An array of Amazon Resource Names (ARNs) of the SAML provider for your identity.
        :param pulumi.Input[Dict[str, pulumi.Input[str]]] supported_login_providers: Key-Value pairs mapping provider names to provider app IDs.
        :param pulumi.Input[Dict[str, pulumi.Input[str]]] tags: A map of tags to assign to the Identity Pool.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['allow_unauthenticated_identities'] = allow_unauthenticated_identities
            __props__['cognito_identity_providers'] = cognito_identity_providers
            __props__['developer_provider_name'] = developer_provider_name
            if identity_pool_name is None:
                raise TypeError("Missing required property 'identity_pool_name'")
            __props__['identity_pool_name'] = identity_pool_name
            __props__['openid_connect_provider_arns'] = openid_connect_provider_arns
            __props__['saml_provider_arns'] = saml_provider_arns
            __props__['supported_login_providers'] = supported_login_providers
            __props__['tags'] = tags
            __props__['arn'] = None
        super(IdentityPool, __self__).__init__(
            'aws:cognito/identityPool:IdentityPool',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, allow_unauthenticated_identities=None, arn=None, cognito_identity_providers=None, developer_provider_name=None, identity_pool_name=None, openid_connect_provider_arns=None, saml_provider_arns=None, supported_login_providers=None, tags=None):
        """
        Get an existing IdentityPool resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] allow_unauthenticated_identities: Whether the identity pool supports unauthenticated logins or not.
        :param pulumi.Input[str] arn: The ARN of the identity pool.
        :param pulumi.Input[List[pulumi.Input['IdentityPoolCognitoIdentityProviderArgs']]] cognito_identity_providers: An array of Amazon Cognito Identity user pools and their client IDs.
        :param pulumi.Input[str] developer_provider_name: The "domain" by which Cognito will refer to your users. This name acts as a placeholder that allows your
               backend and the Cognito service to communicate about the developer provider.
        :param pulumi.Input[str] identity_pool_name: The Cognito Identity Pool name.
        :param pulumi.Input[List[pulumi.Input[str]]] openid_connect_provider_arns: A list of OpendID Connect provider ARNs.
        :param pulumi.Input[List[pulumi.Input[str]]] saml_provider_arns: An array of Amazon Resource Names (ARNs) of the SAML provider for your identity.
        :param pulumi.Input[Dict[str, pulumi.Input[str]]] supported_login_providers: Key-Value pairs mapping provider names to provider app IDs.
        :param pulumi.Input[Dict[str, pulumi.Input[str]]] tags: A map of tags to assign to the Identity Pool.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["allow_unauthenticated_identities"] = allow_unauthenticated_identities
        __props__["arn"] = arn
        __props__["cognito_identity_providers"] = cognito_identity_providers
        __props__["developer_provider_name"] = developer_provider_name
        __props__["identity_pool_name"] = identity_pool_name
        __props__["openid_connect_provider_arns"] = openid_connect_provider_arns
        __props__["saml_provider_arns"] = saml_provider_arns
        __props__["supported_login_providers"] = supported_login_providers
        __props__["tags"] = tags
        return IdentityPool(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

