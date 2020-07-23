# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables


class SecretVersion(pulumi.CustomResource):
    arn: pulumi.Output[str] = pulumi.output_property("arn")
    """
    The ARN of the secret.
    """
    secret_binary: pulumi.Output[Optional[str]] = pulumi.output_property("secretBinary")
    """
    Specifies binary data that you want to encrypt and store in this version of the secret. This is required if secret_string is not set. Needs to be encoded to base64.
    """
    secret_id: pulumi.Output[str] = pulumi.output_property("secretId")
    """
    Specifies the secret to which you want to add a new version. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret. The secret must already exist.
    """
    secret_string: pulumi.Output[Optional[str]] = pulumi.output_property("secretString")
    """
    Specifies text data that you want to encrypt and store in this version of the secret. This is required if secret_binary is not set.
    """
    version_id: pulumi.Output[str] = pulumi.output_property("versionId")
    """
    The unique identifier of the version of the secret.
    """
    version_stages: pulumi.Output[List[str]] = pulumi.output_property("versionStages")
    """
    Specifies a list of staging labels that are attached to this version of the secret. A staging label must be unique to a single version of the secret. If you specify a staging label that's already associated with a different version of the same secret then that staging label is automatically removed from the other version and attached to this version. If you do not specify a value, then AWS Secrets Manager automatically moves the staging label `AWSCURRENT` to this new version on creation.
    """
    # pylint: disable=no-self-argument
    def __init__(__self__, resource_name, opts: Optional[pulumi.ResourceOptions] = None, secret_binary=None, secret_id=None, secret_string=None, version_stages=None, __props__=None, __name__=None, __opts__=None) -> None:
        """
        Provides a resource to manage AWS Secrets Manager secret version including its secret value. To manage secret metadata, see the `secretsmanager.Secret` resource.

        > **NOTE:** If the `AWSCURRENT` staging label is present on this version during resource deletion, that label cannot be removed and will be skipped to prevent errors when fully deleting the secret. That label will leave this secret version active even after the resource is deleted from this provider unless the secret itself is deleted. Move the `AWSCURRENT` staging label before or after deleting this resource from this provider to fully trigger version deprecation if necessary.

        ## Example Usage
        ### Simple String Value

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.secretsmanager.SecretVersion("example",
            secret_id=aws_secretsmanager_secret["example"]["id"],
            secret_string="example-string-to-protect")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] secret_binary: Specifies binary data that you want to encrypt and store in this version of the secret. This is required if secret_string is not set. Needs to be encoded to base64.
        :param pulumi.Input[str] secret_id: Specifies the secret to which you want to add a new version. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret. The secret must already exist.
        :param pulumi.Input[str] secret_string: Specifies text data that you want to encrypt and store in this version of the secret. This is required if secret_binary is not set.
        :param pulumi.Input[List[pulumi.Input[str]]] version_stages: Specifies a list of staging labels that are attached to this version of the secret. A staging label must be unique to a single version of the secret. If you specify a staging label that's already associated with a different version of the same secret then that staging label is automatically removed from the other version and attached to this version. If you do not specify a value, then AWS Secrets Manager automatically moves the staging label `AWSCURRENT` to this new version on creation.
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

            __props__['secret_binary'] = secret_binary
            if secret_id is None:
                raise TypeError("Missing required property 'secret_id'")
            __props__['secret_id'] = secret_id
            __props__['secret_string'] = secret_string
            __props__['version_stages'] = version_stages
            __props__['arn'] = None
            __props__['version_id'] = None
        super(SecretVersion, __self__).__init__(
            'aws:secretsmanager/secretVersion:SecretVersion',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, arn=None, secret_binary=None, secret_id=None, secret_string=None, version_id=None, version_stages=None):
        """
        Get an existing SecretVersion resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The ARN of the secret.
        :param pulumi.Input[str] secret_binary: Specifies binary data that you want to encrypt and store in this version of the secret. This is required if secret_string is not set. Needs to be encoded to base64.
        :param pulumi.Input[str] secret_id: Specifies the secret to which you want to add a new version. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret. The secret must already exist.
        :param pulumi.Input[str] secret_string: Specifies text data that you want to encrypt and store in this version of the secret. This is required if secret_binary is not set.
        :param pulumi.Input[str] version_id: The unique identifier of the version of the secret.
        :param pulumi.Input[List[pulumi.Input[str]]] version_stages: Specifies a list of staging labels that are attached to this version of the secret. A staging label must be unique to a single version of the secret. If you specify a staging label that's already associated with a different version of the same secret then that staging label is automatically removed from the other version and attached to this version. If you do not specify a value, then AWS Secrets Manager automatically moves the staging label `AWSCURRENT` to this new version on creation.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["secret_binary"] = secret_binary
        __props__["secret_id"] = secret_id
        __props__["secret_string"] = secret_string
        __props__["version_id"] = version_id
        __props__["version_stages"] = version_stages
        return SecretVersion(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

