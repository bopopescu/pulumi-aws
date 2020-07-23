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


class NfsFileShare(pulumi.CustomResource):
    arn: pulumi.Output[str] = pulumi.output_property("arn")
    """
    Amazon Resource Name (ARN) of the NFS File Share.
    """
    client_lists: pulumi.Output[List[str]] = pulumi.output_property("clientLists")
    """
    The list of clients that are allowed to access the file gateway. The list must contain either valid IP addresses or valid CIDR blocks. Set to `["0.0.0.0/0"]` to not limit access. Minimum 1 item. Maximum 100 items.
    """
    default_storage_class: pulumi.Output[Optional[str]] = pulumi.output_property("defaultStorageClass")
    """
    The default storage class for objects put into an Amazon S3 bucket by the file gateway. Defaults to `S3_STANDARD`. Valid values: `S3_STANDARD`, `S3_STANDARD_IA`, `S3_ONEZONE_IA`.
    """
    fileshare_id: pulumi.Output[str] = pulumi.output_property("fileshareId")
    """
    ID of the NFS File Share.
    """
    gateway_arn: pulumi.Output[str] = pulumi.output_property("gatewayArn")
    """
    Amazon Resource Name (ARN) of the file gateway.
    """
    guess_mime_type_enabled: pulumi.Output[Optional[bool]] = pulumi.output_property("guessMimeTypeEnabled")
    """
    Boolean value that enables guessing of the MIME type for uploaded objects based on file extensions. Defaults to `true`.
    """
    kms_encrypted: pulumi.Output[Optional[bool]] = pulumi.output_property("kmsEncrypted")
    """
    Boolean value if `true` to use Amazon S3 server side encryption with your own AWS KMS key, or `false` to use a key managed by Amazon S3. Defaults to `false`.
    """
    kms_key_arn: pulumi.Output[Optional[str]] = pulumi.output_property("kmsKeyArn")
    """
    Amazon Resource Name (ARN) for KMS key used for Amazon S3 server side encryption. This value can only be set when `kms_encrypted` is true.
    """
    location_arn: pulumi.Output[str] = pulumi.output_property("locationArn")
    """
    The ARN of the backed storage used for storing file data.
    """
    nfs_file_share_defaults: pulumi.Output[Optional['outputs.NfsFileShareNfsFileShareDefaults']] = pulumi.output_property("nfsFileShareDefaults")
    """
    Nested argument with file share default values. More information below.
    """
    object_acl: pulumi.Output[Optional[str]] = pulumi.output_property("objectAcl")
    """
    Access Control List permission for S3 bucket objects. Defaults to `private`.
    """
    path: pulumi.Output[str] = pulumi.output_property("path")
    """
    File share path used by the NFS client to identify the mount point.
    """
    read_only: pulumi.Output[Optional[bool]] = pulumi.output_property("readOnly")
    """
    Boolean to indicate write status of file share. File share does not accept writes if `true`. Defaults to `false`.
    """
    requester_pays: pulumi.Output[Optional[bool]] = pulumi.output_property("requesterPays")
    """
    Boolean who pays the cost of the request and the data download from the Amazon S3 bucket. Set this value to `true` if you want the requester to pay instead of the bucket owner. Defaults to `false`.
    """
    role_arn: pulumi.Output[str] = pulumi.output_property("roleArn")
    """
    The ARN of the AWS Identity and Access Management (IAM) role that a file gateway assumes when it accesses the underlying storage.
    """
    squash: pulumi.Output[Optional[str]] = pulumi.output_property("squash")
    """
    Maps a user to anonymous user. Defaults to `RootSquash`. Valid values: `RootSquash` (only root is mapped to anonymous user), `NoSquash` (no one is mapped to anonymous user), `AllSquash` (everyone is mapped to anonymous user)
    """
    tags: pulumi.Output[Optional[Dict[str, str]]] = pulumi.output_property("tags")
    """
    Key-value map of resource tags
    """
    # pylint: disable=no-self-argument
    def __init__(__self__, resource_name, opts: Optional[pulumi.ResourceOptions] = None, client_lists=None, default_storage_class=None, gateway_arn=None, guess_mime_type_enabled=None, kms_encrypted=None, kms_key_arn=None, location_arn=None, nfs_file_share_defaults=None, object_acl=None, read_only=None, requester_pays=None, role_arn=None, squash=None, tags=None, __props__=None, __name__=None, __opts__=None) -> None:
        """
        Manages an AWS Storage Gateway NFS File Share.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.storagegateway.NfsFileShare("example",
            client_lists=["0.0.0.0/0"],
            gateway_arn=aws_storagegateway_gateway["example"]["arn"],
            location_arn=aws_s3_bucket["example"]["arn"],
            role_arn=aws_iam_role["example"]["arn"])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[List[pulumi.Input[str]]] client_lists: The list of clients that are allowed to access the file gateway. The list must contain either valid IP addresses or valid CIDR blocks. Set to `["0.0.0.0/0"]` to not limit access. Minimum 1 item. Maximum 100 items.
        :param pulumi.Input[str] default_storage_class: The default storage class for objects put into an Amazon S3 bucket by the file gateway. Defaults to `S3_STANDARD`. Valid values: `S3_STANDARD`, `S3_STANDARD_IA`, `S3_ONEZONE_IA`.
        :param pulumi.Input[str] gateway_arn: Amazon Resource Name (ARN) of the file gateway.
        :param pulumi.Input[bool] guess_mime_type_enabled: Boolean value that enables guessing of the MIME type for uploaded objects based on file extensions. Defaults to `true`.
        :param pulumi.Input[bool] kms_encrypted: Boolean value if `true` to use Amazon S3 server side encryption with your own AWS KMS key, or `false` to use a key managed by Amazon S3. Defaults to `false`.
        :param pulumi.Input[str] kms_key_arn: Amazon Resource Name (ARN) for KMS key used for Amazon S3 server side encryption. This value can only be set when `kms_encrypted` is true.
        :param pulumi.Input[str] location_arn: The ARN of the backed storage used for storing file data.
        :param pulumi.Input['NfsFileShareNfsFileShareDefaultsArgs'] nfs_file_share_defaults: Nested argument with file share default values. More information below.
        :param pulumi.Input[str] object_acl: Access Control List permission for S3 bucket objects. Defaults to `private`.
        :param pulumi.Input[bool] read_only: Boolean to indicate write status of file share. File share does not accept writes if `true`. Defaults to `false`.
        :param pulumi.Input[bool] requester_pays: Boolean who pays the cost of the request and the data download from the Amazon S3 bucket. Set this value to `true` if you want the requester to pay instead of the bucket owner. Defaults to `false`.
        :param pulumi.Input[str] role_arn: The ARN of the AWS Identity and Access Management (IAM) role that a file gateway assumes when it accesses the underlying storage.
        :param pulumi.Input[str] squash: Maps a user to anonymous user. Defaults to `RootSquash`. Valid values: `RootSquash` (only root is mapped to anonymous user), `NoSquash` (no one is mapped to anonymous user), `AllSquash` (everyone is mapped to anonymous user)
        :param pulumi.Input[Dict[str, pulumi.Input[str]]] tags: Key-value map of resource tags
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

            if client_lists is None:
                raise TypeError("Missing required property 'client_lists'")
            __props__['client_lists'] = client_lists
            __props__['default_storage_class'] = default_storage_class
            if gateway_arn is None:
                raise TypeError("Missing required property 'gateway_arn'")
            __props__['gateway_arn'] = gateway_arn
            __props__['guess_mime_type_enabled'] = guess_mime_type_enabled
            __props__['kms_encrypted'] = kms_encrypted
            __props__['kms_key_arn'] = kms_key_arn
            if location_arn is None:
                raise TypeError("Missing required property 'location_arn'")
            __props__['location_arn'] = location_arn
            __props__['nfs_file_share_defaults'] = nfs_file_share_defaults
            __props__['object_acl'] = object_acl
            __props__['read_only'] = read_only
            __props__['requester_pays'] = requester_pays
            if role_arn is None:
                raise TypeError("Missing required property 'role_arn'")
            __props__['role_arn'] = role_arn
            __props__['squash'] = squash
            __props__['tags'] = tags
            __props__['arn'] = None
            __props__['fileshare_id'] = None
            __props__['path'] = None
        super(NfsFileShare, __self__).__init__(
            'aws:storagegateway/nfsFileShare:NfsFileShare',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, arn=None, client_lists=None, default_storage_class=None, fileshare_id=None, gateway_arn=None, guess_mime_type_enabled=None, kms_encrypted=None, kms_key_arn=None, location_arn=None, nfs_file_share_defaults=None, object_acl=None, path=None, read_only=None, requester_pays=None, role_arn=None, squash=None, tags=None):
        """
        Get an existing NfsFileShare resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN) of the NFS File Share.
        :param pulumi.Input[List[pulumi.Input[str]]] client_lists: The list of clients that are allowed to access the file gateway. The list must contain either valid IP addresses or valid CIDR blocks. Set to `["0.0.0.0/0"]` to not limit access. Minimum 1 item. Maximum 100 items.
        :param pulumi.Input[str] default_storage_class: The default storage class for objects put into an Amazon S3 bucket by the file gateway. Defaults to `S3_STANDARD`. Valid values: `S3_STANDARD`, `S3_STANDARD_IA`, `S3_ONEZONE_IA`.
        :param pulumi.Input[str] fileshare_id: ID of the NFS File Share.
        :param pulumi.Input[str] gateway_arn: Amazon Resource Name (ARN) of the file gateway.
        :param pulumi.Input[bool] guess_mime_type_enabled: Boolean value that enables guessing of the MIME type for uploaded objects based on file extensions. Defaults to `true`.
        :param pulumi.Input[bool] kms_encrypted: Boolean value if `true` to use Amazon S3 server side encryption with your own AWS KMS key, or `false` to use a key managed by Amazon S3. Defaults to `false`.
        :param pulumi.Input[str] kms_key_arn: Amazon Resource Name (ARN) for KMS key used for Amazon S3 server side encryption. This value can only be set when `kms_encrypted` is true.
        :param pulumi.Input[str] location_arn: The ARN of the backed storage used for storing file data.
        :param pulumi.Input['NfsFileShareNfsFileShareDefaultsArgs'] nfs_file_share_defaults: Nested argument with file share default values. More information below.
        :param pulumi.Input[str] object_acl: Access Control List permission for S3 bucket objects. Defaults to `private`.
        :param pulumi.Input[str] path: File share path used by the NFS client to identify the mount point.
        :param pulumi.Input[bool] read_only: Boolean to indicate write status of file share. File share does not accept writes if `true`. Defaults to `false`.
        :param pulumi.Input[bool] requester_pays: Boolean who pays the cost of the request and the data download from the Amazon S3 bucket. Set this value to `true` if you want the requester to pay instead of the bucket owner. Defaults to `false`.
        :param pulumi.Input[str] role_arn: The ARN of the AWS Identity and Access Management (IAM) role that a file gateway assumes when it accesses the underlying storage.
        :param pulumi.Input[str] squash: Maps a user to anonymous user. Defaults to `RootSquash`. Valid values: `RootSquash` (only root is mapped to anonymous user), `NoSquash` (no one is mapped to anonymous user), `AllSquash` (everyone is mapped to anonymous user)
        :param pulumi.Input[Dict[str, pulumi.Input[str]]] tags: Key-value map of resource tags
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["client_lists"] = client_lists
        __props__["default_storage_class"] = default_storage_class
        __props__["fileshare_id"] = fileshare_id
        __props__["gateway_arn"] = gateway_arn
        __props__["guess_mime_type_enabled"] = guess_mime_type_enabled
        __props__["kms_encrypted"] = kms_encrypted
        __props__["kms_key_arn"] = kms_key_arn
        __props__["location_arn"] = location_arn
        __props__["nfs_file_share_defaults"] = nfs_file_share_defaults
        __props__["object_acl"] = object_acl
        __props__["path"] = path
        __props__["read_only"] = read_only
        __props__["requester_pays"] = requester_pays
        __props__["role_arn"] = role_arn
        __props__["squash"] = squash
        __props__["tags"] = tags
        return NfsFileShare(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

