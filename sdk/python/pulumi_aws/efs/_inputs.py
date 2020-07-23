# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables

@pulumi.input_type
class AccessPointPosixUserArgs:
    gid: pulumi.Input[float] = pulumi.input_property("gid")
    """
    The POSIX group ID used for all file system operations using this access point.
    """
    uid: pulumi.Input[float] = pulumi.input_property("uid")
    """
    The POSIX user ID used for all file system operations using this access point.
    """
    secondary_gids: Optional[pulumi.Input[List[pulumi.Input[float]]]] = pulumi.input_property("secondaryGids")
    """
    Secondary POSIX group IDs used for all file system operations using this access point.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, gid: pulumi.Input[float], uid: pulumi.Input[float], secondary_gids: Optional[pulumi.Input[List[pulumi.Input[float]]]] = None) -> None:
        """
        :param pulumi.Input[float] gid: The POSIX group ID used for all file system operations using this access point.
        :param pulumi.Input[float] uid: The POSIX user ID used for all file system operations using this access point.
        :param pulumi.Input[List[pulumi.Input[float]]] secondary_gids: Secondary POSIX group IDs used for all file system operations using this access point.
        """
        __self__.gid = gid
        __self__.uid = uid
        __self__.secondary_gids = secondary_gids

@pulumi.input_type
class AccessPointRootDirectoryArgs:
    creation_info: Optional[pulumi.Input['AccessPointRootDirectoryCreationInfoArgs']] = pulumi.input_property("creationInfo")
    """
    Specifies the POSIX IDs and permissions to apply to the access point's Root Directory. See Creation Info below.
    """
    path: Optional[pulumi.Input[str]] = pulumi.input_property("path")
    """
    Specifies the path on the EFS file system to expose as the root directory to NFS clients using the access point to access the EFS file system. A path can have up to four subdirectories. If the specified path does not exist, you are required to provide `creation_info`.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, creation_info: Optional[pulumi.Input['AccessPointRootDirectoryCreationInfoArgs']] = None, path: Optional[pulumi.Input[str]] = None) -> None:
        """
        :param pulumi.Input['AccessPointRootDirectoryCreationInfoArgs'] creation_info: Specifies the POSIX IDs and permissions to apply to the access point's Root Directory. See Creation Info below.
        :param pulumi.Input[str] path: Specifies the path on the EFS file system to expose as the root directory to NFS clients using the access point to access the EFS file system. A path can have up to four subdirectories. If the specified path does not exist, you are required to provide `creation_info`.
        """
        __self__.creation_info = creation_info
        __self__.path = path

@pulumi.input_type
class AccessPointRootDirectoryCreationInfoArgs:
    owner_gid: pulumi.Input[float] = pulumi.input_property("ownerGid")
    """
    Specifies the POSIX group ID to apply to the `root_directory`.
    """
    owner_uid: pulumi.Input[float] = pulumi.input_property("ownerUid")
    """
    Specifies the POSIX user ID to apply to the `root_directory`.
    """
    permissions: pulumi.Input[str] = pulumi.input_property("permissions")
    """
    Specifies the POSIX permissions to apply to the RootDirectory, in the format of an octal number representing the file's mode bits.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, owner_gid: pulumi.Input[float], owner_uid: pulumi.Input[float], permissions: pulumi.Input[str]) -> None:
        """
        :param pulumi.Input[float] owner_gid: Specifies the POSIX group ID to apply to the `root_directory`.
        :param pulumi.Input[float] owner_uid: Specifies the POSIX user ID to apply to the `root_directory`.
        :param pulumi.Input[str] permissions: Specifies the POSIX permissions to apply to the RootDirectory, in the format of an octal number representing the file's mode bits.
        """
        __self__.owner_gid = owner_gid
        __self__.owner_uid = owner_uid
        __self__.permissions = permissions

@pulumi.input_type
class FileSystemLifecyclePolicyArgs:
    transition_to_ia: pulumi.Input[str] = pulumi.input_property("transitionToIa")
    """
    Indicates how long it takes to transition files to the IA storage class. Valid values: `AFTER_7_DAYS`, `AFTER_14_DAYS`, `AFTER_30_DAYS`, `AFTER_60_DAYS`, or `AFTER_90_DAYS`.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, transition_to_ia: pulumi.Input[str]) -> None:
        """
        :param pulumi.Input[str] transition_to_ia: Indicates how long it takes to transition files to the IA storage class. Valid values: `AFTER_7_DAYS`, `AFTER_14_DAYS`, `AFTER_30_DAYS`, `AFTER_60_DAYS`, or `AFTER_90_DAYS`.
        """
        __self__.transition_to_ia = transition_to_ia

